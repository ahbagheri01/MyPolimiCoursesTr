# SE2-20261001-ExercisesOnRE — Additional Professor Notes

**Transcripts:** SE2 - 1 1_10_2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02f.ExercisesRE.pdf

> **Coverage notes:** Exercise session taught by the TA (Simone Reale), not the main professor; "professor" below means the TA. Covered: a short review of world/machine/phenomena, AdmissionManager Q1–Q2 (incl. the domain-assumption question on p.8) and its use case diagram (p.15), then all three PaasPopCoin questions (p.20–26). Not discussed in the recording: p.9 (are the two registration requirements well formulated?) and p.16–17 (Send Application use case description). For the milk vending machine (p.27–30) the TA only read the text and started an online quiz; the recording stops there, so the solution table on p.30 was not discussed. He said that from now on he will upload the exercise slides before each session.

## World, Machine and Shared Phenomena: The TA's Framing

**Reference:** None (not in this deck; review of earlier lectures, used for p.20 and p.29)

- **World:** the part of reality the system affects. The whole intent (the goal) of what we build lives in the world, not in the machine: we want to change the external reality.
- **Machine:** the portion of the system we design, i.e. what we can actually build and manage.
- **Phenomena:** observable events or states. Ambulance example from the lectures: an accident happens in the world, and in the machine you create an "accident object". The two are correlated.
- **Shared phenomena** are what we mostly care about. They are the interface with the world: the machine's processes are built on them. Think of them as "your window on the world", the main way your system can affect the world.

## R and D ⊨ G Is the Whole Method for These Exercises

**Reference:** None (not in this deck; applies to p.7–13)

The TA reviewed the logical entailment (requirements and domain assumptions, all true together, imply the goals) and drew two consequences:
- Requirements are not just sentences that start with "shall". They are what, together with the assumptions, makes the goal hold.
- Domain assumptions are critical: if a **single** domain assumption does not hold, the whole argument built on the requirements collapses.

He called this entailment "the entire mental process" needed to solve this kind of exercise.

## Why "User Sends an Application" Is Not a Well-Formed Goal

**Reference:** 02f.ExercisesRE.pdf, p.5–6

The slides ask whether G1–G4 are well-formed and then give a better version, without saying what was wrong. The TA's answer: they are not meaningless, they are at the **wrong abstraction level**. A goal must state *why the system exists for the stakeholder* (the intent). G1–G4 describe operational steps, which belong to use cases.

His analogy: he woke up at 4 a.m. hungry and wanted to eat something from the fridge. The goal is to eat. "Get up from the bed, go to the fridge, open the fridge" are steps, not the goal.

## Goals Must Not Change When the Implementation Does

**Reference:** 02f.ExercisesRE.pdf, p.6

The improved goals ("parents can manage applications…", "school administrators can manage applications…") do not depend on the implementation. For example, if AdmissionManager starts as a website and later becomes an app, the goals stay the same. That is why goals matter for **traceability**: implementation details change much faster than what users actually need.

## Requirements Are Capabilities, Domain Assumptions Are Dependencies

**Reference:** 02f.ExercisesRE.pdf, p.10–11 (R1.x, A1.1)

- **Requirements:** put the system at the centre and think in **capabilities**: what should AdmissionManager enable (e.g. parents register, log in…)? In practice, read the description, note the verbs/actions performed by each actor (e.g. the parents), and collect every **prescriptive statement** in the text.
- **Domain assumptions:** think in **dependencies**: what does the system need in order to work? Answering a student, he compared dependencies to the parameters of a function: the input, or more precisely the fact that the input you give is correct.
- Applied to G1: "How can AdmissionManager work correctly if you provide wrong data?" It has no means of knowing whether the data is correct. So the one important domain assumption for G1 is that parents provide correct data (A1.1).

## Boring, Repetitive Requirement Lists Are Fine (Exam and Project)

**Reference:** 02f.ExercisesRE.pdf, p.10–13

Real-world requirements are often a very boring list, because precision matters much more than cleverness. The TA said explicitly that in the exam or the project it does not matter if you write a list of "AdmissionManager allows…, AdmissionManager allows…". Being precise matters more than being clever or elegant, and a repeated structure is a good thing in requirements.

## The "Switch Off the System" Test for Domain Assumptions

**Reference:** 02f.ExercisesRE.pdf, p.8

The slide asks whether "As soon as an application arrives to the system, a status needs to be assigned to it" is a domain assumption, but gives no answer. The TA's fastest test is a thought experiment: **imagine the system switched off ("kill the system") and ask whether the statement still holds, i.e. still describes the domain.**
- Status assignment: with the system off it no longer holds. So it is **not** a domain assumption: it is something you want to achieve, i.e. prescriptive (a requirement).
- "Parents give correct information": still true in the world with the system off, so it is descriptive of the world and is a domain assumption.

He repeated this test when a student asked about it after the exercise.

## Actors Set the System Boundary and Are Roles, Not People

**Reference:** 02f.ExercisesRE.pdf, p.15

- The first step of a use case diagram is to identify the actors. An actor need not be a person: it is any entity that interacts with the system.
- Actors **define the system boundary**. Choosing them says what is inside the system (what you can manage) and what is outside.
- Actors are abstract roles, not tied to physical people. The same person can be a parent at one time and a school administrator at another, or both a school administrator and a system administrator (answer to a student question).

## Initiate vs Participate in Use Case Diagrams

**Reference:** 02f.ExercisesRE.pdf, p.15

- He derived the use cases directly from the requirement list. Use cases decompose the goals into operational steps, so every goal and requirement leads to a part of the diagram.
- **«initiate»:** the actor who triggers the use case, i.e. the first to interact with the system. It matches the initiating actor in the textual use case description. **«participate»:** the actor is involved at some point inside the use case but is not in charge of it. In his words, "a matter of accountability and of who starts the use case".
- To decide, break the use case into its steps. Each use case corresponds to a specific function (e.g. in the UI):
  - *Send application:* the parent starts it. At the end a notification goes to the school admin, who therefore only participates.
  - *Accept/reject application:* the school admin retrieves the applications, opens one, reads it and decides. This admin is active and actually uses the function. The parent is passive (only gets the notification), so the parent participates.

## Classifying a Phenomenon Is a Decision About the Boundary

**Reference:** 02f.ExercisesRE.pdf, p.21–22

The question to ask is: **can the machine observe this phenomenon?** The answer depends on where you put the boundary, so sometimes there is no single correct answer:
- *User buys a Class A ticket:* calling it shared means the system is notified of ticket purchases, i.e. you are also building a backend for the ticketing system. Here the system only manages coin transactions and has no part in ticket buying, so it is world-only.
- *User inserts money/coins into an ATM:* two answers are possible. Making it shared, as the solution does, states that your application can observe that event, which says something about your system's boundary.

## Deciding Who Controls a Shared Phenomenon: Who Is Active?

**Reference:** 02f.ExercisesRE.pdf, p.22

Ask who is in charge (active) and who is passive:
- *User inserts coins into the ATM:* world-controlled, because the user initiates it.
- *System enables cash-back after checking the ID card and returned coins:* shared but **machine-controlled**. The user is passive and makes no decision there.
- *Cashier enters an ID card number:* shared, world-controlled, because the cashier is an external actor running the process.

The TA said this is the kind of reasoning you should use when doing the project.

## A Domain Class Diagram Is Not an Implementation Diagram

**Reference:** 02f.ExercisesRE.pdf, p.23–24

- This use of class diagrams is unusual. Class diagrams usually describe the implementation units given to programmers. Here they describe the **domain**: things are treated as entities, there is no direct link to the implementation, and you should be as abstract as you want.
- He called it a brainstorming of the entities to consider, done even before a first sketch of the application. The solution adds attributes, methods, labels and cardinalities, but he said they are not that important at this level of abstraction.
- Answering a student ("are we implying this class is implemented in the software?"): no. This is like the first meeting with your colleagues. During development you write several class diagrams at different levels of detail, and this is the most coarse-grained one, with no real correspondence to the code. For example, money and coins are separate entities here but may be the same thing in the implementation.

## Building the Domain Model by "Grammatical Analysis" of the Text

**Reference:** 02f.ExercisesRE.pdf, p.24

- Start from the most cited noun, the one performing the most actions: here **User**. Then model the kinds of user the text lists as a specialization hierarchy (VIP, event organiser, ticket holder → Class A / regular).
- Then add what the user handles (money, coins, ID card, products). At this abstract level you do distinguish coins from money. He warned not to draw these links with the specialization arrow, which is only for the user hierarchy.
- Cashier and ATM have exactly the same methods: the same interface offered by two different actors, which he said is quite common in software systems.
- He compared the method to Italian *analisi logica* (grammatical analysis): find the nouns/subjects and the actions they perform. Most of the time subjects become entities and actions become relationships (e.g. the shop clerk *tracks* Sale, and Sale is linked to the analytics service).

## What Leaving the ATM Out as an Actor Says

**Reference:** 02f.ExercisesRE.pdf, p.26

He called the PaasPopCoin use case diagram "quite stupid but quite important". The User **initiates** the ATM use cases directly. In the cashier use cases the **Cashier initiates** (and is in charge) and the user only participates. The key point is that the ATM is **not** an external actor. That implicitly says the ATM is part of our system, i.e. our system must also live inside the ATM and model part of it. That is a strong statement about the system, made only by leaving something out. He said the rest of this diagram is not that important.

## Diagrams Carry Negative Information Too

**Reference:** 02f.ExercisesRE.pdf, p.26

When drawing a use case diagram, think about both the **positive information** (what you state explicitly) and the **negative information** (what you imply by *not* stating something). The TA said this matters in real contexts: his department works a lot with judges, and when one company sues another it is "always because of that". If you want to "avoid jail" when designing software, check what your diagrams say by omission.
