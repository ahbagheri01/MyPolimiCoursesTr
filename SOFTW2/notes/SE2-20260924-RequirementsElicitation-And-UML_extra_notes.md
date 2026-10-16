# SE2-20260924-RequirementsElicitation-And-UML — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260924.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02b.video1_ElicitationOfRequirements.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02d.video2_ModelingReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf

## Refining Flow-of-Events Descriptions to Clarify System Responsibilities

**Reference:** 02c.ExampleScenarioUCReqs.pdf (slide 4)

Natural-language use case steps often mistakenly use passive or ambiguous phrasing (e.g., 'the Dispatcher is notified'). Such descriptions must be rewritten to explicitly state the system's role (e.g., 'FRIEND receives the form and notifies the dispatcher'). Similarly, when moving from a user action to an exit condition, missing intermediate system steps—such as the system receiving a response and relaying it—should be made explicit so that system boundaries and functional obligations are unambiguous.

## Role and Limitations of AI Agents in Requirements Elicitation

AI agents can assist in requirements elicitation by reading project documentation and generating initial draft scenarios or skeleton use cases based on structured prompts (such as identifying system vs. actor actions). However, AI agents cannot directly observe human stakeholders in their operational environment, and the ultimate responsibility of identifying actors, judging scenario completeness, and discovering system boundaries must remain under human control.

## Avoid Modeling the 'System' as an Actor in Use Case Diagrams

**Reference:** 02e.UML4RE.pdf (slide 5)

In UML use case diagrams, students frequently make the error of adding an actor stick-figure labeled 'System'. The system to be developed is the entity implementing and supporting all use cases; therefore, it cannot be modeled as an external actor interacting with itself. While some modeling tools permit drawing a rectangular boundary around the use cases to denote the system perimeter, the system is fundamentally everything inside that perimeter rather than an external participant.

## Domain Operations vs. Software Implementation Operations in Class Diagrams

**Reference:** 02e.UML4RE.pdf (slide 9)

Unlike software design class diagrams which list software methods and programmatic operations, conceptual domain-level class diagrams generally omit operations and focus strictly on domain entities, attributes, and relationships. When an operation is exceptionally included at the requirements level (for example, 'moves' for an Ambulance), it must model a real-world physical phenomenon in the application domain rather than a programmatic method of a software class.

## Modeling Choices for Attributed Relationships: Class vs. Association Class

**Reference:** 02e.UML4RE.pdf (slide 11)

When performing noun-verb analysis, verbs sometimes carry their own descriptive data (such as 'bid', which is grammatically a verb but carries an amount and a timestamp). In UML, this can be modeled either as an explicit domain entity (class) connected via associations to other classes, or as an association class linking participants and items with attributes. While experienced UML practitioners may use association classes with attributes, reifying the concept as an explicit class is often clearer and equally valid.

## UML Semantics and Multiplicity Distinction (* vs 1..*)

**Reference:** 02e.UML4RE.pdf (slide 11)

In UML class diagram associations, multiplicity must be chosen deliberately: using an asterisk (*) alone denotes 0..* (zero or more), whereas 1..* denotes one or more. For example, an item in an auction might have zero or more bids (represented by *), while an auction must involve a batch of items (represented by 1..*). The official standard defines the precise semantics, though accessible online resources can serve as practical intermediate references despite advertising clutter.
