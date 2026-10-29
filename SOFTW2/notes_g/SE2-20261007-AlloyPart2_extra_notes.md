# SE2-20261007-AlloyPart2 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261007.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Built-in Universal Types and Sets in the Alloy Analyzer

**Reference:** Slide 13-14

The professor explains that when generating an instance, the Alloy Analyzer automatically builds the universal set (`univ`), which contains all atoms from user-defined signatures as well as built-in default entities: integers (specifically spanning -8 to 7 in the default bitwidth), a built-in integer set, sequences, strings (which may be empty if unconstrained), and `none` (the empty set). These types exist implicitly in all instances even if the user never defines them.

## Mechanics of the Relational Join Operator and Dropping the Join Element

**Reference:** Slide 15-16

The professor contrasts the Alloy join operator (`.`) with database joins, emphasizing a key mechanical difference: the matching 'join element' between the two tuples is completely dropped from the resulting tuple. For example, joining a unary set `Book = {(B0)}` with a ternary relation `addr = {(B0, N0, A0)}` drops `B0`, producing the binary tuple `(N0, A0)`.

## Diagnosis of Inconsistency in show3: Multiplicity Clash

**Reference:** Slide 18

The professor steps through why running `pred show [b: Book] { #b.addr > 1; some n: Name | #n.(b.addr) > 1 }` returns 'no instance found / predicate may be inconsistent'. The signature declaration defined `addr: Name -> lone Addr` (specifying each name can have at most one address), directly contradicting the existential quantifier asking for a name with cardinality strictly greater than one (`> 1`). Replacing `lone` with `set` resolves the contradiction and allows an instance to be generated.

## Pre-Alloy 6 State Modeling and the Aliasing Identity Trap in add

**Reference:** Slide 19

Before the temporal logic introduced in Alloy 6, dynamic evolution had to be modeled idiomatically by passing pre-state and post-state atoms (`b` and `bpost`) as parameters. When defining `bpost.addr = b.addr + n -> a`, the analyzer produced a surprising instance where `b` and `bpost` were mapped to the exact same book atom. The professor explains the mechanism: set union with an element already present in the set is an idempotent operation (`X + X = X`), so no state change occurs, satisfying the formula with a single book atom.

## Analysis of the Counterexample in delUndoesAdd

**Reference:** Slide 21-22

When checking whether delete undoes add (`assert delUndoesAdd`), the Alloy Analyzer finds a counterexample due to set union idempotence: if a book already contains `(n, a)`, executing `add` leaves the book unchanged (`b = bpost`), but subsequent execution of `del` removes `n`, resulting in an empty or smaller book (`bppost != b`). The professor notes two distinct ways to resolve this: either modify the assertion by adding a precondition ensuring `n` is not already in `b` (`no n.(b.addr)`), or modify the `add` operation predicate itself.

## Methodological Comparison: Bounded Verification vs. Software Testing

**Reference:** Slide 24

The professor provides a conceptual and geometric comparison between bounded model checking and testing: bounded verification performs exhaustive analysis of all possible configurations strictly within a predefined finite boundary (scope), leaving everything outside unknown; software testing samples arbitrary points across the entire input space, which can reach larger states but can never be exhaustive. Therefore, the two techniques are complementary and should be used together.

## Distinction Between Predicates, Functions, and Facts

**Reference:** Slide 25-27, 43

The professor delineates the semantic roles of these core Alloy constructs: predicates evaluate to a Boolean truth value (true/false) and are checked only when explicitly invoked (e.g., via a `run` command or within another expression); functions return relational expressions/sets (e.g., `lookup` returning a set of addresses) rather than Booleans; facts are global properties and constraints that must hold across all atoms and relations in every valid generated world at all times without needing to be invoked.

## Meta-Model Visualization in the Alloy Analyzer

**Reference:** Slide 30

The professor demonstrates a specific tool feature in the Alloy Analyzer: displaying the 'meta-model'. Unlike ordinary instance visualizations that depict individual atoms and tuple relations in a specific generated world, the meta-model visualizes the signatures and relations at the schema level (e.g., `Book`, `Addr`, and `Name` connected by `addr`). Every valid instance must conform to this overarching meta-model.
