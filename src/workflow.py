"""Agentic lecture-note extraction workflow."""

from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable

from .llm import LLMClient
from .loaders import expand_material_paths, load_material, load_transcripts
from .models import Candidate, Decision, LectureConfig, LectureResult, LoadedMaterial, Note
from .prompts import COMPARE_PROMPT, EXTRACT_PROMPT, REVIEW_PROMPT, SYSTEM_PROMPT

VALID_DECISIONS = {"NEW", "EXPANDED", "EXAMPLE", "REDUNDANT", "UNCERTAIN"}
KEEP_DECISIONS = {"NEW", "EXPANDED", "EXAMPLE"}


class LectureWorkflow:
    def __init__(self, client: LLMClient, cache_dir: Path, settings: dict[str, Any] | None = None) -> None:
        self.client = client
        self.cache_dir = cache_dir
        self.settings = settings or {}
        self.transcript_chunk_chars = int(self.settings.get("transcript_chunk_chars", 45_000))
        self.material_max_chars = int(self.settings.get("material_max_chars", 120_000))
        self.candidate_batch_size = int(self.settings.get("candidate_batch_size", 20))

    def run(self, lecture: LectureConfig) -> LectureResult:
        transcripts = load_transcripts(lecture.transcripts)
        material_paths, limitations = expand_material_paths(lecture.materials)
        materials = [load_material(path, self.cache_dir) for path in material_paths]
        limitations.extend(f"Unreadable material: {item.path} ({item.error})" for item in materials if item.error)
        candidates = self.extract_candidates(lecture.id, transcripts)
        decisions = self.compare_candidates(lecture.id, candidates, materials, limitations)
        accepted = self._accepted_notes(candidates, decisions)
        notes, audit = self.review(lecture.id, transcripts, materials, accepted, limitations)
        notes_dir = lecture.course_dir / "notes"
        notes_dir.mkdir(parents=True, exist_ok=True)
        notes_path = notes_dir / f"{_safe_name(lecture.id)}_extra_notes.md"
        notes_path.write_text(self.render_markdown(lecture, notes, limitations), encoding="utf-8")
        self._write_audit(lecture.id, candidates, decisions, audit)
        return LectureResult(lecture.id, lecture.course_dir, notes_path, len(candidates), len(accepted), len(notes), limitations)

    def extract_candidates(self, lecture_id: str, transcripts: list[tuple[Path, str]]) -> list[Candidate]:
        primary_chunks = _chunks(transcripts[0][1], self.transcript_chunk_chars)
        candidates: list[Candidate] = []
        for index, primary in enumerate(primary_chunks):
            evidence = [f"--- {transcripts[0][0].name} (primary) ---\n{primary}"]
            start, end = index / len(primary_chunks), (index + 1) / len(primary_chunks)
            for path, text in transcripts[1:]:
                left, right = int(len(text) * start), int(len(text) * end)
                evidence.append(f"--- {path.name} (alternate ASR, approximate aligned region) ---\n{text[left:right]}")
            payload = self.client.json(SYSTEM_PROMPT, EXTRACT_PROMPT.format(
                lecture_id=lecture_id, chunk_number=index + 1, chunk_count=len(primary_chunks),
                transcripts="\n\n".join(evidence)))
            for item in _object_list(payload, "candidates"):
                candidates.append(Candidate(
                    id=f"C{len(candidates) + 1:04d}", topic=_required(item, "topic"),
                    insight=_required(item, "insight"), evidence=_required(item, "evidence"),
                    transcript_source=str(item.get("transcript_source") or transcripts[0][0].name),
                    timestamp=_nullable(item.get("timestamp")), usefulness=str(item.get("usefulness") or ""),
                    uncertain=bool(item.get("uncertain", False))))
        return candidates

    def compare_candidates(self, lecture_id: str, candidates: list[Candidate], materials: list[LoadedMaterial], limitations: list[str]) -> list[Decision]:
        decisions: list[Decision] = []
        for batch in _batched(candidates, self.candidate_batch_size):
            payload = self.client.json(SYSTEM_PROMPT, COMPARE_PROMPT.format(
                lecture_id=lecture_id, limitations="; ".join(limitations) or "None",
                candidates=json.dumps([c.to_dict() for c in batch], ensure_ascii=False, indent=2),
                materials=self._materials_text(materials)))
            returned = {str(item.get("candidate_id")): item for item in _object_list(payload, "decisions")}
            for candidate in batch:
                item = returned.get(candidate.id)
                if item is None:
                    raise RuntimeError(f"Comparison response omitted candidate {candidate.id}")
                decision = str(item.get("decision", "")).upper()
                if decision not in VALID_DECISIONS:
                    raise RuntimeError(f"Invalid decision {decision!r} for {candidate.id}")
                decisions.append(Decision(candidate.id, decision, _nullable(item.get("accepted_insight")),
                                          _nullable(item.get("material_reference")), str(item.get("rationale") or "")))
        return decisions

    def review(self, lecture_id: str, transcripts: list[tuple[Path, str]], materials: list[LoadedMaterial], accepted: list[Note], limitations: list[str]) -> tuple[list[Note], dict[str, Any]]:
        payload = self.client.json(SYSTEM_PROMPT, REVIEW_PROMPT.format(
            lecture_id=lecture_id, limitations="; ".join(limitations) or "None",
            accepted_notes=json.dumps([n.to_dict() for n in accepted], ensure_ascii=False, indent=2),
            transcripts=self._transcripts_text(transcripts, int(self.settings.get("review_transcript_max_chars", 160_000))),
            materials=self._materials_text(materials)))
        notes: list[Note] = []
        for item in _object_list(payload, "notes"):
            classification = str(item.get("classification", "")).upper()
            if classification not in KEEP_DECISIONS:
                raise RuntimeError(f"Invalid final classification: {classification!r}")
            notes.append(Note(_required(item, "title"), _required(item, "insight"),
                              _nullable(item.get("reference")), _nullable(item.get("timestamp")),
                              str(item.get("transcript_source") or "Transcript"), classification,
                              str(item.get("evidence") or "")))
        audit = payload.get("audit_summary") if isinstance(payload.get("audit_summary"), dict) else {}
        return notes, audit

    def _accepted_notes(self, candidates: list[Candidate], decisions: list[Decision]) -> list[Note]:
        by_id = {candidate.id: candidate for candidate in candidates}
        notes: list[Note] = []
        for decision in decisions:
            if decision.decision in KEEP_DECISIONS:
                candidate = by_id[decision.candidate_id]
                notes.append(Note(candidate.topic, decision.accepted_insight or candidate.insight,
                                  decision.material_reference, candidate.timestamp, candidate.transcript_source,
                                  decision.decision, candidate.evidence))
        return notes

    def _materials_text(self, materials: list[LoadedMaterial]) -> str:
        sections = [f"--- {item.path.name} ---\n{item.text}" for item in materials if item.text]
        return _truncate_sections(sections, self.material_max_chars) or "[No readable mapped materials]"

    @staticmethod
    def _transcripts_text(transcripts: list[tuple[Path, str]], limit: int) -> str:
        return _truncate_sections([f"--- {path.name} ---\n{text}" for path, text in transcripts], limit)

    def _write_audit(self, lecture_id: str, candidates: list[Candidate], decisions: list[Decision], audit: dict[str, Any]) -> None:
        audit_dir = self.cache_dir / "audits"
        audit_dir.mkdir(parents=True, exist_ok=True)
        data = {"lecture_id": lecture_id, "candidates": [c.to_dict() for c in candidates],
                "decisions": [asdict(d) for d in decisions], "review": audit}
        (audit_dir / f"{_safe_name(lecture_id)}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def render_markdown(lecture: LectureConfig, notes: list[Note], limitations: list[str]) -> str:
        lines = [f"# {lecture.id} — Additional Professor Notes", "",
                 "**Transcripts:** " + ", ".join(path.name for path in lecture.transcripts),
                 "**Materials:** " + (", ".join(str(path) for path in lecture.materials) or "None mapped"), ""]
        if limitations:
            lines.extend(["> **Material limitations:** " + " ".join(limitations), ""])
        if not notes:
            lines.extend(["No sufficiently supported additional insights were identified.", ""])
        for note in notes:
            lines.extend([f"## {note.title}", ""])
            if note.reference:
                lines.append(f"**Reference:** {note.reference}")
            if note.timestamp:
                lines.append(f"**Timestamp:** {note.timestamp}")
            if note.reference or note.timestamp:
                lines.append("")
            lines.extend([note.insight.strip(), ""])
        return "\n".join(lines).rstrip() + "\n"


def write_index(notes_dir: Path, results: Iterable[LectureResult]) -> Path:
    notes_dir.mkdir(parents=True, exist_ok=True)
    lines = ["# Lecture Notes Index", ""]
    for result in results:
        suffix = " — material limitations reported" if result.limitations else ""
        lines.append(f"- [{result.lecture_id}]({result.notes_path.name}) ({result.final_notes} notes){suffix}")
    path = notes_dir / "INDEX.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_course_indexes(results: Iterable[LectureResult]) -> list[Path]:
    """Write one index inside each course's notes directory."""
    groups: dict[Path, list[LectureResult]] = {}
    for result in results:
        groups.setdefault(result.course_dir, []).append(result)
    return [write_index(course / "notes", group) for course, group in groups.items()]


def _chunks(text: str, size: int) -> list[str]:
    if size < 1:
        raise ValueError("Chunk size must be positive")
    paragraphs = re.split(r"(?<=\n)\s*\n", text)
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        if current and len(current) + len(paragraph) > size:
            chunks.append(current)
            current = ""
        while len(paragraph) > size:
            chunks.append(paragraph[:size])
            paragraph = paragraph[size:]
        current += paragraph
    if current or not chunks:
        chunks.append(current)
    return chunks


def _batched(items: list[Any], size: int) -> Iterable[list[Any]]:
    if size < 1:
        raise ValueError("Batch size must be positive")
    for index in range(0, len(items), size):
        yield items[index:index + size]


def _truncate_sections(sections: list[str], limit: int) -> str:
    if not sections:
        return ""
    allowance = max(1, limit // len(sections))
    rendered = [section if len(section) <= allowance else section[:allowance] + "\n[truncated]" for section in sections]
    return "\n\n".join(rendered)[:limit]


def _object_list(payload: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = payload.get(key)
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise RuntimeError(f"Model JSON field {key!r} must be a list of objects")
    return value


def _required(item: dict[str, Any], key: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Model result is missing non-empty field {key!r}")
    return value.strip()


def _nullable(value: Any) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._") or "lecture"
