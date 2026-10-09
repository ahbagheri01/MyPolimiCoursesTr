# Reference-free ASR evaluation

This project compares the four transcript sets in `ANN2DL/transcript` without
claiming ground-truth accuracy. It produces pairwise disagreement, leave-one-out
consensus pseudo-WER, segment diagnostics, bootstrap intervals, JSON/CSV output,
and an HTML report.

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe evaluation\main.py
```

Outputs are written to `evaluation/results/`.

## Interpretation

- Lower pairwise disagreement and pseudo-WER mean closer agreement with the
  other systems; they are not measured WER.
- The consensus is the medoid transcript among the other three models for each
  segment. This avoids inventing words through unconstrained voting.
- Canary output already has 30-second lines. The other models have five-minute
  lines, which are divided proportionally by word count into ten 30-second
  windows. Those sub-line timestamps are approximate because the original
  transcripts contain no word timestamps.
- Hallucination and omission flags in Phase 1 are text-consensus heuristics.
  Audio-conditioned VAD and an independently validated quality estimator remain
  future modules and are reported as unavailable rather than fabricated.

