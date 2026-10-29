# SE2-20260923-WorldMachine-Turnstile-And-Airbus — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260923.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02c.ExampleScenarioUCReqs.pdf

> **Coverage notes:** Both decks were read in full. This lecture covered only 02a.RE.pdf slides 17-42 and 44. Slides 2-16 belong to an earlier lecture, and the slide-43 exercise (G2) was not discussed. 02c.ExampleScenarioUCReqs.pdf (use cases, scenarios) was not discussed at all. The transcript has several gaps where the ASR dropped speech: the spoken definition of goals (slide 23), the start of the domain-assumption walk-through (slide 24), the Airbus introduction (flight details and the human-error causes, slide 27) and the introduction of the wheel sensors (slide 28). Nothing could be noted for those parts.

## Why the World–Machine Intersection Must Never Be Empty

**Reference:** 02a.RE.pdf, slides 20-22

- A phenomenon is any event in the evolution of the whole system (machine plus world). For each one, the first question is whether it happens in the world or inside the machine. Machine-internal phenomena (a database update, a change of state inside the software) matter for design and implementation, not for requirements engineering.
- The professor stressed that the intersection between world and machine must be non-empty. With no shared phenomena, the machine could bring no advantage to that part of the world. The shared phenomena are "particularly important" because they define how the machine and the world communicate.

## World-Only Phenomena Cannot Trigger Any Machine Reaction

**Reference:** 02a.RE.pdf, slide 22

- The machine has no way to see a world-only phenomenon, such as an ambulance breaking down or an accident happening. So it cannot react to it. For the machine to have any effect on the world, the relevant events must reach the intersection.
- Example: *call encoding* is the shared counterpart of the world-only *public call*. It is the action, done after the call by an operator or by the caller, of entering the relevant accident information into the system.

## Who Controls Each Shared Phenomenon in the Ambulance System

**Reference:** 02a.RE.pdf, slide 22 (the diagram does not show control direction)

Inside the intersection, some phenomena are caused by the world and observed by the machine, and others are caused by the machine and affect the world:
- **Call encoding:** world-controlled. A person types in the content of the call.
- **Ambulance allocation:** machine-controlled. Using the positions of the available ambulances, the software picks one. As a result, the ambulance crew gets an alert and drives to the accident.
- **Ambulance location update:** this is how the machine observes the world-only "GPS detects ambulance position". There must be a communication link between the GPS and the system.
- **Ambulance availability update:** the crew signals availability through the mobile data terminal, and the information reaches the machine by radio. The analyst must make sure this phenomenon actually *arrives* at the machine. Otherwise the machine cannot observe it or react to it.

## The Typical Shape of a Requirement

**Reference:** 02a.RE.pdf, slide 23

Requirements are written only in terms of shared phenomena because those are the only ones the machine can observe or affect. In general, a requirement says that the system *shall act on some shared phenomenon it controls*, *given the occurrence of some other shared phenomenon it can observe*.

## Domain Assumptions Are "Our Requirements for the Environment"

**Reference:** 02a.RE.pdf, slides 23-24

- From the software developer's point of view, domain assumptions are what we *expect* from the environment. In a sense they are requirements on the environment. They are called assumptions because the software has no way to control that behaviour.
- **Why they must be stated explicitly:** if they stay implicit, people in the world may think the system will work even if they skip their part, for example not signalling ambulance availability or not encoding the call correctly.
- **Why they must be reasonable:** if an assumption is something people or devices cannot or will not actually do, the software will not work properly. Assumptions are therefore "quite critical".

## What Each Ambulance Domain Assumption Protects Against

**Reference:** 02a.RE.pdf, slide 24

- *Correct encoding:* if the operator enters the wrong address by mistake, the ambulance goes to the wrong place. The system relies on humans encoding properly.
- *Shortest possible time:* the crew does not, for example, stop for a break on the way.
- *Accurate GPS:* if location updates have a significant error, the software cannot do its job. Positions only need to be "reasonably precise".
- *Availability notifications:* the crews really do signal availability through the existing terminal.

## The Ambulance R and D Do Not Entail the 15-Minute Goal

**Reference:** 02a.RE.pdf, slides 24-25

The professor asked the class whether the requirement plus the assumptions on slide 24 satisfy the goal. He noted that this check can be a formal proof if the statements are in a formal language, or an informal analysis of the statements if they are in natural language.
- **Gap 1 (from a student):** nothing says what happens if no ambulance is available. One fix is a new requirement, for example that the system signals the problem.
- **Gap 2:** even with an available ambulance, correct encoding, location updates and a crew driving as fast as possible, nothing guarantees arrival *within 15 minutes*. "Shortest possible time" is not a bound. The goal also mentions phenomena that are not shared: the machine sees the ambulance's arrival only indirectly, through GPS updates.
- Two ways out: (1) add domain assumptions and/or requirements, or understand the system better, until R and D ⊨ G; or (2) negotiate the goal with the customer and reduce its scope, for example by dropping the maximum time.

## Relaxing 15 to 30 Minutes Does Not Fix It: You Need Assumptions on the Fleet

**Reference:** 02a.RE.pdf, slide 24

A student suggested relaxing the limit to 30 minutes. The professor answered that, given only what is on the slide, *no* time bound can be guaranteed. What is missing are assumptions about the number of ambulances and how well they cover the area. A small town is very different from Milan, and Rome is even harder. A possible new requirement: at start-up and periodically (every day or every few hours), the system redistributes the ambulances across the city so they are not all in one place. With only one or two ambulances in a large city, either none will be available or they cannot arrive in time, whatever the software does.

## Unachievable Goals Must Be Raised With Stakeholders Early

**Reference:** 02a.RE.pdf, slides 24-25, 45

- If you build the best, highest-quality software but the customer then says it does not meet the 15 minutes, the project is a failure. You promised something the software alone could never achieve, because it cannot control everything. So such points must be discussed with stakeholders as early as possible.
- Main message of the section: do not focus narrowly on what the software does. Look at the real objectives of the stakeholders and at what the rest of the environment must do. Often a complete set of requirements is only possible after extending the set of domain assumptions.

## Airbus A320: Observation and Control in the Braking Logic

**Reference:** 02a.RE.pdf, slides 27-29

- The professor said the course focuses on the software problem (braking activated about 9 s too late), and that the root cause was a misunderstanding of how the braking system should work as a whole.
- *Wheels turning* happens in the world and cannot be observed directly. Sensors turn it into the shared signal *wheel pulses on*, which the software observes.
- *Reverse enabled* is a command the software sends. The braking system itself belongs to the world.
- **Reverse thrust:** the engines are made to work in reverse, so their power slows the aircraft. It must not be activated unless the aircraft is on the runway, hence the goal "reverse thrust enabled iff moving on the runway".

## Airbus: The Assumption That Failed Was "Wheels Turning iff Moving on Runway"

**Reference:** 02a.RE.pdf, slides 30-31

It is easy to check that R and D entail G, and still the accident happened. One domain assumption did not always hold in the real weather conditions: on a wet runway, aquaplaning lets the aircraft move along the runway while its wheels do not necessarily turn. So "wheels turning ⇔ moving on runway" was false, and he named this as the cause of the problem. The professor summed it up as a misunderstanding of how the aircraft actually behaves.

## Wrong Domain Assumptions Surface Late and Can Force a Redesign

**Reference:** 02a.RE.pdf, slide 31

- Domain assumptions that do not hold in reality are often discovered only once the system is in operation.
- The impact can be critical: if the whole design relies on a property that turns out to be false, the system may need to be redesigned completely.

## Assignment: Two Videos for the Next Classes

**Reference:** 02a.RE.pdf, slide 44

The two videos (requirements elicitation, and modelling) are about 20 minutes each, according to the professor. Watch them as soon as possible, since the next classes start from them. The elicitation video covers how to get from stakeholders the information needed for reasonable requirements and domain assumptions. The modelling video covers what a model is, which in short is a representation of reality.

## Turnstile Phenomena: Reasoning Behind the Classification

**Reference:** 02a.RE.pdf, slides 33-36

The example is a slightly re-elaborated version of the one in the Jackson & Zave paper. In class the phenomena were derived together:
- **Person buys the token:** world-only and not observed by the machine, but still relevant, because if nobody buys a token nothing else can happen.
- **Person scans the token:** a student said world-only. The professor said that, assuming a scanning mechanism turns the act into data, it is treated as *shared* for simplicity. It is *world-controlled* because the person decides to scan.
- **System checks the token is valid:** machine-only. How to do this is decided later, in design.

## Adding a "Token Confirmed" Feedback, and Why There Is No Single Correct Analysis

**Reference:** 02a.RE.pdf, slide 36

- In class they added a phenomenon that is not on the slide: *the system confirms to the user that the token is valid*. It is shared and machine-controlled, because the machine has to give the environment some feedback.
- At a higher level of abstraction, this can be merged with the validity check. The merged phenomenon is then shared and machine-controlled. Which choice to make depends on the abstraction level that is relevant to the analysis.
- The slide uses "the visitor pushes the barrier doors" (shared, environment-controlled) as the step that continues the flow. The class used "the person passes through the door". The professor's point: different perspectives can give different but equally reasonable sets of phenomena, as long as they support proper goals, assumptions and requirements.

## Detecting Passage Needs a Sensor

**Reference:** 02a.RE.pdf, slide 36

- *The doors open:* shared and machine-controlled. It is the final purpose of the machine.
- *The person who has the token passes through (and not someone else):* a world phenomenon. The professor noted the system can hardly tell one person from another, but the phenomenon is still relevant. The system has to know that someone has passed, otherwise it cannot control when the doors close. That implies a sensor detecting the passage. With such a sensor, the phenomenon becomes shared.
- Once the person is inside the restricted area, they are outside the machine's control.

## Door Closing Can Be Machine-Controlled or Purely Mechanical

**Reference:** 02a.RE.pdf, slide 36

The machine must also close or lock the doors to keep others out. Whether "doors close" is a machine-controlled shared phenomenon or a world-only one depends on the physical devices. Example: the old metal turnstiles in the metro (before the new automated gates) rotated so that once one person moved through, the bars automatically blocked the person behind. With a mechanism like that, closing needs no software command.

## Goals: Operational Wording of G1 and Iterating on Phenomena

**Reference:** 02a.RE.pdf, slide 37

- A student proposed the two goals: people with a ticket must be able to enter, and people without one must not. G1 expresses the second goal in an "operational" way: at any time, entries never exceed scanned valid tokens. For example, you cannot have 3 entries if only 2 tokens were scanned. Conceptually it is the same as "people who did not pay do not enter".
- While writing goals, you may find you need a phenomenon you had not identified. Then you go back and add it. The process is iterative.

## Why Each Turnstile Domain Assumption Is Needed

**Reference:** 02a.RE.pdf, slide 38

The physical system includes the door mechanics and also the visitors' behaviour:
- **DA1:** visitors do not jump over the doors. If they did, the system would have no way to control those entries.
- **DA2:** a visitor who pushed and got the doors open really does enter and does not just walk away. Otherwise someone else could enter in their place, letting in a person who did not pay.
- **DA3:** the doors close fast enough that a second person cannot run in right behind the first one before they shut.
- At least two of these three say that people do not cheat. **DA4** is only a simplification: when the software triggers open or close, the doors move instantly.

## Rationale for the Turnstile Requirements, and an Extra Initial Condition

**Reference:** 02a.RE.pdf, slides 39-42

- The machine cannot act on entries or on scanning. It acts on entries only indirectly, by keeping the doors closed, and that works only under the assumption that nobody jumps over.
- **R3** (open only if pushed): doors that open with no push would let people in without any control. The procedure is: push, then enter.
- **R4** is directly linked to **DA3**: the doors must close within d_e, fast enough that the next person cannot slip through.
- In addition to R5 (doors initially closed), the professor suggested also requiring that the count of scanned tokens starts at zero. Otherwise the system could start from an inconsistent state. On slide 42 this appears only as a fact inside the proof.
- The proof was not done in detail for lack of time. He only pointed out that its first part (e ≤ o) relies mostly on the domain assumptions, while the second part shows o ≤ s. Together they give e ≤ o ≤ s.
