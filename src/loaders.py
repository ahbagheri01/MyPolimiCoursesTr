"""Configuration, transcript, and course-material loading."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import yaml

from .models import LectureConfig, LoadedMaterial

TEXT_EXTENSIONS = {".txt", ".md", ".rst", ".py", ".html", ".htm", ".csv", ".json", ".yaml", ".yml"}
MATERIAL_EXTENSIONS = TEXT_EXTENSIONS | {".pdf", ".ipynb"}


def load_config(path: Path) -> tuple[dict[str, Any], list[LectureConfig]]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict) or not isinstance(raw.get("lectures"), list):
        raise ValueError("Configuration must contain a 'lectures' list")
    base = path.parent.resolve()
    lectures: list[LectureConfig] = []
    seen: set[str] = set()
    for index, item in enumerate(raw["lectures"], 1):
        if not isinstance(item, dict) or not item.get("id"):
            raise ValueError(f"Lecture #{index} must be a mapping with an id")
        lecture_id = str(item["id"])
        if lecture_id in seen:
            raise ValueError(f"Duplicate lecture id: {lecture_id}")
        seen.add(lecture_id)
        status = str(item.get("status", "")).upper()
        if status not in {"COMPLETE", "INCOMPLETE"}:
            raise ValueError(
                f"Lecture {lecture_id!r} needs status: COMPLETE or status: INCOMPLETE"
            )
        transcripts = [_resolve(base, value) for value in _string_list(item.get("transcripts"), lecture_id, "transcripts")]
        materials = [_resolve(base, value) for value in _string_list(item.get("materials", []), lecture_id, "materials")]
        course_dir = _resolve(base, str(item["course"])) if item.get("course") else infer_course_dir(transcripts)
        lectures.append(LectureConfig(lecture_id, status, course_dir, transcripts, materials))
    return raw, lectures


def _string_list(value: Any, lecture_id: str, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
        raise ValueError(f"Lecture {lecture_id!r} field {field!r} must be a list of paths")
    if field == "transcripts" and not value:
        raise ValueError(f"Lecture {lecture_id!r} needs at least one transcript")
    return value


def _resolve(base: Path, value: str) -> Path:
    path = Path(value).expanduser()
    return (base / path).resolve() if not path.is_absolute() else path.resolve()


def infer_course_dir(transcripts: list[Path]) -> Path:
    """Infer ``<course>`` from ``<course>/transcript/<model>/<file>`` paths."""
    inferred: list[Path] = []
    for transcript in transcripts:
        transcript_parent = next((parent for parent in transcript.parents if parent.name.casefold() == "transcript"), None)
        if transcript_parent is None:
            raise ValueError(
                f"Cannot infer course folder from {transcript}. Add 'course: path/to/course' to this lecture."
            )
        inferred.append(transcript_parent.parent.resolve())
    first = inferred[0]
    if any(path != first for path in inferred[1:]):
        raise ValueError("All ASR transcripts for one lecture must belong to the same course folder")
    return first


def expand_material_paths(paths: Iterable[Path]) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    limitations: list[str] = []
    for path in paths:
        if not path.exists():
            limitations.append(f"Missing material: {path}")
        elif path.is_dir():
            matches = sorted(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in MATERIAL_EXTENSIONS)
            if not matches:
                limitations.append(f"No supported materials found in directory: {path}")
            files.extend(matches)
        elif path.suffix.lower() in MATERIAL_EXTENSIONS:
            files.append(path)
        else:
            limitations.append(f"Unsupported material type: {path}")
    return list(dict.fromkeys(files)), limitations


def load_transcripts(paths: Iterable[Path]) -> list[tuple[Path, str]]:
    result: list[tuple[Path, str]] = []
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(f"Transcript not found: {path}")
        result.append((path, path.read_text(encoding="utf-8-sig", errors="replace")))
    return result


def load_material(path: Path, cache_dir: Path) -> LoadedMaterial:
    cache_dir.mkdir(parents=True, exist_ok=True)
    stat = path.stat()
    cache_key = hashlib.sha256(f"{path.resolve()}|{stat.st_size}|{stat.st_mtime_ns}".encode()).hexdigest()
    cache_file = cache_dir / f"{cache_key}.json"
    if cache_file.exists():
        cached = json.loads(cache_file.read_text(encoding="utf-8"))
        return LoadedMaterial(path, cached["text"], cached.get("error"))
    try:
        text = _extract_material(path)
        error = None if text.strip() else "No extractable text found"
    except Exception as exc:
        text, error = "", f"{type(exc).__name__}: {exc}"
    cache_file.write_text(json.dumps({"text": text, "error": error}, ensure_ascii=False), encoding="utf-8")
    return LoadedMaterial(path, text, error)


def _extract_material(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        import pymupdf

        with pymupdf.open(path) as document:
            return "\n\n".join(f"[Page {i + 1}]\n{page.get_text('text')}" for i, page in enumerate(document))
    if suffix == ".ipynb":
        import nbformat

        notebook = nbformat.read(path, as_version=4)
        parts: list[str] = []
        for index, cell in enumerate(notebook.cells, 1):
            parts.append(f"[Cell {index}: {cell.cell_type}]\n{cell.source}")
            if cell.cell_type == "code":
                for output in cell.get("outputs", []):
                    if "text" in output:
                        parts.append(f"[Cell {index} output]\n{output['text']}")
                    elif "data" in output and "text/plain" in output["data"]:
                        parts.append(f"[Cell {index} output]\n{output['data']['text/plain']}")
        return "\n\n".join(parts)
    return path.read_text(encoding="utf-8-sig", errors="replace")
