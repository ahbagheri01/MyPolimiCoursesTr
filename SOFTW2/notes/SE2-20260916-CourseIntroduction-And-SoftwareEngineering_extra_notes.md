# SE2-20260916-CourseIntroduction-And-SoftwareEngineering — Additional Professor Notes

**Transcripts:** Software Engineering 2 20260916.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\00.CourseIntro.pdf, E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\01.IntroSE.pdf

> **Coverage notes:** 01.IntroSE.pdf is shared with the next lecture (17/09). This lecture stopped after the waterfall slide (slide 17) plus a short remark on maintenance, so only that part was compared. Slide numbers below are the numbers printed on the slides. In 01.IntroSE.pdf these skip, so they do not match PDF page numbers (e.g. printed slide 8 is PDF page 4).

## SE2 Moves From Software "In the Small" to Software "In the Large"

**Reference:** 00.CourseIntro.pdf, slide 3

Di Nitto said that Polimi students have so far mostly studied software engineering "in the small", meaning programming. SE2 is about turning programming skills into the ability to build software in the large and to keep the development process under control.

## Lecture Timing, Availability and the Provisional Schedule

**Reference:** 00.CourseIntro.pdf, slides 2 and 4

- Each student is assigned to one of the three classes, so check which class you are in.
- Each academic hour is 45 minutes of lecture. Lectures start at 8:30 and usually go on until about 10:00, so there is a break at the end.
- The professor is available for questions before and after the lectures. You can also message her to set up a meeting at another time.
- The schedule linked from WeBeep is still provisional and will change during the semester, so check it regularly. The links to the recordings are in the same schedule table.

## Recordings Are Best-Effort and In-Person Attendance Is Expected

**Reference:** 00.CourseIntro.pdf, slide 4

- There is no live streaming. The only exception is a case raised through Polimi's Multichance service, for example a student who is ill and must follow remotely.
- Why attend in person: the content is the same, but the experience is completely different. In class you can talk with colleagues and ask questions, instead of listening alone in your room.
- Recordings can take a few days to appear because of the instructors' schedules. Recording is also best-effort: it usually works, but the professor cannot check it while she is talking, and sometimes it fails.

## Study Material Beyond the Slides

**Reference:** 00.CourseIntro.pdf, slide 5

- Besides the slides, WeBeep has relevant papers, the recordings and **past years' exams**, which are useful for exam preparation.
- The reference textbook was written specifically for this course. It is also available through the university library. The slide is missing the link to the online version, and an announcement on WeBeep will provide it.
- More general advice: learn how the Polimi library's online resources work, because they are useful for other courses too.

## What Each Assessment Block Means and How Blocks Combine

**Reference:** 00.CourseIntro.pdf, slide 7

- **WE1** tests the specific techniques presented in class. **WE2** gives a problem description ("a company wants software that does this and this") and asks you to do the requirements analysis and design for it.
- The **full project** (requirements, design, implementation, testing, then presentation) replaces the written part completely. You pass by presenting and defending it well.
- The **research project** can replace WE1 because, like WE1, it focuses on one specific technique or approach.
- The allowed combinations are: full project; WE1 + WE2; WE1 + R&DD; RP + WE2; RP + R&DD. The quizzes add up to 2 points on top of any combination.
- The professor said the scheme is deliberately complicated so that you can pick the learning experience that matches your goals. Choose based on what you want to do and how important software engineering is for you.

## Score Rounding and Laude

**Reference:** 00.CourseIntro.pdf, slides 7-8

The maximum is 32 points: 30 from the blocks plus 2 from the quizzes. A total of 31 or more gives 30 cum laude. Scores are rounded up to the next integer, with one exception: 30.5 is rounded down to 30.

## Projects Only in the Winter Session; Written Exams at Any of the Five Calls

**Reference:** 00.CourseIntro.pdf, slides 8 and 17

- All projects and the quizzes happen only in this winter session. The written exams can be taken at any of the **five exam calls** of the academic year.
- Both WE1 and WE2 are offered at every call, and you choose which part to take and when. Examples she gave:
  - do the R&DD project, then take WE1 in the first, third or fifth call;
  - do the RP, then take WE2 in any call;
  - take WE1 in call 1 and WE2 in call 3.
- The final grade is registered once both parts are complete and sufficient.

## What WE1 and WE2 Typically Ask

**Reference:** 00.CourseIntro.pdf, slide 17

Answer to a student question:

- The material to study is what is presented in class. The exercises change from call to call.
- **WE1** always includes one exercise where you write an **Alloy specification**. The other two exercises are typically on **testing**, on **assessing availability** (a non-functional property of a software architecture), or on **project management**.
- **WE2** gives a problem and asks you to define its requirements. Alternatively, it gives a basic structure of a possible architecture and asks you to complete it or to define the interfaces of the components.
- Each part lasts 1h30, so you have little time to do the RASD/DD-style work of WE2.

## Written Exams Are Open Book but AI Is Forbidden

**Reference:** 00.CourseIntro.pdf, slide 17

Both parts are open book, so you can bring and use your material. You cannot use AI during the exam.

## Why Groups, and Why the Same Group for R&DD and I&T

**Reference:** 00.CourseIntro.pdf, slides 9-10

- Single-student projects are allowed, but groups are strongly encouraged because these projects require interaction and discussion with teammates.
- The group must stay the same from R&DD to I&T for organizational reasons. A group that changes between phases is hard for the instructors to assess, and it would be hard for the students to produce something meaningful.

## Cross-Class Groups and the Reference Professor

Groups can mix students from the three classes. At enrollment you fill in a form with the group members, and a cross-class group explicitly selects one instructor as its **reference professor**. If one instructor ends up with too many projects, cross-class groups may be redistributed, but the instructors generally try to respect your choice.

## What Is Expected From I&T: Core Features, Well Tested, Not Bug-Free

**Reference:** 00.CourseIntro.pdf, slide 10

- The project is usually fairly complex. The implementation covers only the most important, core features. The idea is to have a vision, deliver the core part, and in principle add the rest incrementally, but in the course you stop at the core.
- The software must be well tested, and you must be able to show the results of your testing activities.
- It **does not have to be bug-free**. What matters is that you have everything under control: you know the possible defects and what is good and bad in your software.

## Acceptance Testing Grades the Reviewing Group, Not the Reviewed One

**Reference:** 00.CourseIntro.pdf, slides 10-11

- At the end of I&T, each full-project group is assigned another group's project. Group B acts as the **customer** of group A:
  - it runs A's code and analyzes the documentation;
  - it checks whether the software meets the expected requirements and what is wrong;
  - it judges the overall quality of the documentation.
- B's review is **not** used to grade A. It is used to assess B's ability to critically analyze software produced by someone else.

## AI in the Project Is Allowed, but You Must Be Able to Defend Everything

**Reference:** 00.CourseIntro.pdf, slide 11

- Over the last two years, LLMs have been generating parts of projects. Some students at the discussion did not know what was in their own documents.
- The instructors are therefore giving **more weight to the discussion than to the documentation**. The document is read, but you must be able to defend it.
- AI is allowed for preparing documents and software, but it must be used responsibly. If you passively paste AI output, you might hope to pass, but you gain nothing.
- As software engineers, we should dominate and steer the AI, not the other way round.
- The instructors' own experiment: given a project description and asked to "create requirements", an AI produces a very long list of requirements that looks good. Looking at the details, important pieces are missing. The sheer amount of output can also make you overlook the important aspects.
- At the discussion it must be clear that you are the ones responsible for the project.

## Deadlines Are Real but Slightly Flexible

**Reference:** 00.CourseIntro.pdf, slide 12

- The technical projects have deadlines because companies also have deadlines, and you must get used to meeting them.
- Submitting two or three days late is generally fine, especially with a good reason.
- If you see that you will be late, contact your reference professor, explain the problem, and a solution will be found.

## Keep All Artifacts Aligned as Your Ideas Evolve

**Reference:** 00.CourseIntro.pdf, slides 12-13

- **RASD** = Requirements Analysis and Specification Document. **DD** = Design Document. These acronyms are used throughout the course.
- The time between deadlines exists because, while designing or implementing, you naturally realize that something in an already submitted document should change. You can modify a deliverable and resubmit it by the next deadline.
- What the instructors care about is **alignment between all artifacts**. For example, they do not want a DD where you changed your mind while the RASD still says the old thing, because then you are designing software for different requirements than the ones you defined. Likewise, the implementation must match the design.
- You do not have to stick with your original choices. Everything evolves, and you update all documents based on your findings, as happens in real projects.

## Why the Quizzes Moved Into the Classroom

**Reference:** 00.CourseIntro.pdf, slides 14-15

- Until last year these 2 points came from homework done at home. Many answers turned out to be heavily LLM-derived, so the work now ends with a quiz taken in class.
- You still review the past RASD/DD at home. The quiz then asks about the document, for example what could have been done better and what problems you found.
- The old homework had open questions such as "what is good or bad in this section". The instructors were still deciding the new format: most likely multiple choice, if meaningful questions can be found for that format.
- After each quiz there is an in-class discussion of the pros and cons of the document. Each quiz is given only once and cannot be redone.

## Research Projects: Topics, Tutors, Publications, and This Year's Timing

**Reference:** 00.CourseIntro.pdf, slide 16

- The full project is R&DD plus the follow-up I&T **on the same problem**. A research project can instead be on a completely different topic.
- Last year's RP topics included:
  - use of LLMs in software testing;
  - analysis of algorithms for quantum computing;
  - techniques for developing autonomic software;
  - performance verification of a scheduling algorithm.
- Each RP has a tutor, and you work in a research team toward a specific result. Several RPs have led to conference or journal publications, and a couple have won awards. "It is real research work."
- After an RP you can continue with other projects or with a thesis.
- RPs usually have no deadline except completion by September 2027. This year the RP descriptions will be published **at the same time** as the R&DD/I&T project descriptions. The reason: in past years, a team planned the full project, then one or two members found an interesting RP and left. The team broke up, and the remaining students could not do the implementation project they wanted.

## How Project Presentation Dates Are Booked

**Reference:** 00.CourseIntro.pdf, slide 12

Answer to a student question:

1. The instructors propose a list of dates in January and February. Each date has a maximum number of groups.
2. A WeBeep announcement gives the dates. Prepare a priority list of your preferred ones.
3. The announcement also states the day and time when the booking queues open. Each queue is a forum message, one per date.
4. You reply to the message for the date you want. Booking is first come, first served, so if a queue is full you move to another date.

## CrowdStrike: Why a Tiny Bug Stopped the World

**Reference:** 01.IntroSE.pdf, slide 3

- Until a few years ago a software failure could often be tolerated by just restarting. Today failures can be very critical and have effects nobody could foresee.
- As the professor described it, the faulty piece was a small component from CrowdStrike used on Windows systems. Through the automatic update mechanism, many servers worldwide received the new version on the same day, and all of them crashed.
- Her reading of the root cause: the developers **did not agree on an interface between two components**. One component sent the other too much information, which caused the array out-of-bounds error.
- The point is not that particular error but what it caused. This is why software engineering aims at high-quality software.

## Software Engineering in the Age of AI Agents

**Reference:** 01.IntroSE.pdf, slides 8-9

- AI agents can produce software for a given task. The hard part is understanding whether the result meets all the requirements, especially the **non-functional** ones that make the software robust and able to work in every situation.
- So the software engineer's responsibility has **increased**. We are becoming coordinators and controllers of the work done by AI agents, and that requires experience and skills that are not easy to acquire.
- Companies used to train new graduates for some months before giving them responsibility. Now they will likely expect new graduates to control AI agents right away, like experienced managers.
- To get there, you must first be developers yourselves. Only then can you understand, manage, modify and control the software the agents produce.

## Correction to the Definition: "Multi-Agent" Construction

**Reference:** 01.IntroSE.pdf, slide 8

The professor said the slide's definition, "multi-person construction of multi-version software", should be corrected. Today it is a **multi-agent construction**, where the agents are humans and also AI agents working together. AI agents make the problem harder, not simpler, if you want to stay effective in the job market.

## What Each Software-Engineer Skill Means in Practice

**Reference:** 01.IntroSE.pdf, slide 10

- **Technical** skills mean more than "I can program in Python or Java".
- **Cognitive:** you must find good solutions and also spot problems in solutions that someone or something else (e.g. an AI) produced for you.
- **Different cultures:** large project teams often include people from several countries. You must understand how they think and what works or fails in that interaction.
- **Domain knowledge** is especially critical. Software is built for a domain such as hospitals, finance or aircraft control. Each domain has its own rules, and sometimes physical laws, that you must know to judge whether the software fits that context. You need to be expert enough in the domain, or at least able to talk with good domain experts.
- This is why human quality matters so much: understanding, interacting, and recognizing things that are new, which AI cannot identify.

## Intangibility and Malleability: The Car-Engine Comparison

**Reference:** 01.IntroSE.pdf, slide 12

- **Intangible:** apart from the user interface, which is a small part, software cannot be seen or touched. This makes it hard to show customers what the software is like and how difficult it was to build.
- **Malleable**, illustrated with a car: mounting the engine in a slightly different position changes the whole production chain. A small software change can be made by one developer, or one AI agent, in minutes or seconds.
- This is good because bugs can be fixed very easily. It is dangerous because we make quick changes without thinking carefully about their impact on the rest of the system and on other systems that use the software.
- CrowdStrike can be read this way too: developers changed something without agreement with the rest of the team.
- **Human intensive** is probably less true now that agents help, but things still have to be kept properly under control.

## Concrete Threats From Technology and Schedule

**Reference:** 01.IntroSE.pdf, slide 12

- **Development technology:** using a programming language that is not appropriate for the software, or an unstable library, hurts product quality.
- **Time and schedule:** when development time is too short, the activities that tend to be cut are verification of software quality. You may then deliver software and only discover later that it is not good enough for the problem.

## Reading the ISO/IEC 25010 Quality Model

**Reference:** 01.IntroSE.pdf, slide 13

- The standard was created much earlier. The 2023 version is its latest update.
- **Functional suitability:** the software implements all the functionalities identified for it.
- **Performance efficiency:** the software must be fast enough (time behavior) and must not waste resources such as memory, CPU and network.
- **Compatibility:** if your software must interact with other software, you must be aware of that and verify that it interoperates.
- **Maintainability:** the software can evolve over time, for bug fixes and for new functionality. The more maintainable it is, the fewer problems the team has when it must change.
- **Flexibility:** for example scalability, the ability to accept increasing amounts of requests.
- **Interaction capability:** human-computer interaction matters, but the external environment today also includes other machinery and other software.
- Security was deliberately skipped: it is so important that it has its own specialized courses.

## Reliability: Faultlessness Is a Dream, So Organize Repair

**Reference:** 01.IntroSE.pdf, slide 13

- Faultlessness is "like a dream": all software has some faults. The goal is to keep their number low and to keep the repair process under control.
- When software fails you need an organization that can restart it quickly, to reduce time out of service. You also need one that can diagnose whether there is a bug to fix. This is where **availability** comes in, and it will be treated in detail later in the course.
- **Fault tolerance** (and similarly recoverability) is the software's ability to tolerate faults and recover from them.

## Safety: Failures That Cost Lives or Money

**Reference:** 01.IntroSE.pdf, slide 13

- Safety concerns avoiding loss of human life. One example: the software controlling a radiation machine used for cancer therapy caused an over-radiation, an emission of a large amount of radiation, and people died.
- She also mentioned a case involving space software.
- Safety can also relate to losing money.

## Qualities Can Conflict: Reliability vs Performance

**Reference:** 01.IntroSE.pdf, slide 13

You must first understand which qualities are relevant for your software, because some of them partly conflict. Achieving good reliability usually adds overhead to the execution of tasks to make sure everything works. That overhead works against performance, i.e. spending the minimum possible time. You then have to decide which quality matters most.

## Why Productivity Must Be Measured, and Why Function Points

**Reference:** 01.IntroSE.pdf, slide 14

- Productivity matters, and it will come back at the end of the course. When a customer asks you to develop software, you need to know your productivity to forecast the effort needed, and therefore how much money to ask.
- A student asked a question about measuring productivity (ASR unclear). She agreed that measuring productivity is a real and hard problem. Her remark that "nowadays this is not anymore the case" seems to refer to lines of code no longer being a good measure (uncertain).
- The function points approach, covered later, measures productivity in terms of the amount of **functionality delivered** instead of lines of code. She considers this more appropriate nowadays.

## What to Keep and What to Drop From the Waterfall Model

**Reference:** 01.IntroSE.pdf, slides 16-17

- **Keep:** the waterfall's identified activities are still important, because they define the tasks every development must accomplish.
- **Drop:** the principle that the activities must run strictly one after another without iterations is no longer current.
- Iterations are now **highly recommended**. In the more specific activities (design, coding, testing) we learn things that let us improve the earlier ones.
- How work actually runs today:
  - requirements analysis and specification run together with at least a preliminary design, which is refined later;
  - coding may start in parallel, either on parts you already know how to implement, or as experiments on parts you don't know well, to find a solution;
  - testing is no longer confined to the end: you test as soon as something has been developed that can be checked.

## Maintenance Now Happens While the System Runs

**Reference:** 01.IntroSE.pdf, slides 17 and 24

Maintenance now interacts closely with execution. Many systems must run continuously and at the same time evolve, for example to add functionality. We do not want to stop the service, change the system and restart it. We want to change the service on the fly while it keeps running. This is not trivial, and it is a main focus of modern lifecycles.
