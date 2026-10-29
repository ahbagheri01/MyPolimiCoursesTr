# SE2-20261014-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261014.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Session Scope: End of Alloy 6 Temporal Operators, Then Traffic Lights and the Start of Luggage Keeper

**Reference:** 03a.AlloyPart1-2.pdf, p.61-77 (slides 62-78); 03b.AlloyExercises.pdf, p.2, p.12-18, p.49-55

- The lecture first finished the Alloy 6 temporal part of 03a (device example, then the mailbox/trash example). It then moved to 03b and solved **Traffic Lights**. The plan also included Towers and Cubes and Luggage Keeper. Towers and Cubes was postponed ("maybe 10 minutes tomorrow"). For Luggage Keeper only the description, phenomena, use cases, class diagram and the Question 2 text were covered. The Alloy solution was left for the next lecture. Communication Networks, Social Network, City Center Area, Airbus and Recipe Management were not covered.
- Logistics: the project description had been published. The next lecture (15/10) would cover the typical structure of the RASD and answer project questions, so students were asked to read the description and bring their list of questions.

## How to Use the Exercise Deck and Past Exams

**Reference:** 03b.AlloyExercises.pdf, p.2

- 03b is a **catalog** for self-practice, and not every exercise will be done in class. More examples are in previous years' exams on WeBeep, and those exams come with full solutions.
- He strongly recommended reading the text and building **your own** model before looking at a solution. Writing an Alloy specification is "essentially like programming": if you only read someone else's solution you may think you understood it, but you still will not be able to build a model yourself.
- There are many valid approaches. The solution on the slides is "not even necessarily the best one, the most elegant, it is just one solution". Each example models something different and has a different purpose, so study each one individually.

## `always` Is a Future Operator, and the Inner `always` in NoRepair Is Redundant

**Reference:** 03a.AlloyPart1-2.pdf, p.61 (slide 62), p.63 (slide 64), p.70 (slide 71)

- Despite its name, `always` only predicates from the **current instant onward**. It covers the whole timeline only because the initial instant is one of the possible "current" instants.
- In `always (d.status = Broken implies after always d.status = Broken)`, the inner `always` can be omitted without changing the meaning. `always (Broken implies after Broken)` already says "if it is broken now, it is broken at the next step", and the outer `always` applies this at every instant.

## NoRepair Is Vacuously True for a Device That Never Breaks; Combining It with `eventually`

**Reference:** 03a.AlloyPart1-2.pdf, p.63-64 (slides 64-65)

- The second timeline on the slide (Working, Working, Working, ...) satisfies NoRepair because the antecedent `d.status = Broken` is always false, so the implication is always true.
- If NoRepair and NotAlwaysFunctioning are both in the same specification, every working device eventually breaks, and from that point on it stays broken forever.

## Alloy Traces Are Finite in Time

**Reference:** 03a.AlloyPart1-2.pdf, p.65 (slide 66)

- An instance starts at an initial instant and time flows from there. The professor stated that the analyzer cannot represent an infinite future or an infinite past. So `historically` looks back only through the preceding steps, down to the initial state.
- More generally, every verification Alloy performs is done on **finite domains**, and this affects how temporal facts are checked.

## Why NowWorkingPreviouslyWorking2 Starts with `after always`

**Reference:** 03a.AlloyPart1-2.pdf, p.66-67 (slides 67-68)

- Since `before F` is false in the first instant, writing `always (Working implies before Working)` would make the fact **false at the first instant** whenever the device starts working. That rules out the intended behaviours.
- `after always` is "just a trick" to skip evaluating the formula in the first instant. He said Alloy "doesn't work well" with `before` there, because it cannot refer to an instant outside the finite time domain.
- Answer to a student: the constraint still covers every instant from the second one on. From instant 1, `after` moves you to instant 2, where you check the status and use `before` to look back at instant 1. From instant 2 you move to instant 3, and so on.

## Operations Are Precondition + Postcondition; Prime and `after` Are Interchangeable for a Single Next Step

**Reference:** 03a.AlloyPart1-2.pdf, p.68 (slide 69), p.73 (slide 74)

- In `pred break[d]`, `d.status = Working` is the precondition (true in the current instant). `d.status' = Broken` is the postcondition (true in the following instant). It can equivalently be written `after d.status = Broken`. Delete and restore in the mailbox example follow the same pattern.
- `break[d]` and `d.break` are the same call (syntactic sugar). A student misread it, so note that `d` is simply the specific device passed as the parameter.
- `restoreEnabled[m]` has a different role: it does not describe an operation, it describes a **condition** (`m in Trashed`). It is then reused as the precondition of `restore`.

## A `var sig` Can Also Gain New Atoms

**Reference:** 03a.AlloyPart1-2.pdf, p.72 (slide 73)

Because `Message` itself is declared `var`, not only can a message move in and out of `Trashed`, but **new message atoms can appear** in `Message` over time. The professor noted that the three-instant figure does not show this.

## Frame Conditions: Anything You Do Not Constrain Can Change Arbitrarily

**Reference:** 03a.AlloyPart1-2.pdf, p.73-74 (slides 74-75)

- Student question: is `Message' = Message` in `delete` really needed? Answer: **yes**. In Alloy "everything could happen": if you do not explicitly constrain an element of the specification, it can change arbitrarily in the next instant. So every operation must state what happens to **all** elements, including the ones that stay the same.
- Why `Message` stays unchanged in `delete`/`restore`: `Trashed` is a subset of `Message`. A message entering the trash (or leaving it, like m4 in the figure) is still in `Message` either way.

## Scope of `after` in deleteTrashed, and When the Prime Is Mandatory

**Reference:** 03a.AlloyPart1-2.pdf, p.74 (slide 75)

- The professor first suggested rewriting the predicate as `after (#Trashed = 0 and Message = ...)`, then **corrected himself**. `Message' = Message - Trashed` relates Message in the *next* instant to Message and Trashed in the *current* instant, so it needs the prime. A single `after` block cannot express that relation.
- Without parentheses, `after` applies **only** to `#Trashed = 0`. All the other constraints are evaluated at the current instant, and `Message'` is read relative to the current instant. Reordering the lines does not change the meaning.
- If you put `Message' = ...` *inside* `after ( ... )`, the prime would be read from the next instant, so it would refer to **two** steps ahead. That is wrong.
- Equivalent alternative for the first part: `#Trashed' = 0` in place of `after #Trashed = 0`. Use either `after` or the prime for a single next step.

## receiveMessages Needs `Message in Message'`

**Reference:** 03a.AlloyPart1-2.pdf, p.74 (slide 75)

`#Message' > #Message` alone is not enough. `Message'` could be a larger set made of *different* messages from the current ones. Adding `Message in Message'` forces the current messages to still be there, so the operation only **adds** new messages and never removes existing ones. `Trashed' = Trashed` is the frame condition for the trash.

## systemBehavior: Why `no Trashed` Is Outside `always`

**Reference:** 03a.AlloyPart1-2.pdf, p.75 (slide 76)

- `no Trashed` (equivalent to `Trashed = none`) is placed **outside** `always`, so it constrains only the initial state. Inside `always`, it would force the trash to be empty in every state, which is not what we want.
- The `always ( ... or ... )` part lists the possible evolution steps, using all the predicates defined before. Many different evolutions satisfy the fact: one where `doNothing` is always true, or a more dynamic one (receive messages, later delete something, etc.). This is why `doNothing` matters: it lets "nothing happens" be a legal step.

## Mailbox Assertions: messagesNeverChange Does Not Hold

**Reference:** 03a.AlloyPart1-2.pdf, p.76-77 (slides 77-78)

- About `messagesNeverChange`, the professor said "it is clear that this doesn't hold, and maybe also others". He did not go through the others.
- Exercise left to students: run all four assertions in the analyzer, find which hold, and **motivate** why.

## There Is No Temporal `some`; `once` Means "at Some Past Instant"

**Reference:** 03a.AlloyPart1-2.pdf, p.69-70 (slides 70-71)

- Student question about using `some` in a temporal sense. Answer: `some` is a quantifier or a multiplicity/cardinality constraint, not a temporal operator. The temporal operators are only the six in the summary table.
- `once` does not mean "exactly one time". It means "for some instant in the past", so one or more instants. A message deleted several times is fine for `restore[m] implies once delete[m]`.

## Traffic Lights: Static Model and the Choice of `one sig` Constants

**Reference:** 03b.AlloyExercises.pdf, p.13-14

- Color and Traffic (FLOWING/STOPPED: the traffic status of a road) are modelled as abstract signatures with `one sig` sub-signatures. They use `one` because we never want several GREEN atoms or several FLOWING atoms. An `enum`, as in the device example, would work equally well. The slide uses this form just to show that there are several ways to represent such concepts.
- In `color: one Color` the `one` could be omitted, since it is the default.
- Nothing in this model is `var`. It is a static snapshot of the intersection, not its dynamics.

## Signature Facts: Implicit Quantification (and Implicit `always`)

**Reference:** 03b.AlloyExercises.pdf, p.14

- `sig Intersection { connection: Semaphore -> Road } { #connection = 2 }`: the block after the signature is a constraint on **every** atom of that signature. It is equivalent to `fact { all i: Intersection | #i.connection = 2 }`, but more compact because the quantifier is implicit.
- He also stated that if the model had variable elements, a constraint written in a signature fact holds **at every instant** even without `always`. Note: the Airbus solution (03b p.38) writes `always` explicitly inside its signature facts. By this statement that `always` is redundant but harmless.

## Reading the Ternary `connection` Relation Through the Getter Functions

**Reference:** 03b.AlloyExercises.pdf, p.14-15

- `connection` is a ternary relation Intersection × Semaphore × Road, like `addr` in the address book. The three functions act like getter methods in OO programming.
- `getIRoads[i] = Semaphore.(i.connection)`: `i.connection` gives the (semaphore, road) pairs of `i`. Joining with the whole set `Semaphore`, which certainly contains this intersection's semaphores, leaves that intersection's roads.
- `getSRoads[s] = s.(Intersection.connection)`: `Intersection.connection` drops the first column, giving every (semaphore, road) pair of any intersection. Joining with `s` gives the roads of that semaphore.
- `getSemaphores[i] = (i.connection).Road`: `i`'s pairs joined on the right with `Road` give the semaphores linked to some road of `i`.

## `let` Is Just a Temporary Name

**Reference:** 03b.AlloyExercises.pdf, p.16-17

`let s = getSemaphores[i] | #s = 2` names an intermediate result, like a temporary variable. In `intersectionStructure` it is not needed: you can write `#getSemaphores[i] = 2`, `#getIRoads[i] = 2` and `all sem: Semaphore | #getSRoads[sem] = 1` directly. He said `let` is more useful when the named result is reused, as in `greenIsExclusive`.

## greenIsExclusive: Why `s1 != s2` (or `disj`) Is Required

**Reference:** 03b.AlloyExercises.pdf, p.17

- When you quantify twice over the same set, `s1` and `s2` can be bound to the **same** atom, so you must state explicitly that they are two different semaphores. Equivalent form: `all disj s1, s2: Semaphore | ...`. Either way, distinctness must be stated explicitly.
- `intersectionStructure` already forces exactly two semaphores per intersection. But in general `s` could hold more than two, which is why the fact is written over any pair in `s`.
- General lesson he drew here: you must spell out every detail of what a "good" instance looks like (2 semaphores, 2 roads, how colours relate to traffic). Alloy will not assume any of it.

## The Fact's Name Promises Less Than Its Body Enforces

**Reference:** 03b.AlloyExercises.pdf, p.17

The name `greenIsExclusive` suggests only "no two greens", so in principle two reds would be allowed. The body (`s1.color != s2.color`) forbids **any** equal colours, two reds included. Always check whether a constraint really says what you intend, and change it if it does not. Here the slide keeps the "different colours" version.

## goWithGreen: Reading the `iff` and the Road-Side Constraint

**Reference:** 03b.AlloyExercises.pdf, p.17

- `s.color = RED iff r.traffic = STOPPED` works in both directions: red implies stopped, and stopped implies red.
- `(Intersection.connection).r` is the set of semaphores associated with road `r` in any intersection. Requiring its cardinality to be > 0 means there is a semaphore on that road. (The transcript says "greater than one", probably a slip; the slide has > 0.) So traffic is stopped **only** where a semaphore stops it.
- This is a deliberate modelling choice. In reality traffic can stop because of an accident or a jam, but that was chosen not to be modelled.

## Choosing What to Put in a Model Is a Critical Decision

**Reference:** None (not in slides)

What you can verify on a model depends on what you represent in it. You must decide your objective, include the relevant elements and skip useless details. Adding irrelevant details only gives a heavyweight model that takes a long time to verify, with no benefit. He called this non-trivial but said it is not the focus yet: for now the goal is learning the language.

## Luggage Keeper: "Lockers Are Opened with an Electronic Key" Should Be Split

**Reference:** 03b.AlloyExercises.pdf, p.50, p.52

- The professor flagged a probable mistake on the slide. "Some lockers are opened with an electronic key" is listed as a world-controlled shared phenomenon, but it mixes two phenomena with different controllers:
  - the tourist **gives** the electronic key to the machine (world-controlled);
  - the machine **checks** that the key is correct and **opens** the locker (machine-controlled).
- It should be rephrased and split, with each part assigned to world or machine.
- To classify a phenomenon, ask who generates and gives the key, and who or what opens the locker. Phenomena must be stated unambiguously, and he said some on this slide (e.g. "the system confirms unlock of some luggage keepers") may be ambiguous. Getting the world/machine assignment right matters for understanding the model.

## Luggage Keeper Use Cases: How to Read the Diagram

**Reference:** 03b.AlloyExercises.pdf, p.53

- **Locker** is an actor: an external device the system interacts with, because the system locks and unlocks it.
- The **tourist** initiates Lock/Unlock because the tourist provides the luggage or the key.
- For the shop owner:
  - "Configure luggage keeper" means, for example, declaring how many lockers the shop has.
  - "Enable payment" means confirming that someone has actually brought the luggage.
  - The shop owner can visualize the ratings, and maybe the payments too.

## From Class Diagram to Alloy

**Reference:** 03b.AlloyExercises.pdf, p.54, p.56

A UML class diagram is a useful intermediate step toward an Alloy model. Classes become signatures, and associations become relations together with their cardinality constraints. The result is conceptually equivalent to the class diagram.

## Why the Class Diagram Has Both `owns` and `carries`

**Reference:** 03b.AlloyExercises.pdf, p.54-55

- Student question about the two Tourist–Luggage associations:
  - a tourist **owns** the luggage at all times, even while it is stored at a luggage keeper;
  - a tourist **carries** it only while bringing it around.
- The professor agreed that this distinction does **not** come from the textual description. It was added on purpose because the Alloy part needs it: domain assumption D1 defines luggage as safe if it is carried by its owner, or stored in a locker whose key the owner holds.
