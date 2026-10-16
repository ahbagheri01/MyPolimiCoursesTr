"""Command-line entry point for the lecture analysis agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from src.llm import LLMClient
    from src.loaders import load_config
    from src.workflow import LectureWorkflow, write_course_indexes
else:
    from .llm import LLMClient
    from .loaders import load_config
    from .workflow import LectureWorkflow, write_course_indexes


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Extract the professor's added educational value from lectures.")
    result.add_argument("--config", type=Path, required=True, help="YAML course configuration")
    result.add_argument("--lecture", help="Process only this lecture id")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        from dotenv import load_dotenv
    except ImportError:
        load_dotenv = None
    if load_dotenv is not None:
        load_dotenv()
    try:
        raw, lectures = load_config(args.config.resolve())
        if args.lecture:
            lectures = [lecture for lecture in lectures if lecture.id == args.lecture]
            if not lectures:
                raise ValueError(f"Lecture not found in configuration: {args.lecture}")
        complete = [lecture for lecture in lectures if lecture.status == "COMPLETE"]
        for lecture in complete:
            print(f"Skipping {lecture.id} (COMPLETE)")
        lectures = [lecture for lecture in lectures if lecture.status == "INCOMPLETE"]
        if not lectures:
            print("No incomplete lectures to process.")
            return 0
        base = args.config.resolve().parent
        cache_dir = (base / raw.get("cache_dir", ".lecture-agent-cache")).resolve()
        workflow = LectureWorkflow(LLMClient(raw.get("llm", {})), cache_dir, raw.get("workflow", {}))
        results = []
        for lecture in lectures:
            print(f"Processing {lecture.id} ...", flush=True)
            result = workflow.run(lecture)
            results.append(result)
            print(f"  wrote {result.notes_path} ({result.final_notes} notes)", flush=True)
        for index in write_course_indexes(results):
            print(f"Wrote {index}")
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
