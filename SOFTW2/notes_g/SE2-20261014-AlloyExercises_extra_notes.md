# SE2-20261014-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261014.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Redundancy of Inner 'Always' in Status Propagation Fact

**Reference:** 03a.AlloyPart1-2.pdf#page=64

In the temporal fact `all d: Device | always (d.status = Broken implies after always d.status = Broken)`, the inner 'always' can be omitted without changing the meaning of the fact. Since the outer 'always' evaluates at every time instant, requiring `after d.status = Broken` at each step where status is broken inductively enforces that the device remains broken in all future steps.

## Handling the Undefined 'Before' Operator in the Initial State via 'After Always'

**Reference:** 03a.AlloyPart1-2.pdf#page=67

Because Alloy traces operate over finite domains with a discrete starting instant, the `before` operator is false or undefined at the very first step (instant 0). To express past preservation properties like `d.status = Working implies before d.status = Working` without making the fact false at the initial instant, one uses the prefix `after always`. This shifts evaluation to begin strictly from the second instant onward.

## Equivalence and Syntax of Transition Specifications: Prime Notation vs After Operator

**Reference:** 03a.AlloyPart1-2.pdf#page=69

In state-transition predicates, the postcondition relation state can be specified either using prime notation (e.g., `d.status' = Broken` or `Trashed' = Trashed + m`) or by wrapping the expression with the temporal operator `after` (e.g., `after d.status = Broken` or `after #Trashed = 0`). Additionally, invoking predicates with square brackets (e.g., `break[d]`) is syntactic sugar for dot invocation (`d.break`).

## Semantics of 'Once' vs 'Some' in Alloy Temporal Logic

**Reference:** 03a.AlloyPart1-2.pdf#page=70

Alloy temporal logic does not feature a temporal quantifier keyword named `some` for time instants; `some` is strictly used for relational or existential quantification over atoms. Instead, the past temporal operator corresponding to 'at some point in the past' (one or more previous instants) is `once`, which is the dual of `eventually`.

## Subset Declarations: 'in' vs 'extends' and Mutability

**Reference:** 03a.AlloyPart1-2.pdf#page=73

Declaring a signature with `sig Sub in Super` establishes `Sub` as an arbitrary subset of `Super` rather than a partition, allowing multiple sub-signatures to overlap. In contrast, using `extends` forces distinct extending signatures to be mutually disjoint. In dynamic models, marking both signatures as `var` (`var sig Message`, `var sig Trashed in Message`) allows atoms to dynamically enter or leave subsets and relations across steps.

## Necessity of Frame Conditions in Alloy State Transitions

**Reference:** 03a.AlloyPart1-2.pdf#page=74

In declarative modeling with Alloy, every relation or signature not explicitly constrained in a transition predicate can change arbitrarily. Therefore, transition operations (such as `delete` and `restore`) must explicitly state frame conditions (e.g., `Message' = Message`) to forbid unconstrained side effects.

## Scope of Temporal Operators and Operator Precedence in Predicates

**Reference:** 03a.AlloyPart1-2.pdf#page=75

In predicate formulas containing multiple clauses, temporal operators like `after` apply only to the immediately following relational constraint unless grouped using explicit parentheses. For example, in `after #Trashed = 0 and Message' = Message - Trashed`, `after` binds strictly to `#Trashed = 0`, while `Message'` and `Trashed` in the subsequent clause evaluate relative to the current time instant.

## Initial State Constraints Outside the 'Always' Loop

**Reference:** 03a.AlloyPart1-2.pdf#page=76

In system behavior facts (e.g., `fact systemBehavior { no Trashed; always (...) }`), initial state specifications like `no Trashed` must be kept strictly outside the `always` block. Placing them inside `always` would unintentionally force the mailbox trash to remain empty across all states throughout the entire trace, making delete operations unsatisfiable.

## In-Signature Block Constraints: Implicit Quantification and Temporal Invariance

**Reference:** 03b.AlloyExercises.pdf#page=14

Appending an expression block directly to a signature declaration (e.g., `sig Intersection { connection: Semaphore -> Road }{ #connection = 2 }`) eliminates the need for explicit universal quantification over that signature. Furthermore, if any relations in the signature are mutable (`var`), the in-signature constraint holds as an invariant across all time steps without requiring an explicit `always` operator.

## Function and Let Semantics in Traffic Lights Intersection Model

**Reference:** 03b.AlloyExercises.pdf#page=15

Functions in Alloy act like object-oriented getter methods by navigating relations using relational joins (e.g., `(i.connection).Road` or `Semaphore.(i.connection)` on ternary relations). The `let` construct provides temporary variable names for intermediate evaluation results (e.g., `let s = getSemaphores[i] | #s = 2`), improving readability, although simple cardinality checks could equivalently be applied directly to function call results.

## Need for Explicit Disjointness in Multi-Variable Quantification

**Reference:** 03b.AlloyExercises.pdf#page=17

When quantifying over multiple variables from the same signature set (e.g., `all s1: Semaphore, s2: Semaphore | s1 in s and s2 in s ...`), Alloy permits both variables to bind to the exact same atom. To enforce constraints across distinct pairs, one must explicitly add `s1 != s2` or use the `disj` keyword (`all disj s1, s2: Semaphore | ...`).

## Discrepancy Between Name and Semantics in 'greenIsExclusive' Fact

**Reference:** 03b.AlloyExercises.pdf#page=17

The fact named `greenIsExclusive` states `s1 != s2 implies s1.color != s2.color`. While the name suggests preventing two green lights simultaneously, the formula actually enforces that the two semaphores must always have different colors (one red, one green), thereby also ruling out the safe state where both lights are red.

## Modelling Scope vs Performance: Abstraction Trade-offs in Road Traffic Model

**Reference:** 03b.AlloyExercises.pdf#page=17

In the traffic light example, stopped traffic is modelled as `r.traffic = STOPPED implies #((Intersection.connection).r) > 0`, explicitly associating stopped traffic strictly with the presence of a semaphore and ignoring real-world factors like jams or accidents. Deciding what to abstract away is a crucial engineering trade-off: omitting extraneous real-world phenomena prevents creating an overly heavyweight specification that becomes intractable for the solver to verify.

## Shared Phenomena Disambiguation: Electronic Key Locker Unlocking

**Reference:** 03b.AlloyExercises.pdf#page=52

Shared phenomena descriptions in natural language can be ambiguous regarding world vs machine control. For 'some lockers are opened with an electronic key', analysis reveals it must be split into two phenomena: the tourist presenting the electronic key to the locker (world-controlled shared phenomenon) and the machine verifying the key and releasing the lock mechanism (machine-controlled shared phenomenon).

## Domain Model Differentiation: 'carries' vs 'owns' in Luggage Keeper

**Reference:** 03b.AlloyExercises.pdf#page=54

In the Luggage Keeper domain model, two separate relations are introduced between `User` and `Luggage`: `owns` and `carries`. While the informal problem description did not make this explicit, this distinction is essential for formalizing domain assumption D1 (luggage safety): a tourist permanently owns their luggage throughout the process, but only 'carries' it when physically holding it outside of locked locker storage.
