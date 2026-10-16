# SE2-20260930-PreviousYearRecording-UML-And-AlloyPart1 — Additional Professor Notes

**Transcripts:** SE2 20251002.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## State Diagrams vs. Sequence Diagrams: Scope of Modeling

**Reference:** 02e.UML4RE.pdf, slide 24

State machine diagrams provide class-level documentation representing every possible lifecycle evolution for all instances of an entity. In contrast, sequence diagrams operate at the instance level, capturing individual execution scenarios or specific interaction traces.

## State Transition Semantics Without Explicit Trigger Events

**Reference:** 02e.UML4RE.pdf, slide 23

Transitions lacking explicit triggering events in a state machine diagram can fire spontaneously at any time once their source state is active, unless overridden by a competing event-triggered transition.

## Representing Out-of-System Interactions as Domain Assumptions

**Reference:** 02e.UML4RE.pdf, slide 28

In requirements-level sequence diagrams, interactions between external actors outside the software-to-be help explicitly define domain assumptions, documenting operational preconditions rather than software behavior.

## Disciplinary Role of UML When Formulating Non-Expressible Assertions

**Reference:** 02e.UML4RE.pdf, slide 36

Because pure UML lacks declarative semantics for assertions and constraints, requirements engineers must ensure all terms used in informal natural language properties strictly reference entities defined in the domain class diagram.

## Exam Warning: Alloy 5 vs Alloy 6 Paradigm Shift

**Reference:** 03a.AlloyPart1-2.pdf, slide 4

Past exam papers prior to 2022/2023 rely on Alloy 5 idioms. Unlike Alloy 6, Alloy 5 lacked native mutable signatures and relations, requiring manual snapshot-passing or explicit time orderings.

## Relational Join Tuple Truncation Semantics in Alloy

**Reference:** 03a.AlloyPart1-2.pdf, slide 16

In an Alloy relational join (p.q), the operation matches the last column of p with the first column of q, discarding the matched interface element and preserving tuple ordering across the remaining components.

## Alloy Visualizer Singleton Naming Idiosyncrasy

**Reference:** 03a.AlloyPart1-2.pdf, slide 17

The Alloy Visualizer graph view frequently omits indexing labels for singleton instances (e.g., displaying Book instead of Book$0), whereas text and tree outputs display the full internal identifier.
