# SE2-20261008-AlloyPart3 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261008.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Alloy ternary relations and field semantics

**Reference:** 03a.AlloyPart1-2.pdf, slide 12, 32

Declaring a signature field whose range is defined by a Cartesian product (for example, within signature S, a field declared as A -> B) creates an ordered ternary relation typed as S -> A -> B, where the host signature forms the relation's domain.

## Alloy default run behavior and need for constraints

Executing an Alloy specification lacking an explicit run command or target predicate causes the Alloy Analyzer to automatically instantiate a default predicate and run command. This explores unconstrained relational bindings between signature elements, often producing nonsensical domain instances if semantic rules are omitted.

## Signature multiplicity / cardinality prefixes

**Reference:** 03a.AlloyPart1-2.pdf, slide 12, 31

When a signature declaration omits a cardinality prefix, Alloy defaults to the multiplicity prefix `set` (signifying zero, one, or multiple instances), in contrast to explicit prefixes like `one` or `some`.

## Relational join and function call syntax equivalence

**Reference:** 03a.AlloyPart1-2.pdf, slide 34

Function calls and relational dot joins in Alloy are interchangeable syntactical forms (e.g., `P.grandpas` is strictly equivalent to `grandpas[P]`). Parameterized calls must strictly use square brackets instead of standard parentheses.

## Naming facts, predicates, and assertions

**Reference:** 03a.AlloyPart1-2.pdf, slide 45

Fact identifiers are purely informative metadata meant for human readability and are completely ignored by the Alloy Analyzer engine. In contrast, predicates, functions, and assertions require names as programmatic identifiers so they can be referenced and invoked by `run` or `check` directives.

## Relational vs. first-order logic modeling styles in Alloy

**Reference:** 03a.AlloyPart1-2.pdf, slide 40-41, 45-47

Constraints in Alloy can typically be expressed in two interchangeable paradigms: a relational/set-algebraic style (using operators like union, intersection, transpose, and transitive closure) or a first-order logic style (quantifiers, implications, equality). Relational expressions yield concise and compact formulas, whereas first-order formulations are more verbose but often more approachable to specify.

## Using assertions to compare constraint strength

**Reference:** 03a.AlloyPart1-2.pdf, slide 49-51

To evaluate relative constraint strength between two prospective facts, wrap each as a parameterless predicate and run bidirectional assertions (`A implies B` and `B implies A`). If only one direction passes without counterexamples, a strict hierarchy of strength is verified; counterexamples in both directions demonstrate incomparable constraints.

## Temporal operator `always` in facts

**Reference:** 03a.AlloyPart1-2.pdf, slide 61, 75

Dynamic models in Alloy evaluate bare facts at the initial state step (time 0) by default. Therefore, dynamic domain invariant facts almost universally require the `always` operator to ensure constraints apply across every reachable execution step.

## `enum` vs. abstract signatures in Alloy

**Reference:** 03a.AlloyPart1-2.pdf, slide 62

Alloy's `enum` construct serves as syntactic sugar for an abstract signature extended by singleton sub-signatures, but it is restricted to flat constant values and cannot be used when members require individual relations, fields, or properties.

## Temporal implication and `eventually` vs. `always`

**Reference:** 03a.AlloyPart1-2.pdf, slide 63, 64

A safety persistence property specified as `always (d.status = Broken => always d.status = Broken)` vacuously permits an execution where an entity stays `Working` indefinitely; enforcing that an event or state transition must occur requires a liveness property formulated with `eventually`.
