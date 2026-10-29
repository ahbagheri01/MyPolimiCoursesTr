# SE2-20260924-RequirementsElicitation-And-UML — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260924.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02b.video1_ElicitationOfRequirements.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02d.video2_ModelingReqs.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf

## Wrap-Up: Finding the World/Machine Boundary Is Itself the Creative Work of RE

**Reference:** None (recap of the previous lecture's final slide; that deck is not among the mapped materials)

The lecture opened by recapping the previous one:

- The boundary between the world and the machine is generally not given, and it is unknown when requirements engineering starts. Identifying it is one of the main purposes of RE. It is not trivial and needs effort and creativity.
- Once the boundary is understood, you identify goals and explore alternatives. You can roll back and change a goal, which changes the requirements and domain assumptions. You can also strengthen the domain assumptions, or look at how some requirements could be implemented.
- There is no single solution. You evaluate the trade-offs between options, compare them, and decide which one to follow.

The details of scenarios and use cases are in the assigned videos (02b, 02d). In class the professor only summarized them and invited students who had watched the videos to give feedback.

## Making the System's Role Explicit in Each Use-Case Step (ReportEmergency Critique)

**Reference:** 02b.video1_ElicitationOfRequirements.pdf, pp. 15-17, 21; 02c.ExampleScenarioUCReqs.pdf, slide 4

The professor criticized the course's own ReportEmergency use case:

- **"At which point, the Dispatcher is notified"** is poorly written. It does not say what the system does. Is it FRIEND that notifies the dispatcher? "Hopefully" it is, but the text does not say so. A clearer version: *"FRIEND receives the form and notifies the Dispatcher that the form has been prepared."*
- **There is a gap before the exit condition.** The flow ends with "the Dispatcher selects a response and acknowledges the report", but the exit condition says the Field Officer *has received* them. A step is missing: *"FRIEND receives the response and the acknowledgement and transfers them to the Field Officer."* The exit condition describes the state of the environment plus the machine at the end of the use case.
- **Why it matters:** you improve the description iteratively so that it says, as explicitly as possible, which actions the software-to-be performs and which ones the other actors perform. Modelling these interactions is how you find out what the system has to offer.
- **Practical tip:** give the system-to-be a concrete name (here FRIEND), so you can refer to it clearly throughout the analysis.

## Why the Connection-Loss Exceptions Exist

**Reference:** 02b.video1_ElicitationOfRequirements.pdf, p. 19; 02c.ExampleScenarioUCReqs.pdf, slide 5

Both the Field Officer and the Dispatcher are notified immediately when a connection is lost. The point is that, whenever there is a connection problem, everyone is aware of it and can try to find a different way to communicate.

## Using AI Agents for Scenarios and Use Cases, and What Must Stay With You

**Reference:** None (not in slides)

- **What an AI agent cannot do (for now):** watch what stakeholders do.
- **What it can do:**
  - read the documentation and propose relevant scenarios, which you then supervise and revise;
  - from those scenarios, create use-case skeletons if you give it the required structure and precise instructions (e.g. "identify the actions to be executed by the system and by the actors").
- **What stays with you:**
  - **Adding scenarios** from your own observations and interviews.
  - **Judging completeness.** You can never be sure the set of scenarios is complete. You can only reach the point where everything you currently think is needed is described somehow.
  - **Identifying the actors.** The professor thinks this should remain your responsibility, because the actions depend on which actors were identified.
  - **Running the activity.** You conduct it and keep everything under control. Discovering the system's boundaries and how it interacts with the environment is your job.

## Reading the Scheduling Scenario's Event Categories

**Reference:** 02c.ExampleScenarioUCReqs.pdf, slides 10-11

- **Several categories at once:** one appointment or task can belong to several categories. "Working on the project" is both *fixed-time* and a *working* event. Other events can be *personal*.
- **Fixed-time** means the event cannot be moved within the schedule.
- **Flexible, minimum length 30 min:** lunch is currently scheduled for one hour. It can be shortened, but it must keep at least 30 minutes.
- **Why the overlap warning is acceptable:** lunch overlaps the new meeting, but lunch is flexible, so the overlap is fine. What matters is that the user still has enough time to get to the meeting location. (The transcript around this point is partly garbled, so it is uncertain exactly which time he referred to.)

## The Insert Fixed Time Event Use Case: From a Student Project, Imperfect but Useful

**Reference:** 02c.ExampleScenarioUCReqs.pdf, slides 13-16

- **Origin:** the scenario and the use case were taken from the documentation of a student project of a few years ago ("worked by colleagues of you"). The course just extracted them. The GPS Service is an actor because the problem involves locations and travel times.
- **Imperfect but useful:** the use case is "not necessarily perfect", but you can still derive requirements from it. The software must:
  - offer a form where all the listed pieces of information can be inserted;
  - use GPS both to get the current location and to give path indications;
  - calculate travel paths;
  - place the new event in the user's calendar.
- **Scenario detail:** the professor also seemed to say that the scenario is more detailed than the use case in places, in particular about which pieces of information the user inserts. Much of the read-through of the use-case table is garbled in the transcript (ASR unclear).
- **World-only phenomenon:** while the user is going to the meeting, the system does not take part in the interaction. That is why "user goes to meeting" is a world-only phenomenon.

## Q&A: Exit Condition Overlapping With the Exception, and Why Use Cases Are Never Perfect

**Reference:** 02c.ExampleScenarioUCReqs.pdf, slide 14

- **The question:** a student noticed that the exit condition ("…if there are overlaps … shown as warnings") repeats what the Exception row says, and asked whether this is necessary.
- **The answer:** it is not. The authors could have stopped the exit condition at "the event is in the User timetable" and described the overlaps and warnings only in the exception.
- **General lesson:**
  - Almost every use case can be cleaned up, and the better you understand the problem, the more you can polish it.
  - Unless a use case is quite small, it is very difficult to write a perfectly clean one. You should still aim to improve it as much as you can.
- **Algorithms appear on the way:** use cases describe the interaction with the environment, not internal algorithms. Still, writing them reveals what has to be implemented, here the GPS interaction and the travel-path calculation. You do not decide *how* to compute the path yet, but you collect information that will help in the later phases.
- **Why bother:** on paper this can look boring, a list of sentences and small details to watch. Once you are immersed in a project, it becomes a useful tool for thinking about how the system should interact with the environment.

## UML in RE: Prerequisites and Scope

**Reference:** 02e.UML4RE.pdf, slide 3

- **Prerequisite:** the professor assumes everyone already knows UML. Anyone who does not should tell him, and he will provide material. Only the main elements will be reviewed, but UML will be used extensively in the course examples.
- **What UML is used for here:** in requirements analysis, UML models the *problem* and its structure, not the structure of the solution. That is why only the highlighted subset of diagrams is used. The others are not relevant for RE tasks.

## Use-Case Diagrams: What the Name and the Relationships Tell You

**Reference:** 02e.UML4RE.pdf, slides 4-7

- **Why the name matters:** a use-case diagram shows all use cases at once, and each one appears only by its name. A meaningful, action-like name is what gives the reader an immediate idea of the task.
- **Include** (functional decomposition) was already used twice:
  - ReportEmergency invokes AllocateResources;
  - the scheduling use case's step 9 is "Included use case: Calculate travel paths".
- **Generalization** uses the same arrow as class generalization in UML and means the same kind of relation. The base use case plays the role of a class higher in a hierarchy, and the specialization is a specific type of task (a specific ATM transaction such as withdrawing cash).
- **Extend** adds an optional, independent feature to a base use case that is complete on its own. It is usually conditional: it comes into action when a specific condition holds. The professor tied this to the ReportEmergency exception: the condition "the connection is broken" could become its own use case that extends the main use case.
- **Why include at all?**
  - You could avoid it and describe the steps inline.
  - But a task like customer authentication is needed in several use cases: it is included both in the ATM transaction and in a home-banking transaction. It is convenient to describe how authentication works once and include it wherever it is needed, much like a function reused in several parts of your code.
  - An included use case is required and has no explicit condition, because it happens anyway.

## Where to Check UML Semantics

**Reference:** 02e.UML4RE.pdf, slide 7 (uml-diagrams.org links)

- **The UML standard** is the reference for the actual semantics of the language elements.
- **The uml-diagrams.org site linked on the slide** gives informal documentation that is quite accurate and aligned with the standard, so it is a useful intermediate reference.
- **Its drawback:** it is full of advertisements, so it takes some time to get through, but you will find reasonably clear content there.

## Reading the Refined Incident-Management Diagram

**Reference:** 02e.UML4RE.pdf, slide 8

- **A lower level of abstraction:** the refined diagram details the three use cases of slide 5 (ReportEmergency, OpenIncident, AllocateResources).
- **What the diagram shows:**
  - ReportEmergency is a specialization of a more general ReportIssue, which can have other specializations.
  - ManageConnectionProblem extends ReportEmergency and handles the lost-connection case.
  - ViewMap is included by both OpenIncident and AllocateResources. It seems to visualize the positions of the incident and of the resources (ASR partly unclear).
  - AllocateResources involves not only the Dispatcher, who initiates it, but also the ResourceAllocator and the Resources as participants.
- **Actors are not necessarily human:** the stick-figure icon suggests a human being, but an actor can be legacy software, hardware, or anything in the external environment that is not under your responsibility and interacts with your software.
- **Q&A: why ReportRobbery?** The system is about reporting emergencies, so ReportRobbery is there only to show the various relations in a complete diagram. If the software really had to handle other kinds of situations too, you would have to define those use cases in detail as well.

## Common Mistake: Do Not Draw "System" as an Actor

**Reference:** 02e.UML4RE.pdf, slides 5, 8

The professor asked the class where the system-to-be is in the diagram, because "often we see the problems" here.

- **It is not one element:** all the use cases together are the system. It is "everywhere", because it implements and supports all the activities.
- **The mistake:** adding an actor icon and calling it "System".
- **The rectangle:** some tools suggest drawing a box that represents the system, with all actors outside it. The course diagrams leave it out because it is fairly useless: the system is everything that is not an actor. You may still draw the rectangle, e.g. for graphical reasons.

## Domain Class Diagrams: The Gap to Implementation, and Which Operations Are Allowed

**Reference:** 02e.UML4RE.pdf, slide 9

- **Domain entities and implementation:** the domain model's entities belong to the description of the world, but some of them may end up in the implementation. "Incident" will most likely become a database entry, and in an object-oriented implementation probably also an `Incident` class. For now you only care about the concept at domain level. The gap between the two is filled during design.
- **Why there are usually no operations:**
  - Implementation-level classes list operations.
  - Most domain concepts have no operations relevant to describing the domain, so you describe them by their attributes (qualities) only.
- **The exception:** an operation that happens *in the application domain*. For example, "the ambulance moves" could be modelled as a `moves` operation of Ambulance. That is a domain-level operation, not an implementation one. All decisions on how things are implemented are postponed.

## Auction Exercise: Noun-Verb Analysis Is a Set of Modelling Decisions

**Reference:** 02e.UML4RE.pdf, slides 10-11

- **Many models are possible:** the final diagram is "one possible model", and others are possible. The essential parts are:
  - naming each relationship, because the name carries its meaning;
  - getting the cardinalities right, i.e. how many elements of one entity relate to how many of the other.

  The professor called this the main message.
- **Choosing relevant nouns and verbs is your decision.** In "Each auction involves a batch of items…", you may decide that *batch* is not a relevant concept, or make it one. In the model it is not a class: the batch is mapped into the `1..*` cardinality on Item (an auction involves one or more, an unbounded number of, items).
- **Every cardinality excludes cases (counterexample):** the `1` on the Auction side says that an item belongs to exactly one auction. So selling an item today and putting it up again in another auction a month later is not foreseen by this model. A different cardinality would be needed for that (the follow-up remark is partly garbled, ASR unclear).
- **`*` vs `1..*`:** a bare `*` means `0..*`, not `1..*`. So `Item 1 — * Bid` allows an item with zero bids. The two are similar but not the same.

## Auction Exercise: Bid as a Class vs. an Association With Attributes

**Reference:** 02e.UML4RE.pdf, slides 11-12

- **The alternative:** instead of a Bid class, you could model the bid as a relationship between Participant and Item ("participant bids for item"). That is a different but legitimate modelling choice.
- **Why the slides chose a class:** in the rest of the description the bid carries information, such as an amount of money, which must be tracked.
- **Q&A on the alternative:** a student asked whether a UML relation can have attributes. Yes: you attach a box with the attributes to the association (an association class). This is a reasonable model too, just a bit more complicated.
- What matters is that the information is modelled in one way or the other.

## Auction Exercise: Reading the Full Solution

**Reference:** 02e.UML4RE.pdf, slide 12

- **No direct Participant–Item link:** there is no direct association between Participant and Item, because the bid is an explicit concept. Participant *makes* Bid, and Bid *concerns* Item.
- **`isHighest`:** this association links an item to its highest bid. It is important because that is the winning bid, the one tied to the final purchase of the item.
- **The other elements:**
  - a third-party application *monitors* auctions;
  - organizers, directors and assistants are different roles;
  - Date, Time and Timestamp are data types used as attribute types (e.g. Auction `date: Date`, Bid `time: Timestamp`).
- **The professor's advice:** do the noun-verb analysis on the description yourself as an exercise. You need to get used to building such diagrams from a general description. If you define proper associations and careful cardinalities, the result is a summary of the description that, in the end, has a formal meaning.
