# SE2-20261015-RASD-And-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261015.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02g.CreatingRASD.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Strict Exclusion of Design Decisions from the RASD

**Reference:** 02g.CreatingRASD.pdf (slide 14)

Requirements documents must strictly exclude premature technical implementation choices (e.g., choosing a web application vs. mobile/desktop) unless explicitly mandated as constraints by external stakeholders. Prematurely embedding implementation assumptions artificially restricts the design space during later architecture phases.

## Scope and Objectives for Course Project Alloy Modeling

**Reference:** 02g.CreatingRASD.pdf (slide 23)

Students are explicitly advised against attempting a comprehensive Alloy formalization of the entire system specification. Instead, formal analysis in the RASD project should target at most one or two critical, non-trivial core properties to validate the correctness of system invariants without unnecessary model bloat.

## Shortcomings of the Static GenKey Specification and State Evolution

**Reference:** 03b.AlloyExercises.pdf (slide 60)

The basic temporal GenKey formulation in slide 60 exhibits two subtle modeling caveats: (1) with an immutable `sig EKey`, the operation merely reassigns an existing key without checking if that key is already bound to another locker (`not EK in Locker.hasKey`); and (2) keeping `storesLuggage` invariant across transitions allows an empty locker to generate a key without confirming luggage was deposited.

## Alternative Signature Hierarchies for Typed Cubes vs. Size Field

**Reference:** 03b.AlloyExercises.pdf (slide 45)

Modeling cube sizes can either be done via a dedicated `Size` signature associated with an attribute on `Cube`, or via direct subtype hierarchy where `Cube` is an abstract parent extended by `LargeCube`, `MediumCube`, and `SmallCube`. The attribute-based representation is slightly more verbose in Alloy than direct subtyping.

## Semantic Tooling Distinction: Pure Drawing vs. Model-Based UML Tools

Pure drawing tools (e.g., Draw.io) maintain isolated visual shapes rather than true conceptual entities, forcing error-prone duplicate rework across views. In contrast, model-based UML modeling tools (Visual Paradigm, StarUML) persist shared semantic entities across use cases and class diagrams.
