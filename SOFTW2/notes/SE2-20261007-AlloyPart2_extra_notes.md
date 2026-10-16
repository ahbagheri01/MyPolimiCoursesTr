# SE2-20261007-AlloyPart2 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261007.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Alloy Signatures and OOP Analogy

**Reference:** 03a.AlloyPart1-2.pdf, slide 4, 12, 31

Signatures in Alloy define entities and are conceptually analogous to classes in object-oriented programming.

## Alloy Case Sensitivity and Field Distinction

Alloy is case-sensitive: an uppercase signature identifier (e.g., Addr) and a lowercase relation name (e.g., addr) are treated as distinct, unrelated entities.

## Modeling Ternary Relations in Address Book

**Reference:** 03a.AlloyPart1-2.pdf, slide 12

The relation over Book -> Name -> Addr is modeled as ternary rather than binary because mappings between names and addresses are book-dependent (the same name may map to different addresses in different books).

## Alloy Analyzer Built-in Universe Elements

The universal set 'univ' automatically computed by the Alloy Analyzer includes built-in types such as integers (-8 to 7 by default), strings, and 'none' (empty set), alongside declared signature atoms.

## Relational Join Operator Mechanics

**Reference:** 03a.AlloyPart1-2.pdf, slide 15, 16

In Alloy relational join ('.'), the matching boundary atom shared between relations is dropped, reducing the arity of the resulting tuple (e.g., joining Book with Book->Name->Addr drops Book, producing Name->Addr).

## Run Commands and Default Scope

**Reference:** 03a.AlloyPart1-2.pdf, slide 17

Empty predicates evaluate to true by default, allowing them to act as generator entry points. Running commands without explicit scope uses default bounds (e.g., 3-4), whereas 'for X but Y Sig' sets a general upper bound with specific per-signature overrides.

## Cardinality Inconsistency Example

**Reference:** 03a.AlloyPart1-2.pdf, slide 18

Walkthrough diagnosing unsatisfiability: a predicate requiring 'some n: Name | #(n.(b.addr)) > 1' contradicts the signature field multiplicity 'lone Addr' (<= 1), which can be resolved by relaxing the field to 'set Addr'.

## Pre-Alloy 6 State Modeling Idiom

**Reference:** 03a.AlloyPart1-2.pdf, slide 19, 55

Prior to Alloy 6's temporal logic, state evolution was modeled idiomatically by defining multiple signature atom instances representing pre-state and post-state of the same entity (e.g., b and bpost).

## Declarative vs. Operational Operation Specifications

**Reference:** 03a.AlloyPart1-2.pdf, slide 5, 19

Operation predicates in Alloy are declarative relational specifications that describe constraints relating pre- and post-states, rather than operational procedures or step-by-step mutating algorithms.

## Corner Case: Idempotent Add and Pre/Post State Aliasing

**Reference:** 03a.AlloyPart1-2.pdf, slide 19, 21, 22

In an add predicate defined as 'bpost.addr = b.addr + n->a', if 'n->a' is already in the address book, set union is idempotent, allowing the analyzer to satisfy the predicate by aliasing 'b' and 'bpost' to the same book atom.

## Counterexample in Add-Delete Inversion Assertion

**Reference:** 03a.AlloyPart1-2.pdf, slide 21, 22

Walkthrough of delUndoesAdd counterexample: deleting after adding fails to restore the initial book if 'n->a' already existed (making add a no-op while del still strips the entry), resolved by adding the precondition 'no n.(b.addr)'.

## Bounded Verification vs. Software Testing

**Reference:** 03a.AlloyPart1-2.pdf, slide 24

Bounded verification is sound and exhaustive across all possibilities within a fixed scope bound (missing errors outside bounds), whereas software testing samples arbitrary inputs across an infinite domain without exhaustive coverage, making them complementary.

## Functions vs. Predicates in Alloy

**Reference:** 03a.AlloyPart1-2.pdf, slide 25, 26

In Alloy, functions ('fun') evaluate to expressions/values (such as relations or sets of atoms), whereas predicates ('pred') evaluate strictly to Boolean truth values.

## Alloy Metamodel Visualization

**Reference:** 03a.AlloyPart1-2.pdf, slide 30

The metamodel view in the Alloy Analyzer displays structural signatures and relations at the schema/type level, as opposed to instance graphs of individual atoms and tuples.

## Facts vs. Predicates Execution Semantics

**Reference:** 03a.AlloyPart1-2.pdf, slide 26, 43

Facts are global invariant constraints enforced unconditionally across every generated instance of a specification, whereas predicates only enforce constraints when invoked via a run command or referenced within another expression.
