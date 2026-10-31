# SE2-20260930-PreviousYearRecording-UML-And-AlloyPart1 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260930.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02e.UML4RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

> **Material limitations:** The 30/09/2026 lecture recording failed. The course links the previous year's recording instead (02/10/2025), and these notes are based on that transcript. Anything about dates, the book edition, or "next week" refers to the 2025 edition and may not hold for 2026. Deck 03a is shared with later Alloy lectures: this lecture only reached slide 17 (the empty `show` predicate run in the Analyzer), so the notes were compared against the whole deck but only cover that part. 03a has 77 PDF pages, but its printed slide numbers run to 78 (there is no slide 61). References below use the printed slide numbers. Some parts of the transcript are garbled or partly cut (the fork/join part of the activity diagram, part of the "UML for RE" summary). Those are marked where relevant.

## Reading the ATM State Machine: Composite States and Separate Sub-Diagrams

**Reference:** 02e.UML4RE.pdf, slides 22-23

- Notation: rounded rectangles are states. The filled dot points to the initial state (Open in the Problem diagram, Off in the ATM). The bullseye means the entity's evolution is finished and the diagram stops there.
- **Serving Customer** is a high-level state "exploded" into sub-states. When a transition (e.g. cardInserted) enters it, the inner state machine starts and you immediately enter its initial sub-state, Customer Authentication. From there you go to Selecting Transaction, then Transaction, then the inner end.
- The small icons on Customer Authentication and Transaction mean these states are decomposed further, but in **a different diagram**. You cannot put every sub-diagram in one diagram or it becomes unreadable, so you defer them.
- When the inner machine terminates, the ATM goes back to Idle through the transition that has no triggering event.

## Entry/Exit Actions and Event/Action Labels on Transitions

**Reference:** 02e.UML4RE.pdf, slide 23

- `entry / readCard` runs when you enter Serving Customer, **before** you even enter the Customer Authentication sub-state. `exit / ejectCard` runs when the transaction terminates, before you leave the state.
- On a transition labelled `turn on / startup`, the part before the slash is the **triggering event** and the part after is an **action** executed while the transition happens. If nobody turns the system on, the ATM simply stays in Off.
- A transition with **no triggering event** (e.g. Self Test → Idle) "can happen at any time". If a failure occurs instead, the `failure` transition to Out of Service is taken.
- The `cancel` and `failure` transitions leaving Serving Customer can also fire at any moment while you are inside it, e.g. while you are in Selecting Transaction.
- In summary, a state diagram can express states, hierarchical states detailed into sub-states, transitions triggered by specific events, and actions executed on top of moving to the new state.

## State Diagrams Are Class-Level, Sequence Diagrams Show One Evolution

**Reference:** 02e.UML4RE.pdf, slides 20, 24

- You build a state diagram when you take an entity from the class diagram (e.g. Problem in Trip Tracker) and decide its internal behaviour must be modelled explicitly. It is class-level because **every** instance (every particular problem, every particular ATM) evolves through that same state machine.
- A sequence diagram is instance-level: it shows one possible evolution with specific instances. Example: the Trip Tracker SD assumes the reply to `subscribe` is OK. If there were an error at subscription, `notify(problem)` would not happen. That case is not in this SD but could be described in a **different** sequence diagram.

## Activity Diagrams: Relation to BPMN and How Decisions/Merges Form Loops

**Reference:** 02e.UML4RE.pdf, slides 25-26

- Activity diagrams are for describing processes. For students who took Information Systems, they are similar or essentially equivalent to **BPMN** diagrams. BPMN is richer because it is specialised for processes, but activity diagrams can also be used for that.
- In the exam-registration example, the login is a **loop**: if the user is not valid, you go back through the merge and redo the login activity. The "external exam" branch is an exam offered, e.g., by another university, which leads to mailing the instructor instead of registering on the web.
- The same diamond icon is used both for decisions and for the points where flows from different directions merge. As in a program's control-flow diagram, decisions express both selections between paths and loops.
- Swimlanes (Student vs System) can be used in any activity diagram to show who or what is responsible for each action.
- After the fork, each parallel sub-process (store, tell instructor) is a single activity here, but in general a sub-process can contain several activities. At the join, the parallel execution stops and the flow continues to the end. Part of this explanation is lost in the transcript (ASR gap).

## Sequence vs Activity Diagrams Can Describe the Same Thing

**Reference:** 02e.UML4RE.pdf, slide 26

The professor added that something described with a sequence diagram could, in principle, also be described with an activity diagram. Swimlanes identify the actors/objects performing each action. The choice is about emphasis: the activity diagram stresses the activities and their flow, while the sequence diagram stresses the message exchange between the parties. That is why SDs suit interaction protocols and ADs suit processes.

## Requirement-Level Sequence Diagrams May Show Interactions Outside the System

**Reference:** 02e.UML4RE.pdf, slides 20, 28

- At requirements level, an SD can describe interactions between actors and the system, or **between actors themselves**. Such an interaction is irrelevant for the system's design. It can still be worth drawing at requirements level, to make clear that the interaction happens outside the system.
- Such an interaction typically leads to a **domain assumption**, e.g. "we assume this specific interaction happens outside the system between these two actors".
- The interaction between two actors can also be **mediated by the system**: one actor sends a message, and before replying the system first interacts with the other actor.
- These requirement-level SDs are very simple and focus on the protocol through which the parties communicate. If you care about the process rather than the interaction, you could draw an activity diagram instead, e.g. with three swimlanes for the two actors and the system.
- (Part of this passage is garbled in the transcript.)

## Airbus Model: Deliberate Oversimplifications and What the Diagrams Are For

**Reference:** 02e.UML4RE.pdf, slides 32-34

- Class diagram: the model is deliberately oversimplified. An aircraft has three or four wheels, but at this level of abstraction they are treated as **one single entity** (Wheel), so no cardinality is given for the aircraft–wheel relation.
- The aircraft state machine is useful mainly to show which part of the life cycle matters: the bottom portion, and in particular the transition from **Landing** to **Moving on runway for landing**.
- You might have modelled the states differently, and that is fine: any system can be modelled in multiple ways. As an exercise, try other state machine diagrams for this example.
- Use case Enabling Reverse Thrust: the rotation sensor is the **initiator**, because it produces the signals that activate the use case. The reverse thrust system is a **participant**. These roles could have been stated explicitly in the diagram.

## Asynchronous vs Synchronous Messages in the Airbus Sequence Diagram

**Reference:** 02e.UML4RE.pdf, slide 34

- The rotation sensor sends an **asynchronous** message ("wheels rotating") to the aircraft braking system (the software-to-be). This triggers an activity, the activation rectangle. Within it, the braking system sends a **synchronous** request to the reverse thrust system and waits for the "ok" reply.
- Asynchronous messages expect no reply, so the sender continues its work without being blocked.
- Synchronous messages block the sender, or at least part of it: a system may do several things in parallel, but some part of it will be waiting for the reply.
- The professor said it is important to distinguish the two.

## Filling UML's "Last Mile": Discipline in Natural Language, Then Alloy

**Reference:** 02e.UML4RE.pdf, slides 35-36

- UML helps identify actors and the important domain elements, but it cannot express the constraints/rules (goals, domain properties, requirements such as "reverse enabled iff wheel pulses on"). That is the missing "last mile".
- You can write those constraints informally in natural language. A good discipline is to **never use, in a goal, domain property or requirement, an entity that does not appear in the class diagram**. This forces you to clarify each entity's role before using it.
- Alloy is introduced exactly for this. In Alloy you can also write these constraints and **formally verify** whether, given the requirements and domain properties, the goal is achieved. It is not achieved if the definition is incomplete.

## Course Book and Alloy Study Resources (2025 Edition)

**Reference:** 02e.UML4RE.pdf, slide 37; 03a.AlloyPart1-2.pdf, slide 3

- Chapters 3–8 of the course book cover the requirements engineering part. **Alloy is not in the book.** In 2025 the authors were planning a new chapter, but the current edition did not have it.
- The book is a first edition and probably contains errors. The professor asked students to report any error or issue they find.
- For Alloy, the freely available online book (Practical Alloy) "should be more than enough" for the course's usage. *Software Abstractions* is the first book on Alloy.

## Model Checking and the Alloy 5 vs Alloy 6 Warning for Old Exams

**Reference:** 03a.AlloyPart1-2.pdf, slides 4, 9

- Verifying properties with the Analyzer is technically **model checking**, a discipline of its own. The course "Formal Methods for Software Engineering" covers it fully. SE2 only gives a taste.
- Alloy's "strong mathematical foundation" means it is based on (first-order) logic. It does **not** mean it is good at mathematical operations, which in fact it is "quite bad" at.
- **Old exams use Alloy 5.** Exam exercises from earlier years (the professor was unsure of the cutoff: before 2023, or perhaps before 2022) use the previous version. You can still use them to study, but in Alloy 6 some things are done slightly differently, so the model you get is slightly different.
- The main Alloy 6 change is that time and entities changing state can be modelled naturally. Before, all sets and relations were immutable; now mutable elements can be introduced.
- Modules will not be studied in detail because the course uses small models. In some cases, though, the course will use external modules that already come with Alloy.

## Why Verify a Model That Is Not the Implementation, and Choosing the Abstraction Level

**Reference:** 03a.AlloyPart1-2.pdf, slides 5-7

- Objection: proving properties on the model does not guarantee the implementation has them. The professor agreed. His point is that if you never define the properties and constraints explicitly and prove them at model level, you may not understand the problem well enough to write a program that fulfils them. Formal verification is a **tool for understanding the problem better**, and should be used that way.
- So do not model too many details. Too much detail makes verification very complex and slow. You may fail to get a clear model and get stuck trying to prove properties.
- The right level of abstraction keeps the problem tractable while still exposing the issues you will face in design and implementation. Finding that balance is the real difficulty.

## Formal Methods in Industry: STMicroelectronics Example

**Reference:** 03a.AlloyPart1-2.pdf, slide 8

Besides the Intel and NASA papers on the slide, the professor mentioned a formal methods conference held about a year earlier (relative to 2025), in that same lecture room. There, STMicroelectronics, an important Italian microprocessor company, explained how it uses formal methods to prove properties of hardware and of software interacting with hardware. Formal verification is gaining momentum in industry because the techniques have become sophisticated enough for real use. It is not only for university people.

## Address Book: Signatures, the Hidden Ternary Relation, and the Effect of `lone`

**Reference:** 03a.AlloyPart1-2.pdf, slides 11-14

- The entities (book, name, address) emerge naturally from the textual description, and each becomes a signature. Example address book: the name "Professor Rossi" linked to his email address, "Professor Camilli" linked to his. `sig Name, Addr {}` declares two distinct signatures with no internal characteristics, i.e. ground elements.
- `addr` looks like a field of Book but is really a **ternary** relation. Example triples: (B1, N1, A0), (B1, N2, A3), (B2, N1, A2), (B2, N2, A3), and as many more as you want. Conceptually, B1 and B2 are two different address books with different contents.
- Because of `lone`, a name in a given book maps to at most one address, so (B1, N1, A0) and (B1, N1, A1) cannot coexist. Remove `lone` and both become allowed. On multiplicities: `set` can be empty, while `some` requires at least one element.
- Atoms (B1, N1, A0, …) cannot be divided but can take part in relations. "Uninterpreted" means a **ground concept** in logic, a basic notion that needs no explanation.
- Order inside a tuple is fixed and typed: in `addr` the Book is always first, the Name second, the Addr third.

## Getting a Binary Relation: Blackboard Example

**Reference:** 03a.AlloyPart1-2.pdf, slide 14

The professor asked the class how to obtain a **binary** relation (pairs) instead of a ternary one. His answer was a field such as `id` declared on Name with type String, so that `id` contains pairs whose first element is a Name and whose second is a String. He added that the String signature then needs to be defined. The exact code was written on the board and is not in the transcript (uncertain).

## A World May Contain Atoms That Appear in No Relation

**Reference:** 03a.AlloyPart1-2.pdf, slide 15

- If `addr` contains certain triples, every atom in them must exist in the corresponding signature's set. Each signature corresponds to the set of all its atoms instantiated in a particular world that satisfies the specification.
- The sets may contain **more** atoms than those used in `addr`. A name N3 that appears in no triple still gives a valid world, because no constraint says every name must belong to `addr`. Likewise Addr contains at least A0, A1, A2 but may contain others.
- Scalars such as `myName = {N1}` are singleton sets. The course will not use this mechanism much.

## How the Join (`.`) Works: The Matched Element Is Dropped

**Reference:** 03a.AlloyPart1-2.pdf, slides 15-16

- The dot is one of Alloy's most important operators. It corresponds to the relational-calculus join, with one difference: **the element used for matching is dropped from the result**.
- `Book.addr`: for each element of Book, take the triples of `addr` whose first element equals it. B0 matches (B0, N0, A0) and (B0, N1, A1), and dropping B0 gives (N0, A0), (N1, A1). B1 gives (N1, A2), (N2, A2).
- General rule: the **last** element of each left tuple is matched with the **first** element of each right tuple, and the matched element is dropped. If the left side held pairs (e.g. (A0, B1)) instead of single atoms, the join would use the pair's last element.
- `myName.(Book.addr)` contains two joins. Its meaning: `Book.addr` gives all name–address pairs across all books, and joining with `myName` extracts all addresses that correspond to my name in **any** book, here {A1, A2}.

## Running the Empty `show` Predicate: What "Instance Found" Means

**Reference:** 03a.AlloyPart1-2.pdf, slide 17

- In the demo the professor declared the signatures on separate lines and noted that this is equivalent to the slide's `sig Name, Addr {}`.
- An empty predicate contains no constraint, so it is always true. Running it just asks for worlds that satisfy the signature declarations.
- `run show for 3 but 1 Book` means **at most** 3 instances of each signature, but at most 1 Book. The world first shown in the demo had 2 names, 2 addresses and 1 book, which is valid because the bounds are upper bounds.
- "Instance found" means there exists at least one world (a set of entities) satisfying the specification. In the graph view, the arrows are the `addr` relation, e.g. the triple (Book, Name0, Addr1).
- Practical tip: copy-pasting code from the slides sometimes brings extra characters that stop the specification from working in the Analyzer.

## Analyzer Visualizer Details: Atom Labels, Built-in Sets, and the "New" Button

**Reference:** None (not in slides)

- **Label quirk:** when a signature has a single atom, the graph view shows just "Book". Its real, unique ID is "Book0", which the text view shows. Every element has a unique ID.
- The text view lists all generated sets, including predefined ones: an empty `String` set, sequences (covered later), and the integers **from −8 to 7**, which are part of every world. It also shows two integer-related sets ("similar to Java"; their exact names are ASR unclear) and `univ`, the universe, which contains every atom. Tabular and tree views are also available.
- **New** asks the Analyzer for another world that still satisfies the specification. Example: 3 addresses, only 2 of which belong to the book while the third stays "free". Another valid world has just one name and one address.
- When no significantly different worlds remain, the Analyzer shows a message. Pressing New again starts showing worlds from the beginning.
- The professor recommended playing with the Analyzer to see what happens.
