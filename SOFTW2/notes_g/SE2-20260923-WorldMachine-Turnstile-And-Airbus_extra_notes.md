# SE2-20260923-WorldMachine-Turnstile-And-Airbus — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260923.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf

## Resolving Unfulfillable Goals in Ambulance Dispatching

**Reference:** 02a.RE.pdf page 24, 25

When analyzing the ambulance dispatching system, the professor points out that the software and existing assumptions cannot mathematically or operationally guarantee the 15-minute arrival goal (e.g., driver delays, traffic, distance). When a goal cannot be entailed by R and D (R ∧ D ⊭ G), the engineer has two main options: (1) iterate to add new requirements and domain assumptions to make the goal satisfiable (e.g., specifying fleet size, assumptions about geographic ambulance distribution across the city, or periodic automated redistribution algorithms); or (2) negotiate early with stakeholders to relax or reduce the goal's scope (e.g., removing the hard 15-minute upper bound). Crucially, the professor warns that promising an unfulfillable constraint leads to project failure even if the software implementation itself is of the highest quality.

## Airbus A320 Accident: Severe Impact of Invalid Domain Assumptions

**Reference:** 02a.RE.pdf page 27-31

The professor provides deep contextual commentary on the Airbus A320 accident: the formal argument was completely sound on paper (R ∧ D ⊨ G), but one domain assumption—that wheels turn if and only if the plane is moving on the runway—broke in reality due to aquaplaning. The software delayed reverse thrust deployment by 9 seconds because wheel sensors gave no pulses on the water film. The professor emphasizes a critical software engineering takeaway: discovering an invalid domain assumption during operation often necessitates a complete redesign of the system, because the core software logic was architected around a physical property that does not hold.

## Modelling Access Control: Granularity and Mechanical vs Software Enforcement

**Reference:** 02a.RE.pdf page 35, 36, 38

During the interactive walkthrough of the Physical Access Control System (PACS), the professor explores alternative modeling decisions not detailed on the slides: (1) Feedback vs internal state: checking token validity is internal machine-only, but providing confirmation/feedback to the user is shared and machine-controlled; analysts can either represent both separately or merge them at a higher level of abstraction depending on the desired model scope; (2) Mechanical turnstiles vs automated doors: the door closure phenomenon can be machine-controlled (via software actuating automated doors within delay d_e) or world-only (if a passive mechanical turnstile/barrier, like older metro turnstiles, physically ratchets closed after a person pushes through, preventing tailgating by design).

## Physical Access Control System: Two-Stage Structure of the Correctness Proof

**Reference:** 02a.RE.pdf page 41, 42

The professor explains the mathematical and structural intuition behind proving goal G1 (e ≤ s, entries never exceed scanned tokens) using requirements R1–R5 and domain assumptions DA1–DA4: the proof cannot link entries e and scans s directly because the machine cannot observe entries nor force scans. Instead, it must be decomposed into two distinct halves mediated by the number of door openings o: first proving e ≤ o (which relies primarily on physical domain assumptions DA1–DA4 regarding human behavior and door closure speed d_e), and second proving o ≤ s (which relies primarily on software requirements R1–R3 enforcing that door openings never exceed valid token scans and initial conditions R5/s=0). Combining e ≤ o and o ≤ s establishes e ≤ s.
