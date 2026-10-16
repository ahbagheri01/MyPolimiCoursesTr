"""Data models used between workflow stages."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class LectureConfig:
    id: str
    status: str
    course_dir: Path
    transcripts: list[Path]
    materials: list[Path]


@dataclass(slots=True)
class Candidate:
    id: str
    topic: str
    insight: str
    evidence: str
    transcript_source: str
    timestamp: str | None = None
    usefulness: str = ""
    uncertain: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Decision:
    candidate_id: str
    decision: str
    accepted_insight: str | None
    material_reference: str | None
    rationale: str


@dataclass(slots=True)
class Note:
    title: str
    insight: str
    reference: str | None
    timestamp: str | None
    transcript_source: str
    classification: str
    evidence: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class LoadedMaterial:
    path: Path
    text: str
    error: str | None = None


@dataclass(slots=True)
class LectureResult:
    lecture_id: str
    course_dir: Path
    notes_path: Path
    candidates: int
    accepted_before_review: int
    final_notes: int
    limitations: list[str] = field(default_factory=list)
