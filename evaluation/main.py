from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.pipeline import evaluate, save_results  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Reference-free comparison of four ANN2DL ASR outputs")
    parser.add_argument("--course", type=Path, default=ROOT.parent / "ANN2DL")
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    try:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError as exc:
        raise SystemExit("Run with the project .venv containing imageio-ffmpeg") from exc
    summary, rows = evaluate(args.course / "transcript", args.course, ffmpeg)
    save_results(args.output, summary, rows)
    print(f"Evaluated {len(summary['recordings'])} recordings in {len(rows)} common 30-second segments")
    print("Consensus ranking (estimated, no ground truth): " + " < ".join(summary["rankings"]["consensus_agreement"]))
    print(f"Report: {args.output / 'report.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

