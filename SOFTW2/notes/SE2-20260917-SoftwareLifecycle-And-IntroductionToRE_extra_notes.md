# SE2-20260917-SoftwareLifecycle-And-IntroductionToRE — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260917.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\01.IntroSE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf

## Role of Human Engineers vs. AI Delegation in Coding, Requirements, and Testing

**Reference:** 01.IntroSE.pdf, slide 23

AI agents may reduce boilerplate coding effort, but shift human responsibility towards qualifying, monitoring, architecting, and verifying software. Delegation to AI requires human-defined problem understanding: code documentation requires an existing human idea, while test generation cannot be delegated without human-provided functional/non-functional requirements, architectural design, and explicit testing criteria (e.g., target code coverage). Requirements analysis cannot be delegated to AI because problem discovery and stakeholder intent understanding are fundamentally creative human responsibilities.

## Contractual Implications Distinguishing Correction from Evolution

**Reference:** 01.IntroSE.pdf, slide 25

Distinguishing between corrective maintenance (bug fixing) and evolutionary maintenance is legally and commercially critical: developers are contractually obligated to fix faults/bugs within the original scope, whereas evolutionary modifications (adaptive or perfective changes to new conditions or requirements) permit renegotiation and new contracts with the client.

## Concrete Contrast: Adaptive vs. Perfective Maintenance

**Reference:** 01.IntroSE.pdf, slide 24

Perfective maintenance modifies or adds functionalities directly requested by users (e.g., adding an e-commerce feature allowing users to view cart contents before checkout). Adaptive maintenance keeps the user-facing functionality unchanged while altering the implementation to adapt to external environment changes, such as replacing deprecated third-party libraries or altering data collection workflows to comply with regulations like GDPR or the EU AI Act.

## Modifying Design Before Implementation: Component Interface Bug Example

**Reference:** 01.IntroSE.pdf, slide 27

Applying bug fixes directly to code risks breaking interdependent systems. For instance, if an operation parameter is removed in component B to fix a defect, altering the code without consulting the design may silently break dependent components C and D (especially in languages lacking static interface checking at compile time). Inspecting architectural design first identifies all affected consumers and the holistic impact.

## Preconditions for Feature-by-Feature Lifecycle Execution

**Reference:** 01.IntroSE.pdf, slides 31-32; 02a.RE.pdf, slide 3

Adopting an iterative feature-by-feature lifecycle is effective when the system architecture is well-understood and standardized (e.g., a standard multi-tier web application with known database, backend, and UI structures). However, when developing novel, non-standard systems interacting with complex legacy systems, architecture and interfaces across all systems must be studied and established globally before developing isolated features.

## System Boundaries: Shared System-Environment Goals vs. Software Requirements

**Reference:** 02a.RE.pdf, slides 5, 11, 12, 13

Statements that depend on external autonomous actors (e.g., 'The system should guarantee that the reserved taxi picks the user up' or 'The user must have Adobe Acrobat installed') cannot be software requirements. A software system cannot unilaterally control taxi drivers or force user installation without authorization. Such statements belong either to higher-level system/environment goals achieved collaboratively with external entities or to domain assumptions.

## Design-Specific Statements as Valid Technical Requirements

**Reference:** 02a.RE.pdf, slides 5, 6, 12

While implementation details (e.g., using Java, implementing search inside a 'class Controller') are typically design choices, they become legitimate technical requirements/constraints when explicitly imposed by the client—often due to legacy integration, customer-side developer skills, or existing enterprise architecture.

## Latency Constraints by Interaction Type: Netflix vs. Ariane 5

**Reference:** 02a.RE.pdf, slide 8

The domain and interaction type determine acceptable non-functional latency metrics. In entertainment systems like Netflix, human UI response can tolerate second-level latencies due to biological reaction times, whereas video streaming components require millisecond-level speeds. In mission-critical embedded systems like the Ariane 5 launcher, all subsystems must strictly execute within milliseconds or less.
