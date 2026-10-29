# SE2-20261015-RASD-And-AlloyExercises — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261015.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\02g.CreatingRASD.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03b.AlloyExercises.pdf

## Session Scope: RASD Slides, Project Q&A, Then Two Alloy Exercises

**Reference:** 02g.CreatingRASD.pdf, p.1-26; 03b.AlloyExercises.pdf, p.42-60

The lecture had three parts. (1) A quick pass over the RASD slides, about general RASD structure "independently of the specific format that we adopt in this course". (2) An open Q&A on the project assignment. The professor did not go through the assignment section by section and assumed students had read it. (3) Alloy exercises. The Luggage Keeper exercise (p.54-60) was continued from the previous lecture. The Towers and Cubes exercise (p.42-46) was only started: Question 1 up to the piling-rules fact. Questions 2-3 on cubes and the other examples in 03b were not covered.

## Why the RASD Matters Beyond the Contract

**Reference:** 02g.CreatingRASD.pdf, p.4-5

- **Verification depends on it:** if the document misses some important element, verification can still succeed, but the customer will be unhappy when they get the software. Verification only checks against what the RASD captured.
- **Evolution:** when a new requirement arrives, the RASD is the first document to look at. You use it to see how the new requirement relates to the existing (and hopefully implemented) ones, and what its impact is on the requirements and then on the design.
- **Multi-layer document:** the readers have completely different skills, so the RASD must be readable at different levels of abstraction. The introductory part is the one future users are likely to read, to get the main ideas and the offered features. The detailed requirements come later.

## IEEE 29148 (2018): What Changed and Where Domain Assumptions Go

**Reference:** 02g.CreatingRASD.pdf, p.6

- The professor usually checks every year whether a newer version of the standard exists. This year he forgot, so there may be a newer version than 2018. Each new version changes the structure a little, but the main idea stays.
- **Verification (section 4) is a new addition** compared with the previous template. It reflects the recognition that verifying that requirements are fulfilled matters, so the *plan* for verifying requirements is now part of the requirements document itself.
- In the IEEE structure, what the course calls **domain assumptions** would go under *Assumptions and dependencies* in the appendices (5.1).
- User characteristics matter because the UI and its characteristics depend on them (e.g., disabilities, expertise). *Limitations* can be technical aspects that reduce the developers' degrees of freedom.

## Organising Functional Requirements: A Project-Flavoured Example

**Reference:** 02g.CreatingRASD.pdf, p.7-8

How to organise section 3.1 is the group's own decision. Besides organising by user class, you can group by feature categories that become subsections. The professor's example used this year's project: "requirements related to the acquisition of data from the OpenF1 API" and "requirements related to visualization of certain data on the UI". Inside each category you can optionally use a hierarchy of high-level requirements refined into sub-requirements. The aim for 3.1 is to give as many details as possible.

## Why Use the Requirement Sentence Templates

**Reference:** 02g.CreatingRASD.pdf, p.9

He gave two reasons for the [Subject][Action][Constraint of action] structure:
1. The sentence is in **active form**, so it is always clear *who or what* performs the action.
2. A fixed structure **guides you** in what each requirement must express.

The [Condition] variant is for cases like "if condition X holds, do this". A different condition is then covered by **another, separate requirement** that describes a different action. The [Object] slot is used when you must say what the action applies to (in the ambulance example, the recorded ambulance position).

## Precise Quality Requirements vs. "Software System Attributes"

**Reference:** 02g.CreatingRASD.pdf, p.10-11

- **NFR sections (3.2, 3.3, ...):** you cannot be exhaustive. Every type of system has some qualities that are more critical than others. Write specific requirements only for those, because each one will have to be **checked during verification**.
- **Section 3.7 (software system attributes):** these are qualities for which you do **not** write precise, verifiable requirements. Instead you state general objectives that guide the developers.
  - Precise, checkable requirement: "the system shall respond to this request within X seconds".
  - System-attribute style: "the system should be as reliable as possible, and the specific critical situations to pay attention to are these...". This is less precise than a requirement but still useful guidance.

## Our Template vs. IEEE: Why Revision History and Document Structure Are Explicit

**Reference:** 02g.CreatingRASD.pdf, p.18

- Every year the instructors think about aligning the course template with the new IEEE structure, but they keep their own for simplicity. All the main IEEE elements are still there, organised slightly differently.
- The **Formal analysis using Alloy** section had no counterpart in the old IEEE template. It corresponds well to the new **Verification** section.
- **Revision history** is explicit in the course template but not in IEEE. In industry, keeping track of document versions is normal practice, so IEEE probably did not feel the need to state it. For students it is made explicit so that you remember to track the document's history.
- **Document structure** is not redundant with the table of contents. The TOC shows only section headers, while this section explains how the sections are organised. A document-structure section will also be expected in your thesis, "so it is something that it is good to start getting used to".
- The course template's *Assumptions, dependencies and constraints* (2.D) corresponds to IEEE 5.1.

## Effort Spent and the Mandatory AI-Usage Section

**Reference:** 02g.CreatingRASD.pdf, p.23

- **Effort spent:** report how much time each group member dedicated to the project, and possibly to the different parts of the document (the slide mentions only hours per member).
- **AI usage:** if you use AI for part of the work (in a controlled way), you **must add an explicit extra section**, for example at the end of the document, describing how you used it. The assignment contains guidelines and a code of conduct on generative AI. This section is not in the slide template.

## The Target Qualities Are the Grading Criteria

**Reference:** 02g.CreatingRASD.pdf, p.13-17

- The professor said explicitly that these qualities will be used to **assess the project RASD** and the **W2 part of the written exam** (for students who take that part).
- They also guide the questions of the **in-class quiz**. The transcript says the quiz is "planned for the 4th of October if I'm not mistaken". That date is already past at this lecture (15 October), so it is probably misspoken or an ASR error (uncertain). Check the course calendar, which he said has the date.
- He added that completeness also applies to the document itself: no section may be left unwritten.

## Pertinence: Keep Design Decisions Out (the "Web Application" Trap)

**Reference:** 02g.CreatingRASD.pdf, p.14

A typical mistake is writing in the requirements "we will develop a web application". Maybe 99% of the time it will be one. But during design you might find that a mobile or desktop application is better, so why fix that technical constraint in the requirements? Keep **every design decision outside the RASD**. The only exception is technical constraints imposed by the **stakeholders**: if they require a certain way of working or a certain technology, it must go in the requirements, because it is part of the contract with them.

## Traceability Is What Makes Change Cheap

**Reference:** 02g.CreatingRASD.pdf, p.16-17, p.24-25

- **Change scenario:** the customer comes back and says "we had this goal, but now we want to change it slightly by adding this new idea". If you recorded the links goal → requirements/domain assumptions (and use cases ↔ requirements), you can check every requirement and domain assumption tied to that goal and understand the impact.
- **The same idea applies to design:** record that a requirement is implemented by a certain subset of components. If the requirement changes, you know which components to work on.
- **Traceability matrix:** give every requirement, use case and domain assumption a unique label. Relations are not one-to-one, so the same goal, requirement or use case can appear on several rows. During development the matrix grows: besides a test-case column, you can add a **components** column. In industry these matrices are usually managed with dedicated tools.

## What to Put in Overall Description (Beyond the Slide)

**Reference:** 02g.CreatingRASD.pdf, p.20

- **Product perspective:** besides scenarios and the class diagram, add **state diagrams** to describe the states of a specific element that matters to the system. Add **activity diagrams** if they help describe the processes the system has to work within.
- **Product functions:** include the use cases related to the **scenarios defined in the previous section**. You can also start identifying the **categories of requirements** that section 3 then details.
- **Constraints (2.D):** besides domain assumptions, list the technical constraints here, if there are any.

## Alloy Section of the RASD: Model One or Two Critical Points Only

**Reference:** 02g.CreatingRASD.pdf, p.23

- **Why the section exists:** modelling in Alloy is a useful exercise. It helps you reason about your problem and gives you **formal feedback** on that reasoning.
- **Scope:** modelling *all* of a complex problem is very difficult and time-consuming, and is **not expected**. Pick **one, at most two** points that are particularly important for understanding a critical element of your system, and build the model around them.
- **What the section must contain:**
  - the objectives and why they matter for your problem;
  - the Alloy model;
  - evidence that you verified it: the predicates and assertions you defined and the outcome of the verification, e.g., screenshots of generated worlds with an explanation of what they represent.

## Project Logistics Said Aloud

**Reference:** None (not in slides)

- **Research projects** were to be published "I hope today". After seeing them, you decide whether to do a research project, the implementation, or the written exam.
- **Group setup:** fill in the group form. Create a **private repository**, preferably on GitHub (Bitbucket is fine if GitHub is a problem), and **invite the instructors**.
- **Artifacts:** the deliverable is the documents, as **PDF**, whatever editor you used. It would be good to also commit the **Alloy file**, because that simplifies their work even though the model is in the document (the transcript says "we couldn't copy paste from the document", ASR unclear). For the design document, also commit the **sources of your UML diagrams**.
- **Where you work:** work in the repository. If you write in Google Docs, put a link to the working document in the repository README so they can look at it.
- **Next week's room:** the lecture on the 29th is in **room 502**, only that day, because of the bachelor intermediate exams.

## Writing Tools: LaTeX / Overleaf Recommended

**Reference:** None (not in slides)

- **Recommendation:** his personal suggestion is LaTeX, either locally or on **Overleaf**, because the graphical result is much better than with other tools. The initial syntax effort is "really a no problem today" since you can ask an LLM.
- **Overleaf:** it makes collaboration easier. Polimi has a licence: log in with your Polimi account, or link your private account to it. Then you can connect the Overleaf project to your **GitHub** repository so your files are stored there automatically.
- **Tables:** these used to be "a nightmare" in LaTeX. Besides an LLM, he uses a web tool with a spreadsheet-like UI, sometimes building the table in Excel first, uploading it, and generating the LaTeX code.
- **Other editors:** Google Docs, OneDrive or Word are also acceptable.

## UML Tools: Use a Modelling Tool, Not Draw.io

**Reference:** None (not in slides)

- **Don't use Draw.io.** It is a drawing tool with a palette of UML icons, but it does not support UML as a modelling language. VS Code extensions are fine only if they support the UML concepts.
- **Visual Paradigm (recommended):** very good quality, though it takes some effort to learn. It is available on all platforms including Linux, and he uses the free version.
  - Workaround for the free version's watermark on exported images: take a screenshot of the diagram ("good enough for a document"), or export as SVG (a text file) and delete the Visual Paradigm label. You can also just leave the label in, since "it doesn't disturb".
  - To get started, use the *Diagram Navigator* to pick a diagram type (e.g., a new use case diagram).
- **Key advantage: a real model behind the diagrams.** Elements you create (e.g., an actor and a use case) appear in the *Model Explorer*. You can then import the same element (e.g., the User) into another diagram, such as a class diagram, with all its characteristics. In a drawing tool you redo everything each time.
- **Alternatives:**
  - **StarUML:** good, but not available on Linux.
  - **PlantUML:** a rendering tool that builds diagrams from a precise text syntax. An LLM can generate it, with some mistakes you fix yourself. Drawback: there is no shared model as in Visual Paradigm or StarUML.

## Project Background: Formula One and OpenF1

**Reference:** None (not in slides)

The project idea came on a Sunday while Kimi Antonelli was winning a race. The instructors then found **OpenF1**, which the professor said is "actually not an API, it's a system that keeps track of data". He mentioned a video of someone who built a physical model of a circuit with LED light strips, where each car is a light that moves using live F1 data, as a source of ideas. The assignment is deliberately **not too prescriptive**, so you can interpret the project according to your preferences.

## Luggage Keeper: Field Multiplicities Capture Only One End of an Association

**Reference:** 03b.AlloyExercises.pdf, p.54, p.56

- **Boolean attribute:** `isSafe: bool` in the class diagram became an abstract `Status` sig with `Safe`/`Unsafe` extensions. As in the earlier device example, an `enum` would also work.
- **One end only:** in `Locker`, `hasKey: lone EKey` represents only **one** of the two cardinality constraints on the *isLockedBy* association: at most one key per locker. Likewise, `set` in `User` (owns/carries/hasKeys) captures only the tourist-side multiplicity (0..*).
- **Consequence:** if the task is to represent the class diagram *completely*, you must add **facts** for the multiplicities on the other ends (e.g., a luggage is owned by exactly one tourist). He left writing these facts as an exercise.

## Luggage Keeper: The Question Said "Predicate" but Meant "Fact"

**Reference:** 03b.AlloyExercises.pdf, p.55, p.57-59

- **Slide correction:** Question 2 asks for "a predicate capturing" D1, R1, etc. The professor said this is a mistake: they meant **facts**, and the solution indeed defines facts.
- **The difference:** a fact holds in every instance, while a predicate holds only when it is called explicitly. Converting one into the other only means changing the keyword.
- **Goal G1** is deliberately kept as a predicate, so that it can be run to check the goal.

## Luggage Keeper D1 and R1: How to Read and Write the Formulas

**Reference:** 03b.AlloyExercises.pdf, p.57-58

- **D1:** the inner `all u: User | lg in u.owns implies ...` serves to identify the owner. Over the bare signatures there could in principle be many owners, even though the class diagram says only one. Read in full, the "relatively articulated" fact translates the textual domain assumption almost one-to-one: carried by the owner, or stored in a locker with a non-`none` key that the owner holds.
- **R1:** "a key opens only one locker" is written **negatively** with `no disj lk1, lk2`. `disj` forces `lk1` and `lk2` to be different atoms, so the same locker cannot be taken twice under two variable names. A positive version is possible but more verbose: for every key and locker such that the key opens that locker, there is no other locker the key opens.

## GenKey: What the Slide Solution Does Not Guarantee

**Reference:** 03b.AlloyExercises.pdf, p.60

- **Temporal style:** an operation can be modelled in the Alloy 5 style, with two atoms for the locker before and after. He said the Alloy 6 approach is "much better": mark the mutable relations as `var` (`hasKey`, so keys can be attached and detached, and `storesLuggage`, so luggage can be added and removed) and use primed values.
- **No key is actually created.** `sig EKey {}` is not variable, so the set of keys is fixed. The predicate only *picks one existing key* and associates it with the locker.
- **Missing check: the key may already be in use.** Fix: add `and not ek in Locker.hasKey`, where `Locker.hasKey` is the set of all keys currently associated with some locker.
- **Alternative: make `EKey` a `var sig`.** The predicate then states that the key does not exist at the current instant and is added to the set of keys in the next one. He left this as an exercise.
- **Student question: "How do we know the locker is free?"** The predicate does **not** check it. It only keeps `storesLuggage` unchanged: if there was luggage it stays, and if not, an empty locker gets locked. The professor agreed that this `GenKey` "does not completely address" the "given a locker that is free" part of the question. To also model inserting the luggage, you would extend the predicate or write a separate operation that inserts the luggage and generates the key.

## Towers and Cubes: Modelling Alternatives and the Purpose of No-Circular-Piling

**Reference:** 03b.AlloyExercises.pdf, p.43-46

- **Direction of the relation:** `cubeUp` links a cube to the cube placed on top of it. The opposite relation, to the cube underneath, would work equally well.
- **Alternative to the `Size` attribute:** make `Cube` abstract and specialise it into `LargeCube`, `MediumCube` and `SmallCube`. He noted that the slide's `Size`-based specification is "a bit more verbose" than one relying on cube specialisations. These are different design choices.
- **`noCircularPiling`:** this is "similar to the ancestor problem". The transitive closure `^cubeUp` prevents the same cube from appearing more than once anywhere in a tower, not just directly on itself. Separate facts (`pilingUpRules`) are still needed for the size rules.
- **Scope:** the session ended here. canPileUp (Q2) and the top-component extension (Q3) were not discussed.
