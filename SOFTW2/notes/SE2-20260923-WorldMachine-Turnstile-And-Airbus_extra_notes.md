# SE2-20260923-WorldMachine-Turnstile-And-Airbus — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260923.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf

## The Purpose of the Machine and Why Intersection is Mandatory

**Reference:** 02a.RE.pdf, slide 20-22

In the Jackson-Zave framework, the purpose of a machine always lies in the world. Consequently, the intersection between the world and the machine (shared phenomena) must be non-empty; if there were no intersection, the machine would have no means of interacting with or producing any advantage for that part of the world.

## Why Goals Cannot Be Formulated as Pure Requirements (Ambulance 14/15-min Example)

**Reference:** 02a.RE.pdf, slide 23-25

Goals often predicate over phenomena that are strictly world-only (e.g., physical arrival of an ambulance at the scene within 15 minutes). Software cannot directly observe or guarantee this outcome on its own without assuming environment cooperation (sufficient fleet size, geographical distribution, traffic conditions). When R and D fail to entail G, engineers must either renegotiate/relax the goal or add domain assumptions and software requirements (e.g., proactive periodic re-distribution of ambulances).

## Critical Architectural Impact of Flawed Domain Assumptions

**Reference:** 02a.RE.pdf, slide 29-31

In the Warsaw Airbus A320 accident, the correctness argument (R and D entail G) was logically sound, but the domain assumption 'wheels turning iff moving on runway' proved false due to aquaplaning. The professor stresses that an invalid domain assumption is particularly critical because entire architectural and design decisions are built upon it; discovering its invalidity in production often forces a complete redesign of the system.

## Subjectivity of Phenomenon Classification and Level of Abstraction

**Reference:** 02a.RE.pdf, slide 35-36

Phenomenon classification is not unique and depends on the chosen level of abstraction and physical design. For example, validating a token and acknowledging validity can be split into an internal machine phenomenon ('validates token') and an output shared phenomenon ('confirms valid token'), or combined into a single machine-controlled shared phenomenon. Similarly, door closing can be shared machine-controlled (motorized barrier) or world-only (a mechanical turnstile resetting automatically after passage).

## Two-Part Decomposition of Physical Access Invariant Proof

**Reference:** 02a.RE.pdf, slide 41-42

To prove that the physical access system satisfies the safety goal G1 (entries e <= scanned tokens s), the formal argument is split across the intermediate boundary variable 'openings' (o). First, prove e <= o using domain assumptions about human behaviour and sensor timing (DA1-DA4) and requirements R3-R5. Second, prove o <= s using requirements controlling door opening (R1, R2, R3) and initial state. Combining both yields e <= o <= s, demonstrating G1 holds.
