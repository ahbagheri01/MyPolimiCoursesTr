# SMBUD01-20260915-CourseIntroduction-BigData — Additional Professor Notes

**Transcripts:** SMBUD01-Marco Brambilla PoliMi-20260915 1410-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-00-intro_course.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-01-bigdata.pdf

> **Coverage notes:** The lecture ended with the Netflix conclusion slide (SMBUD-01 p.56). The "Big Data = Big Problems?", "Notice anything?" and "Problems" slides (p.57–59) were left for the next lecture: as homework, students should look at their Netflix/Prime Video catalogue and see whether they notice anything weird. The professor said it would be part of the "next examination", which is probably an ASR error for "next explanation" (uncertain). The hype cycle, AI market, "collect/analyse/build value" and "cleanse vs. analyse as is" slides were shown with little or no spoken comment.

## SQL Is a Prerequisite, and "When to Use What" Is the Core Skill

**Reference:** SMBUD-00-intro_course.pdf p.3–6

- This course is the "next chapter" after the bachelor database courses: moving from relational to non-relational databases. Knowing relational databases (ER model, relational model, SQL) is a requirement. "We will talk about NoSQL, but you need to know SQL." There will only be a very quick recap.
- The professor called this the **most important part** of the course: being able to decide, from the problem, setting and scenario, which kind of database is best ("when to use what").
- The catalogue covers 8 *kinds* of databases, not 8 databases. Each kind has its own products, data model, query language and design approach. Every kind gets a quick introduction, and only the most prominent/popular ones are covered in depth. For each approach at least one real product (commercial or open source) is named, and the course also looks inside the implementation (how scalability, distribution and reliability are guaranteed).

## Exam Format Details Not on the Evaluation Slide

**Reference:** SMBUD-00-intro_course.pdf p.9

- **Written exam:** in presence, during the official exam sessions, split into theory and practice.
  - Theory: closed questions (multiple choice / true–false). It is very short, about 10–12 minutes (about 15 minutes all included). The theory part is closed before you move on.
  - Practice: exercises on the topics and technologies of the course, worth 24 points, about 2 hours.
- **Format:** usually on your own laptop in a safe exam browser that only allows the exam website. On some calls it may be on paper for technical reasons, with the same kind of questions. Everything is closed book; you may bring only a thin, transparent pen. On exam day you sign explicit anti-cheating rules, and if you don't agree you leave.
- **Laptop:** the safe browser does not work on Linux, so you need a Mac or Windows machine (borrowing one is fine). If you only have Linux, tell the instructors in advance. A test to run at home will be provided weeks before. On exam day the exam will **not** be stopped if your browser fails to open.
- **Project (+1):** only if you already have ≥29 in the written part, to reach 30 / 30 cum laude. It can only be done after you have taken the practice exam at least once. It is fully optional.
- **Intermediate tests (3 × 1 pt, "continuous evaluation"):** optional, in class on your laptop, closed-answer, **pass/fail** against a threshold (1 point or 0). If there are many students, they take it in groups (e.g. 300 → 3 groups of 100) with different questions per group. Dates will be announced later.
- **Oral:** the instructors can require it ("force you") when they need more evidence. It comes after the written part and checks that you actually know what you wrote.

## No Single Textbook Covers the Course

**Reference:** SMBUD-00-intro_course.pdf p.10–11

No single book covers all these topics. Kleppmann's book covers data-intensive application design but not everything. For the individual technologies you should also read their official documentation and online resources.

## Why Big Data Matters, and Why It Is Not Mainly About Size

**Reference:** SMBUD-01-bigdata.pdf p.4

- Motivation: big data is the foundation of everything innovative in computer science today. AI, machine learning and data science work only because big data sources exist.
- Reading of the IBM survey (biggest customers, late 2000s when the idea emerged): the top answers were scope, new kinds of data/analysis and real-time; "large volumes" comes only near the bottom. Size is one complexity factor, but not the only one and probably not the most critical.

## Volume: Where "Big" Starts, and Why We Underestimate It

**Reference:** SMBUD-01-bigdata.pdf p.5

- Individual or consumer data is never "big": megabytes to terabytes, even a few hundred TB, is still small. Big data starts beyond the **petabyte** (exabytes and up), which is usually only reached by large organisations. Storing small amounts is almost free (a disk, a cheap cloud subscription). Storing and managing big data is still expensive, and the problems start from the exabyte level on.
- **Money analogy for the ×1000 steps:** if I pay you 1 € per kilobyte, I owe 1,000 € per megabyte, 1 million € per gigabyte, 1 billion € per terabyte and 1 trillion € per petabyte. Nothing else in the real world grows across scales like this. Because data is intangible, we don't notice how much we "waste" when saving photos and videos.

## Variety Is Really Heterogeneity

**Reference:** SMBUD-01-bigdata.pdf p.6

The correct technical term is **heterogeneity**: data differs in structure, format, type and storage standard. Traditional sources (banks, traditional companies) stored mostly numbers and a few strings. Processing video, audio or multimedia is dramatically different, and that is why dedicated tools, AI and machine learning are needed.

## Velocity: If You Are Too Slow, the Data Is Lost

**Reference:** SMBUD-01-bigdata.pdf p.7

Data is generated continuously by huge numbers of sources, and this continuous flow is what defines data streaming. Networks and systems must process data as fast as it is generated. With sensors, IoT and smart devices, much data is produced, transferred and then **immediately deleted**. You analyse it in real time, keep only the analytics/aggregations and throw away the raw data. If the system is too slow, you miss that data forever and lose the opportunity.

## Veracity = Data Quality, and It Is Worse Than in the Past

**Reference:** SMBUD-01-bigdata.pdf p.8

- Veracity is essentially **data quality**: errors, noise, missing values and wrongly aggregated values, so the data cannot be trusted.
- This is a step back from the past. Traditional internal company data was higher quality because companies kept it clean, organised and structured. Today data comes from many sources we have no control over, and with so many producers a mistake somewhere is very likely.
- **Data integration** is itself a source of errors. When internal and external data are combined, it is easy to connect or match the wrong records, or match missing values with real data.

## Dirty Data Makes Models Learn a Wrong Reality

**Reference:** None (not in slides)

AI, ML and LLMs are all built on data, so feeding them dirty data makes them "learn a wrong reality". Before thinking about models and optimisation, ask whether you have the data and whether its quality is good enough. If not, clean and prepare it first. The professor quoted industrial estimates that **60–75% of the cost** of ML/AI/data-science projects goes into data cleaning (removing nulls, fixing wrong digits in numbers…), even for top deep-learning experts.

## The Vs Become Requirements for Database Systems

**Reference:** SMBUD-01-bigdata.pdf p.9

You can add as many extra Vs as you like (5V, 6V…), but the four above are the key ones. These features of the data are also **mandatory requirements** for modern data systems. This is why relational databases are no longer enough: they don't comply with most of these aspects (to be developed in later lectures).

## Why Now: Falling Costs Changed People's Behaviour

**Reference:** SMBUD-01-bigdata.pdf p.12–16

- The storage cost chart is on a **log scale**: from about $600/GB to a fraction of a cent. At $600/GB people would take fewer photos of their food, make fewer copies of the same file, and not save a 215 MB PowerPoint. Cheaper storage changes behaviour, and that creates the data.
- Same for devices (a phone with today's iPhone features would have cost a few million dollars 20 years ago) and bandwidth (a fibre subscription costs about 20 € today; in 1999 it cost about $1,200, and only in a few places).
- This feeds the virtuous cycle on the slide, which over about 30 years produced exponential data growth. The professor's rough figures: about 10 ZB/year around ten years ago with ~50% year-over-year growth, and today on the order of a few hundred ZB, still growing at about the same rate (approximate spoken figures).

## When Will Data Growth Stop? Saturation, Not Storage, Is the Real Limit

**Reference:** None (not in slides)

- Running out of material to store data is centuries away. The earlier and more relevant question is when the **market saturates**: can we keep producing ~50% more data every year forever? This is like a country's GDP, which must keep growing. Generative AI boosts generation even more.
- Empirically every phenomenon eventually reaches a **plateau**. If data growth plateaus, content production and **technology evolution** stagnate too. Technology investment (e.g. faster processors) is paid for by the returns from growing data and consumption, so companies would stop investing.
- The estimate is still about 20–30 years of exponential growth, with no decrease in sight for the next 15–20 years.

## From Linear to Exponential Growth: the Analysis Gap

**Reference:** SMBUD-01-bigdata.pdf p.39

Until about 2000, data in traditional enterprise systems grew roughly **linearly**. Around 2000, with the growth and success of the web, it became **exponential**. Tools built for traditional data cannot analyse it at the same scale, so the gap widens. More data does not mean more value: without enough analysis you cannot take decisions and execute improvements, and you lose opportunities. The answer has two sides: evolve the **technology** (market) and the **people** (way of working).

## The Three Market Pillars and Hidden Value

**Reference:** SMBUD-01-bigdata.pdf p.32–33

- **Infrastructure:** everything from hardware up to software for data acquisition, storage, transfer and processing (e.g. Oracle, SAP, Google Cloud, MongoDB, Azure). **Analytics:** turns stored raw data into value (data science, ML/AI, visualisation, search engines). **Applications:** internal or customer-facing apps (web, mobile), which are how value reaches users. **Data sources:** today data can also be bought from data vendors and integrated.
- Users only see the application (e.g. scrolling Instagram). Most of the value sits in the infrastructure (thousands of distributed, replicated servers) and the analytics (ML/AI models optimising the experience). Media also talk about apps (ChatGPT), not about data centres or the GPT model.
- **Example:** Musk's purchase of Twitter (about $44B, "I think") got huge media coverage. A larger acquisition at about the same time (about $48B, the professor was unsure) of VMware went almost unnoticed. VMware does virtualisation, cloud and cluster infrastructure, without which Instagram, Facebook or Twitter could not run. This shows the gap between technical value and perceived value.

## Full-Stack Vendors: Integration vs. Vendor Lock-in

**Reference:** SMBUD-01-bigdata.pdf p.32–33 ("cross-infrastructure" / "full data stack providers")

- Big vendors (Amazon, Google, Microsoft, IBM, SAP…) expand from their original business (e.g. Oracle from databases) to cover the whole stack. Their customers are mostly companies, not end users.
- **Advantage:** everything is integrated. On Azure you find databases, file systems, ML models, analytics, visualisation and app development environments that ideally work together, so developers don't have to integrate products from different vendors. This is their main marketing message.
- **Disadvantages:** everything is standardised, so there is no custom development and you must configure it yourself. The main problem is portability, i.e. **vendor lock-in**: once database, cloud and AI models all come from one vendor, moving away is a "nightmare" and so expensive that if they raise prices you are effectively stuck (quasi-monopolistic).

## Open Source: Not Lower Quality, but Not Free

**Reference:** SMBUD-01-bigdata.pdf p.32–33 ("open source platforms")

- Open source is **not lower quality**. In the big data market most commercial tools are built on open-source technology, which the commercial vendors themselves develop.
- **Open ≠ free.** The source code is free, but management, daily operations, infrastructure and the people to run it are not. You also need a strong technical team. Commercial "fully managed" deployments instead come with guaranteed operation, customer service and automatic updates.
- Practically all NoSQL databases (MongoDB, Redis, Neo4j) come both as an open-source version and as a commercial/cloud service sold by the same company.

## Big Data Projects Fail Mostly Because of People

**Reference:** None (not in slides)

Most big data and data-science projects that fail do so not for technical reasons but because of **people's attitude**. Organisations say they want innovation, but people who have worked one way for years resist change. Big data therefore requires changing how people perceive and use data. The following paradigm shifts are about mindset, not technology.

## Sampling Was Forced, Not Chosen: Barilla and Auditel

**Reference:** SMBUD-01-bigdata.pdf p.20–22

- Statistical sampling was not a "nice to have". It was forced because the whole population (people, services, products…) could not be processed. The limit was also on **collection**, not only analysis: today the whole stack for collecting, storing and transferring data exists.
- **Barilla example:** 50 years ago, to learn what customers thought of a new pasta, you sent people with paper questionnaires into supermarkets ("did you like the colour of the box?") and got 50–100 answers. Today you use web and social-media analytics and ad monitoring (how many watch, click, for how long). Someone used to paper surveys finds this change hard.
- **Auditel example (analog TV):** of about 60 million Italians, about 5,000 families were paid to host a device that recorded remote-control channel changes. "15 million watched Sanremo" was extrapolated from them, so everything depended on the sample being statistically representative. With streaming (Netflix) everyone is monitored second by second.
- The Union Pacific slide was described as full-scale monitoring of US railway tracks (the professor said "through drones"; the slide photo shows a track-mounted device).

## Data-Driven Exploration: Insights Can Seed Hypotheses

**Reference:** SMBUD-01-bigdata.pdf p.23–25

- Traditional: observe a phenomenon, formulate a hypothesis, run an experiment, then accept or reject it based on the data (e.g. "we sell less", form a hypothesis, try to fix it).
- Data-driven (bottom-up): explore the data for correlations, connections and probabilities. The result is an **insight, not necessarily an answer**, but it can be used to *formulate* a hypothesis. This is most useful when you have no idea what the solution might be, or when the problem or data is so complex that a hypothesis is impossible to formulate.
- **Example:** genomics. One DNA sequencing run produces terabytes of data, and you cannot write hypotheses from terabytes of bits. You first explore with statistics and correlation.

## From Periodic Reports to Real-Time Dashboards

**Reference:** SMBUD-01-bigdata.pdf p.29–31

Traditionally, data goes into a database or data warehouse, and analysis is **periodic and delayed**: historical reports (monthly sales, yearly financials, quarterly…), typically PDF files. Today data up to last night is available, so managers analyse it almost in real time. With current market dynamics a six-month-old analysis is "like going back to prehistoric times", basically useless. The shift is from reports to **dashboards**: interactive, dynamic (usually web) applications where the manager can explore, zoom in and out, and change perspective at any time.

## Big Data Without Value Creation Is Wasted Money

**Reference:** SMBUD-01-bigdata.pdf p.38

Companies push hard to "have" big data and AI and are happy once they can say so. This risks a bad disillusionment, because these things cost a lot: owning an infrastructure or an AI team produces no value by itself. Collecting and analysing must end in value for someone (company, customers, shareholders), otherwise it is wasted money. If value is created, the cycle repeats with continuously better performance. Value can be of any kind (sales, better processes, happier people), but there must be a **quantitative** improvement.

## Netflix's DVD Era: Small Data for Logistics

**Reference:** SMBUD-01-bigdata.pdf p.43–47

- Netflix (about 400 million customers today, per the professor; the slide's 50 million is old) has its value in its data, and this was true from the beginning.
- About 20 years ago it shipped DVDs by mail. Customers picked a movie on a basic website and got it by the next evening, anywhere in the US (New York to Alaska), otherwise they would go to Blockbuster or rental shops. Its advantage over shops was **catalogue variety**, like Amazon vs. a bookstore.
- The four data points (customer, movie, rating, date) were used to **predict demand**. One-day shipping was hugely expensive and DVDs are physical, so they had to decide which movies to stock, how many copies to print, where to place them and how to ship in time.
- With streaming, every click, stop, restart, preview, scroll and catalogue view is recorded, giving millions of data points per customer.

## Netflix Personalisation via Clustering, and Why Cluster Instead of Per-User

**Reference:** SMBUD-01-bigdata.pdf p.49–50

- Each customer is a point in a space describing their behaviour. Customers are clustered with ML, movies are clustered too, and user clusters are associated with movie clusters ("these users like these movies"). This produces thousands of very specific categories (e.g. "TV programs featuring a strong female lead"), each shown only to the interested users.
- **Student question — why cluster users instead of personalising per user?** People with similar preferences are similar enough that grouping them causes only a small error. This is *not* sampling. The gain is **computational efficiency**: about 2,000 profiles instead of 400 million cuts the computation by several orders of magnitude.

## Netflix Strategy and Interface: Continuous Experiments on Customers

**Reference:** SMBUD-01-bigdata.pdf p.51–55

- **Strategy:** data on which actors, directors and kinds of movies people liked drove what to produce or buy. The professor said that when entering the European market Netflix bought the rights to House of Cards for an investment on the order of $25 million (figures as stated in class).
- **Interface:** every pixel (colours, figures, labels, even fonts) is decided from data. Customers are "guinea pigs" in a continuous experiment: for the same series you see different previews on different days, and they measure how you react (whether and when you click, how long you stay). A student called this A/B testing and the professor agreed. The results decide which preview version to show for future movies. All big players do this.

## Ethical Concern: Data-Driven Personalisation Can Shape Taste

**Reference:** None (not in slides)

This practice is ethically debatable. According to the professor, long-term studies show it can **change people's tastes** and steer them toward certain movies. Applied to news or political advertising, it becomes "a little bit creepy". He stressed that Netflix is not singled out as "the bad guy": basically all big players act this way.

## "Data Companies": Value in Data, Not Assets

**Reference:** SMBUD-01-bigdata.pdf p.56

Uber is the biggest car-rental company in the world and owns no cars. Airbnb is the same for houses. Their value is in the data and the optimisation built on it, which is why they are called data companies rather than car or housing companies.
