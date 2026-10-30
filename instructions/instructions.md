# instructions.md — How Claude Writes "Professor-Only" Lecture Notes By Hand

This file is for **Claude** (the assistant working in this repository). It explains how to do the
lecture-note task **manually**: read the transcripts and course materials yourself and write the
notes yourself.

> Not to be confused with `transcribe_instructions.md` (same folder), which documents Stage 1 transcription (`transcribe.py`).

---

## 0. Hard rules (read first)

1. **Do not run the pipeline.** Do not run `src/main.py`, `transcribe.py`, the tests, or any script
   that calls an LLM API (OpenRouter, etc.). Do not read or use the key in `.env`.
   You *are* the analysis agent. The code in `src/` is only a reference for the method and the
   output format.
2. **Do not invent anything.** Every note must trace back to something the professor actually said
   in the transcript. Background knowledge may help you *understand* a passage, never to *add* content.
3. **Do not overwrite finished work without asking.** If a lecture is `status: COMPLETE` in its
   YAML, or its `_extra_notes.md` already exists, ask the user before regenerating it.
4. **Read everything you rely on.** Never call something "not in the slides" if you did not
   actually open and read the relevant slides. If a material is missing or unreadable, say so in
   the notes (see §7).
5. **Recall first, then filter.** Missing a useful oral insight is worse than keeping a partly
   redundant one. But a note that just restates a slide adds nothing, so leave it out.
6. **Materials = the professors' slides and notes only.** Never use a textbook (e.g.
   `Multiagent Systems.pdf`), external papers, or past exams as materials, even if the schedule
   points to them. If a lecture has no slides yet, do not substitute the book: leave the lecture
   out and tell the user.
7. Ask the user only when blocked (e.g., unknown material mapping, ambiguous lecture identity).
   Otherwise proceed.

---

## 1. The goal in one paragraph

Imagine **Student A** who only studies the slides/notebooks, and **Student B** who studies them
*and* attends every lecture. Write the notes that give Student A everything extra Student B gained:
explanations of *why/how*, intuition, concrete examples, counterexamples, assumptions, limitations,
corrections to slides, practical/implementation advice, comparisons between methods, answers to
student questions, and **explicit** exam/grading guidance. Capture the professor's unique
contribution as **completely** as possible, written as **concisely** as possible.

You are not a summarizer, not a transcriber, and not a textbook writer.

---

## 2. Where everything lives

| Thing | Location |
|---|---|
| Course configs (lecture ↔ transcript ↔ materials mapping) | Inside each course folder: `ANN2DL/ann2dl.yaml`, `Data Mining/data-mining.yaml`, `SMBUD/smbud.yaml`, `SOFTW2/software-engineering-2.yaml`, `Multi agents/multi-agents.yaml`. Relative paths in a YAML (transcripts, `course: .`) are relative to that course folder. |
| Transcripts | `<Course>/transcript/<asr-model>/<recording>.txt` (prefer `parakeet-tdt-0.6b-v3`; other model folders, if present, are alternate versions of the **same** lecture) |
| Course materials (slides, PDFs, notebooks) | Outside the repo: `E:\amirhossein\Polimi\POLIMI\<Course>\...` (absolute paths are in the YAML) |
| Output notes | `<Course>/notes/<lecture-id>_extra_notes.md` |
| Course index | `<Course>/notes/INDEX.md` |
| Your working files (not committed) | `.lecture-agent-cache/manual/<lecture-id>/` (folder is git-ignored) |
| Original long specification | `src/prompts.txt` (re-read it if in doubt about what counts as valuable) |
| Stage prompts used by the code | `src/prompts.py` (same method, condensed) |

Course folders in this repo: `ANN2DL`, `Data Mining`, `SMBUD`, `SOFTW2`, `Multi agents`, `TCS`.
`TCS` has **no YAML yet**. For it, find matching materials under
`E:\amirhossein\Polimi\POLIMI\Theoretical computer science` and confirm the mapping with the user
before writing notes, unless it is obvious from dates/file names. For `Multi agents`, the course
schedule is `Multi agents/Multiagent Systems 2026-2027 Schedule.pdf`.

Transcripts are plain text, roughly 50–70k characters, about 20 long lines each, and have **no
timestamps**. They can be read with the Read tool in one go or in a few parts.

---

## 3. Picking the work

1. Open the course YAML. Lectures with `status: INCOMPLETE` are pending. Ones with
   `status: COMPLETE` are done (see Hard rule 3).
2. If the user names a lecture/course, do that one. Otherwise list the pending lectures and do
   them in chronological order.
3. Do **one lecture at a time, fully** (all steps in §4) before starting the next.
4. If a transcript file listed in the YAML does not exist, stop on that lecture and tell the user.

---

## 4. Per-lecture procedure

Create `.lecture-agent-cache/manual/<lecture-id>/` and keep working notes there. This survives
context compaction across a long session, so write to it as you go.

### Step 1 — Inventory the materials (read them first)

- Resolve every path in `materials:`. A directory means: recursively include all `.pdf`, `.ipynb`,
  `.md`, `.txt`, `.py`, `.html`, `.csv`, `.json`, `.yaml` files inside it.
- **PDFs:** read with the Read tool using `pages` (max 20 pages per call, e.g. `1-20`, `21-40`, …)
  until the end. Look at the slides, not just their text: figures and worked examples matter.
- **Notebooks (`.ipynb`):** read the cells *and* the outputs (markdown explanations, code comments).
- Write `materials.md` in the working folder: a compact per-slide/per-cell inventory, e.g.
  `01-DeepLearningIntro.pdf p.12: perceptron = weighted sum + step; figure of Rosenblatt; no derivation`.
  Record what each slide **states**, what examples it **already shows**, and what it **omits**
  (no proof, no intuition, no numbers…). This is what you will compare against.
- A material may be shared by several lectures (e.g., one slide deck spans two days). Professors
  may skip slides or go out of order, so do not assume the transcript follows slide order.
- Record any missing/unreadable file as a **limitation**.

### Step 2 — Read the full transcript sequentially

- Read the primary transcript from the **first** to the **last** character. Do not skim the end.
  The end of a lecture often has exam hints, corrections, and Q&A.
- If alternate ASR transcripts exist for the same lecture, use them to resolve garbled passages
  (technical terms, numbers, formulas). Do not treat them as extra lectures.
- ASR noise: fix only **clear** errors supported by context or by agreement between transcripts
  (e.g., "back propagation" for "back pro gay shun"). If a meaningful statement stays ambiguous,
  keep it but mark it as uncertain ("the transcript suggests…", "(ASR unclear)").
- Ignore administrative chatter and audio checks *unless* they contain real information
  (exam dates/format, grading rules, project rules, what can be skipped). Those count.

### Step 3 — Extract candidates (high recall, no filtering yet)

Go through the transcript in order. For **each** substantive passage, ask whether the professor:

- explained *why* a method works, or *why* it fails;
- justified a step, derived something, or gave intermediate reasoning;
- stated assumptions, restrictions, edge cases, failure cases;
- gave practical/implementation advice, trade-offs, parameter choices and their consequences;
- gave a real-world application, a personal research story with a teaching point, a numerical
  example, an analogy, a counterexample;
- compared two similar methods or concepts;
- explained a modelling choice and what follows from it;
- warned about a misconception, or corrected the slides;
- answered a student question with substance;
- gave **explicit** exam/grading/project guidance.

Write each candidate in `candidates.md` as:

```
C012 | topic | specific insight (keep the concrete example/mechanism) | evidence: short quote or close paraphrase + rough position (e.g. "line 7", "~40% in") | uncertain: yes/no
```

Rules for this step:

- **Do not** drop candidates because you think the slides cover them. That is decided in Step 4.
- **Do not** merge distinct contributions just because they share a concept.
- **Preserve examples literally.** If the professor says two customers spend the same weekly amount
  but one shops daily and one weekly, write *that*, not "similarity depends on the application".
- Keep the mechanism. Write "with Euclidean distance a feature on a larger numeric scale dominates
  even if it's not more important, so scaling changes implicit feature weights", not "scaling
  affects clustering".
- Before moving on, revisit the whole transcript and ask: did I miss examples? practical advice?
  why/how explanations? Q&A? qualifications? Did I treat the last third as carefully as the first?

### Step 4 — Compare every candidate against the materials

For each candidate, look up the relevant slides/cells in `materials.md` (and reopen the PDF page
when needed). Ask: **"Could a student learn THIS specific explanation, example, or consequence
from the materials alone?"** Compare meaning, not keywords.

Classify:

| Label | Meaning | Keep? |
|---|---|---|
| **NEW** | Information absent from the materials | Yes |
| **EXPANDED** | Topic is on the slides, but the professor adds reasoning, intuition, mechanism, limitations, implications, or interpretation | Yes, but keep **only the added part** |
| **EXAMPLE** | A concrete example, counterexample, analogy, or application not in the materials | Yes |
| **REDUNDANT** | The *same specific* content is already adequately in the materials (including the professor just reading/paraphrasing the slide) | No |
| **UNCERTAIN** | Transcript too garbled, or evidence too thin | Keep only if important, worded cautiously and flagged; otherwise drop |

Key comparison rules:

- A formula or algorithm being on a slide does **not** make the professor's explanation of *why it
  holds / when it fails / how to read it* redundant.
- A general slide statement does **not** cover a specific spoken example.
- If a candidate is partly redundant, keep the non-redundant part.
- If you could not inspect the relevant material, you cannot call the candidate REDUNDANT. Treat it as
  NEW/EXPANDED and note the limitation.
- Record the decision and the slide/page reference next to each candidate in `candidates.md`.

### Step 5 — Write the notes

Turn the kept candidates into the Markdown file (format in §5):

- Organize by **topic**, roughly in lecture order. Not one note per transcript paragraph.
- Merge true duplicates (the professor repeating the same point) but **never** lose a distinct
  example, reasoning step, limitation, or qualification while merging.
- Usually one short paragraph or 1–4 bullets per note. Make it longer only when needed to keep an
  example or a multi-step argument intact.
- Write in clear exam-revision English. Do not copy spoken language verbatim unless the exact phrasing
  matters (e.g., a definition the professor insists on, or an exam statement).
- Include formulas only when they add something not on the slides. Define symbols. Never add a
  derivation of your own as if the professor gave it.
- Exam importance: state it **only** if the professor said so explicitly ("this will be in the
  exam", "you must know how to…", "you can skip…"). Time spent on a topic is not evidence.
- No notes count target. The right number is however many real contributions there were.

### Step 6 — Independent second pass (mandatory)

Re-read the **whole transcript again** from start to end with the draft notes beside you. Look for:

- a lecture section with substantive extra content but no note;
- an example that got compressed into a generic principle;
- an algorithm explanation reduced to its final result;
- a dropped assumption, limitation, warning, or modelling consequence;
- a comparison between two methods that disappeared;
- a student question whose answer clarified something;
- something rejected only because the general topic appeared on a slide;
- the final part of the lecture handled less carefully.

Recover what is missing (verify against transcript and materials first). Then verify **every**
note: Is it supported by the speech? Does it keep the professor's meaning and qualifications? Does
it avoid unsupported additions? Is its reference correct? Fix or remove as needed.

Final question: *"If a student reads the slides AND these notes, what meaningful thing would they
still miss from this lecture?"* If the answer is not "nothing", go back.

### Step 7 — Save and update

1. Write `<Course>/notes/<lecture-id>_extra_notes.md` (create `notes/` if needed).
   File name: the lecture id with anything other than `A-Z a-z 0-9 . _ -` replaced by `_`.
2. Update `<Course>/notes/INDEX.md` (format in §6). Add or replace this lecture's line, keep
   other lines, keep chronological order, and keep the note count correct.
3. In the course YAML, change this lecture's `status: INCOMPLETE` to `status: COMPLETE` so the
   pipeline won't overwrite it later. Change nothing else in the YAML.
4. Optionally write `audit.md` in the working folder: candidate count, kept, redundant, uncertain,
   recovered in second pass, limitations.
5. Do **not** commit unless the user asks.
6. Tell the user in 2–4 lines: which lecture, how many notes, any limitations or uncertain points.

---

## 5. Output file format (must match existing notes)

The existing notes (written by `render_markdown` in `src/workflow.py`) look like this. Match it
exactly so the courses stay consistent:

```markdown
# <lecture-id> — Additional Professor Notes

**Transcripts:** <transcript file name(s), comma-separated, names only>
**Materials:** <material paths exactly as in the YAML, comma-separated, or "None mapped">

> **Material limitations:** <only if any: missing/unreadable files, etc.>

## <Descriptive topic/insight title>

**Reference:** <material file name, slide/page or notebook cell>
**Timestamp:** <omit this line: transcripts have no timestamps; never invent one>

<Concise explanation of what the professor added, keeping the concrete example or reasoning.>

## <Next title>
...
```

Details:

- The header line uses an em dash `—`.
- Omit the `**Reference:**` line if there is no related material (pure NEW content such as an
  anecdote with a teaching point). Use `**Reference:** None (not in slides)` only if it adds clarity.
- Leave one blank line between blocks. The file ends with one newline.
- If truly nothing qualifies, the body is the single line:
  `No sufficiently supported additional insights were identified.`
- Titles should say *what the insight is* ("Why ReLU Avoids Vanishing Gradients in Deep Nets"), not
  just the topic name ("ReLU").
- Uncertain content: phrase it cautiously and add `(ASR unclear)` or "uncertain" inside the text.

## 6. INDEX.md format

```markdown
# Lecture Notes Index

- [<lecture-id>](<lecture-id>_extra_notes.md) (<N> notes)
- [<lecture-id>](<lecture-id>_extra_notes.md) (<N> notes) — material limitations reported
```

## 7. Limitations

Report under `> **Material limitations:**` in the lecture file, and append
` — material limitations reported` to the index line, whenever:

- a mapped material file/folder does not exist or cannot be read;
- a PDF is image-only and unreadable;
- no materials are mapped (then every note is effectively NEW; say so).

Never claim something is absent from materials you could not inspect.

Do **not** put coverage remarks in the limitations line (which slides the lecture reached, slide
numbering quirks, transcript gaps). If those are worth stating, use a separate line
`> **Coverage notes:** ...` instead. It does not trigger the index flag.

---

## 8. Quality checklist (run before saving each lecture)

**Completeness**
- [ ] Read every mapped material fully.
- [ ] Read the full transcript twice (extraction + second pass), including the end.
- [ ] Concrete examples kept as examples, not reduced to conclusions.
- [ ] Why/how reasoning, assumptions, limitations, warnings, comparisons, Q&A captured.
- [ ] Explicit exam/grading/project rules captured.

**Non-redundancy**
- [ ] Each note adds something beyond the materials.
- [ ] For EXPANDED notes, only the added part is written, not the whole slide.
- [ ] No duplicate notes. Merges lost nothing.

**Faithfulness**
- [ ] Every note traces to the transcript. No outside textbook facts, no invented examples.
- [ ] No invented timestamps, slide numbers, or exam importance.
- [ ] Ambiguous ASR marked as uncertain.

**Format**
- [ ] Matches §5 exactly, file name correct, INDEX.md updated, YAML status flipped.

---

## 9. Good vs. bad notes (calibration)

**Bad** (generic, loses the teaching point):
> Distance metrics are application-dependent.

**Good** (keeps the professor's example):
> **Similarity depends on what behaviour matters:** two customers who spend the same amount per week
> can behave very differently if one shops every day and the other once a week. Comparing only total
> expenditure hides this, so the features/distance must reflect the behaviour you care about.

**Bad** (restates the slide):
> Dropout randomly switches off neurons during training.

**Good** (only the added reasoning, if the professor said it):
> The professor explained dropout as training an implicit ensemble of sub-networks: since a neuron
> cannot rely on any specific other neuron being present, it is forced to learn features that are
> useful on their own, which is where the regularization effect comes from.

**Bad** (invented importance):
> This is a very important exam topic.

**Good** (only when said explicitly):
> The professor stated that the exam will ask to compute one backpropagation step by hand on a small network.

(These are calibration examples, not content to copy into notes.)
