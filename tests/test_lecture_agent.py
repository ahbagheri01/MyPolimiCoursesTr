from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from src.loaders import infer_course_dir, load_config
from src.models import LectureConfig
from src.workflow import LectureWorkflow, write_course_indexes


class FakeClient:
    def json(self, system: str, prompt: str) -> dict:
        if prompt.startswith("Stage 1"):
            return {"candidates": [{"topic": "Why scaling matters", "insight": "Large scales dominate distance.",
                "evidence": "the large number dominates", "transcript_source": "qwen.txt",
                "timestamp": None, "usefulness": "Avoids a mistake", "uncertain": False}]}
        if prompt.startswith("Stage 2"):
            return {"decisions": [{"candidate_id": "C0001", "decision": "EXPANDED",
                "accepted_insight": "A numerically larger feature can dominate distance.",
                "material_reference": "Scaling", "rationale": "The mechanism is extra."}]}
        return {"notes": [{"title": "Why scaling matters",
            "insight": "A numerically larger feature can dominate distance.", "reference": "Scaling",
            "timestamp": None, "transcript_source": "qwen.txt", "classification": "EXPANDED",
            "evidence": "the large number dominates"}],
            "audit_summary": {"removed": 0, "recovered": 0, "warnings": []}}


class WorkflowTest(unittest.TestCase):
    def test_course_inference_and_course_notes_output(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            course = root / "Data Mining"
            qwen = course / "transcript" / "qwen" / "lecture.txt"
            parakeet = course / "transcript" / "parakeet" / "lecture.txt"
            qwen.parent.mkdir(parents=True)
            parakeet.parent.mkdir(parents=True)
            qwen.write_text("The large number dominates.", encoding="utf-8")
            parakeet.write_text("The larger value dominates.", encoding="utf-8")
            material = course / "slides.txt"
            material.write_text("Scaling is important.", encoding="utf-8")
            self.assertEqual(infer_course_dir([qwen, parakeet]), course.resolve())

            result = LectureWorkflow(FakeClient(), root / "cache").run(
                LectureConfig("lecture_01", "INCOMPLETE", course, [qwen, parakeet], [material]))
            self.assertEqual(result.notes_path.parent, course / "notes")
            self.assertIn("A numerically larger feature", result.notes_path.read_text(encoding="utf-8"))
            indexes = write_course_indexes([result])
            self.assertEqual(indexes, [course / "notes" / "INDEX.md"])
            self.assertTrue(indexes[0].exists())

    def test_config_requires_valid_status(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            transcript = root / "Course" / "transcript" / "model" / "lecture.txt"
            transcript.parent.mkdir(parents=True)
            transcript.write_text("text", encoding="utf-8")
            config = root / "course.yaml"
            config.write_text(
                "lectures:\n  - id: one\n    status: COMPLETE\n    transcripts:\n"
                "      - Course/transcript/model/lecture.txt\n    materials: []\n",
                encoding="utf-8",
            )
            _, lectures = load_config(config)
            self.assertEqual(lectures[0].status, "COMPLETE")


if __name__ == "__main__":
    unittest.main()
