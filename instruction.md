# GPU Transcription Tool

## Purpose

`transcribe.py` transcribes the video or audio files belonging to a course with one or more open speech-recognition models. It requires CUDA by default and is designed for the 8 GB NVIDIA RTX 3070 in this machine.

The supported models are:

| CLI name | Model ID | Transcript folder |
|---|---|---|
| `qwen3` | `Qwen/Qwen3-ASR-1.7B` | `Qwen3-ASR-1.7B` |
| `canary` | `nvidia/canary-qwen-2.5b` | `canary-qwen-2.5b` |
| `parakeet` | `nvidia/parakeet-tdt-0.6b-v3` | `parakeet-tdt-0.6b-v3` |
| `whisper` | `openai/whisper-large-v3` | `whisper-large-v3` |

Models are loaded and unloaded one at a time. This is important because the GPU cannot hold several of these models simultaneously.

## Folder structure

Each top-level course folder contains video and/or audio files belonging to that course. Every course folder has a `transcript` subfolder. The program creates the selected model folder when it is needed.

```text
<course>/
|-- <media-file>
`-- transcript/
    `-- <model-name>/
        `-- <media-file-stem>.txt
```

For example, transcribing `Data Mining/lecture-01.mp4` with Qwen produces:

```text
Data Mining/transcript/Qwen3-ASR-1.7B/lecture-01.txt
```

## Environment setup

The local Python 3.12 environment is `.venv`. Activate it in PowerShell and install the CUDA dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-gpu.txt
```

Model weights are not stored in this repository. The relevant library downloads them from Hugging Face the first time each model is used.

## Running the tool

Pass either one media file or one course folder, followed by the requested list of models in `--models`:

```powershell
python transcribe.py "Data Mining" --models qwen3 parakeet
python transcribe.py "Italian\lecture-01.mp4" --models whisper
python transcribe.py "Italian" --models all
```

`--models` accepts one or more of `qwen3`, `canary`, `parakeet`, and `whisper`. `all` selects all four. Use `python transcribe.py --list-models` to display the registry.

The input behavior is:

- A folder input scans only supported media files directly inside that folder. It does not recurse into subfolders.
- A file input processes only that file and uses its parent course folder to locate `transcript`.
- Supported extensions are `.aac`, `.flac`, `.m4a`, `.mka`, `.mkv`, `.mov`, `.mp3`, `.mp4`, `.mpeg`, `.mpg`, `.ogg`, `.opus`, `.wav`, `.webm`, `.wma`, and `.wmv`.
- Every input is converted temporarily to 16 kHz mono WAV with the FFmpeg binary supplied by `imageio-ffmpeg`. The temporary WAV is removed after transcription.
- Long recordings are split into sequential five-minute chunks by default so model attention fits in 8 GB of GPU memory. Override this with `--chunk-seconds`, but values below 30 seconds are rejected.
- CUDA is mandatory unless `--allow-cpu` is explicitly supplied. CPU mode is intended only for diagnosis and will be very slow for large models.
- `--language` may provide a language hint. It is used by Qwen and Whisper; Parakeet detects its supported languages automatically and Canary is English-only.

## Completion ledger and resume behavior

`transcription_status.csv` is the persistent processing ledger. Each attempt records:

- UTC timestamp
- absolute source file path
- SHA-256 source file hash
- model alias and full model ID
- status (`running`, `finished`, or `failed`)
- transcript output path
- error message, if any

Before processing, the program hashes the source file. It skips a model/file pair only when the ledger contains a matching source hash and model ID with `finished` status and the expected transcript file still exists. A changed file is processed again because its hash changes. Use `--force` to ignore a prior successful record.

An item is marked `finished` only after the transcript is written successfully. Failures are recorded and do not stop other files or other selected models. The command exits nonzero if any attempted transcription fails.

## GPU memory notes

- Inference uses half precision on CUDA.
- Models are processed sequentially and GPU memory is cleared between them.
- Canary is close to the 8 GB limit. Close other GPU-heavy applications before running it.
- Do not run multiple copies of this program at the same time against the same GPU or ledger.
