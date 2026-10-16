
"""Prompts for the three-stage lecture-note workflow."""

SYSTEM_PROMPT = """You are an academic lecture analysis agent.

Your PRIMARY objective is to preserve ALL meaningful educational information the
professor communicates that a student could miss by studying the supplied course
materials alone.

This includes new facts, explanations, reasoning, intuition, concrete examples,
analogies, counterexamples, modelling choices, assumptions, limitations, corrections,
practical advice, implementation details, student-question answers, and explicit
exam guidance.

PRIORITY: MAXIMIZE RECALL OF PROFESSOR-ONLY INFORMATION.

Missing a useful oral insight is a more serious failure than including a partly
redundant insight. Do not sacrifice coverage for brevity, elegance, or unusually
strict filtering.

Distinguish between:
- A concept being mentioned in slides.
- The professor explaining that concept in an additional, meaningful way.
- The professor demonstrating the concept through a useful example.

These are NOT automatically equivalent.

A general principle does not replace a meaningful concrete example. Similarly,
an example does not replace a separate useful explanation of the underlying
mechanism. Preserve both when each adds distinct educational value.

Do not impose an arbitrary limit on the number of insights.

Be strictly source-grounded. Every extracted insight must come from what the
professor actually said, not from your general knowledge. Never invent evidence,
timestamps, slide references, technical details, or certainty.

ASR may be noisy. Resolve only clear errors supported by context or transcript
agreement; otherwise preserve uncertainty.

Return only valid JSON matching the requested shape, with no Markdown fences
or commentary."""


EXTRACT_PROMPT = """Stage 1 — HIGH-RECALL candidate extraction.

Read this sequential portion of one lecture carefully and completely.

Multiple ASR versions describe the SAME lecture and are alternate evidence,
not concatenated lectures.

Your task is to build a COMPREHENSIVE inventory of potentially meaningful oral
contributions. Optimize for recall. Do NOT filter against materials yet.

MANDATORY EXTRACTION METHOD:

1. Examine the lecture sequentially, from the beginning of the provided chunk
   to its end. Do not rely on remembering only the most prominent topics.

2. Identify every substantive explanation, observation, demonstration, example,
   argument, comparison, or practical remark that could help a student understand
   or apply the subject.

3. For EACH substantive topic, actively look for:
   - What the professor explained beyond a definition.
   - Why a method works or fails.
   - How the professor justified a claim or algorithmic step.
   - Assumptions, restrictions, and edge cases.
   - Practical implementation decisions and trade-offs.
   - Real-world applications and personal research examples.
   - Numerical examples, analogies, and counterexamples.
   - Differences between theoretically similar approaches.
   - Modelling choices and their consequences.
   - Misconceptions, warnings, and corrections.
   - Questions from students and the professor's substantive answers.
   - Explicit exam advice.

4. EXAMPLE PRESERVATION IS MANDATORY:
   When the professor provides a concrete educational example, preserve its
   specific situation, comparison, and teaching point.

   Do NOT replace an example with only its abstract conclusion.

   For instance, if the professor says two customers spend the same amount
   but shop at different frequencies, extract the actual customer example.
   Do not write only "Similarity depends on the application."

   If the example and the general reasoning add distinct value, extract both,
   or combine them while preserving all the essential information.

5. Do not ignore conversational explanations merely because they are informal.
   Informal speech often contains valuable practical insights unavailable in
   formal course materials.

6. Do not focus only on formulas, named algorithms, and technical terminology.
   Practical anecdotes, interpretation, and application-specific consequences
   are equally eligible when educationally meaningful.

7. Preserve meaningful multi-step reasoning. Do not compress it into a vague
   conclusion that loses the mechanism or the professor's important qualification.

8. Do not merge distinct educational contributions solely because they concern
   the same concept.

9. Do not remove candidates because you suspect the slides already cover them.
   That decision belongs exclusively to Stage 2.

10. Before finishing, mentally revisit the entire chunk and ask:
    - Did I miss any concrete examples?
    - Did I miss any practical advice?
    - Did I miss any explanation of why something works or fails?
    - Did I miss any modelling choices or consequences?
    - Did I miss any student questions or important qualifications?
    - Did I cover the END of the chunk as carefully as the beginning?

Do not generate candidates for meaningless filler, administrative chatter,
or repetitions that introduce no distinct educational content.

For each candidate return: topic, insight, brief evidence, transcript_source,
timestamp (only if supported, otherwise null), usefulness, and uncertain (boolean).

The insight must retain enough specificity that a later stage can recover the
professor's actual example or explanation.

The evidence must correspond to the claimed insight. Do not use a generic
passage as evidence for additional facts.

Return: {{"candidates": [...]}}.

Lecture: {lecture_id}
Chunk: {chunk_number}/{chunk_count}
ASR evidence:
{transcripts}
"""


COMPARE_PROMPT = """Stage 2 — RECALL-PRESERVING material-aware comparison.

Compare each oral candidate's SPECIFIC educational meaning with mapped
materials. Use semantic comparison, not keyword overlap.

Your goal is to identify genuine professor-only contributions WITHOUT
accidentally deleting valuable explanations or examples.

Decisions: NEW, EXPANDED, EXAMPLE, REDUNDANT, or UNCERTAIN.

IMPORTANT COMPARISON RULES:

1. The mere presence of the same topic, formula, algorithm, or terminology
   in a slide does NOT make an oral contribution redundant.

2. Distinguish what the slides STATE from what the professor EXPLAINS.

   A slide might provide an equation while the professor explains why it
   holds, when it fails, or how to interpret it. Preserve that explanation
   unless the same reasoning is adequately conveyed in the materials.

3. Compare explanations at the level of specific information, not headings.
   Ask: "Could a student reasonably learn THIS particular explanation,
   interpretation, or consequence from the materials alone?"

4. Treat useful concrete examples as independent educational contributions.

   A slide stating "distance depends on the application" does not contain
   a professor's detailed customer-shopping-frequency example.

   Preserve such examples unless the materials already adequately convey
   the same example or its distinctive teaching point.

5. Preserve oral explanations of implementation choices, practical risks,
   real-world constraints, and modelling consequences even when the
   underlying algorithm is described in the slides.

6. If a candidate contains both redundant background and new educational
   content, retain the additional information in accepted_insight.

   Do not discard a candidate merely because part of it is redundant.

7. Do not aggressively compress an accepted insight.
   Retain the concrete example, mechanism, qualification, or comparison that
   makes it valuable.

8. Use REDUNDANT only when the materials already adequately convey the
   SAME specific educational information.

9. When the available evidence does not establish redundancy, prefer
   UNCERTAIN over confidently rejecting a potentially valuable insight.

10. Missing, unreadable, or uninspected materials cannot justify a claim
    that the professor's information is absent from the materials.

11. Do not add facts, examples, or reasoning that the professor did not say.

12. Evaluate EVERY candidate individually. Do not silently omit candidates
    because several concern the same slide or concept.

DECISION GUIDANCE:

NEW:
The professor communicates specific information absent from the materials.

EXPANDED:
The materials introduce the subject, but the professor adds meaningful
reasoning, intuition, mechanisms, limitations, implications, or practical
interpretation.

EXAMPLE:
The professor supplies a concrete educational example, counterexample,
analogy, or application that adds information beyond the materials.

REDUNDANT:
The same specific educational contribution is already adequately conveyed
by the materials. Use this classification conservatively.

UNCERTAIN:
The available evidence is insufficient for a reliable classification.
Preserve the uncertainty rather than inventing certainty.

FINAL COVERAGE CHECK:

Before returning, ask whether any NEW, EXPANDED, or EXAMPLE contribution
was accidentally discarded because the general topic already appeared
in the slides.

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


REVIEW_PROMPT = """Stage 3 — INDEPENDENT OMISSION SEARCH and fidelity audit.

Your primary responsibility is to discover professor-only educational
information that the preceding stages MISSED.

Do not merely polish, summarize, or validate the currently accepted notes.

Review the complete lecture evidence AGAIN, independently and sequentially,
against the existing notes and mapped materials.

PRIMARY OBJECTIVE:
Maximize coverage of meaningful professor-only insights while ensuring that
every final note is grounded in what the professor actually said.

MANDATORY REVIEW PROCEDURE:

PASS A — INDEPENDENT TRANSCRIPT COVERAGE

1. Examine the transcript from beginning to end.

2. For every substantive lecture section, identify what the professor
   actually added through:
   - Explanations
   - Intuition
   - Intermediate reasoning
   - Practical observations
   - Modelling decisions
   - Applications
   - Examples and counterexamples
   - Assumptions and limitations
   - Failure cases
   - Implementation advice
   - Student-question answers
   - Explicit exam guidance

3. Independently compare these contributions with the mapped materials.

4. Compare the qualifying contributions with the currently accepted notes.

5. Identify any contribution that is missing or insufficiently represented.

6. In particular, check whether the current notes preserve the professor's
   SPECIFIC examples rather than only their general conclusions.

PASS B — TARGETED OMISSION SEARCH

Actively search for these common failure patterns:

- A real-world example was discarded as an irrelevant anecdote.
- A concrete example was compressed into a generic principle.
- An algorithm explanation was reduced to its final result.
- An assumption or limitation was omitted.
- A practical implementation warning was overlooked.
- A modelling decision and its consequences were omitted.
- A student question revealed a useful clarification.
- A professor compared two methods, but the comparison disappeared.
- A lecture section containing substantive additional information has no
  corresponding note.
- The final portion of the lecture was processed less thoroughly.
- Information was mistakenly rejected because the general concept
  appeared in the slides.

Recover all meaningful missing contributions.

PASS C — SOURCE-GROUNDED VERIFICATION

Check every existing and newly recovered note:

1. Is the insight supported by the professor's speech?
2. Does it preserve the professor's actual meaning?
3. Does it avoid unsupported additional claims?
4. Does it preserve important qualifications?
5. Is its concrete example or reasoning still present?
6. Is the timestamp supported, if supplied?

Correct unsupported details and factual distortions.

Merge true duplicates only when doing so does NOT lose any distinct example,
reasoning step, limitation, or practical observation.

Do NOT remove notes simply because they are somewhat redundant or lengthy.
Coverage is the priority.

PASS D — FINAL COMPLETENESS CHECK

Before finishing, ask:

- If a student reads the slides AND these notes, what meaningful things
  would they STILL miss from the professor's lecture?
- Have all distinctive educational examples been preserved?
- Have all important explanations of WHY and HOW been preserved?
- Have practical warnings and implementation insights been captured?
- Are any substantive lecture sections unjustifiably absent?
- Did I mistakenly assume an example was covered because its general
  concept appeared in the slides?

If the answer reveals a missing educational contribution, recover it.

For every recovered insight, verify transcript support and compare against
the materials before including it.

Do not invent notes merely to cover every lecture section.
Do not add outside textbook knowledge.
Do not present uncertain ASR content as established fact.

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
