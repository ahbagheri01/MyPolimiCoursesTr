# GPU Course Transcription

`transcribe.py` transcribes every supported audio or video file directly inside a course folder. It supports five open speech-recognition models and processes them one at a time to fit an 8 GB NVIDIA GPU.

## Supported models

| CLI name | Model |
|---|---|
| `qwen3` | `Qwen/Qwen3-ASR-1.7B` |
| `canary` | `nvidia/canary-qwen-2.5b` |
| `parakeet` | `nvidia/parakeet-tdt-0.6b-v3` |
| `parakeet1.1b` | `nvidia/parakeet-tdt-1.1b` (English only) |
| `whisper` | `openai/whisper-large-v3` |

## Installation

Python 3.12 and a CUDA-capable PyTorch installation are expected. On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-gpu.txt
```

The model libraries download weights from Hugging Face on first use. Model files are not stored in this repository.

## Usage

Activate the environment, then provide either a course folder or one media file:

```powershell
.\.venv\Scripts\Activate.ps1
python transcribe.py "E:\amirhossein\Polimi\Video_C\ANN2DL" --models whisper
```

Run all five models sequentially:

```powershell
python transcribe.py "E:\amirhossein\Polimi\Video_C\ANN2DL" --models all
```

Run selected models:

```powershell
python transcribe.py "ANN2DL" --models qwen3 parakeet whisper
```

Run the English-only 1.1B Parakeet model:

```powershell
python transcribe.py "ANN2DL" --models parakeet1.1b
```

Run the selected model group (Parakeet 0.6B v3, then Qwen3-ASR-1.7B):

```powershell
python transcribe.py "SOFTW2" --models selected
```

Useful options:

```text
--language en         Language hint for Qwen and Whisper
--chunk-seconds 300   Audio chunk duration; minimum 30 seconds
--force               Reprocess completed model/file pairs
--allow-cpu           Allow very slow CPU inference when CUDA is unavailable
--list-models         Display the model registry
```

## Output and resume behavior

Transcripts are written beside each course's recordings:

```text
ANN2DL/
`-- transcript/
    |-- Qwen3-ASR-1.7B/
    |-- canary-qwen-2.5b/
    |-- parakeet-tdt-0.6b-v3/
    |-- parakeet-tdt-1.1b/
    `-- whisper-large-v3/
```

The local `transcription_status.csv` ledger records running, completed, and failed attempts. A completed transcript is skipped on later runs when the source hash, model, and output file still match. Use `--force` to run it again. The ledger is intentionally excluded from Git because it contains machine-specific absolute paths.

Interrupted lectures resume from saved chunk transcripts in the course's local `.asr-cache/` folder. Checkpoints are keyed by source SHA-256, model ID, chunk duration, and language. Audio chunks remain available after failure and are removed after successful completion; chunk transcripts are retained. Rerun the same command to resume. `--force` discards matching chunk transcripts and transcribes again. The cache is excluded from Git.

## Notes

- CUDA is required unless `--allow-cpu` is supplied.
- Input folders are scanned non-recursively.
- Long recordings are normalized to 16 kHz mono WAV and split into five-minute chunks by default.
- Canary uses its SALM loader and caps chunks at 30 seconds, including when running `--models all`.
- Models are loaded and released sequentially. Do not run multiple copies against the same GPU or ledger.
- The Whisper loader reads normalized WAV chunks directly with `soundfile`, so a system-wide FFmpeg installation is unnecessary.

## Lecture analysis agent

The `src` package compares one or more ASR transcripts for each lecture with mapped
PDFs, notebooks, and text/code materials. It performs candidate extraction, semantic
material comparison, and a second-pass coverage audit before writing concise Markdown.

Install its lightweight dependencies separately from the GPU transcription stack:

```powershell
python -m pip install -r requirements-agent.txt
```

Copy `src/course.example.yaml`, update the transcript/material paths and model, then run:

```powershell
python src/main.py --config course.yaml
python src/main.py --config course.yaml --lecture lecture_03
```

Transcript paths normally follow `<course>/transcript/<ASR model>/<lecture>.txt`. The
course folder can be supplied with `course:` in YAML or inferred from that structure.
The agent creates `<course>/notes/` automatically and writes each lecture note plus that
course's `INDEX.md` there. The API key is read from `OPENROUTERAPIKEY` in `.env` by
default. Extracted material and internal evidence audits are cached in
`.lecture-agent-cache`.

Every lecture entry must contain `status: INCOMPLETE` or `status: COMPLETE`. Completed
lectures are skipped, including when selected explicitly with `--lecture`.
