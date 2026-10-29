# SE2-20260917-SoftwareLifecycle-And-IntroductionToRE — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260917.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\01.IntroSE.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02a.RE.pdf

> **Material limitations:** The professor briefly showed some slides on AI coding agents (a blog post saying they are "not production ready", AWS outages linked to AI-agent code changes, developers moving to "architecting and verifying"). These slides, and a slide pointing to chapters 1–2 of the course book, are not in the mapped version of 01.IntroSE.pdf, so those notes are compared against nothing. The lecture covered 01.IntroSE.pdf from slide 17 onward, and 02a.RE.pdf only up to slide 16 (RE workflow). Later 02a slides (World and Machine, Airbus, PACS) belong to the following lectures.

## What the Waterfall Placement of Deployment and Maintenance Implies

**Reference:** 01.IntroSE.pdf, slides 16-17

The professor said that waterfall as a strict sequence of phases is no longer current, but the phases are still useful to name the activities that matter. Putting deployment and maintenance at the very end suggests that once the software leaves the developers' hands it is no longer their responsibility. Responsibility only comes back in maintenance (e.g. making the software more robust or more tolerant to failures). He said this last part later evolves into something more sophisticated (DevOps, see below).

## Coding Is Only 20% of the Effort, and AI Agents Shift Effort Toward Control

**Reference:** 01.IntroSE.pdf, slide 23

- The chart is from 2008 but the professor still considers it current. Its point is that coding matters (without it there is no software) but it is not the most important activity. V&V (45%) plus requirements, specification and design take most of the effort.
- He said AI agents may partly help with coding, but they will certainly *increase* the time people spend controlling all the other activities to make sure everything works.

## Humans Must Stay Responsible When Using AI Agents

**Reference:** None (not in slides)

- Even if AI agents are used for coding or other development activities, a human must stay in the loop and be responsible for the work. Responsibility cannot be delegated to someone or something else.
- So human effort has to become *more* qualified: engineers must be able to control, coordinate, monitor and understand what other people or agents do.

## What Can and Cannot Be Delegated to an AI Agent: Documentation, Testing, Coding

**Reference:** None (not in slides)

A student reported an online discussion (probably Stack Overflow) saying practitioners mostly use AI agents for documentation and testing. The professor asked what delegating these really means:

- **Documentation:** first decide which kind (code, requirements, design). The engineer does the creative work and the agent can help *describe* it. Example: given code you wrote, you can ask the agent to describe it. For requirements this matters even more. The hard part is not writing the document but *understanding and identifying* the requirements, and that cannot be delegated. You can only give an agent directions after you have understood the problem and organized the solution.
- **Testing:** to get a good automated testing framework instead of a random one, you must give the agent more than the code. You give it the functional and non-functional requirements (what matters most to check), the design (how the software is organized), and criteria such as "reach 90% code coverage". Writing those inputs requires understanding the problem, so requirements and design remain human creative work.
- **Coding:** boilerplate code can be delegated. Non-boilerplate code is a creative activity and probably cannot ("at least this is my opinion").

## Maintenance Categories: Concrete Examples and Practical Remarks

**Reference:** 01.IntroSE.pdf, slide 24

- **Corrective:** faults found, hopefully during testing, but sometimes only in the operational software.
- **Preventive:** re-engineering the system every once in a while to improve its quality, especially maintainability. The professor said this rarely happens because teams are in a hurry to meet deadlines, but it is good practice.
- **Adaptive:** the "environment" includes the execution environment, other software components that interact with ours, and regulations (e.g. GDPR or the AI Act forcing software to be adapted). From the users' point of view the offered functionality does not change. Examples: a library you use is no longer available, so you move to its new version or another library; or because of GDPR you can no longer store or acquire certain personal data, or you must ask the user's permission first.
- **Perfective:** changing the software because requirements evolve, i.e. adding functionality that was not foreseen. Example: the company running your e-commerce system asks that users can see their cart contents before paying. The 50% share shows that requirements change a lot and that this is normal. After years of evolution, probably very little of the original code remains.

## Why Correction vs. Evolution Matters: Who Pays

**Reference:** 01.IntroSE.pdf, slide 25

The professor said the distinction is often tricky but matters mainly for contractual reasons. If the software has a bug, fixing it is the developers' responsibility. If it must be modified for other reasons (evolution), the developers can sign a new contract with the customer.

## Uncontrolled Evolution and Anticipating Change

**Reference:** 01.IntroSE.pdf, slides 26-27

- Software is malleable and can be changed in minutes, so changes are often made in a hurry. Over time the real software then drifts away from the original idea and documentation. In the long run nobody can understand the actual software from its documentation, so evolution must be controlled and the implications of each change thought through.
- **Anticipating change, example:** if the system must interact with one external component, wrap that interaction. Then, if the component changes or a new component doing the same job replaces it, only the code handling that interaction changes and the rest of the system is untouched. This should be done from the very beginning. Planning for future evolution (maintainability, evolvability) is what makes a good software engineer.

## Why "First Modify the Design, Then the Implementation": the Interface Example

**Reference:** 01.IntroSE.pdf, slide 27

A student asked what this practice means in practice (the point is not to change only the design, but to look at the design first, or change both together). The professor's example:

- Component B offers operation P1 with parameters P1, P2, P3 (as transcribed), used by component A. A bug in B is traced to parameter P3, which A should not pass, so you decide to remove P3.
- If you change the code right away without checking who else uses the operation, you break the system. In languages that check interface use against interface definitions at compile time you find out then. In other languages you may not notice, and you can ship software whose components disagree on their interfaces, which is a critical problem.
- Looking at the design document may show that C and D use the operation too, so their code must change as well. Looking at the design first means you assess the impact of a change on the whole system, decide whether you can afford it, or look for a different solution, instead of fixing one tiny thing on the fly.

## Waterfall as a Black Box: Why Transparency and Early Feedback Emerged

**Reference:** 01.IntroSE.pdf, slides 28-29

- The external stakeholders are the customer, future users, system administrators, and anyone outside the development team you need to interact with. In waterfall they saw only the start and the final product. If they then said "I don't like it", all the effort had already been spent.
- The need for transparency became clear only after some unsuccessful and very expensive projects.
- The first key feedback point comes after the requirements, as the team understood them, are written into documentation: stakeholders must agree on them. This is why a good requirements document matters. It is the means of interacting with customers and stakeholders in the early steps.
- Later on, it helps to have something concrete to show. So flexible processes try to produce a prototype as early as possible (e.g. starting part of the design during requirements, and some implementation during design).

## DevOps: What Each Activity Absorbs

**Reference:** 01.IntroSE.pdf, slide 32

- Agile processes are one class of flexible processes, and XP and Scrum belong to it. DevOps gives much more weight to the operational part of the life cycle.
- In DevOps, **build** absorbs most development activities (requirements analysis, design, implementation, …). **Test** is separate. **Release** becomes very important. During operation there is **continuous monitoring** and **continuous planning** of new changes.
- More detail is in chapters 1 and 2 of the course book.

## Typical Verification Questions

**Reference:** 01.IntroSE.pdf, slide 30

Verification (the arrows between phases) happens inside the team. It asks whether what is being done in one activity is consistent with what was done before. For example: did we forget any requirement? Is there an inconsistency between what was decided in the previous phase and what we have now? Is the software consistent with the design and compatible with the defined interfaces? (The professor's explanation of validation just before this is mostly lost in the transcript.)

## AI Coding Agents and the AWS Outages: Keep Agents Under Control

**Reference:** None (not in slides)

- The professor showed a blog post (from February this year) saying AI coding agents are not production ready. He said this may change as agents keep improving, but either way it remains our responsibility to guarantee the quality of our software.
- He cited AWS: two outages linked to code changes made by AI agents, one a 13-hour disruption. Amazon attributed them to human misconfiguration, a developer's mistake, and called the AI involvement coincidental. The professor said this was "rightly" so, in his view, because the developer's mistake was not controlling the agent. Some experts warn that the more autonomy agents get, the more problems happen outside our control. The mistake comes from delegating too much.
- Another view he presented: the most advanced developers have moved from writing code to *architecting and verifying* work done by AI agents. Architecting and verifying require a lot of practice, so students should do that practice during their studies, learning by doing and experimenting.

## Requirements Engineering Is Present Throughout Development

**Reference:** 02a.RE.pdf, slide 3

The professor called RE, in his view, the most important phase, because it is where the problem is understood, and it must be understood correctly to find the right solution. Besides its place in the waterfall, RE activities happen throughout development. During design you check that the design fulfils all requirements. In testing you test the software *against* the requirements.

## Student Q&A: When Can You Run a Mini-Lifecycle Feature by Feature?

**Reference:** None (not in slides)

A student asked (the question is ASR unclear) whether you can go through requirements, design, implementation and testing one feature at a time. The professor's answer:

- It works when the **architecture is clear**. Example: a web application has a well-known structure (database, backend server, possibly a server for the UI, and the UI). You can start from the most important feature, e.g. browsing products in an e-commerce system, implement it completely, and soon give customers something to try and give meaningful feedback on.
- It is harder for non-standard systems. Example: a control system for a specific environment that you have never built before, which must talk to several legacy systems. There you first need to establish the architecture by studying the surrounding systems and how to interface with them. Only then can you go feature by feature.
- Features can be highly intertwined (one needs another first), so you must pick a feature that is both important and as independent as possible. This is not always straightforward.
- In every case you must first understand which features, i.e. requirements, the system has to fulfil.

## Even the Stakeholders Must Be Discovered

**Reference:** 02a.RE.pdf, slide 4

- When someone brings you a problem, they do not tell you everything you need to know. Much must be discovered by reasoning and by studying how the system should work and which processes it needs. Even finding the stakeholders (those more or less directly affected by the system or interacting with it) is non-trivial.
- Documentation is needed because without a document you cannot interact with others and check whether you have reached agreement.

## Classifying the Taxi Candidate Requirements: the Professor's Reasoning

**Reference:** 02a.RE.pdf, slides 5-6, 12

- All the sentences have the same assertive form ("the system shall/should…"), but they are of different kinds, and some are not requirements at all.
- **"Feedback in 5 seconds":** a student said it depends on the number of taxis. The professor said this dependency can be limited, e.g. with timeouts, so the user gets an answer anyway. The real issue is that it does not say *feedback to what*. Read generally, it means every request reaching the system gets a response within 5 s. That makes it a non-functional (performance) requirement, not a specific functionality.
- **A typical trait of NFRs:** phrased this way, the requirement could be copied unchanged into another system's requirements, because NFRs refer to qualities rather than to functionality. "Available 24/7" is similar, but it is an *availability* requirement, while the 5-second one is a *performance* requirement.
- **"Reserve taxis"** is a typical functional requirement. The details of the mechanism can be worked out later.

## "The Reserved Taxi Picks the User Up" Is Not a Requirement for the Software

**Reference:** 02a.RE.pdf, slides 12-13

A student noted that this depends on the taxi driver. The professor agreed. It may be a requirement for a larger system made of the software plus drivers, taxis and even users on the street, but the software alone cannot guarantee it. Software always works in an environment, and higher-level requirements (later to be called *goals*) are often met only through collaboration between the software and external users or other hardware/software systems. Since we are responsible for the software, only what pertains specifically to it should be called a requirement. Making this distinction is sometimes tricky.

## When "Implemented in Java" or "In Class Controller" Can Be Legitimate Requirements

**Reference:** 02a.RE.pdf, slides 5-6

- Both look design-specific, but both can be real requirements, called *technical requirements* or *technical constraints*.
- Customers usually do not impose a programming language, but they may. For example, they use Java elsewhere, or they have Java programmers in their team who should be able to follow the development.
- Even "implement the search in class Controller" can be a requirement. This happens when you are extending a pre-existing system and the customer has a clear idea of what should be done and how. It is not frequent, but it happens.

## NFRs: Visibility, Measurability, and Why Functional Requirements Are "Binary"

**Reference:** 02a.RE.pdf, slides 7-8

- Any of the non-functional qualities in the quality model can be the subject of an NFR. Whether a quality counts as "visible" depends on how much visibility the stakeholders want on the system.
- For an NFR such as "feedback in 5 seconds", when you define it you must also decide how you will *measure* whether it is met (5 s vs. 10 s).
- Well-expressed functional requirements are more or less binary: the system either lets users reserve taxis or it doesn't. If someone objects that it does so but with too much user effort, that is a separate *usability* NFR.
- "Constraints on how functionality is provided", made concrete: "respond in 5 s" means every request is answered within 5 s. "Available 24 h" means any request can be answered at any time.

## Netflix vs. Ariane 5: How the Domain Changes NFRs

**Reference:** 02a.RE.pdf, slide 8

- A student suggested "users must not be able to record the screen" for Netflix. The professor said this is probably functional, or in between.
- On whether 5-second responses are fine for Netflix, the professor said you must separate two kinds of request. Requests from users can be handled at the scale of seconds, because human reaction time is in the order of seconds. The video-streaming mechanisms need millisecond-level speed, otherwise streaming does not work.
- For Ariane 5 (a launcher for space missions) no such split is possible: everything must work at the millisecond level or faster.
- He also said every component should have at least one replica, otherwise the requirement simply cannot be met. Replicas raise new questions, such as how they share state, to be discussed under design. (From the transcript it is unclear whether this refers to Ariane 5 or to the slide's 24/7-availability example.)

## Dissecting the Bad-Requirement Examples

**Reference:** 02a.RE.pdf, slides 9-11

- **Credit cards and cashier's checks:** there are actually more than two concerns: validation and acceptance of credit cards, and validation and acceptance of cashier's checks. These may need different processes. Split them so that in testing each sub-requirement gets a clear yes/no (e.g. "the system shall validate credit cards"). Also, "validation" and "acceptance" must be defined beforehand (what they mean, how the steps work), otherwise the requirement is ambiguous.
- **"Very fast mouse clicks":** a working heuristic for every requirement you write is to ask yourself *how you will check its fulfilment*. If that is not clear, make the requirement clearer.
- **"The user must have Adobe Acrobat installed":** the problem is not the cost (assume it is the free Reader). Software cannot force the user to install other software. It could run the installation, but only with the user's authorization. So this should be stated as an *assumption*: the user has it installed, or the user accepts that we install it for them. A decision that belongs to the user cannot be a requirement of our system, because we cannot fulfil it without the user's acceptance. Requirements are only what our software system can be responsible for.

## Why Poor Requirements Are Ubiquitous

**Reference:** 02a.RE.pdf, slides 13-14

- It is hard for anyone to make sure that everything needed to understand a requirement is defined (as with "validation" and "acceptance" above). People also often fail to notice that a sentence describes something broader that cannot be assigned to our software. So requirements must be refined continuously until they are clear, unambiguous and, above all, *feasible* by the software being built.
- On Boehm's chart (old but still useful), the professor stressed that late correction is especially expensive when the error affects the general organization of the software, so the fix cannot be confined to one part of the system.

## RE Is About People and Agreement, Not Just Writing Requirements Well

**Reference:** 02a.RE.pdf, slides 15-16

- Many concerns and many stakeholders mean conflicts, and stakeholders may disagree on what the system should do. Good requirements analysis resolves these conflicts. A lot of it is about understanding other people and the application domain and helping people reach agreement on what they want, not just phrasing requirements well.
- In the RE workflow, requirement models can be plain natural-language descriptions or use specific specification languages. The analysis checks whether they are coherent, and the loop is repeated until consensus with stakeholders is reached. That needs a lot of interaction inside the team and with external stakeholders. By comparison, creating and formatting the final requirements document is the easy part.
