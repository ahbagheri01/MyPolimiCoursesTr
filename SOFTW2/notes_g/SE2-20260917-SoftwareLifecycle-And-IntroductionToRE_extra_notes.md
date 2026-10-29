# SE2-20260917-SoftwareLifecycle-And-IntroductionToRE — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260917.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\01.IntroSE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf

## Limitations and Human Oversight of AI Coding Agents

While AI agents can assist with boilerplate coding, documentation descriptions, and generating automated test frameworks, humans must remain strictly in the loop because accountability cannot be delegated. Practitioners must control AI tools by supplying precise inputs (functional and non-functional requirements, architectural design, coverage thresholds like 90%). The professor highlights a real-world outage case at AWS (a 13-hour disruption caused by code changes performed by AI agents) where AWS attributed the incident to human configuration error, emphasizing that developer failure to oversee and verify AI agent modifications is ultimately the human's professional responsibility.

## Contractual and Legal Dimension in Distinguishing Corrective vs. Evolutionary Maintenance

**Reference:** 01.IntroSE.pdf, slide 24-25

Differentiating between corrective maintenance (bug fixing) and evolutionary maintenance (adaptive or perfective changes) carries critical contractual consequences: resolving bugs and defects in existing specifications is typically the developer's legal and contractual responsibility (at developer cost), whereas modifications driven by external environmental shifts or new client requirements allow developers to bill under a new contract. Concrete examples of adaptive maintenance include adapting to legal regulatory mandates (such as GDPR or the EU AI Act) and third-party library deprecations.

## Modifying Design Before Implementation to Prevent Architectural Erosion and Hidden Breakages

**Reference:** 01.IntroSE.pdf, slide 27

When evolving software or patching bugs, modifications must be designed and evaluated at the architectural model level before touching the codebase. The professor illustrates this through an architectural dependency example: if component B changes its method interface (e.g., removing parameter P3 from operation P1) to fix an issue with component A, directly altering the code without consulting design models conceals that components C and D also depend on B. In statically typed compiled languages, mismatches might be detected at compile time, but in dynamically checked languages, uncoordinated interface adjustments propagate unnoticed to production runtime failures.

## Feasibility and Architectural Preconditions for Feature-by-Feature Development

**Reference:** 01.IntroSE.pdf, slide 31-32

Developing an application feature-by-feature in small iterative cycles is viable only when the underlying architectural structure is already clear and standard (such as a standard 3-tier web application consisting of a database, backend server, UI optimization layer, and frontend client, where an independent feature like browsing products in an e-commerce platform can be delivered end-to-end early). Conversely, for novel, non-standard systems (such as a bespoke environmental control system interfacing with heterogeneous legacy systems), development cannot proceed feature-by-feature until domain study and architectural integration boundaries are comprehensively established.

## Latency Tolerance Dichotomy in Real-Time vs. User-Facing Systems (Netflix vs. Ariane 5)

**Reference:** 02a.RE.pdf, slide 8

Non-functional requirements (NFRs) are heavily dictated by the operational domain. While a 5-second response time requirement might seem excessive, human cognitive reaction time operates on the scale of seconds; thus, user-facing UI interactions in consumer entertainment applications (e.g., Netflix search/browsing) can tolerate multi-second latencies, whereas Netflix's underlying media streaming pipeline requires millisecond timing to avoid buffering. In stark contrast, safety-critical aerospace launch systems (e.g., Ariane 5) cannot tolerate multi-second human scales and mandate sub-millisecond real-time predictability across all software functions.

## System Scope vs. Software Responsibility: Taxi Reservation and User Installation Analysis

**Reference:** 02a.RE.pdf, slide 5, 11, 12

Requirements assigned to software must only predicate over phenomena within the software machine's sphere of control. In the taxi reservation candidate requirement ('The system should guarantee that the reserved taxi picks the user up'), the assertion describes a high-level system goal achievable only through collaboration with external physical actors (the taxi driver and passenger) rather than software alone. Similarly, stating 'The user must have Adobe Acrobat installed' cannot be a software requirement because an application cannot forcibly install software without user authorization; it must instead be formulated as an external environmental domain assumption.

## Defending Overly Specific Technical Requirements as Valid Constraints in Pre-Existing Systems

**Reference:** 02a.RE.pdf, slide 5, 6, 12

While requirements such as 'The system should be implemented in Java' or 'The search for the available taxi should be implemented in class Controller' appear overly design-specific and contrary to the principle of implementation independence, they represent valid technical requirements/constraints when imposed by customer organizational constraints (e.g., maintaining alignment with in-house Java developers) or when extending legacy codebases where functionality must integrate into established architectural components.
