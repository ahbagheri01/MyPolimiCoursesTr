# Video_C: from lecture recordings to exam-ready "professor-only" notes

This repository turns recorded university lectures into short Markdown notes that contain **only what the professor said out loud that is not already in the slides or notebooks**. The idea is that a student who has carefully read every slide still learns something from these notes: intuitions, missing reasoning, examples, warnings, corrections, and explicit exam hints.

It is a two-stage pipeline:

```text
 recordings (.mp3/.mp4)                              slides / notebooks (PDF, .ipynb)
        |                                                         |
        v                                                         |
 STAGE 1  transcribe.py   (local GPU speech-to-text)              |
        |                                                         |
        v                                                         v
 <Course>/transcript/<asr-model>/<lecture>.txt  --->  STAGE 2  src/main.py  (LLM agent via OpenRouter)
                                                              |
                                                              v
                                       <Course>/notes/<lecture>_extra_notes.md  +  <Course>/notes/INDEX.md
```

- **Stage 1** runs open speech-recognition models locally on an NVIDIA GPU and writes plain-text transcripts.
- **Stage 2** sends each transcript plus its mapped slides/notebooks to an LLM, which extracts candidate insights, checks each against the materials, and audits the result. A YAML file per course tells it which transcript belongs with which slides.

Nothing here needs to be read in code to be used: everything is driven by `transcribe.py` and one YAML config per course.

---

## 1. Repository map

| Path | What it is |
|---|---|
| `transcribe.py` | Stage 1. GPU transcription CLI (five ASR models, resumable, hash ledger). |
| `run_parakeet.ps1` | Convenience script: transcribes every course folder with Parakeet, then deletes `.asr-cache/` folders. |
| `src/main.py` | Stage 2 entry point (`python src/main.py --config <course>.yaml`). |
| `src/workflow.py` | Stage 2 logic: extract, compare, review, render Markdown, write `INDEX.md`. |
| `src/prompts.py` | The three LLM prompts (extract, compare, review) and the system prompt. |
| `src/prompts.txt` | The longer natural-language specification the prompts were derived from. Documentation only; not read by code. |
| `src/llm.py` | OpenRouter/OpenAI-compatible client. Sends PDFs natively, requests JSON, repairs common JSON glitches. |
| `src/loaders.py` | Reads the YAML config, loads transcripts, extracts text from PDFs/notebooks (cached). |
| `src/models.py` | Small dataclasses passed between stages. |
| `tests/test_lecture_agent.py` | Unit tests for config loading, course inference and the workflow (uses a fake LLM, no network). |
| `data-mining.yaml`, `software-engineering-2.yaml`, `smbud.yaml`, `ann2dl.yaml` | Per-course Stage 2 configs: lecture list, transcript paths, material paths, status flags. |
| `instruction.md` | Detailed reference for Stage 1 (`transcribe.py`). |
| `intrsutaanlysy.md` | The original specification of what a good note is (the "professor-only insights" brief). Historical; may be absent in your checkout. |
| `requirements-gpu.txt` | Dependencies for Stage 1 (CUDA PyTorch, NeMo, Qwen-ASR, Whisper...). |
| `requirements-agent.txt` | Lightweight dependencies for Stage 2. |
| `.env` | Holds `OPENROUTERAPIKEY` (git-ignored). |
| `<Course>/` | One folder per course, see below. |

### Course folder layout

```text
<Course>/
|-- <recordings>.mp3 / .mp4          local only, git-ignored
|-- transcript/
|   `-- <asr-model>/<recording>.txt  committed
`-- notes/
    |-- <lecture-id>_extra_notes.md  committed, the final product
    `-- INDEX.md                     committed, links to every lecture's notes
```

Slides, PDFs and notebooks live **outside** the repository (in `E:\amirhossein\Polimi\POLIMI\<Course>\...`) and are referenced by absolute path from the YAML.

### Current state of each course

| Course folder | Recordings | Transcripts | Config | Notes |
|---|---|---|---|---|
| `Data Mining` | 9 mp3 | Parakeet (lectures 1-8) | `data-mining.yaml` | 8 lectures done (lecture 9 is not transcribed yet) |
| `SOFTW2` (Software Engineering 2) | mp3 | Parakeet (+ others) | `software-engineering-2.yaml` | 9 lectures done |
| `SMBUD` (Systems and Methods for Big and Unstructured Data) | 6 lectures + 2 Neo4j exercise sessions | Parakeet | `smbud.yaml` | 8 done |
| `ANN2DL` (Artificial Neural Networks and Deep Learning) | 6 theory lectures + 3 lab sessions | Parakeet (+ others for theory) | `ann2dl.yaml` | 9 done |
| `Multi agents` | 6 mp4 | Parakeet | none yet | not started |
| `TCS` | none committed | none | none | not started |

---

## 2. Setup

Requirements: Windows with an NVIDIA GPU (developed on an 8 GB RTX 3070), Python 3.12, and an OpenRouter API key for Stage 2.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-gpu.txt      # Stage 1 (GPU transcription)
python -m pip install -r requirements-agent.txt    # Stage 2 (note extraction)
```

Always use the project's `.venv`. Create a `.env` file in the repository root containing:

```text
OPENROUTERAPIKEY=<your key>
```

Model weights for Stage 1 are downloaded from Hugging Face on first use and are not stored in the repository.

---

## 3. Stage 1: transcription (`transcribe.py`)

Transcribes every supported media file **directly inside** a course folder (no recursion), or a single file.

```powershell
python transcribe.py "ANN2DL" --models parakeet
python transcribe.py "SMBUD\some-lecture.mp4" --models whisper
python transcribe.py "Data Mining" --models qwen3 parakeet
python transcribe.py --list-models
```

| `--models` name | Model | Notes |
|---|---|---|
| `parakeet` | `nvidia/parakeet-tdt-0.6b-v3` | The default choice in this repo; fast, good quality. |
| `qwen3` | `Qwen/Qwen3-ASR-1.7B` | Accepts `--language`. |
| `whisper` | `openai/whisper-large-v3` | Accepts `--language`. |
| `canary` | `nvidia/canary-qwen-2.5b` | English only; near the 8 GB limit; 30 s chunks. |
| `parakeet1.1b` | `nvidia/parakeet-tdt-1.1b` | English only. |
| `all` / `selected` | all five / `parakeet` then `qwen3` | Group names must be used alone. |

Behaviour worth knowing:

- Output goes to `<Course>/transcript/<model-folder>/<recording-stem>.txt`.
- Audio is converted to 16 kHz mono WAV and cut into 5-minute chunks (`--chunk-seconds`, minimum 30) so the models fit in GPU memory. Models are loaded one at a time.
- CUDA is required unless `--allow-cpu` is passed (very slow; diagnosis only).
- **Resume:** `transcription_status.csv` (a git-ignored ledger) records every attempt with the file's SHA-256. A finished model/file pair is skipped on rerun; `--force` redoes it. Interrupted files resume from per-chunk checkpoints in `<Course>/.asr-cache/`.
- Transcripts are plain text with **no timestamps** (so any timestamp in a note is the LLM's estimate from context; treat it as a pointer, not a measurement).
- `run_parakeet.ps1` runs Parakeet over all course folders and removes `.asr-cache/` afterwards.

More detail in [instruction.md](instruction.md).

---

## 4. Stage 2: the lecture analysis agent (`src/`)

### Running it

```powershell
python src/main.py --config ann2dl.yaml                      # all INCOMPLETE lectures
python src/main.py --config ann2dl.yaml --lecture <lecture-id>
```

Only lectures marked `status: INCOMPLETE` are processed. `COMPLETE` lectures are skipped, **even if you pass them with `--lecture`**. Progress is printed per lecture; the run stops at the first error.

### What happens to each lecture

1. **Load.** Read the transcript(s). PDFs are attached directly to the model as files (native PDF processing, so figures and equations are seen, not just extracted text). Notebooks and text files are flattened to text (cells plus outputs) and cached.
2. **Stage 1: extract candidates.** The LLM reads the whole transcript and lists every potentially valuable oral contribution, each with a quote as evidence. Candidates **without a supporting quote are discarded** (anti-hallucination guard). The prompt is tuned for high recall.
3. **Stage 2: compare with materials.** Candidates are checked in batches of 20 against the slides/notebooks and labelled `NEW`, `EXPANDED`, `EXAMPLE`, `REDUNDANT` or `UNCERTAIN`. Only the first three are kept.
4. **Stage 3: review/audit.** The LLM sees the kept notes again together with the full transcript and materials, removes duplicates and unsupported items, can recover missed insights, and returns the final notes.
5. **Write.** `<Course>/notes/<lecture-id>_extra_notes.md` is written, and the full audit trail (every candidate, every decision, the review summary) is saved to `.lecture-agent-cache/audits/<lecture-id>.json` (git-ignored) so you can see why something was dropped.

After the run, `<Course>/notes/INDEX.md` is rewritten (see Gotchas).

### Note format

Each note file looks like:

```text
# <lecture-id> — Additional Professor Notes
**Transcripts:** ...   **Materials:** ...
## <Specific topic>
**Reference:** Slide 52 (...)        <- where in the materials this relates
**Timestamp:** ...                    <- approximate, may be absent
<the extra insight, in prose>
```

If a mapped material is missing or unreadable, a "Material limitations" line is added at the top of the note instead of failing silently.

### The YAML config

One file per course. Minimal example:

```yaml
llm:
  model: google/gemini-3.8-flash        # any OpenRouter model id
  base_url: https://openrouter.ai/api/v1
  api_key_env: OPENROUTERAPIKEY         # name of the variable in .env
  temperature: 0.1
  max_tokens: 24000                     # cap per response; keeps credit reservation sane
  pdf_engine: native                    # send PDFs straight to the model
  reasoning: {effort: minimal, exclude: true}   # optional, provider-specific

cache_dir: .lecture-agent-cache

workflow:                               # 0 = unlimited (send everything in full)
  transcript_chunk_chars: 0
  material_max_chars: 0
  review_transcript_max_chars: 0
  candidate_batch_size: 20

lectures:
  - id: ANN2DL-20260924-Backpropagation-LossFunctions   # unique; also the note filename
    status: INCOMPLETE                  # INCOMPLETE = will run, COMPLETE = skipped
    course: ANN2DL                      # course folder (notes go to <course>/notes/)
    transcripts:                        # one or more ASR versions of the SAME lecture
      - "ANN2DL/transcript/parakeet-tdt-0.6b-v3/<recording>.txt"
    materials:                          # PDFs, notebooks, text files, or whole directories
      - 'E:\amirhossein\Polimi\POLIMI\ANN2DL\02 - Perceptron2NeuralNetworks.pdf'
      - 'E:\amirhossein\Polimi\POLIMI\ANN2DL\03 - NeuralNetworksTraining.pdf'
```

Rules: relative paths are relative to the YAML file; every lecture needs `id`, `status` and at least one transcript; `materials` may be empty (then everything counts as new); a directory in `materials` is scanned recursively for supported files (`.pdf .ipynb .txt .md .py .csv .json ...`); if several transcripts are listed, the first is primary and the others are treated as alternate evidence, aligned only approximately.

---

## 5. How to add a new course (the whole workflow)

1. Put the recordings in `<Course>/` (e.g. `Multi agents/`).
2. Transcribe: `python transcribe.py "<Course>" --models parakeet`.
3. Collect the slides/notebooks somewhere and note their absolute paths.
4. **Map each recording to its materials.** Use the course schedule for dates and topics, then confirm by reading the start and end of each transcript (the professor usually recaps and previews). Lectures often span two decks; map both. Lab/exercise recordings map to their notebooks or exercise PDFs.
5. Copy an existing YAML (e.g. `smbud.yaml`) to `<course>.yaml`, edit the lecture list, set every lecture `INCOMPLETE`.
6. Run `python src/main.py --config <course>.yaml`.
7. Read the output in `<Course>/notes/`, spot-check a couple of notes against the transcript, and set finished lectures to `COMPLETE`.
8. Commit the notes, the YAML and the transcripts (recordings are git-ignored).

---

## 6. Known gotchas and limits

- **`INDEX.md` only lists the lectures processed in the latest run.** It is rewritten from that run's results. If you process a course in several runs, re-add the earlier lectures by hand (or rerun everything).
- **Failures are all-or-nothing per lecture.** Intermediate candidates are not cached, so a failed lecture is re-paid from the start. Do not flip statuses to `COMPLETE` until the log shows the lecture was written.
- **Quotes and timestamps are not machine-verified.** The code checks that an evidence quote exists, not that it appears in the transcript. Spot-check important notes.
- **Audio only.** Live coding, board work and screen demos (Alloy, notebooks, Neo4j sessions) are only partly captured by speech, so exercise-session notes are thinner.
- **Mapping is manual.** A wrong lecture-to-slides mapping silently skews the "already covered vs. new" decisions.
- **JSON hiccups.** Models sometimes return invalid JSON (stray backslashes, trailing text). `src/llm.py` repairs both cases; anything else aborts the run with the error shown.
- **Transcription is non-recursive** and must not be run twice at once against the same GPU or ledger.
- Windows paths in YAML are safest in single quotes, as in the examples.

---

## 7. Tests

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_lecture_agent
```

The tests use a fake LLM client, so they need no network or API key.

---

## 8. What is committed and what is not

Committed: transcripts, final notes and indexes, YAML configs, source code, docs.
Git-ignored: recordings (`.mp3`, `.mp4`, ...), `.venv/`, `.env`, `.asr-cache/`, `.lecture-agent-cache/` (including the audit JSONs), `transcription_status.csv`, `__pycache__/`.
