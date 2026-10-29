# SMBUD03-20260922-DataArchitectures-TowardsBigData — Additional Professor Notes

**Transcripts:** SMBUD03-Marco Brambilla PoliMi-20260922 1407-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-04-data-architectures.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-05-nosql.pdf

> **Coverage notes:** This lecture covered SMBUD-04 pp.10–19 (partitioning, replication, scalability, ingestion, wrangling) and SMBUD-05 pp.3–23 (flexibility, schema, data lakes, ORM, vertical/horizontal scalability) and pp.33–37 (CAP theorem). The transaction/ACID slides were not discussed here. The lecture stopped before ACID vs BASE, and the professor said consistency vs performance would come "next time".

## Partition as a Set Partition, and Why Only Horizontal/Vertical Splits Are Used

**Reference:** SMBUD-04-data-architectures.pdf p.11–12

- The professor defined partitioning formally. The parts must together give back the whole data set (union = whole set), and any two parts Pi, Pj must have an empty intersection. So partitioning neither loses data nor creates extra data by mistake.
- In principle any arbitrary cut of a table that "rebuilds the puzzle" is a valid partition. In practice it is unusable, because you could no longer find out which partition holds a piece of data under such "blurry" conditions. That is why in reality only two schemes are used: horizontal (subsets of rows, all columns) and vertical (subsets of columns, all rows).

## Horizontal vs Vertical Partitioning: Record Integrity and Tuple Reconstruction

**Reference:** SMBUD-04-data-architectures.pdf p.11–12

- **Horizontal:** every record stays intact and the schema is the same in every partition. Inserting or reading a whole row touches only one place.
- **Vertical:** a row is split across partitions, so it has to be rebuilt with what is basically a join. To do that, at least one key attribute must be stored in every vertical partition. Otherwise you cannot tell which pieces belong together.
- **Growth (answer to a student question):** vertical partitions also fill up as rows grow. You can keep splitting the columns further (e.g., putting B and C on two servers), but once a single column no longer fits on one node, you have to add horizontal partitioning as well.
- Horizontal partitioning is the natural default. It matches the meaning of the data, scales better, and is what most database technologies use.

## When Vertical Partitioning Makes Sense (Niche Cases)

**Reference:** SMBUD-04-data-architectures.pdf p.11

The professor called these niche cases:
- Most operations touch only a few attributes. For example, if B and C are always extracted together, keeping them in one partition means they are always in the same place.
- Statistics or aggregations over one or a few attributes. For example, computing the average of column D is easier when all D values are stored together. This makes vertical partitioning useful for analytics.
- Very heavy write workloads, because the write task is split into different parts, which can be very fast. The professor said "we'll see" this later.

## Sharding and a Question on Sensitive Data

**Reference:** SMBUD-04-data-architectures.pdf p.12

- Sharding is "horizontal partitioning with a modern flavor": horizontal partitioning over non-relational data, with features that are convenient for developers. The professor said the word is used a lot today and that it will be covered with MongoDB, which he called the best implementation of sharding.
- **Q: does it make sense to use partitioning for sensitive data?** It is possible, but he does not usually see it. When data is sensitive, it is usually the whole record that must be protected, not some of its columns.

## Why Replication Is Needed and How Many Copies to Keep

**Reference:** SMBUD-04-data-architectures.pdf p.13

- Partitioning solves scalability, but spreading data over many nodes (e.g., cloud servers "somewhere in the world") reduces your control over it. You cannot assume the data will always be retrievable without loss, damage or attacks, so a second mechanism is needed: replication.
- Database systems usually let you configure the number of copies. Typical defaults are **1** (no extra copy: if something goes wrong, everything is lost) or **3 in total** (the original plus two).
- **Why 3:** with only two copies, the same failure can realistically happen twice. Three failures hitting the same piece of data is less likely. You can go higher (usually odd numbers: 5, 7, 9), but every copy multiplies storage. A 20 TB database already takes 60 TB with 3 copies. So 3 is the usual trade-off between space used and availability guaranteed.

## Backup vs Fault Tolerance Are Not Synonyms

**Reference:** SMBUD-04-data-architectures.pdf p.13

- **Backup:** essentially offline copies, kept for future reference in case a disaster happens.
- **Fault tolerance:** an automatic mechanism. When a failure occurs, the system automatically replaces the damaged data with another copy, without slowing down or stopping.

## Combining Partitioning and Replication: Physical Layout and Opposing Effects

**Reference:** SMBUD-04-data-architectures.pdf p.14–15

- Real systems use both, whether they copy first and then split, or the other way round. The result is the same: every partition is replicated as many times as requested (e.g., 3 copies each of A, B and C) and spread over the nodes.
- The A/B/C split is conceptual. Physical placement depends on each node's resources: one node might hold A and B, another B and C, and a bigger node A, B and C.
- The two techniques complement each other, but they can also work against each other:
  - **Partitioning** raises scalability and performance. Each server holds less data and serves fewer user requests. Used alone, however, it causes reliability problems.
  - **Replication** gives reliability. It also speeds up reads, because many users asking for the same values can be sent to different copies. Writes become more expensive, though, since every piece of data has to be written once per copy, and constantly sending copies around loads the network.

## Working Definition of Scalability

**Reference:** SMBUD-04-data-architectures.pdf p.17

The professor gave this working definition, and said a more precise one would come later. A system is scalable if it keeps pace with growth in **data, users and computation**, meaning its performance does not degrade as these grow.

## Data Ingestion at Scale and a Slide Typo ("Outlier", not "Outliner")

**Reference:** SMBUD-04-data-architectures.pdf p.18–19

- At very large scale, even trivial problems need dedicated solutions. Ingestion ("just get the data and save it") is one example. The third part of the course will cover specific bus-based, event-based and stream-based technologies that collect data from many sources, blend and integrate it, and save it. Data quality is handled by preprocessing at ingestion time.
- The professor corrected the data wrangling slide: "outliner" should read **outlier**. During augmentation, the data is enriched with derived properties.

## Flexibility as the Guiding Principle of the Move to Big Data

**Reference:** SMBUD-05-nosql.pdf p.4–5

Relational databases were used for about 50 years. The changes made for big data all follow one principle: flexibility. Relational transactions are extremely rigid, relational schemas are rigid and must be defined in advance, and the technologies were very limited in their ability to grow. Flexibility was therefore wanted in three places: data shapes, hardware management (how you pay for resources), and computation (integrating AI, ML and real-time processing).

## Schema-less vs Implicit Schema (Dynamic Typing Analogy)

**Reference:** SMBUD-05-nosql.pdf p.7

- The reasoning was: if the schema is too constrained and "only there to annoy the developer", get rid of it. You save data without defining tables, columns or structure in advance. "Schema-less" and "schema-free" mean the same thing.
- In practice, many systems use an **implicit schema** rather than none at all. You never declare a schema, but the database infers it when it reads the data. The professor compared this to dynamic typing in programming languages: you no longer state each variable's type, and the language works it out.
- So there are two routes: remove the schema completely, or postpone it, which leads to schema on read.

## Schema on Read: Advantages Beyond the Slides

**Reference:** SMBUD-05-nosql.pdf p.8–9

Schema on write forces each incoming item to be transformed to fit tables someone defined beforehand. ("Structured" query language is called that "not by chance".) Schema on read gives four advantages:
1. **Faster, simpler writes:** no transformation or reshaping, the raw data is saved as it is.
2. **Simpler schema:** each analysis defines a small schema that covers only the data it needs. In schema on write, one complex schema with tens or hundreds of tables describes the whole business.
3. **Simpler queries:** the small schema is designed for the query, so the data is already in the right shape for it.
4. **Raw data is preserved:** nothing is dropped or altered to fit a table, so any future analysis can start again from the original data instead of a simplified subset.

A student pointed out that schema on read avoids schema **migrations**. The professor agreed: changing a fixed schema (adding, changing or removing columns) is a huge problem nobody wants to deal with, and it is one of the main drivers behind schema-less and postponed-schema approaches.

## Example: Storing a Student's Bachelor Exam Records

**Reference:** SMBUD-05-nosql.pdf p.8–9

Suppose a student sends the list of exams from their bachelor, as a CSV, JSON or Word file.
- **Schema on write:** someone, or a program you have to build, must extract every value and put it into the relational tables. This takes a lot of time, the original document is lost, and both building the process and writing are expensive. In exchange, SQL queries are available later.
- **Schema on read:** the file is saved in whatever format the university delivered. If someone later only wants the course titles, they build a small schema just for that: one table with the student name and the list of courses.

Caveat: you can keep raw data with all its format variations, but you must make sure someone will be able to open and use it in the future.

## The Big Data Architecture Still Needs Preparation Before Storage

**Reference:** SMBUD-05-nosql.pdf p.10

- The schema-on-read picture is simplistic. You cannot just drop a raw file in storage with no description, or nobody will be able to use it later. Some wrangling (cleaning, standardization, descriptions) has to happen before storage. After that, everyone can build their own schema on top.
- The **data views** in the architecture are the same idea as SQL views (partial, dedicated views), applied to any kind of data rather than only relational tables.
- Storage differs by technology. Some store the raw file exactly as received. Others convert it to a format that is still unstructured but standardized, such as Parquet or ORC (ASR-garbled as "par K or C", reconstructed with the help of the slide).
- How to use the data, which parts to use and how to reshape them is decided by the analyst, or the data engineer supporting the analyst, at read time.

## Downside of Schema Flexibility: Data Quality Responsibility

**Reference:** SMBUD-05-nosql.pdf p.7–10

Answer to a student question. Removing or delaying the schema means losing control over data shape and quality. More flexibility means more risk of mistakes, because people can store data in bad formats or bad shapes. With a flexible schema or none, all responsibility for data quality falls on whoever saves the data: "with more flexibility comes more responsibility". The preparation layers before storage exist to limit this risk.

## Data Lake: What It Is and What It Is Not

**Reference:** SMBUD-05-nosql.pdf p.11

- A data lake is where the schema-on-read approach ended up. It is a dedicated technology that companies buy as a long-term store for every piece of company information: essentially a huge database with no schema, like a city's water reservoir.
- It does **not** replace the company's existing databases and systems. Those keep working as before, and everything is also copied into the lake.
- It is schema on read: when managers ask for analytics, someone picks the relevant pieces from the lake, builds an aggregated schema for them, and runs the analysis.
- **Not just a Google Drive (student question):** to someone uploading, it may look like an online drive. To data users it is closer to a database, because they see both the raw files and their catalog descriptors.
- **Ingestion is automated, not manual.** For example, a process forwards every email received by the company's mail server to the lake, and another saves all sales data. Manual acquisition of everything would be too expensive.

## Why Pay for a Data Lake if the Data Already Exists Elsewhere

**Reference:** SMBUD-05-nosql.pdf p.11

- Students suggested the integrated view and aggregation across business units as benefits. The professor added that the lake is also costly: if each source is already big data, the lake is "big, big data", which in a way wastes resources.
- He named the key benefit: **one single place that everyone knows holds the data.** In many organizations the real barrier is first finding where the data is (among hundreds of databases owned by different offices and teams), then getting permission and access. According to him, that alone typically costs "three months of your life" spent asking for favors and chasing who knows what.
- Risks: the lake becomes very large, and without proper management it quickly turns into a **dump** that nobody can use.

## Data Lake Zones: Why They Exist and How Data Moves Through Them

**Reference:** SMBUD-05-nosql.pdf p.12

- The zones are essentially data wrangling specialized for data lakes, done before the final write. "Flexibility doesn't mean total chaos."
- **Catalog:** without one, you do not even know you have the data. **Metadata:** what the data is about, what is inside, what to expect, statistics. **Protection:** having everything in one place does not mean everyone can see everything; each person sees only what their rights allow.
- **Trusted vs refined (student question):** the trusted zone (quality and validation) removes what is wrong: noisy or missing data, wrong values, wrong matches between sources. The refined zone (enrichment, also called "augmenting") adds value. Examples are precomputing derived attributes (useful especially for ML, even though they could always be derived later) and integrating public or third-party sources, such as standardized addresses or locations, or pointers to public datasets.
- **Why they are called "zones":** each one is an actual temporary storage area. Incoming volumes are huge and the steps cannot run synchronously. Data piles up in a zone, a process takes the next item, cleans it and moves it to the next zone, and so on, incrementally and asynchronously. It works like a **multi-step buffer** whose queues should ideally be empty.
- **Formats (student question):** not everything ends in the same format. For example, a manufacturer's technical documentation PDFs might be kept as they are and indexed like a search engine rather than converted to tables. Each source needs its own custom process, usually tied to its application (the mail server, the document management system, etc.).

## Object-Relational Mismatch: Where Exactly It Lies

**Reference:** SMBUD-05-nosql.pdf p.13

- A student mentioned foreign keys and N:M relationships. The professor said the mismatch already shows up with a single table. A class is instantiated into objects, while a table is a schema whose items are rows, and **a row is not an object**.
- In an OO language (Java, Python…), you open a connection or session and send an SQL query. What comes back is a **result set** (a list of tuples), not objects. To get objects, you loop over the result set and convert each element by hand.
- Developers therefore wanted new technologies to be OO-compatible, whether or not they had a schema. Object-oriented databases were tried (around the '90s, by the professor's recollection) and were a "total failure". NoSQL systems were instead designed so the database and the software space match directly. That is why MongoDB and similar systems are much more developer-oriented.

## Vertical vs Horizontal Scalability: Not Related to Partitioning; Drawbacks of Scaling Up

**Reference:** SMBUD-05-nosql.pdf p.16–19

- **Warning:** vertical/horizontal *scalability* has nothing to do with vertical/horizontal *partitioning*.
- For about 50 years, companies scaled vertically. They bought IBM servers costing tens of thousands of dollars, a few years later ones costing hundreds of thousands, and migrated everything each time. Consumers do the same with laptops and phones.
- Problems with vertical scaling raised in class:
  - expensive migrations;
  - costs are linear only up to a point, then become exponential;
  - there is a physical limit, since no machine can be infinitely big;
  - you cannot go back down if needs shrink (the old machine was thrown away, and paying to downgrade makes no sense);
  - a single point of failure;
  - you have to buy ahead of current needs or the machine is already outdated, so part of it sits unused for some time, which is a waste;
  - one very big machine probably uses more energy than many small ones (the professor agreed with a student on this, with hedging).
- The hardware tiers on the slides: **commodity** is something you just buy (e.g., on Amazon, a rack server). An **appliance** is a dedicated machine (e.g., Oracle). **Exceptional** hardware means building your own machine, at more than a million dollars.

## Horizontal Scalability: Linear Cost, Higher Entry Cost, and How to Choose

**Reference:** SMBUD-05-nosql.pdf p.20–23

- **Horizontal:** keep the old server and add more of roughly the same size (maybe slightly bigger), sharing resources across them. Each machine costs about the same, so cost grows linearly. The initial cost is higher, though (the intercept in the chart), because even with one machine you must buy infrastructure able to connect future machines.
- **Choosing:** with a small database and no big growth expected, buy one server and keep it (vertical). With huge data, or data expected to grow, go horizontal. In the grey zone the choice is unclear, because you cannot predict the future or every cost exactly. The rule is to project your expected resource use and pick the cheaper option.
- The curves move over time with pricing. In the professor's rough estimates, horizontal paid off beyond tens to hundreds of petabytes about 20 years ago, around 1 PB a few years later, and beyond a few terabytes today. The slide's own figures (10 PB in 2006 down to about 10 TB today) differ slightly.
- **Q: can SQL scale horizontally?** Yes, with no problem. But NoSQL technologies were built for horizontal scaling from day zero, so they fit it more naturally. The "traditional" icons on the Big Data vs Traditional slide stand for a centralized data center or mainframe (big IBM systems), versus simple servers spread across the cloud.

## Elasticity: Scaling Down Is Not Failure

**Reference:** SMBUD-04-data-architectures.pdf p.17

Scalability also means shrinking when fewer resources are needed, which is elasticity. Needing less is not a sign of failure. Many businesses are seasonal. The professor's example: Amazon sells roughly 50% of its products in two months, with a huge peak at Christmas, so it takes on temporary workers and temporary servers to keep the same speed, then scales back down. The model should allow growing and shrinking with demand.

## CAP: C, A and P as Properties of Data, System and Network; Intuitive Proof

**Reference:** SMBUD-05-nosql.pdf p.33–35

- The professor tied each letter to a different layer:
  - **Consistency** is a property of the *data*: every copy and piece, across partitions and replicas, is coherent and aligned.
  - **Availability** is a property of the *system*: users always see it as up and always get some answer. During a partial failure some features may not work, but the system does not shut down.
  - **Partition tolerance** is a property of the *network*: the links between nodes can fail. If you are lucky, alternative routes exist. If a critical link fails, the system splits into a left part and a right part that can no longer talk to each other.
- **Intuitive proof (no formal proof given):** after a partition, suppose both sides keep computing independently so users on each side still see the system as available (A + P). Then a change made on one side cannot reach the other, so consistency is lost.
- **Real causes of partitions:** roadworks cutting cables, a broken Wi-Fi router, or, in the dramatic case, 9/11. According to the professor, entire countries were cut off from the internet for hours because network centers for those countries were located under Ground Zero.
- Traditional databases chose CA because data was centralized, so partitions were not a concern. Today data is spread across the cloud and P is a given, so the real choice is between C and A.

## Giving Up Consistency Means Accepting Wrong Answers — and Why Companies Do It

**Reference:** SMBUD-05-nosql.pdf p.35–37

- Reducing consistency is never something you want for its own sake: inconsistent data means **wrong data**, so queries return wrong answers, "full stop". It is accepted only for "the better good" of availability.
- Examples raised in class where degradation is tolerated so the system keeps running:
  - online video games (occasional delays);
  - video and other streaming services;
  - sensor streams where some readings get lost;
  - phone calls with degraded signal.
- **Social media:** you search Instagram or TikTok for "dogs" and get 9.9 million results instead of 10 million. You have no way of knowing, and you survive anyway. With thousands of servers, some regions may be served a subset of results for a few seconds when parts of the infrastructure lag. If everything works, the results are correct.
- **Web in general:** a page might be 10 minutes old. When Amazon shows "only 7 items available", you cannot know if it is really 7, or whether that count is for Italy, Europe or Milan.
- **Why companies accept this:** for them, being online matters more than exact data. Missing three dogs is fine, but Instagram being offline is a disaster. The professor recalled the Meta outage (Facebook, Instagram, etc.) a few months earlier, when "it looked like the world was finishing". Availability protects brand awareness, visibility and the image of reliability.
- **Not Boolean (student question):** you can have some of each. Some systems, but not all, let you choose levels of availability with the matching level of consistency.
