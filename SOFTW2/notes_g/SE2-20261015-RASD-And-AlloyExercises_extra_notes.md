# SE2-20261015-RASD-And-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261015.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02g.CreatingRASD.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Evolution of ISO/IEC/IEEE 29148 Standard and Course RASD Mapping

**Reference:** 02g.CreatingRASD.pdf, slides 6, 18, 19

The professor highlights that in the November 2018 revision of the IEEE/ISO standard (29148), an explicit verification section was added (Section 4), reflecting that verifying the fulfillment of requirements is now an integral part of the requirement specification document itself. In the course's RASD template, the formal analysis with Alloy directly maps onto this verification section. Additionally, the professor notes why Revision History is explicitly added to Section 1 of the course template: in industry, version management of artifacts is standard practice and often handled externally, but academically it must be made explicit. The separate Document Structure section (1.F) is also emphasized beyond a mere table of contents to explain section organization, noting students are expected to provide this in their master's theses as well.

## Excluding Design Choices vs Stakeholder Technical Constraints

**Reference:** 02g.CreatingRASD.pdf, slide 14

When explaining pertinence in the RASD, the professor clarifies a common pitfall: prematurely stating design/implementation choices (e.g., stating 'we will develop a web application'). Even if there is a 99% chance the final software is a web app, defining it in the requirements restricts freedom if design later shows a mobile or desktop app is superior. The strict exception is when the stakeholder explicitly mandates a specific technology or platform as a contractual constraint.

## Scope and Expectations for Formal Analysis with Alloy in the RASD

**Reference:** 02g.CreatingRASD.pdf, slide 23

The professor explicitly advises students on the scope of the Alloy section in the project: students should NOT attempt to model the whole complex system, which would be excessively difficult and time-consuming. Instead, students must identify 1 or at most 2 critical objectives or elements of the system to investigate formally. The RASD must clearly document why those objectives were chosen, present the Alloy model, and provide verification evidence (predicates, assertions, and generated worlds with explanations).

## Recommended Project Tooling: LaTeX/Overleaf and Model-Centric UML vs Drawing Tools

The professor provides specific practical recommendations for project preparation: (1) LaTeX/Overleaf is strongly recommended for document creation due to superior typography; Overleaf can be linked to Politecnico accounts and synced directly with the private GitHub repository. (2) Pure drawing tools (specifically calling out Draw.io) should NOT be used for UML diagrams because they are mere icon palettes and lack an underlying semantic metamodel. Instead, model-centric UML tools such as Visual Paradigm or StarUML should be used because entity definitions are reused across use case diagrams, class diagrams, etc., ensuring semantic consistency. PlantUML is mentioned as an acceptable rendering alternative, though it lacks an integrated model repository.

## Luggage Keeper Alloy Model: Cardinality Incompleteness in Field Signatures

**Reference:** 03b.AlloyExercises.pdf, slides 54, 56

The professor notes an important modelling limitation: when mapping UML bidirectional associations to Alloy signatures, specifying a field multiplicity (such as 'hasKey : lone EKey' or 'owns : set Luggage') only enforces the cardinality constraint in that one direction. To completely represent the full bidirectional multiplicity of a UML class diagram, explicit facts must be written to constrain the reverse side of the associations.

## Luggage Keeper GenKey: Static Allocation vs Dynamic Creation and Free-Key Constraints

**Reference:** 03b.AlloyExercises.pdf, slide 60

In analyzing the 'GenKey' temporal operation in Alloy 6, the professor reveals critical modelling nuances: (1) Because 'sig EKey' is static (immutable), GenKey does not dynamically instantiate a new key; it merely selects an existing key atom from the universe and binds it. To guarantee proper semantics, an additional check ('not ek in Locker.hasKey') should be enforced so an in-use key is not reassigned. (2) Alternatively, the signature itself can be declared mutable ('var sig EKey') with a predicate specifying that the key atom was not in the set in the current state and is introduced in the next state. (3) In response to a student question on whether the locker is free, the professor acknowledges that GenKey assumes luggage is already present ('storesLuggage' = storesLuggage') and only handles assigning the key; to capture the full operation of inserting luggage and generating a key, the predicate must be extended.

## Alternative Modelling Strategy for Towers and Cubes: Hierarchy Specialization vs Size Attribute

**Reference:** 03b.AlloyExercises.pdf, slide 45

When introducing the Towers and Cubes problem, the professor contrasts two alternative modeling approaches: (1) defining a separate 'Size' signature and giving 'Cube' a 'size: Size' field (as shown on slide 45), versus (2) making 'Cube' an abstract signature and subclassing it directly ('sig LargeCube extends Cube', etc.). The professor points out that while using an attribute is functional, it results in a more verbose specification with more complex conditional rules compared to relying directly on subsignature typing.
