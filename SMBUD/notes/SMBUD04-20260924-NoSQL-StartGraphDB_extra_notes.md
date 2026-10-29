# SMBUD04-20260924-NoSQL-StartGraphDB — Additional Professor Notes

**Transcripts:** SMBUD04-Marco Brambilla PoliMi-20260924 1611-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-05-nosql.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

> **Coverage notes:** The lecture picks up SMBUD-05 at the CAP theorem (p.35–38) and goes through BASE, the reasons relational DBMSs did not adapt, NoSQL history, families and originators. It then covers SMBUD-06 from graph theory up to the first Cypher data-creation slides (p.51–52). MERGE, import, indexes, constraints and query syntax were not discussed in this lecture.

## Updated Exam Rules on WeBeep

At the start of the lecture the professor said the exam rules on WeBeep were still last year's. They have been replaced with this year's rules, which show how the exam is split into its different parts, so check the WeBeep version.

## Mixing Consistency and Availability Within One Application: E-commerce

**Reference:** SMBUD-05-nosql.pdf p.35

The slide only says that C and A can be "partially accommodated". The professor's example of what that means:

- In an e-commerce site, the **catalogue and product description pages** should be highly available (always up, always showing pages), even if they contain some obsolete or wrong data.
- **Order submission and payment** must be highly consistent: you must not charge more or less money than needed, or order more or fewer products than the stock has or the user wants.
- So one application can choose availability for some features and consistency for others.
- As a reminder from the previous lecture, he listed streaming, general web applications, social media, and alarm/emergency services as cases where lower consistency is accepted in exchange for higher availability.

## Why Consistency Trades Off Against Performance (Speed)

**Reference:** SMBUD-05-nosql.pdf p.37

The slide only states the trade-off. The explanation from class:

- More consistency means less parallelization. Running more parallel processes improves performance but tends to lower consistency (a student's answer, which the professor confirmed).
- Guaranteeing consistency needs many extra components, as with ACID. You need data replication, checks that every replica holds the same values, and processes that keep versions aligned. All of this is expensive, so the system slows down as you raise the consistency level.
- Sometimes speed matters more than quality. A slow website makes it more likely that the customer simply goes to another site, so you accept lower-quality output in exchange for speed. "Performance" here means speed. He said this will come back when discussing caching.

## Using the CAP Triangle as a Designer

**Reference:** SMBUD-05-nosql.pdf p.38

- You can only be on **one side** of the triangle at a time.
- The CA side is essentially relational/traditional databases. The professor said this side will basically **not be covered in this course**.
- Since P is mandatory, the NoSQL technologies sit on the CP and AP sides.
- The **technology builders** decide whether a product is consistency-oriented or availability-oriented. As an application designer you cannot change those features. You can only pick a product whose orientation matches your requirements: a CP product if you need high consistency, an AP product if you need high availability.
- Choosing a consistent (CP) system roughly means you keep ACID transactions. BASE is the answer to "do we lose every transactional guarantee if we go AP?"
- He added that hybrid solutions exist and will be mentioned later.

## How to Read the BASE Properties (and Why They Are Weak)

**Reference:** SMBUD-05-nosql.pdf p.39, p.42

BASE was proposed so that highly available systems would not lose *all* transactional guarantees. The name itself says it is weaker and poorer than ACID ("basic"), and it has three properties instead of four. Each of them states how far you accept to lower data quality.

- **Basic availability:** the system always answers *something* to every request. The answer may be right or wrong, temporary or final, or just a message, but the system is running. "Basic" means that at least a basic answer is always provided.
- **Soft state:** data is still modelled as a state machine that moves from state to state, but nothing is guaranteed about those states. In ACID, by contrast, states are always consistent.

## Eventual Consistency Is Good for the System, Bad for the User

**Reference:** SMBUD-05-nosql.pdf p.42

The professor called eventual consistency a very controversial property:

- "Eventual" gives no time bound. It could be milliseconds, seconds or days.
- Saying consistency is guaranteed *in the future* means it is *not* guaranteed now, so **users must expect wrong answers**.
- A user who read inconsistent data keeps that wrong answer. They are not told when the data is later corrected, and nothing fixes that.
- So the property is fine from the system's point of view ("I will fix things later") but negative from the user's point of view.

In answer to a student's question, he said a BASE-compliant system **is guaranteed to converge**. In theory that could take a hundred years, but real systems typically converge within **a few seconds, or a few minutes at most**. A system that is not even BASE-compliant might never converge.

## When Stale Data Is Acceptable: E-commerce and Booking Examples

**Reference:** SMBUD-05-nosql.pdf p.41–42

- **Obsolete product page:** you see an outdated product description and a stock count higher than what the company really has. You receive the product as it actually is and return it if you are unhappy. The stock count is corrected shortly afterwards. This is a "non-dangerous" inconsistency.
- **"Last item available" that was already sold:** at Amazon the reordering process is so fast that the item is available again within hours, so you get it anyway. For a hotel room there is no replacement, so you go through a rebooking process.
- In all these cases, the one who pays for the wrong data is typically the **user**.

## Where Inconsistency Actually Comes From: Replica Delays

**Reference:** None (not in slides)

- All of this only happens when something **malfunctions**. In a fully working system none of it occurs.
- The usual cause is not a transaction that is inconsistent in itself. It is that the **copies of the data spread across the network are not yet aligned**, because of network or server delays.
- Distribution mechanisms add delays: replication, realignment, and rebalancing (for example, moving data because one server is too full). "The typical inconsistency problem is a delay problem."
- The system keeps a log of the executed steps, so it can redo them and guarantee that delayed operations are executed sooner or later. That "sooner or later" is the "eventual" in eventual consistency.
- Example: you access the system from Italy, and the servers closest to Italy are not yet aligned with servers in Alaska that hold the latest version. For a few minutes, anyone asking at that moment sees the wrong value.
- He said caching (covered later) can add further delays and inconsistencies.

## Why Relational Vendors Did Not Adapt to Big Data

**Reference:** SMBUD-05-nosql.pdf p.44

The slide lists "consolidated, integration platform, ACID". When the big data wave arrived about 20 years ago, the professor gave these market reasons:

- Relational vendors were **monopolists**, and a monopolist's interest is to keep the market as it is.
- Vendors such as Oracle and IBM had invested many years of work in huge, complex systems, so giving that investment up was not convenient.
- They probably did not see how important the change in requirements was.

These unmet requirements opened a space in the market that new players filled. That is where the NoSQL "revolution" started.

## Database History Before and After the Relational Era

**Reference:** SMBUD-05-nosql.pdf p.47

- The relational model was invented in 1970, became popular from the end of the 1970s, and was a **monopoly until about 2000**. For about 30 years, buying a database basically meant buying a relational one. Lotus Domino was a real exception.
- **Before the 1970s**, databases existed but were not relational. The best-known kind is the **hierarchical database**, which IBM built specifically for NASA to store project data on missiles and space missions such as going to the Moon.
- From 2000, the explosion of the web and of data started the non-relational revolution. Between 2000 and 2010 most of the new technologies appeared, and graph databases (Neo4j, 2000) came first.

## "NoSQL" Is Ambiguous: Which Meaning the Course Uses

**Reference:** SMBUD-05-nosql.pdf p.47, p.54

The professor listed the possible readings:

- **Literally "no SQL":** a system that does not implement SQL. This is Strozzi's 1998 meaning: a *relational* database without SQL.
- **Non-relational:** the database does not store data in tables or use the relational model. This is the most typical meaning and **the one adopted in the course**.
- **"Not only SQL":** systems that do implement SQL, but not only SQL.
- **"NewSQL":** a new way of using SQL that is not on relational data.

Be careful, because people mean different things by the term.

## NoSQL Is a Negative Definition: Use Family Names (Plus Two Extra Families in This Course)

**Reference:** SMBUD-05-nosql.pdf p.50–52

- Defining something by negation ("everything that is not relational") is never a good idea. NoSQL is not one type of database. It covers many types that can be totally different from each other, so use the proper technical family names.
- The four traditional families are **key-value**, **columnar / BigTable**, **document**, and **graph**.
- The course will also cover two more families that are not traditionally under the NoSQL label but are non-relational and very important today:
  - **IR-based databases** (information retrieval, i.e. search-engine / search-based databases);
  - **vector databases**, which come from machine learning and AI use.
- For each family the course will discuss the **data model, query language, architecture, and one example product**.

## NoSQL Adds a Design Decision: Data Type → Family → Product

**Reference:** None (not in slides)

Before NoSQL, designing a database meant building a relational one, and the only choice was the vendor (Oracle, Microsoft, open source, …). Now the first question is **what type of data you have**. That decides which database family to use, and only then do you pick a product within the family. The professor said that a key point of the course will be the **pros and cons of each family and when to use which**.

## What the List of NoSQL Originators Tells You

**Reference:** SMBUD-05-nosql.pdf p.53

- The originators (Google, LinkedIn, Facebook, Twitter, Netflix, CERN, and Amazon, which the professor said should also be on the slide) are **data companies**: social networks, search engines, mobile and web. They should have been the *customers* of database vendors. They could not buy anything that fit their needs, so they had to build it internally.
- Oracle, IBM, Microsoft and SAP are **missing**. Like typical incumbents or monopolists, they did not see the opportunity, or they protected the market they already had.
- **Competitors collaborated** (for example, Facebook and Twitter on Cassandra). They did it to split costs and to get the best possible product, since none of them planned to sell it. Databases were not part of their business model.
- Most of these systems were released as **open source**: roughly 90–95% of the technologies in the NoSQL space. This was a big market change compared with commercial databases costing millions of dollars.
- In the course's exercise sessions, students will use free cloud accounts for convenience, but the open-source versions can be downloaded for free.

## Why Start With Graph Databases

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.1–3

The families are quite independent of each other, so there is no strict order. The professor starts with graph databases because they are a very intuitive way into the non-relational world, and because graph databases were historically the first family to appear. Note that "graph" here means graph theory, not graphics or pictures.

## Real-World Applications of Graphs

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.5–6

- Problems like the travelling salesman problem and map colouring look trivial but have hard answers.
- Industrial examples given in class:
  - electronic component design;
  - **GPS navigation**, where crossroads are the nodes and roads are the arcs;
  - enterprise management tools for scheduling, planning and resource management;
  - **robotics**, where movement/decision and vision models are typically built as graphs;
  - the **web** and **social networks**, which are graphs themselves.
- The point is that such data should be **stored as a graph**, because putting it in tables is not the natural way to solve these problems.

## From Graph Theory to Databases: Attaching Data to Nodes and Arcs

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.16, p.25

- A pure graph has no data anywhere. The first step is adding **weights to arcs**, for example a distance or a duration.
- Example from the right-hand graph on p.16, with weights read as minutes: going from 2 to 5 directly costs 5. Going through node 1 costs 2 + 1 = 3, so it is faster.
- If you can attach numbers to arcs, you can also attach text and values to arcs and to nodes. Nodes and arcs then become structural elements that carry values, which is what turns a graph into a database.
- He asked students to remember the **subgraph** concept, because it is needed later for querying (see pattern matching below).

## Graph Implementations, Matrix Symmetry, and Why Not Build Your Own at Scale

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.27–30

- A graph is an abstract data type, and one ADT can be implemented in many ways. Examples: two vectors (one of nodes, one of arcs), an incidence matrix (edges × nodes), or an adjacency matrix (nodes × nodes).
- For an **undirected** graph, the adjacency matrix is **symmetric with respect to the main diagonal**, because if you can go from 1 to 2 you can also go from 2 to 1.
- The real problem is **efficiency at scale**. The Facebook social graph has about 3 billion users, so its adjacency matrix would be 3 billion × 3 billion. It cannot fit in memory, and searching it is a challenge.
- At billions of nodes you would need to be very smart to build an efficient implementation yourself, so you use a graph database instead.
- In answer to a student's question: there are smarter ways to store such matrices (for example, sparse-matrix approaches), but graph databases take a different route.

## When to Use a Graph DB, and Why Relational DBs Handle Relationships Badly

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.34–40

- **When to use a graph DB:** when there are many relationships and most of the value of the data lies in the **connections** between objects. If every object is self-standing, a graph makes no sense.
- **Why relational DBs are bad at relationships:** the table is the problem. Connections between objects cut across tables, so they need many **join operations**, or even dedicated tables just to represent the connections (foreign keys or intermediate tables).
- **Sailor/boat example:** to say "a sailor reserves a boat" you need three tables. The reservation table has its own primary key plus two foreign keys pointing to the other two tables, and answering "who rents what" takes two joins. A database expert finds this natural, but a non-computer-scientist would find it crazy.
- In a graph you simply say "person rents boat, full stop". It works like a mind map, so it is **more intuitive, closer to reality, and more efficient** for connections.

## Graph DBs Are Schemaless: Freedom (or Chaos)

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.42–43, p.46

- Graph databases are the first example of a schemaless database in the course. In the drawing a sailor is "just a bubble": there is no table with typed columns, and you do not declare the shape of nodes or arcs in advance.
- You can create, remove or modify any node, arc or property at any time, and keep evolving the shape of the graph.
- Each node and arc has its own properties, independent of all the others.
- In the professor's words: "total freedom, or total chaos if you are a bit crazy in the design." The practical warning about this is in the last note.

## Querying by Pattern Matching

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.41

- With no tables or fixed columns, you cannot write SELECT … FROM … WHERE, because there is no table to read from. Queries are written as **pattern matching** instead.
- A pattern is a predefined shape that you search for in a structure. This is a general technique: you can, for example, search a set of images for a striped pattern.
- In a graph DB the **query is itself a piece of graph**, a subgraph. Picture it as a lens moving over the whole database graph (the "facts"). Every place where the lens finds the same shape is returned as an answer (a query match). Shapes that do not match are not answers.
- Example: the pattern "person connected to boat connected to city" returns every (person, boat, city) triple connected that way. You can add further conditions to the pattern.

## Where the Efficiency of Graph Queries Really Comes From

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.35 (index-free adjacency)

A student asked why pattern matching should be cheaper, given that there are no tables and you would in principle scan the whole database. The professor's answer:

- An implementation does not scan everything. For the person–boat–city query it **starts only from nodes that are people, boats or cities** and ignores the rest. That only matches the efficiency you get with tables.
- The **real advantage is in navigating connections**:
  - In a relational DB, following a connection is a join, i.e. matching objects across tables by equality. Even with indexes, it is still a join.
  - In a graph DB, an arc works conceptually like a **pointer in memory**: a direct one-to-one link to the target object, with no join and no path to follow. This makes it enormously faster.
- He said it may not be implemented exactly like that, but that is the concept. Relationship types can restrict the navigation further.

## Neo4j: Origins, the Java Choice, and the Matrix References

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.45

- Neo4j is the main reference implementation of graph databases and one of the first NoSQL systems (about 25 years old). It was not built by a large corporation but by a startup, Neo Technologies, founded specifically to build it in Silicon Valley.
- It was released as open source from the start.
- **"4j" stands for Java.** Writing a database in Java looks strange, since databases are built for efficiency and Java is not. Around 2000, though, Java was the emerging open alternative to C and assembly, and the founders wanted to make a statement about openness.
- **"Neo"** is the hero of *The Matrix*, who aims to break the matrix, here meaning the relational table. **Cypher**, the query language, is another character from the film.

## Neo4j's Position: ACID, Native Graph Storage, Query Engine First

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.46–48

- Neo4j is schema-free. On the CAP choice it **sticks to consistency**: it is an ACID transactional database whose data is always consistent. So in principle you can use it for business applications that need perfectly correct data.
- It is efficient at searching for nodes and patterns.
- It was originally **not** a graph-analysis or statistical tool, for example not a social-media analytics tool. Over the following 20 years it added statistical, machine learning and LLM-based models, but its core component is the **query engine**.
- It uses **native graph storage**. It is not a graph view built on hidden tables: it saves nodes and arcs directly and queries them directly.
- It also supports indexes to speed up some operations. These were to be covered later.

## Cypher: Proprietary Origin, Declarative, and an "ASCII-Art" Notation

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.50–51, p.59–61

- Cypher started as a **proprietary** language for Neo4j and later became part of a broader standardization effort.
- It is designed for nodes and edges rather than tables.
- Like SQL, it is **declarative**: you state *which* data you want, and the system decides the algorithm to find it. Its syntax resembles SQL plus graph notation.
- **Why a textual notation:** you cannot store or query actual drawings, so Cypher writes the picture as text, like ASCII art. The notation imitates the shapes:
  - `( )` for a node (the bubble);
  - `-->`, `<--`, or `--` (no direction) for connections;
  - `[ ]` to name or describe a relationship;
  - `{ }` for attributes;
  - `:` as the separator that introduces the type/label. The professor said "semicolon", but the slides use a colon.
- In `CREATE (Neo:Crew {name:'Neo'})`, the parentheses mean a node is being created, `Crew` is what you would informally call its type, and `{name:'Neo'}` is an attribute. Attributes are completely free: there is no rule that all `Crew` nodes must have the same attributes.

## Aliases in Cypher Are Temporary, and the Slide Snippet Would Fail

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.51

- **The leading `Neo` in `(Neo:Crew …)` is not data.** It is a temporary alias, as in relational queries, and it is only used to refer back to the object later in the same operation (for example, to connect it to another node). It is lost when the operation ends.
- To find the node again later, you must store suitable attributes, such as an ID or a unique name, and query on those values (for example, "find all crew members with name Neo").
- If you only create the node, the alias can be omitted: `CREATE (:Crew {name:'Neo'})`.
- **Correction to the slide:** `(Neo)-[:KNOWS]->(Morpheus)` as shown would give an **error**, because `Morpheus` is never defined. Every reference must be defined first, for example by also creating Morpheus in the same command before connecting the two nodes.

## Why Neo4j Calls Them "Labels", Not Types

**Reference:** SMBUD-06-graphDB-neo4j.pdf p.49, p.52

The professor gave two reasons why `:Crew` is a **label** and not a node type:

1. In computer science a data type implies rules and structural constraints on the data. A label enforces no shape at all.
2. A node can have **several labels**. `CREATE (n:Actor:Director {name:'Clint Eastwood'})` is returned both when you search for actors and when you search for directors. Objects normally do not have two data types or classes.

Labels work like tags or categories: they are purely descriptive, and you can create a new one at any time without any prior declaration.

## The Price of Flexibility: Keeping the Graph Tidy Is Your Job

**Reference:** None (not in slides)

The professor ended with a warning. If every new node gets different attributes, labels and structure, you will no longer be able to find your data. Relational tables forced you to put data in the right place. In a schemaless graph DB it is **up to you** to use the flexibility carefully and keep the data tidy and well designed, "otherwise you'll get lost".
