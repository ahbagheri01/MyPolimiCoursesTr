# SMBUD06-20261013-GraphDB-Wrapup-DocumentDB — Additional Professor Notes

**Transcripts:** SMBUD06-Marco Brambilla PoliMi-20261013 1405-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-07-document-db.pdf

> **Coverage notes:** The lecture covers only the end of SMBUD-06 (stored procedures, architecture, p.45–48 and p.62) and SMBUD-07 up to the JSON/BSON slides (about p.7–23). The query language, architecture and sharding were left for the next lecture. The professor mentioned APOC examples and a Memgraph slide, but neither appears in the mapped version of SMBUD-06.

## Intermediate Tests: In Presence, On a Computer, Pass/Fail for One Point Each

- There is one test per topic (Neo4j, then the next topics). You must be present to take one; remote participation is not possible. Each test is taken on a computer, normally your own.
- The date of each test is announced one week in advance, and there is at least one week between the end of a topic in class and its test.
- Grading: you can reach 30 with the standard final exam alone (theory + practice). Each test adds up to 1 point, so up to 3 extra points in total. Tests are optional and independent, so you can take 1, 2 or 3 of them. Each is graded pass/no pass, giving exactly 1 or 0 points with nothing in between. They are meant for students who attend the classes, but this is not enforced.
- Students who only have Linux devices should borrow a laptop if they can. Otherwise the course will organise an in-presence session in a classroom with Polimi computers for the tests, quizzes and exams.

## Recordings Are Released Only When a Topic Is Finished

Recordings are not published lecture by lecture. When a topic ends (here, Neo4j after Thursday's exercise session), all lecture and exercise-session recordings for that topic are released together, this lecture included.

## Stored Procedures and the APOC Library Are Not Exam Material

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.62

- "Stored" means you write your own functions (in Java or other languages) and import them into the database platform. From then on you can use them in your queries by invoking them with the `CALL` operator directly inside Cypher.
- Libraries of this kind already exist. **APOC** provides functions and procedures for basic data processing in Neo4j: import/export of data, algorithms for data management, a little graph analysis ("not huge") and data transformations.
- **Exam:** the professor said this part will not be in the tests or the exam. You should still know it exists, because it adds a lot of expressive power in practice.

## Why Neo4j's Native Graph Storage Must Run in Main Memory

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.47

Neo4j stores the graph natively, with no tables or other storage model underneath. Moving from a node to its neighbours follows direct adjacencies, and that is only efficient if the graph is in **main memory**, so most of the database's processing has to run there. The JVM is the top layer of the figure because Neo4j is written in Java.

## Record Files Separate the Graph's Topology from Its Values

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.47

The separate record files (nodes, relationships, relationship types, properties) are a deliberate split:
- **Topology:** nodes and relationships describe the shape of the graph. Pattern matching runs on this part.
- **Values:** the informative data (text, numbers…) is attached as properties of nodes and relationships, and is stored separately.

## Multi-Layer Caching: Queries Should Never Run on the Files

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.47

- Ideally a query never touches the files. The data is loaded into a multi-layer cache that uses both the operating system's file-system cache and the JVM's object cache, so that the graph is kept as objects in memory. Users and applications send their requests to the Neo4j API, and the queries run on these in-memory objects.
- If the graph is too big to fit in memory, the query runs on the part that is cached. When data is missing, the system fetches it from disk into memory and then finishes the query.

## Transaction Log and Transaction Management Give Neo4j Full ACID

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.46–47

Neo4j is fully ACID-transactional, and two components in the architecture provide this:
- **Transaction log:** every action is written to the log *before* it is executed, so it can be retrieved and re-run.
- **Transaction management layer:** guarantees the transactional properties every time a transaction is executed.

## Other Graph Databases (Memgraph) and Why Graph Systems Are In-Memory

**Reference:** None (not in slides)

Graph databases are a family of products, and Neo4j is only one of them. Memgraph is a well-known alternative, again a main-memory system. In the professor's words, "you can't do anything good on disk with graphs": files are sequential, but graphs have a topology. Memgraph-like systems are typically used for graph data analytics and for streaming graph evolution. They are not covered in the course.

## Preview: Temporal Graphs in the Exercise Session

**Reference:** None (not in slides)

The exercise session wraps up Neo4j and gives a quick introduction to **temporal graphs**: how a graph evolves over time and how to analyse that evolution. Examples are a social network or a financial system changing over time. The professor called this an important current trend, crucial for optimisation, recommendation and advertising.

## How to Prepare Neo4j/Cypher for the Exam, and the Expected Query Complexity

- The key skill is being able to solve questions on the data. Do the exercises, the hands-on sessions and past exams. Build the solutions yourself instead of only reading the provided ones, because "it's a different thing".
- **Expected complexity:** roughly the level of the queries seen in class and in the exercise sessions. That means simple queries, aggregations, multi-level or combined queries, and at most about two aggregations combined.

## Document Databases Are the Dual of Graph Databases

**Reference:** SMBUD-07-document-db.pdf, p.7

- Use a graph database when the value lies in the **topology and relationships** between objects. Use a document database when the value lies in **complex, self-standing single objects**.
- The professor called this "basically the opposite" use case. Ideally a document has no dependencies on other documents and can be used on its own. Users are expected to work on one object at a time, even if that object is very complex.

## Business Objects vs Relational Granularity: Why Document DBs Were Born

**Reference:** SMBUD-07-document-db.pdf, p.7 (order figure)

- People doing everyday business (invoices, orders, product management, customer management) work with **business objects** such as an invoice, an order, a product sheet or a customer profile. These are much coarser and more complex than the items in relational tables.
- A realistic relational database has many fine-grained tables (orders, customers, credit cards, payment methods, addresses…). To rebuild a single order (ID, customer, order lines with products, quantities and prices, payment, shipment, discounts) you must join data from many tables, sometimes tens of them.
- So the scale at which people *use* data and the scale at which it is *stored* do not match. This also hurts performance: every time you print an order, a complex multi-join query runs again. The idea behind document databases is to store the data natively in the shape in which it is used most of the time.

## What "Document" Means Here: The Sheet in the Drawer

- "Document" does *not* mean Microsoft Office files or similar. It means a complex, structured, multi-level item that is self-standing and comprehensive. If you are handed the full order document, you have everything you need to work on it.
- Analogy from pre-computer offices: an employee opens a drawer and pulls out a sheet of paper, such as the order, the customer sheet, the product sheet or the invoice. That sheet is the document.

## Why Not Just Use Relational Views?

**Reference:** None (not in slides)

Student question: can't we keep relational data and build views at the business-object level? The professor said this is exactly the trick relational databases used: materialised or virtual views over the limited single tables. But the data is still not *stored* in that shape. Through indexes or materialisation you are still working, indirectly, on the original tables. Document databases instead store the data from the start in the shape people expect to use.

## Collections Are Neutral Containers, Like Folders

**Reference:** SMBUD-07-document-db.pdf, p.13, p.18

- You create collections the way you create tables in a relational DB, but a collection is an agnostic container of documents, almost like a folder in a file system. Its meaning comes entirely from you.
- Every document belongs to exactly one collection. Technically you could build a whole database with a single collection holding clients, products and invoices together. The professor said this is possible at implementation level but clashes with good design and is "typically not a good idea".

## JSON Documents: Plain Text, No Declared Types

**Reference:** SMBUD-07-document-db.pdf, p.16, p.19

- About 99% of document databases use a JSON-like format. A JSON file is just a human-readable text file that you could open with Notepad.
- You never declare data types: the system infers them. Nothing has to match a schema defined in advance. At any time you can create a document with a new list of attributes, or decide that an attribute has many values instead of one.

## The `_id` Rule: Why It Exists, Fixed Name, Auto-Generated

**Reference:** SMBUD-07-document-db.pdf, p.19–20

- The one fixed rule (every document has a unique identifier) exists *because* of all this flexibility: without it you might end up unable to tell items apart.
- The name is fixed: it is always `_id`, and you cannot choose another name.
- The example on p.19 has no `_id` because you do not have to write it. If you omit it, the system generates a unique ID for you.

## Sub-Documents: When to Create Them, How Deep, and Why They Have No `_id`

**Reference:** SMBUD-07-document-db.pdf, p.20

- Create a sub-document when a group of fields has value by itself. For example, rather than keeping `phone` and `email` as separate first-level properties, you group them into a `contact`.
- You can nest to any depth in principle, but in practice you typically never go beyond about four levels. Deeper than that, the structure becomes too complex to manage and impractical to use.
- Sub-documents are not self-standing documents, only pieces of the main document. That is why they have no `_id`: only the main document is technically identified.

## In-Class Exercise: Writing the Order Figure as JSON

**Reference:** SMBUD-07-document-db.pdf, p.7 (order figure)

How to write the order business object as JSON:
- The order itself is one document with its own ID and a customer field.
- **Line items** need square brackets *first*, because the three lines are three values of the same property (an array). Each element is then a sub-document in curly brackets: `line_items: [ {product_id, quantity, price}, {…}, {…} ]`.
- **Payment details** is a single object, so it becomes one sub-document: `payment_details: {card, number, expiration}`.

## Design Decisions: Shape the Document for the Users' Everyday Work

**Reference:** SMBUD-07-document-db.pdf, p.23

- The JSON above is the result of design decisions, and there is no fixed solution. Should the credit card be inside the order at all? Should it be a sub-document, or first-level attributes (which would also work)? Should shipment details be added?
- The guiding principle is different from relational design: **keep in the document what users need in their everyday job**, so that whoever works on the order finds everything in one place. Design from the user's perspective.
- **Majority usage:** design for the most likely way the data will be used. If 90% of uses fit this shape, accept that the remaining 5–10% are not optimal. Trying to make everyone happy means "no one happy". The professor called this "maximality of usage probability".

## The Impedance Mismatch Problem, Explained

**Reference:** SMBUD-07-document-db.pdf, p.7, p.10

- The mismatch between relational databases and object-oriented languages (Java, Python, C++, Scala…) is both **logical** and **technical**:
  - **Logical:** relational data is tables and rows, while OO code deals with classes and objects. Objects are closer to business objects than to relational items.
  - **Technical:** you need something to bind the two worlds, either an ORM (object-relational mapping) or hand-written code. By hand, you connect, send the query and get back a result set, then write a loop that reads one row at a time and copies it into objects.
- Documents are the same concept as objects (assuming you have the class). A JSON document can be read directly into an object in Java, JavaScript or another language, and an object can be saved straight to JSON. This saves programmers all the transformation, assignment and loop code.

## References Between Documents Are Just Foreign Keys

**Reference:** SMBUD-07-document-db.pdf, p.21

Using another document's `_id` as an attribute value is exactly the foreign-key trick from relational databases. The ObjectId is just a string of characters (long and unreadable), so you copy it into the other document and the link exists. The professor pointed out that such a reference goes in one direction only, from the document that holds the ID to the referenced one.

## Embedding vs Referencing: Trade-offs from the Class Discussion

**Reference:** SMBUD-07-document-db.pdf, p.20–21, p.23

- The embedded design (contact and access inside the user) and the referenced design (three separate documents linked by IDs) hold the same information.
- Points raised by students and confirmed by the professor:
  - With embedding, the same values get copied into many documents, so keeping them aligned on updates is hard.
  - Embedding creates deeper levels. The professor said this is usually not a problem, because the whole document is read as one block and kept in memory.
  - If a piece of data makes sense by itself, make it an independent document. If it makes no sense without the main document, make it a sub-document.
  - Referencing brings back the problems of relational databases: "we are rebuilding the relational model".
- **Duplication example:** if credit card data is embedded in orders, it is copied into every order where that card was used, so changing the card means fixing every copy. A relational DB keeps one credit-card table with each card stored once, because relational schemas are always normalised. Document databases typically contain a lot of duplication.
- A student suggested storing both the ID and the copied data. The professor answered that you still need a system that fixes the values everywhere, so the consistency problem of multiple copies remains. Document databases deliberately choose comprehensive documents over *reuse* of data: data is copied wherever it is needed instead of being reused.

## Schemaless, Yet Rigid: Relational Is Domain-Driven, Documents Are Use-Case-Driven

**Reference:** SMBUD-07-document-db.pdf, p.22–23

- A paradox raised in class: document databases are schemaless, yet a finished embedded document is very *constrained*. It is a fixed combination of data built for one use case. A relational or referenced model is more flexible, because the pieces are kept separate and can be recombined in any way.
- **Relational design** starts from the *domain*, not the queries. The schema should describe your whole world as generally as possible, so that any future query (joining these tables today, other tables tomorrow) can be written.
- **Document design** fixes, once and for all, one particular selection and combination of that schema: a main entity plus some others embedded as sub-documents. You cannot really design a document without knowing how it will be used, whereas you can design a relational schema knowing only what information must be represented.
- Embedding is therefore a strategic bet: one combination of information is favoured over the others, in the hope that a large majority of users need exactly that shape.
- Efficiency is a *side effect*. The primary criterion is logical: the shape a user would ideally want for their everyday work. Relational is the ideal model for describing the whole domain, but not necessarily the best for any one use case. A document should be the best for a specific use case.

## Bottom Line: Embed; Heavy Referencing Means You Want a Relational DB

References are not wrong in themselves, but they go against the philosophy of document databases:
- If you keep splitting things into referenced pieces, you end up rebuilding the relational model. You also lose the pillar of self-standing, comprehensive documents.
- If your application needs the full domain with separate, independent entities, stay with a relational database.
- If a large share of use cases fit a fixed document shape, use a document DB and typically embed sub-documents, accepting the resulting data duplication.

## Performance: No Simple Benchmark, Fast Only for "Read One Whole Document" Workloads

**Reference:** SMBUD-07-document-db.pdf, p.11

- Asked about benchmarks, the professor said a general speed-up figure cannot be given. There are too many variables: slightly different document designs perform differently, and performance depends on which query or set of queries you measure. Comparing performance across database families is also very hard, because their architectural choices differ.
- General rule: document databases work efficiently when you are sure that about 95% of the time you will read one document at a time, in full.
- They work poorly if half the time users need only one sub-document, or another part, or need to merge data from several documents. The model is best for "a solid monolithic use case" over one document shape.
- New use cases later can be served by designing new documents, since everything is flexible. But each document you design is expected to serve a large share of users.

## Schemaless Means You Are Responsible for Keeping Order

**Reference:** SMBUD-07-document-db.pdf, p.14

- In a schemaless store, documents follow no rules or constraints. You can add or delete attributes, or create a similar document with different attributes or sub-documents. As with graph DBs, this is "probably one of the most schemaless approaches possible", because every document is independent.
- Student question: isn't consistency harder? The professor agreed: you can make a mess. As with any schemaless approach, *you* are in charge of preserving the proper shape and management of the data. Otherwise the data becomes chaotic and unusable in the future.

## MongoDB as the Reference Document Database

**Reference:** SMBUD-07-document-db.pdf, p.9

When people talk about document databases, they mean MongoDB about 90% of the time. It was one of the first document databases and is still among the most adopted, so it is the reference implementation. Like Neo4j, it was developed by a Silicon Valley startup. It stores JSON natively.

## Data Locality and Caching: Why the Document Unit Is Fast

**Reference:** SMBUD-07-document-db.pdf, p.11

- **Locality:** in a relational DB the information for one request is spread around and must be gathered with multiple reads. A document already contains everything the use case needs, so one request returns it. The document is the aggregated unit of data retrieval.
- **Caching:** whole recently used documents are kept in memory. Because a document is an atomic unit, a request finds all of it in memory and gets it immediately.
- **Architecture** (details in the next lecture): MongoDB scales horizontally very well, up to hundreds of servers working in parallel, and it supports replication well.

## "No Schema, No Transactions, No Joins" Is a Design Philosophy, Not a Technical Spec

**Reference:** SMBUD-07-document-db.pdf, p.14

- The professor said the "Facts" slide should be read philosophically, not as a technical specification. These systems should *aim* at not needing transactions or joins.
- The reasoning follows schema-on-read: you design the document shape around how users read it, with all the needed information inside. Then you don't need joins with other documents, or transactions spanning several documents, because users work on one document at a time.
- Example: an order-management application loads the order document, reads or edits it, and saves it without referencing other items.
- That atomic, single-document use is where everything is extremely efficient. Outside it, "things start collapsing". Some relationships will be needed sooner or later, but you should aim for applications that work on one document at a time.

## Why JSON Is Inefficient for Storage, and What BSON Changes in Practice

**Reference:** SMBUD-07-document-db.pdf, p.15, p.17

- **Drawback of JSON:** being text makes it easy for humans to read, but it is not binary. It must be parsed one character at a time, and it takes more space and more time to write and read, because every character has its own encoding. Text is probably the least efficient way to store data.
- So JSON is the **exchange format**, and storage uses BSON, the binary version.
- **In practice:** you will never look at BSON. Everything you send to and receive from the database is JSON. As a programmer you can essentially ignore BSON and just know that the internal storage format is slightly different.

## Quoting Field Names in JSON (and a Slide Typography Caveat)

**Reference:** SMBUD-07-document-db.pdf, p.8, p.16

- Field names may be written in quotes, because a name is also a string or label. Quotes are especially useful when a name contains special characters that might not be recognised. For simple names like `name` you can leave them out.
- **Slide caveat:** the curly typographic quotes (“ ”) on the slides come from PowerPoint's automatic reformatting. In real code use the normal programming double quote `"`.

## Why JSON Is Textual: It Was Born for the Web

**Reference:** None (not in slides)

Every database stores data in binary, so why did document databases adopt a text format? JSON stands for **JavaScript Object Notation** and was invented for the web, not for databases. The web had HTML for page structure, CSS for graphics and JavaScript for programming, but nothing for the data in web pages, and JSON filled that gap. It is textual because everything on the web is textual. It is object-oriented because it is simply the serialisation of JavaScript objects. Since it already suited web and OO developers well, it was then reused for storing data in databases. The professor said some aspects of MongoDB programming still reflect this link with the web, to be shown in the next lecture.
