from __future__ import annotations

import csv
import hashlib
import html
import json
import math
import random
import re
import subprocess
from collections import defaultdict
from pathlib import Path

from .metrics import edit_counts, normalize, normalized_distance, repeated_fraction


MODEL_FOLDERS = {
    "qwen3": "Qwen3-ASR-1.7B",
    "canary": "canary-qwen-2.5b",
    "parakeet": "parakeet-tdt-0.6b-v3",
    "whisper": "whisper-large-v3",
}
SOURCE_CHUNK_SECONDS = {"canary": 30, "qwen3": 300, "parakeet": 300, "whisper": 300}
SEGMENT_SECONDS = 30


def media_duration(ffmpeg: str, path: Path) -> float:
    result = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)],
                            capture_output=True, text=True)
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        raise RuntimeError(f"Could not determine duration for {path}")
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def split_words(words: list[str], pieces: int) -> list[list[str]]:
    return [words[round(i * len(words) / pieces):round((i + 1) * len(words) / pieces)]
            for i in range(pieces)]


def common_segments(text: str, duration: float, source_chunk_seconds: int) -> list[list[str]]:
    lines = text.splitlines()
    expected = math.ceil(duration / source_chunk_seconds)
    if abs(len(lines) - expected) > 1:
        raise ValueError(f"Expected about {expected} chunk lines, found {len(lines)}")
    result: list[list[str]] = []
    for index, line in enumerate(lines):
        remaining = max(0.0, duration - index * source_chunk_seconds)
        pieces = max(1, math.ceil(min(source_chunk_seconds, remaining) / SEGMENT_SECONDS))
        result.extend(split_words(normalize(line), pieces))
    target = math.ceil(duration / SEGMENT_SECONDS)
    return (result + [[] for _ in range(target)])[:target]


def medoid(candidates: dict[str, list[str]]) -> tuple[str, list[str]]:
    winner = min(candidates, key=lambda name: sum(
        normalized_distance(candidates[name], other)
        for other_name, other in candidates.items() if other_name != name
    ))
    return winner, candidates[winner]


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    return ordered[round((len(ordered) - 1) * fraction)]


def bootstrap_ratio(values: list[tuple[int, int]], seed: int, rounds: int = 1000) -> list[float]:
    if not values:
        return [0.0, 0.0]
    rng = random.Random(seed)
    estimates = []
    for _ in range(rounds):
        sample = [rng.choice(values) for _ in values]
        estimates.append(sum(edits for edits, _ in sample) / max(1, sum(words for _, words in sample)))
    return [percentile(estimates, 0.025), percentile(estimates, 0.975)]


def evaluate(transcript_root: Path, media_root: Path, ffmpeg: str) -> tuple[dict, list[dict]]:
    model_files = {
        model: {path.stem: path for path in (transcript_root / folder).glob("*.txt")}
        for model, folder in MODEL_FOLDERS.items()
    }
    common = sorted(set.intersection(*(set(files) for files in model_files.values())))
    if not common:
        raise RuntimeError("No recording has transcripts from all four models")
    pair_totals: dict[tuple[str, str], list[tuple[int, int]]] = defaultdict(list)
    pseudo_counts: dict[str, list[tuple[int, int]]] = defaultdict(list)
    edit_totals = {model: [0, 0, 0, 0] for model in MODEL_FOLDERS}  # S, I, D, ref words
    rows: list[dict] = []
    for recording in common:
        media = next((p for p in media_root.iterdir() if p.is_file() and p.stem == recording), None)
        if media is None:
            raise RuntimeError(f"Original media missing for {recording}")
        duration = media_duration(ffmpeg, media)
        segments = {
            model: common_segments(files[recording].read_text(encoding="utf-8"), duration,
                                   SOURCE_CHUNK_SECONDS[model])
            for model, files in model_files.items()
        }
        count = math.ceil(duration / SEGMENT_SECONDS)
        for index in range(count):
            texts = {model: segments[model][index] for model in MODEL_FOLDERS}
            pair_scores: dict[str, float] = {}
            models = list(MODEL_FOLDERS)
            for left_index, left in enumerate(models):
                for right in models[left_index + 1:]:
                    edits = edit_counts(texts[left], texts[right]).total
                    denominator = max(len(texts[left]), len(texts[right]), 1)
                    pair_totals[(left, right)].append((edits, denominator))
                    pair_scores[f"{left}__{right}"] = edits / denominator
            median_words = sorted(len(words) for words in texts.values())[1:3]
            peer_center = sum(median_words) / 2
            row = {
                "recording": recording, "segment_id": f"{recording}:{index:04d}",
                "start_seconds": index * SEGMENT_SECONDS,
                "end_seconds": min(duration, (index + 1) * SEGMENT_SECONDS),
                "alignment": "native_30s" if all(SOURCE_CHUNK_SECONDS[m] == 30 for m in models)
                             else "30s_native_or_proportional_within_source_chunk",
            }
            row.update({f"text_{model}": " ".join(words) for model, words in texts.items()})
            row.update({f"distance_{key}": value for key, value in pair_scores.items()})
            row["disagreement_intensity"] = sum(pair_scores.values()) / len(pair_scores)
            for model in models:
                peers = {name: words for name, words in texts.items() if name != model}
                consensus_source, consensus = medoid(peers)
                edits = edit_counts(consensus, texts[model])
                denominator = max(len(consensus), 1)
                rate = edits.total / denominator
                pseudo_counts[model].append((edits.total, denominator))
                totals = edit_totals[model]
                totals[0] += edits.substitutions; totals[1] += edits.insertions
                totals[2] += edits.deletions; totals[3] += len(consensus)
                row[f"consensus_source_{model}"] = consensus_source
                row[f"consensus_{model}"] = " ".join(consensus)
                row[f"pseudo_wer_{model}"] = rate
                row[f"repetition_{model}"] = repeated_fraction(texts[model])
                row[f"suspected_hallucination_{model}"] = (
                    len(texts[model]) > max(10, 1.7 * peer_center) or row[f"repetition_{model}"] > 0.2
                )
                row[f"suspected_omission_{model}"] = len(texts[model]) < 0.55 * peer_center
            rows.append(row)

    matrix = {model: {} for model in MODEL_FOLDERS}
    for left in MODEL_FOLDERS:
        for right in MODEL_FOLDERS:
            if left == right:
                matrix[left][right] = 0.0
            else:
                key = tuple(sorted((left, right), key=list(MODEL_FOLDERS).index))
                values = pair_totals[key]
                matrix[left][right] = sum(e for e, _ in values) / sum(d for _, d in values)
    models_summary = {}
    for model in MODEL_FOLDERS:
        s, i, d, reference_words = edit_totals[model]
        counts = pseudo_counts[model]
        models_summary[model] = {
            "mean_pairwise_distance": sum(matrix[model][other] for other in MODEL_FOLDERS if other != model) / 3,
            "consensus_pseudo_wer": (s + i + d) / max(reference_words, 1),
            "substitutions": s, "insertions": i, "deletions": d,
            "agreement_rate_proxy": 1 - sum(matrix[model][other] for other in MODEL_FOLDERS if other != model) / 3,
            "pseudo_wer_bootstrap_95": bootstrap_ratio(counts, int(hashlib.sha256(model.encode()).hexdigest()[:8], 16)),
            "suspected_hallucination_segments": sum(row[f"suspected_hallucination_{model}"] for row in rows),
            "suspected_omission_segments": sum(row[f"suspected_omission_{model}"] for row in rows),
            "reference_free_estimator": None,
            "inference_time_seconds": None, "real_time_factor": None, "peak_vram_mib": None,
        }
    summary = {
        "method": "reference-free proxies; no ground-truth WER",
        "recordings": common, "segment_seconds": SEGMENT_SECONDS,
        "alignment_limitation": "30-second Canary lines; proportional word allocation within 5-minute lines for other models",
        "models": models_summary, "pairwise_distance_matrix": matrix,
        "rankings": {
            "consensus_agreement": sorted(MODEL_FOLDERS, key=lambda m: models_summary[m]["consensus_pseudo_wer"]),
            "pairwise_agreement": sorted(MODEL_FOLDERS, key=lambda m: models_summary[m]["mean_pairwise_distance"]),
        },
        "unavailable": {
            "independent_quality_estimator": "No validated local pretrained estimator integrated in Phase 1",
            "audio_conditioned_vad": "Not integrated in Phase 1",
            "efficiency_metrics": "Historical inference timing and peak VRAM were not recorded during ASR generation",
        },
    }
    return summary, rows


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(rows[0])
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)


def write_summary_csv(path: Path, summary: dict) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        fields = ["model", *next(iter(summary["models"].values())).keys()]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for model, metrics in summary["models"].items():
            writer.writerow({"model": model, **metrics})


def write_html(path: Path, summary: dict, rows: list[dict]) -> None:
    models = list(MODEL_FOLDERS)
    maximum = max(metric["consensus_pseudo_wer"] for metric in summary["models"].values()) or 1
    bars = "".join(
        f'<div class="bar"><b>{m}</b><span style="width:{summary["models"][m]["consensus_pseudo_wer"] / maximum * 70:.1f}%"></span>'
        f'{summary["models"][m]["consensus_pseudo_wer"]:.3f}</div>' for m in models
    )
    matrix_header = "".join(f"<th>{m}</th>" for m in models)
    matrix_rows = "".join("<tr><th>" + left + "</th>" + "".join(
        f'<td style="background:rgba(190,40,40,{summary["pairwise_distance_matrix"][left][right]:.2f})">'
        f'{summary["pairwise_distance_matrix"][left][right]:.3f}</td>' for right in models
    ) + "</tr>" for left in models)
    details = "".join(
        f'<details><summary>{html.escape(row["segment_id"])} — disagreement {row["disagreement_intensity"]:.3f}</summary>' +
        "".join(f'<h4>{m}</h4><p>{html.escape(row[f"text_{m}"])}</p>' for m in models) + "</details>"
        for row in sorted(rows, key=lambda r: r["disagreement_intensity"], reverse=True)[:100]
    )
    ranking = " → ".join(summary["rankings"]["consensus_agreement"])
    path.write_text(f"""<!doctype html><meta charset="utf-8"><title>ANN2DL ASR evaluation</title>
<style>body{{font:15px system-ui;max-width:1200px;margin:30px auto;padding:0 20px;color:#222}}table{{border-collapse:collapse}}th,td{{padding:8px;border:1px solid #ccc;text-align:center}}.bar{{display:flex;gap:12px;align-items:center;margin:9px 0}}.bar b{{width:90px}}.bar span{{height:18px;background:#4d77cf;display:inline-block}}details{{border-top:1px solid #ddd;padding:10px}}.warning{{background:#fff3cd;padding:14px}}</style>
<h1>ANN2DL reference-free ASR evaluation</h1>
<p class="warning"><b>No ground truth:</b> these are disagreement proxies, not measured WER. Timestamps for models other than Canary are approximate proportional subdivisions of five-minute transcript chunks.</p>
<h2>Consensus pseudo-WER (lower is better)</h2>{bars}
<p><b>Provisional consensus ranking:</b> {ranking}</p>
<h2>Pairwise distance matrix</h2><table><tr><th></th>{matrix_header}</tr>{matrix_rows}</table>
<h2>Highest-disagreement segments</h2>{details}
<h2>Unavailable Phase 1 metrics</h2><pre>{html.escape(json.dumps(summary["unavailable"], indent=2))}</pre>
""", encoding="utf-8")


def save_results(output: Path, summary: dict, rows: list[dict]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    (output / "metrics.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary_csv(output / "model_comparison.csv", summary)
    write_csv(output / "segments.csv", rows)
    write_html(output / "report.html", summary, rows)

