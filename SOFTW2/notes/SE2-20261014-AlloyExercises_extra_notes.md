# SE2-20261014-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261014.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Alloy temporal operators: after and always redundancy

**Reference:** 03a.AlloyPart1-2.pdf, slide 63

In an implication enforcing that a broken status remains broken, an inner 'always' can be omitted without changing the meaning because an outer 'always' ensures the step-by-step condition holds at all future time instants.

## Alloy temporal operators: historically on finite domains

**Reference:** 03a.AlloyPart1-2.pdf, slide 65

The 'historically' operator predicates strictly over the finite history of the instantiation from the current step back to the initial state, as Alloy models are evaluated over finite time traces.

## Alloy temporal operators: 'before' at the initial time instant and 'after always' idiom

**Reference:** 03a.AlloyPart1-2.pdf, slide 67

Prepending 'after always' acts as a specific trick/idiom to skip predicate evaluation at step 0, avoiding failure/falsehood where the 'before' operator has no preceding state.

## Alloy temporal operators: prime notation vs. 'after'

**Reference:** 03a.AlloyPart1-2.pdf, slides 59, 68

Primed relation notation (e.g., d.status') and the temporal operator 'after' (e.g., after d.status = Broken) can be used equivalently to express postconditions in transition predicates.

## Alloy state transitions: the frame problem (explicit unchanged constraints)

**Reference:** 03a.AlloyPart1-2.pdf, slide 73

In Alloy operations, any state element not explicitly constrained is free to change arbitrarily; modelers must explicitly specify frame conditions stating what remains unchanged (e.g., message' = message).

## Alloy temporal logic: scope of 'after' vs. prime notation

**Reference:** 03a.AlloyPart1-2.pdf, slide 74

The 'after' operator applies only to the expression directly following it unless parentheses are used. Combining 'after' with primed variables shifts evaluation forward twice (into the step after next).

## Alloy temporal operators: semantics of 'once'

**Reference:** 03a.AlloyPart1-2.pdf, slide 69

The temporal operator 'once' does not mean 'exactly once' in natural language; it means 'at some time instant in the past' (existential past quantification, true for one or more past instants).

## Alloy signatures: constraints defined inside signature blocks

**Reference:** 03b.AlloyExercises.pdf, slide 5, 14

Constraints placed inside curly braces within a signature declaration implicitly apply to all instances without explicit universal quantification, and for variable models, they are implicitly enforced at all times without requiring the 'always' operator.

## Alloy syntax: navigation via relational join on ternary relations

**Reference:** 03b.AlloyExercises.pdf, slide 15

To project fields out of a ternary relation (e.g., connection: Intersection -> Semaphore -> Road), joins can be chained: 'i.connection' leaves (Semaphore, Road) pairs, and joining with 'Road' yields the semaphores.

## Alloy quantification: disjointness of multiple quantified variables

**Reference:** 03b.AlloyExercises.pdf, slides 8, 17

In Alloy universal quantifications like 'all s1, s2: S', variables can bind to the same atom; explicit inequality (s1 != s2) or the 'disj' keyword ('all disj s1, s2: S') must be used to enforce distinctness.

## Alloy specification methodology: abstraction level and model bloat

**Reference:** 03b.AlloyExercises.pdf, slide 17

Deciding which real-world phenomena to include or exclude is critical; modeling unnecessary real-world details (like traffic jams or network-wide routing) creates heavyweight models that take too long to verify without providing benefits.

## Requirements engineering: world vs. machine phenomena classification

**Reference:** 03b.AlloyExercises.pdf, slide 52

Distinguishing world-controlled from machine-controlled phenomena requires decomposing actions: a tourist presenting an electronic key is world-controlled, whereas checking the key and triggering unlocking is machine-controlled.

## Domain modeling vs. Alloy: deriving models from UML class diagrams

**Reference:** 03b.AlloyExercises.pdf, slides 20-22, 54-56

A UML class diagram serves as a direct intermediate step for an Alloy model, where entity classes map to signatures and associations with cardinality constraints map to Alloy relations.

## Domain modeling: rationale for distinct 'carries' vs. 'owns' relations

**Reference:** 03b.AlloyExercises.pdf, slides 54, 56, 57

The distinction between 'carries' and 'owns' relations for luggage is required to formalize the domain assumption of luggage safety (luggage is safe if and only if carried by its owner or locked in a locker with the matching key held by the owner).

## Alloy specification discrepancy: greenIsExclusive vs. slide title semantics

**Reference:** 03b.AlloyExercises.pdf, slide 17

The fact named 'greenIsExclusive' actually constrains two semaphores to strictly have different colors (one red, one green), preventing an all-red intersection state despite the name suggesting only that two greens cannot occur simultaneously.
