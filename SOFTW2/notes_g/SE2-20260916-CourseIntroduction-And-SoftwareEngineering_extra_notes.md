# SE2-20260916-CourseIntroduction-And-SoftwareEngineering — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260916.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\00.CourseIntro.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\01.IntroSE.pdf

## Grading Thresholds and Rounding Rules

**Reference:** 00.CourseIntro.pdf, slide 8

While the maximum possible exam score is 32 (30 from the project/written blocks plus up to 2 bonus points from class quizzes), obtaining 31 or higher before rounding earns a final grade of 30 e Lode (30L). Scores are rounded up to the nearest integer, with the specific exception that 30.5 is rounded down to 30 rather than 31.

## Peer Review and Acceptance Testing Assessment Criteria

**Reference:** 00.CourseIntro.pdf, slide 10

During the Implementation and Testing (I&T) phase, groups perform acceptance testing on another team's running prototype and documentation. The evaluation of this review does not influence the score of the group being reviewed (Group A); instead, grading evaluates the reviewing group's (Group B's) critical analysis ability and testing rigor.

## Impact of Generative AI on Project Discussions and Evaluation

**Reference:** 00.CourseIntro.pdf, slide 11

Because LLMs can easily generate convincing documentation and code, evaluation now prioritizes the oral project defense over static deliverables. Students are permitted to use AI responsibly as a productivity tool, but will be evaluated on their comprehensive ownership of all artifacts, ability to justify design choices, and identification of subtle omissions in AI-generated text.

## Format and Logistics of Written Exam WE1

**Reference:** 00.CourseIntro.pdf, slide 17

WE1 is a 1.5-hour open-book written exam with three exercises covering course techniques. One exercise always requires writing an Alloy formal specification, while the remaining two questions rotate among software testing, architectural availability assessment, or project management.

## Shift from Homeworks to In-Class Quizzes Due to LLMs

**Reference:** 00.CourseIntro.pdf, slides 14-15

Bonus assessments (RASD and DD evaluations) were previously open-ended take-home assignments, but were restructured into in-class quizzes (transitioning to multiple-choice format) because homework submissions became heavily LLM-generated. Students inspect past project documents at home beforehand, take the quiz once during lecture without retake opportunities, and participate in an immediate debrief.

## Iterative Artifact Alignment Across Project Submissions

**Reference:** 00.CourseIntro.pdf, slide 13

Deliverables can be revised and resubmitted across successive project milestones. If design or implementation activities reveal necessary changes to requirements, students must update and resubmit the earlier documents (e.g., the RASD) alongside the new deliverable (e.g., DD) to prevent architectural divergence or unaligned specifications.

## Root Cause and Architectural Lesson of the CrowdStrike Outage

**Reference:** 01.IntroSE.pdf, slide 3

The global CrowdStrike IT failure on July 19, 2024, is framed as a fundamental failure in component interface agreements and software malleability. One component passed unvalidated, oversized data across an uncoordinated interface into another component, triggering an array out-of-bounds read that crashed Windows servers worldwide due to automated kernel updates.

## Redefining Software Engineering for Multi-Agent Systems

**Reference:** 01.IntroSE.pdf, slide 4

The classical definition of software engineering as 'multi-person construction of multi-version software' requires modern updating to 'multi-agent construction', reflecting environments where human engineers collaborate with autonomous AI agents. Because AI agents can generate code and requirements rapidly, human engineers must transition into higher-level system controllers and coordinators.

## Software Intangibility and Hazards of Malleability

**Reference:** 01.IntroSE.pdf, slide 7

Software possesses two distinct physical contrasts with traditional engineering artifacts: intangibility (preventing customers and managers from visualizing complexity and effort, except via user interfaces) and extreme malleability (allowing rapid code modifications in minutes without retooling assembly lines). Malleability creates severe risks when developers make emergency patches without systemic impact analysis.

## Trade-offs Between Reliability and Performance Efficiency

**Reference:** 01.IntroSE.pdf, slide 8

Software product quality attributes frequently conflict. For instance, achieving high reliability and fault tolerance requires introducing runtime monitoring, checks, and redundancy overhead, directly conflicting with performance efficiency goals that require minimal latency and maximum execution speed.

## Safety Failures and the Radiation Machine Example

**Reference:** 01.IntroSE.pdf, slide 8

Illustrating software safety and hazard prevention, the professor references software-induced fatalities in safety-critical medical hardware, specifically radiation therapy machines (Therac-25 context) that administered massive radiation overdoses to patients due to software defects.

## Online Continuous Maintenance and Zero-Downtime Evolution

**Reference:** 01.IntroSE.pdf, slides 12, 14

In modern software lifecycles, maintenance cannot be treated as a detached post-deployment phase where systems are halted for updates. Modern systems require continuous operation, forcing maintenance and architectural evolution to occur on the fly without interrupting running services.
