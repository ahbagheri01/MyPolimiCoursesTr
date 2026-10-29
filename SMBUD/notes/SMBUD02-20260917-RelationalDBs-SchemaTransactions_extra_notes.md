# SMBUD02-20260917-RelationalDBs-SchemaTransactions — Additional Professor Notes

**Transcripts:** SMBUD02-Marco Brambilla PoliMi-20260917 1546-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-03-ER-Relational.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-04-data-architectures.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-05-nosql.pdf

> **Coverage notes:** The ER/relational part was a quick recap of the Database 1 course: the professor went selectively through SMBUD-03 (design levels, ER, relational model, ER-to-relational mapping, the Drinkers example) and said explicitly that normal forms and normalization would not be covered in class. From SMBUD-04 he covered only the Schema and Transactions slides (p.2–9). He also explained ACID orally; the ACID properties appear in SMBUD-05-nosql.pdf (p.24–32). Partitioning, replication and cloud-based distribution are left for the next lecture.

## Relational Databases Still Dominate, So SQL Remains Required

**Reference:** SMBUD-03-ER-Relational.pdf, p.2 (NoSQL cartoon)

The professor warned against concluding that the world has moved to non-relational databases. He estimated that about 90% of the market is still relational, so students "cannot afford" not to know relational databases and SQL. Relational systems are not going away any time soon, especially in large, highly structured organizations.

## Why Design Top-Down, and Why the ER Level Is Technology-Independent

**Reference:** SMBUD-03-ER-Relational.pdf, p.4 (design levels)

- Design goes from concepts (information), to the data schema, to the technical implementation. The professor said this order reduces mistakes, inconsistencies and later errors by the people who use the database.
- At the conceptual level you do not even care whether the data will be stored in a database or on a computer at all. You only describe the domain and its data.
- So the same ER schema can be implemented as a relational database or as any of the non-relational models. The information stays the same; you only choose the storage format. In this course ER is used for concepts, the relational model for the logical level, and non-relational data models will be used at the logical level later. He said this design path will "to some extent" be reused for NoSQL databases.

## An Entity Is a Class-Like Prototype, Named With a Singular Noun

**Reference:** SMBUD-03-ER-Relational.pdf, p.9–10, p.13

- The professor stressed that an entity is not the set of objects but the prototypical representative of the whole class, much like a class in object orientation. That is why entities are named with singular nouns: `Employee`, not `Employees`, because it represents every employee of the company, not the collection.
- Relationships are usually named with verbs, because they say what one entity does with another (an employee *works in* a department, a student *takes* a course). They can be navigated in both directions.
- ISA hierarchies work like inheritance in object orientation.

## How to Read Min/Max Cardinalities

**Reference:** SMBUD-03-ER-Relational.pdf, p.11, p.18

- Each side of a relationship has a (min, max) pair, read in one direction of navigation (e.g. "given one student, how many courses does he take?").
- The minimum can only be 0 or 1. The maximum can only be 1 or N.
- Example: a student takes (0,N) courses, and a course has (1,N) students. N is only a placeholder for "many". The two N's do not have to be the same number.
- The professor said these cardinalities will be used later to optimize the data design (see the ER-to-relational notes below).

## There Is No Single Correct Design, and No Universal World Model

**Reference:** SMBUD-03-ER-Relational.pdf, p.14 (crucial design choices)

- Every domain admits many possible designs, and some are good while others are bad. Telling them apart comes with experience and the ability to judge what in the data matters. According to the professor, this is what separates a good data engineer or analyst from a bad one.
- Modelling also sets the border of the problem: when you design the schema, you decide what is inside your database and what is not, and that decision is yours.
- Why not build one huge model of the entire world once and reuse it for everything? Because every domain, application and company has its own requirements. Every new data store therefore needs a new design, guided by the designer's sensitivity.

## Address: Attribute in a University DB, Entity in a Maps Application

**Reference:** SMBUD-03-ER-Relational.pdf, p.15 (Entity vs. Attribute)

The professor added his own example to the slide's address question. In a university database, a student's address is just an attribute of the student. If you were designing the information structure of "the next Google Maps", the address is a key component of the system and becomes an entity. In general the same concept may be an attribute, an entity, a relationship, or an attribute of a relationship, depending on the problem.

## Reading the E-R Example: Composite Keys, Weak Entities, Optional Attributes

**Reference:** SMBUD-03-ER-Relational.pdf, p.18 (E-R Example)

- The professor called the ER part a summary of the Database 1 course, and said that at the end students should be able to design schemas like this one.
- A filled (coloured) bubble marks a key. `Class` has no single key bubble: a class is identified by the composite key Time + Room + Date, drawn as shown in the figure.
- The diagram also contains a weak entity, whose key is actually the key of a connected entity. The professor only pointed at it in the figure; it is presumably `Employee`/`Professional`, identified through `Trainee`.
- Cardinalities can also be put on attributes. `Marks` on `Attendance` is (0,1) because a trainee gets the grade only at the end of the course. For the whole duration of the course the mark does not exist yet, so some attendees have no mark and those who finished have exactly one.

## Before Relational: The Hierarchical Model and NASA

**Reference:** SMBUD-03-ER-Relational.pdf, p.26 (Codd 1970)

Databases existed before Codd's 1970 relational model. The professor said it is "only 55 years old" and has been the foundation of company data management for about 50 years. One important earlier model, built by IBM and others, was the hierarchical model, which stored objects and sub-objects. It came from NASA, which needed to track millions of components of the vehicles it was sending to space and paid for new database models to do it. Those models could store only part-of hierarchies (a missile is made of subcomponents, which are made of subcomponents, and so on). The relational model was a completely different approach.

## ER "Relationship" vs Relational "Relation": Two Different R's

**Reference:** SMBUD-03-ER-Relational.pdf, p.25–27

The two models are often used together but are not the same thing, and the shared "R" is misleading:
- In ER, R stands for **relationship**: a semantic connection between objects.
- In the relational model, R stands for **relation** in the mathematical sense: a subset of the Cartesian product of sets (domains).

Going from ER to relational is therefore a **mapping**, not an equivalence.

## Why a Mathematical Relation Is a Database Table, and Codd's Column Titles

**Reference:** SMBUD-03-ER-Relational.pdf, p.27–30 (games example)

- Intuition: the Cartesian product string × string × integer × integer contains every possible team pairing with every possible score. The relation `games` keeps only the subset that corresponds to reality. "Out of all the possibilities, we record only the reality", and that is how relations become databases. This is also why tables are technically called relations, and each row records one object or fact.
- The pure mathematical form has two problems: (1) it is positional, because column order is fixed by the order in which the sets are listed; (2) you cannot tell what a column contains. With, say, 50 columns full of numbers you would have no idea what they are.
- The professor described Codd's key intuition as putting titles (attribute names) on the columns. This solves both problems at once: the meaning is now explicit, and if columns are moved, their titles move with them, so no meaning is lost.

## Concrete Examples of Integrity Constraints

**Reference:** SMBUD-03-ER-Relational.pdf, p.35 (integrity constraints)

Constraints are rules that must always be true on the data, and they are used to enforce business requirements and business rules. The professor's examples:
- **Domain (single column):** a social security number must be a six-digit number.
- **Tuple (row-level):** the total price must be greater than the single price, or the discounted price must be lower than the full price.
- **Interrelational:** constraints that connect tables to each other. The most important constraint is the key constraint.

## Nulls: Why Primary Keys Forbid Them and Why They Are So Problematic

**Reference:** SMBUD-03-ER-Relational.pdf, p.34 (types of null), p.39 (primary keys)

- A primary key must be a key and must not allow nulls, because with null values you can no longer identify the objects.
- A null is an empty cell that comes with no explanation. The professor called nulls one of the biggest problems of relational databases and something NoSQL systems will try to address.
- Example with a table of match results: an empty score may mean the result is **unknown** (the match was played but nobody recorded it), or that it **does not exist** (the match has not been played yet, so leaving it empty is correct). When you read the table you cannot tell which case applies, and at least three cases exist (unknown, non-existent, don't know which). He added that philosophers count up to twelve different meanings of a missing item.

## The "NULL" Licence Plate: Nulls as a Data-Integration Disaster

**Reference:** None (not in slides)

A developer customized his California licence plate to read `NULL` to show off. Within days he started receiving thousands of traffic tickets from across the country. Police departments had recorded violations badly (plate missing, or entered in a format that was rejected), so the plate was stored as null. Through various conversion, import/export and integration steps, null became the string "NULL", and all those tickets were assigned to him. The professor's point was that null values create huge data-integration problems in companies, and that handling them will be one of the first requirements placed on NoSQL databases.

## Why Map From ER Instead of Designing Tables Directly; the Always-Safe Baseline

**Reference:** SMBUD-03-ER-Relational.pdf, p.43–46 (ER to relational, steps 1–2)

- If you design tables directly, you can easily make errors. Following the straightforward ER-to-tables procedure ensures the resulting tables comply with the rules of good database design.
- The professor's simplified mapping: one table per entity, one column per attribute, and the entity key probably becomes the primary key.
- For relationships, the easiest solution is always valid: create one table per relationship holding a pointer (foreign key) to each of the two entities, as in student–takes–course. It "seems trivial, but it guarantees proper design of the outcome."
- Depending on the relationship's cardinality, you can then "act smart" and avoid the extra table (next note).

## (1,1)-(1,1): Why You Must Not Post Foreign Keys in Both Directions

**Reference:** SMBUD-03-ER-Relational.pdf, p.49–50 (Sale / Cash Receipt)

- For Sale–Cash Receipt (every sale has one receipt, every receipt belongs to one sale), a separate relationship table would be "overwhelming". Adding one foreign-key column is enough, and since both sides are (1,1) it can go on either side.
- The slides only say "DO NOT do both". The professor explained why. Both pointers would be correct, but keeping both stores the same knowledge twice. That is not only useless but dangerous: if someone later updates one side and forgets the other, the copies become misaligned and the data is inconsistent.
- General rule: never create duplication in the data, because it opens the door to future errors.

## Dependencies in the Data Mean Risk of Misalignment (Drinkers Example)

**Reference:** SMBUD-03-ER-Relational.pdf, p.65–66 (Example FD / Example DF)

- The professor said this is basically the problem of normal forms and normalization, but "we are not going to go into this" in class.
- He stressed that many existing databases have schemas that are "plain wrong", and the Drinkers table is an example. His general reading: whenever there is a dependency in the data (within or across tables), information is duplicated and the database is exposed to misalignment.
- The error looks obvious in this small table, but it is not always so. Things also change over time and such errors pile up. Starting from an ER model would have avoided it completely.

## Drinkers Example Redesigned via ER (Not in the Slides)

**Reference:** SMBUD-03-ER-Relational.pdf, p.65–66 (only the bad table is shown there)

The professor showed the correct design on the board:
- **Entities:** `Person` (name, address), `Drink`, `Manufacturer`.
- **Relationships:** a person *likes* drinks with cardinality (0,N): you might like only water, so zero beers, or many beers. A person has exactly one *favourite* drink (he allowed that it might arguably be zero). Every drink has exactly one manufacturer, and a manufacturer produces many drinks (the transcript is unclear on whether the manufacturer side's minimum is 0 or 1).
- **Mapping:**
  - `Drink` gets a manufacturer-ID foreign key, because each drink has only one manufacturer.
  - `Person` gets a favourite-drink foreign key column, because there is only one favourite.
  - *Likes* becomes a separate table (person ID, drink ID) with one row per pair, e.g. "person A likes drink 1, person A likes drink 2".
- **Why a separate table for likes:** if liked drinks were stored with the person, the person would be duplicated once per liked drink. With this design there are zero overlaps or duplications, simply from modelling the information correctly and applying the mapping rules.

## SQL Is Assumed Knowledge (SELECT-FROM-WHERE)

**Reference:** None (not in slides)

The professor said SQL will not be taught again or used much in the course. Students are assumed to have a basic understanding of it, at least the SELECT-FROM-WHERE query. SQL will be mentioned occasionally as a reference point when introducing the new query languages, which mostly need to do the same things in different ways.

## Why Relational Databases Impose a Rigid Schema Up Front

**Reference:** SMBUD-04-data-architectures.pdf, p.3 (The data schema: typing, coherence, uniformity)

- In relational systems the schema must be defined before you save even the smallest piece of data. The professor gave the 1970-era reasons behind the slide's three bullets:
  - **Typing:** every column has a statically defined type.
  - **Rigidity:** once a table is defined, you do not change it. This guarantees consistency and coherence.
  - **Responsibility:** the person who defines the schema takes responsibility that data saved correctly in the tables is consistent and correct.
- This was a key requirement for traditional business applications such as banks and production companies, which need data that is always correct, aligned and in the same format. The rules also help users avoid mistakes.
- **Longevity argument:** a database designed today may be used for 10, 20, 30 or more years. Some banks still run databases designed in 1980, because "it works, why change it?" The more rules you set, the fewer mistakes people will make with the data decades later. The professor said this was the assumption of that time and will later explain why it is no longer so true.

## Multi-User Access: Race Conditions and Locking

**Reference:** SMBUD-04-data-architectures.pdf, p.4 (Transactions: multi-user); SMBUD-05-nosql.pdf, p.32 (the slide only says "Isolation: concurrency control")

- Databases were multi-user from the start: tens to thousands of concurrent users. In the past these were employees such as bank clerks; today they are also end users connecting through mobile apps. All of them access the same data at the same time.
- With only reads, concurrency is not a real problem; it may just slow the system down. The trouble comes when someone writes while another reads the same value, or worse, when several people write the same value at once.
- This creates a **race condition**. It becomes non-deterministic who reaches the data first, so writes override each other, values are lost, and you do not know which one was kept. It is an unlucky situation, but over millions of operations it does happen, and a bank cannot afford it.
- The original solution is **data locking**: when someone starts writing, the data is locked and the others wait until the write finishes and the data is unlocked. Requests that arrive in parallel are thus put into sequence. Transactions were built on this idea, and every database system implements them.

## Why Atomicity Matters: The Interrupted Money Transfer

**Reference:** SMBUD-04-data-architectures.pdf, p.7 (transfer example); SMBUD-05-nosql.pdf, p.28 (Atomicity), p.29 (Consistency)

- The professor described a failure in the middle of the slide's transfer: it takes two steps (take money from one account, add it to the other). If a shutdown, blackout or cyber attack hits between the two steps, money has either disappeared or "appeared magically", and the database is inconsistent. Atomicity rules this out: the transaction can never stop halfway, and after an abort it can simply be tried again.
- He presented consistency as the *consequence* of atomicity: because no transaction is left half-done, the data always satisfies the integrity constraints.
- Caution: orally he summarised recovery as "on restart, first try to finish the transaction (redo); if that's impossible, undo everything". The slide gives the precise rule: rollback or an error *before* commit leads to UNDO, and a fault *after* commit leads to REDO.
- He added that the transactional model has protected data, and let the economy work, for about 60 years.

## Isolation: Why Intermediate States Must Be Hidden (Domino Effect)

**Reference:** SMBUD-05-nosql.pdf, p.30 (Isolation: intermediate states not exposed, domino effect avoided)

- **Why the intermediate states must stay hidden:** they are only temporary, and the transaction might still roll back. Another transaction that read them would be looking at data that never really existed or was inconsistent, so any decision based on them would be wrong.
- **The domino effect:** the professor spelled out the mechanism. If one transaction fails, every transaction that depended on its visible intermediate states also fails. With millions of transactions running in parallel, such dependencies could crash the entire system.

## The Price of ACID: Rigid and Expensive

**Reference:** SMBUD-05-nosql.pdf, p.32 (Transaction properties and mechanisms). The slide lists the mechanisms but not what they cost.

- The professor named two problems with the ACID guarantees (he said "these five properties", presumably meaning the four ACID ones):
  1. They are **rigid**: you cannot step outside their rules.
  2. They are **expensive**: atomicity, consistency and isolation are not free. They need a lot of metadata and many internal subsystems, so the systems become heavyweight, use more resources and run more slowly.
- This rigidity and cost is another challenge that NoSQL databases will have to overcome.
