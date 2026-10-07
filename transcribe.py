from __future__ import annotations

import argparse
import csv
import gc
import hashlib
import importlib
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Sequence


MEDIA_EXTENSIONS = {
    ".aac", ".flac", ".m4a", ".mka", ".mkv", ".mov", ".mp3", ".mp4",
    ".mpeg", ".mpg", ".ogg", ".opus", ".wav", ".webm", ".wma", ".wmv",
}

LEDGER_FIELDS = (
    "timestamp_utc", "source_path", "source_hash", "model", "model_id",
    "status", "transcript_path", "error",
)


@dataclass(frozen=True)
class ModelSpec:
    alias: str
    model_id: str
    output_folder: str
    loader: Callable[[str], "LoadedModel"]


@dataclass
class LoadedModel:
    transcribe: Callable[[Path, str | None], str]
    resources: tuple[Any, ...] = ()


def _require_import(package: str, install_name: str | None = None) -> Any:
    try:
        return importlib.import_module(package)
    except ImportError as exc:
        dependency = install_name or package
        raise RuntimeError(
            f"Missing dependency '{dependency}'. Install requirements-gpu.txt in .venv."
        ) from exc


def _load_qwen(device: str) -> LoadedModel:
    torch = _require_import("torch")
    qwen_asr = _require_import("qwen_asr", "qwen-asr")
    dtype = torch.float16 if device.startswith("cuda") else torch.float32
    model = qwen_asr.Qwen3ASRModel.from_pretrained(
        "Qwen/Qwen3-ASR-1.7B",
        dtype=dtype,
        device_map=device,
        max_inference_batch_size=1,
        max_new_tokens=4096,
    )

    def transcribe(audio_path: Path, language: str | None) -> str:
        results = model.transcribe(audio=str(audio_path), language=language)
        return str(results[0].text).strip() if results else ""

    return LoadedModel(transcribe=transcribe, resources=(model,))


def _extract_nemo_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if hasattr(value, "text"):
        return str(value.text).strip()
    if isinstance(value, dict) and "text" in value:
        return str(value["text"]).strip()
    if isinstance(value, (list, tuple)):
        return _extract_nemo_text(value[0]) if value else ""
    raise RuntimeError(f"Unsupported NeMo transcription result: {type(value).__name__}")


def _load_nemo_pretrained(nemo_asr: Any, model_id: str) -> Any:
    try:
        return nemo_asr.models.ASRModel.from_pretrained(model_id)
    except FileNotFoundError:
        print(f"REFRESH incomplete NeMo cache for {model_id}")
        return nemo_asr.models.ASRModel.from_pretrained(model_id, refresh_cache=True)


def _load_canary(device: str) -> LoadedModel:
    torch = _require_import("torch")
    nemo_asr = _require_import("nemo.collections.asr", "nemo_toolkit[asr]")
    model = _load_nemo_pretrained(nemo_asr, "nvidia/canary-qwen-2.5b")
    model.eval()
    model.to(device)

    def transcribe(audio_path: Path, _language: str | None) -> str:
        with torch.inference_mode():
            result = model.transcribe([str(audio_path)])
        return _extract_nemo_text(result)

    return LoadedModel(transcribe=transcribe, resources=(model,))


def _load_parakeet(device: str) -> LoadedModel:
    torch = _require_import("torch")
    nemo_asr = _require_import("nemo.collections.asr", "nemo_toolkit[asr]")
    model = _load_nemo_pretrained(nemo_asr, "nvidia/parakeet-tdt-0.6b-v3")
    model.eval()
    model.to(device)

    def transcribe(audio_path: Path, _language: str | None) -> str:
        with torch.inference_mode():
            result = model.transcribe([str(audio_path)])
        return _extract_nemo_text(result)

    return LoadedModel(transcribe=transcribe, resources=(model,))


def _load_whisper(device: str) -> LoadedModel:
    torch = _require_import("torch")
    transformers = _require_import("transformers")
    dtype = torch.float16 if device.startswith("cuda") else torch.float32
    model = transformers.AutoModelForSpeechSeq2Seq.from_pretrained(
        "openai/whisper-large-v3",
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True,
    ).to(device)
    processor = transformers.AutoProcessor.from_pretrained("openai/whisper-large-v3")
    pipe = transformers.pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=1,
        torch_dtype=dtype,
        device=device,
    )

    def transcribe(audio_path: Path, language: str | None) -> str:
        soundfile = _require_import("soundfile")
        audio, sampling_rate = soundfile.read(
            str(audio_path), dtype="float32", always_2d=False
        )
        generation = {"task": "transcribe"}
        if language:
            generation["language"] = language
        result = pipe(
            {"array": audio, "sampling_rate": sampling_rate},
            generate_kwargs=generation,
        )
        return str(result["text"]).strip()

    return LoadedModel(transcribe=transcribe, resources=(pipe, processor, model))


MODELS: dict[str, ModelSpec] = {
    "qwen3": ModelSpec("qwen3", "Qwen/Qwen3-ASR-1.7B", "Qwen3-ASR-1.7B", _load_qwen),
    "canary": ModelSpec("canary", "nvidia/canary-qwen-2.5b", "canary-qwen-2.5b", _load_canary),
    "parakeet": ModelSpec("parakeet", "nvidia/parakeet-tdt-0.6b-v3", "parakeet-tdt-0.6b-v3", _load_parakeet),
    "whisper": ModelSpec("whisper", "openai/whisper-large-v3", "whisper-large-v3", _load_whisper),
}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def discover_media(input_path: Path) -> list[Path]:
    path = input_path.expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Input does not exist: {path}")
    if path.is_file():
        if path.suffix.lower() not in MEDIA_EXTENSIONS:
            raise ValueError(f"Unsupported media extension: {path.suffix or '(none)'}")
        return [path]
    if not path.is_dir():
        raise ValueError(f"Input is neither a regular file nor a directory: {path}")
    return sorted(
        (child.resolve() for child in path.iterdir()
         if child.is_file() and child.suffix.lower() in MEDIA_EXTENSIONS),
        key=lambda item: item.name.casefold(),
    )


def transcript_path(source: Path, spec: ModelSpec) -> Path:
    return source.parent / "transcript" / spec.output_folder / f"{source.stem}.txt"


def read_finished(ledger_path: Path) -> set[tuple[str, str, str]]:
    finished: set[tuple[str, str, str]] = set()
    if not ledger_path.exists():
        return finished
    with ledger_path.open("r", encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            key = (row.get("source_hash", ""), row.get("model_id", ""), row.get("transcript_path", ""))
            if row.get("status") == "finished":
                finished.add(key)
    return finished


def append_ledger(
    ledger_path: Path, *, source: Path, source_hash: str, spec: ModelSpec,
    status: str, output: Path, error: str = "",
) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not ledger_path.exists() or ledger_path.stat().st_size == 0
    with ledger_path.open("a", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=LEDGER_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "source_path": str(source), "source_hash": source_hash,
            "model": spec.alias, "model_id": spec.model_id, "status": status,
            "transcript_path": str(output.resolve()), "error": error,
        })


def normalize_audio_chunks(
    source: Path, destination_dir: Path, chunk_seconds: int
) -> list[Path]:
    imageio_ffmpeg = _require_import("imageio_ffmpeg", "imageio-ffmpeg")
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_pattern = destination_dir / "audio-%05d.wav"
    command = [
        imageio_ffmpeg.get_ffmpeg_exe(), "-nostdin", "-hide_banner", "-loglevel", "error",
        "-y", "-i", str(source), "-vn", "-ac", "1", "-ar", "16000",
        "-c:a", "pcm_s16le", "-f", "segment", "-segment_time", str(chunk_seconds),
        "-reset_timestamps", "1", "-segment_format", "wav", str(destination_pattern),
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"FFmpeg could not decode {source.name}") from exc
    chunks = sorted(destination_dir.glob("audio-*.wav"))
    if not chunks:
        raise RuntimeError(f"FFmpeg produced no audio chunks for {source.name}")
    return chunks


def select_models(names: Sequence[str]) -> list[ModelSpec]:
    if "all" in names:
        if len(names) != 1:
            raise ValueError("Use '--models all' by itself, or list individual models.")
        return list(MODELS.values())
    unknown = [name for name in names if name not in MODELS]
    if unknown:
        raise ValueError(f"Unknown model(s): {', '.join(unknown)}")
    return [MODELS[name] for name in dict.fromkeys(names)]


def choose_device(allow_cpu: bool) -> str:
    torch = _require_import("torch")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
        return "cuda:0"
    if allow_cpu:
        print("WARNING: CUDA is unavailable; using CPU because --allow-cpu was supplied.")
        return "cpu"
    raise RuntimeError(
        "CUDA is not available to PyTorch. Install the CUDA build from requirements-gpu.txt "
        "and verify the NVIDIA driver, or explicitly use --allow-cpu."
    )


def release_model(loaded: LoadedModel | None) -> None:
    if loaded is not None:
        loaded.resources = ()
    gc.collect()
    try:
        torch = __import__("torch")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
    except ImportError:
        pass


def process(
    media: Sequence[Path], specs: Sequence[ModelSpec], *, ledger_path: Path,
    language: str | None, force: bool, device: str, chunk_seconds: int,
) -> int:
    hashes = {source: sha256_file(source) for source in media}
    finished = read_finished(ledger_path)
    failures = 0

    for spec in specs:
        pending: list[tuple[Path, Path]] = []
        for source in media:
            output = transcript_path(source, spec)
            key = (hashes[source], spec.model_id, str(output.resolve()))
            if not force and key in finished and output.is_file():
                print(f"SKIP [{spec.alias}] {source.name}")
            else:
                pending.append((source, output))
        if not pending:
            continue

        loaded: LoadedModel | None = None
        try:
            print(f"LOAD [{spec.alias}] {spec.model_id}")
            loaded = spec.loader(device)
            for source, output in pending:
                source_hash = hashes[source]
                append_ledger(ledger_path, source=source, source_hash=source_hash,
                              spec=spec, status="running", output=output)
                try:
                    print(f"RUN  [{spec.alias}] {source.name}")
                    with tempfile.TemporaryDirectory(prefix="course-asr-") as temp_dir:
                        chunks = normalize_audio_chunks(
                            source, Path(temp_dir), chunk_seconds
                        )
                        parts: list[str] = []
                        for chunk_number, chunk in enumerate(chunks, start=1):
                            print(
                                f"CHUNK [{spec.alias}] {source.name} "
                                f"{chunk_number}/{len(chunks)}"
                            )
                            part = loaded.transcribe(chunk, language).strip()
                            if part:
                                parts.append(part)
                        text = "\n".join(parts)
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text(text.rstrip() + "\n", encoding="utf-8")
                    append_ledger(ledger_path, source=source, source_hash=source_hash,
                                  spec=spec, status="finished", output=output)
                    finished.add((source_hash, spec.model_id, str(output.resolve())))
                    print(f"DONE [{spec.alias}] {output}")
                except Exception as exc:
                    failures += 1
                    append_ledger(ledger_path, source=source, source_hash=source_hash,
                                  spec=spec, status="failed", output=output,
                                  error=f"{type(exc).__name__}: {exc}")
                    print(f"FAIL [{spec.alias}] {source.name}: {exc}", file=sys.stderr)
                    try:
                        torch = __import__("torch")
                        if torch.cuda.is_available():
                            torch.cuda.empty_cache()
                    except ImportError:
                        pass
        except Exception as exc:
            failures += len(pending)
            print(f"FAIL [{spec.alias}] could not load: {exc}", file=sys.stderr)
            for source, output in pending:
                append_ledger(ledger_path, source=source, source_hash=hashes[source],
                              spec=spec, status="failed", output=output,
                              error=f"Model load failed: {type(exc).__name__}: {exc}")
        finally:
            release_model(loaded)
    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Transcribe a course folder or media file with CUDA ASR models."
    )
    parser.add_argument("input", nargs="?", help="Course folder or individual media file")
    parser.add_argument("--models", nargs="+", choices=[*MODELS, "all"],
                        help="One or more model aliases, or 'all'")
    parser.add_argument("--language", help="Optional language hint for Qwen and Whisper")
    parser.add_argument(
        "--chunk-seconds",
        type=int,
        default=300,
        help="Maximum audio chunk duration in seconds (default: 300)",
    )
    parser.add_argument("--force", action="store_true", help="Reprocess completed items")
    parser.add_argument("--allow-cpu", action="store_true",
                        help="Permit CPU inference when CUDA is unavailable (very slow)")
    parser.add_argument("--ledger", type=Path,
                        default=Path(__file__).resolve().parent / "transcription_status.csv",
                        help="CSV ledger path (default: beside this script)")
    parser.add_argument("--list-models", action="store_true",
                        help="List supported models and exit")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.list_models:
        for spec in MODELS.values():
            print(f"{spec.alias:9} {spec.model_id}")
        return 0
    if not args.input:
        parser.error("input is required unless --list-models is used")
    if not args.models:
        parser.error("--models requires one or more model names")
    try:
        if args.chunk_seconds < 30:
            raise ValueError("--chunk-seconds must be at least 30")
        specs = select_models(args.models)
        media = discover_media(Path(args.input))
        if not media:
            print("No supported media files found directly inside the input folder.")
            return 0
        device = choose_device(args.allow_cpu)
        failures = process(media, specs, ledger_path=args.ledger.expanduser().resolve(),
                           language=args.language, force=args.force, device=device,
                           chunk_seconds=args.chunk_seconds)
        return 1 if failures else 0
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
