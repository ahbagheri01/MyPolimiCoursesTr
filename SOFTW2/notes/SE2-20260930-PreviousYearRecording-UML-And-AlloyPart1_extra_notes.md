# SE2-20260930-PreviousYearRecording-UML-And-AlloyPart1 — Additional Professor Notes

**Transcripts:** SE2 20251002.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Substate Explosion and Diagram Decomposition in UML State Machines

**Reference:** 02e.UML4RE.pdf, page 23

When a state in a state machine diagram contains internal substates (such as customer authentication or transaction execution), detailing every subdiagram within the main canvas quickly impairs visual readability. Consequently, UML permits deferring substate machines to separate diagrams while marking the composite state with explosion icons to maintain clarity.

## State Diagrams as Class-Level Models vs. Sequence Diagrams as Instance-Level Scenarios

**Reference:** 02e.UML4RE.pdf, page 24

State machine diagrams provide class-level documentation representing all possible lifecycle state evolutions across every instance of an entity. In contrast, sequence diagrams operate at the instance level, capturing individual execution traces or specific operational subsets under given assumptions (for example, assuming a subscription request returns an affirmative acknowledgment rather than failure).

## Modeling External Actor Interactions to Derive Domain Assumptions

**Reference:** 02e.UML4RE.pdf, page 28

During requirements elicitation, interaction between external actors outside the target software may seem irrelevant to software design. However, modeling direct interactions between external actors is crucial in requirements analysis because it formalizes assumptions about domain behavior that occur independently of system automation.

## Methodological Discipline in UML Assertions and the Need for Alloy

**Reference:** 02e.UML4RE.pdf, page 35-36

While standard UML cannot formally enforce logical constraints or assertions relating goals, domain properties, and requirements, analysts can enforce methodological discipline in natural language by restricting vocabulary strictly to entities defined in the class diagram. This structured approach bridges informal requirements and formal verification frameworks like Alloy.

## Exam Warning Regarding Alloy Version Discrepancies

**Reference:** 03a.AlloyPart1-2.pdf, page 4

Past exam questions prior to academic year 2022/2023 were designed for Alloy version 5, which lacked direct support for mutable constructs and handled temporal behavior differently than Alloy 6. Students reviewing archival exam solutions must note that models from earlier years use alternate modeling idioms.

## Relational Join Evaluation Mechanics in Alloy

**Reference:** 03a.AlloyPart1-2.pdf, page 15-16

When Alloy computes a relational join via the dot operator (such as Book.addr or myName.(Book.addr)), it matches the trailing atom of the left operand with the leading atom of the right operand tuple, creating a resulting tuple with the matched intermediate atom removed. This differs from standard relational algebra joins, where join attributes are retained by default.

## Alloy Analyzer Visualization Anomaly with Singleton Entity Naming

**Reference:** 03a.AlloyPart1-2.pdf, page 17

In the Alloy Analyzer's graphical visualizer, when only one instance of an entity signature exists in a generated instance, the label may omit the numeric index (displaying 'Book' instead of 'Book0'). However, the underlying model engine always assigns unique indexed identifiers (e.g., Book0) to all instantiated atoms, as verified in the textual representation.
