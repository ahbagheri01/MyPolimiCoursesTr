"""Prompts for the three-stage lecture-note workflow."""

SYSTEM_PROMPT = """You are an academic lecture analysis agent. Preserve the professor's
added educational value: information, reasoning, intuition, examples, limitations,
corrections, practical advice, and explicit exam guidance that a student would not
adequately obtain from the supplied course materials alone.

Be source-grounded. Never add outside knowledge or invent evidence, timestamps, slide
references, or certainty. ASR may be noisy. Resolve only clear errors supported by
context or transcript agreement; otherwise preserve uncertainty. Return only valid JSON
matching the requested shape, with no Markdown fences or commentary."""

EXTRACT_PROMPT = """Stage 1 — exhaustive candidate extraction.

Read this sequential portion of one lecture. Multiple ASR versions describe the SAME
lecture and are alternate evidence, not concatenated lectures. Extract every potentially
meaningful oral contribution. Optimize for recall; do not filter against materials yet.
Preserve concrete examples and reasoning.

For each candidate return: topic, insight, brief evidence, transcript_source, timestamp
(only if supported, otherwise null), usefulness, and uncertain (boolean).
Return: {{"candidates": [...]}}.

Lecture: {lecture_id}
Chunk: {chunk_number}/{chunk_count}
ASR evidence:
{transcripts}
"""

COMPARE_PROMPT = """Stage 2 — material-aware filtering.

Compare each oral candidate's SPECIFIC meaning with mapped materials. Use semantic
comparison, not keyword overlap. Decisions: NEW, EXPANDED, EXAMPLE, REDUNDANT, or
UNCERTAIN. If partly redundant, keep only the added value in accepted_insight. Never
claim absence from a missing/unreadable material. Preserve evidence and add no facts.

Return {{"decisions": [{{"candidate_id": string, "decision": string,
"accepted_insight": string|null, "material_reference": string|null,
"rationale": string}}]}} for every candidate.

Lecture: {lecture_id}
Material limitations: {limitations}
Candidates:
{candidates}
Materials:
{materials}
"""

REVIEW_PROMPT = """Stage 3 — independent coverage and fidelity audit.

Review lecture evidence again against accepted notes and materials. Recover missed oral
additions; remove unsupported, redundant, or duplicate notes; retain useful examples and
reasoning. Every note must be traceable to professor speech and add value beyond readable
materials. Do not create notes merely to cover every section.

Return {{"notes": [{{"title": string, "insight": string,
"reference": string|null, "timestamp": string|null,
"transcript_source": string, "classification": "NEW"|"EXPANDED"|"EXAMPLE",
"evidence": string}}], "audit_summary": {{"removed": integer,
"recovered": integer, "warnings": [string]}}}}.

Lecture: {lecture_id}
Material limitations: {limitations}
Current accepted notes:
{accepted_notes}
Transcript evidence:
{transcripts}
Materials:
{materials}
"""
