# SE2-20260924-RequirementsElicitation-And-UML — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260924.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02b.video1_ElicitationOfRequirements.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02d.video2_ModelingReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf

## Requirements engineering and the machine-world boundary

**Reference:** 02c.ExampleScenarioUCReqs.pdf, slide 17; 02d.video2_ModelingReqs.pdf, slide 9

The boundary between the world and the machine is unknown at the beginning of requirements engineering; discovering it is a creative activity of exploring trade-offs across goals, requirements, and domain assumptions.

## Use Case Structure: Entry Conditions

**Reference:** 02b.video1_ElicitationOfRequirements.pdf, slide 13; 02c.ExampleScenarioUCReqs.pdf, slide 7

In a use case specification, an entry condition of 'true' explicitly signifies that the use case can occur at any time without prerequisites.

## Use Case Writing: Clarifying System vs. Actor Actions

**Reference:** 02b.video1_ElicitationOfRequirements.pdf, slides 20, 21

Avoid passive phrasing in use case steps (e.g., 'the dispatcher is notified') because it obscures the system's role; steps should explicitly name the system (e.g., 'FRIEND receives the form and notifies...') to clearly delineate machine actions from actor actions.

## Role of AI Agents in Scenario and Use Case Modeling

AI agents can process existing documentation to propose candidate scenarios and use-case skeletons, but actor identification, system boundary discovery, supervision, and validation must remain human responsibilities.

## UML in Requirements vs. Implementation

**Reference:** 02e.UML4RE.pdf, slides 9, 27

During requirements engineering, UML diagrams are used strictly to model the application domain and the structure of the problem rather than the software solution architecture.

## Common Pitfall in Use Case Diagrams: System as Actor

**Reference:** 02e.UML4RE.pdf, slides 5, 8

In a UML use case diagram, it is an error to model the system itself as an actor icon, because the system boundary encapsulates all use cases and actors must be strictly external entities.

## Conceptual Domain Class Diagrams vs. Implementation Class Diagrams

**Reference:** 02e.UML4RE.pdf, slide 9

Operations should generally be omitted from domain class diagrams unless an operation represents a physical domain event (e.g., 'ambulance moves'), thereby postponing design operations to software design.

## Noun-Verb Analysis for Domain Modeling

**Reference:** 02e.UML4RE.pdf, slide 11

In noun-verb analysis for domain modeling, a verb phrase may be promoted to a domain class/entity rather than an association if it possesses attributes or state of its own (e.g., 'bid' carries an amount of money).

## UML Multiplicities: Star vs. One-to-Star

**Reference:** 02e.UML4RE.pdf, slide 11

In UML class diagram associations, a standalone '*' multiplicity denotes '0..*' (optional / zero or more), distinct from '1..*' which requires at least one.

## Modeling Attributes on Relationships vs. Association Classes

**Reference:** 02e.UML4RE.pdf, slides 11, 12

When an association carries data, UML allows modeling it either as an explicit class/entity or via an association class (a relation box with attributes); choosing an explicit class is often preferred for conceptual simplicity.
