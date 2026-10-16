# SE2-20261008-AlloyPart3 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261008.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Default Run Command in the Absence of Predicates

**Reference:** Slide 35

When an Alloy model contains no explicit `run` command or predicates, the Alloy Analyzer automatically synthesizes and executes a default predicate and default run command upon execution.

## Role of Names in Facts versus Predicates, Functions, and Assertions

**Reference:** Slide 45

Fact names in Alloy are entirely optional and ignored by the analyzer, serving solely human readability purposes. In contrast, identifiers assigned to predicates, functions, and assertions are functionally necessary because they must be invoked or checked by name.

## Empirical Comparison of Constraint Strength via Assertions

**Reference:** Slides 50-51

To formally compare whether one constraint is stronger than another without extensive manual relational algebra proofs, each constraint can be converted into a parameterless predicate, followed by checking bidirectional assertions (`predA implies predB` and `predB implies predA`). If both yield counterexamples, neither constraint is strictly stronger than the other.

## Set-Theoretic versus First-Order Logic Styles in Alloy Constraints

**Reference:** Slides 40, 41, 47

Alloy models allow constraints to be formulated either via higher-level relational/set operators (such as relational transpose `~` and intersection `&`) or via first-order quantified logic statements. Set-based specifications tend to be significantly more compact, whereas logical implications are often more verbose yet conceptually easier for designers to formulate.

## Visualization Interface for Mutable (Temporal) Steps in Alloy 6

**Reference:** Slide 58

In Alloy 6, the visualizer displays dynamic timelines side-by-side displaying exactly two time steps at once (the current step and the subsequent step). Later steps beyond the visible pair appear dimmed or in gray, requiring manual stepping via navigation controls to advance the timeline visualization.

## Necessity of Frame Conditions in Temporal Cardinality Constraints

**Reference:** Slide 57

Simply specifying that the cardinality of a mutable relation increments across successive time steps (`#b.addr = 0; #b.addr = 1; #b.addr = 2`) does not enforce data continuity or persistence; tuples present in one step can be replaced by completely distinct elements in the next unless explicit persistence constraints (frame conditions) are enforced.

## Pervasive Application of 'always' in Temporal Facts

**Reference:** Slide 61

In temporal Alloy models containing `var` signatures or relations, invariants and constraints within `fact` blocks almost universally require being wrapped in the `always` operator; without `always`, a constraint inside a fact is evaluated only at the initial time step (step 0).

## Enumerations versus Abstract Signatures for State Spaces

**Reference:** Slide 62

Alloy `enum` declarations represent syntactic sugar equivalent to an abstract signature extended by disjoint singleton sub-signatures. Enumerations are preferred for simple, atomic state sets without specific relations, but cannot replace abstract signatures when distinct sub-types require unique fields or relational attributes.

## Vacuous Satisfaction in Implicational Temporal Invariants

**Reference:** Slide 63

A temporal rule stating that entering a broken state implies permanently staying broken (`always (status = Broken implies after always status = Broken)`) allows traces where a device remains functioning for its entire lifespan, because the antecedent remains false across all evaluation instants, vacuously satisfying the implication.
