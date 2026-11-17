# SMBUD08-20261022-DocumentDB-MongoDB — Additional Professor Notes

**Transcripts:** SMBUD08-Marco Brambilla PoliMi-20261022 1607-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-07-document-db.pdf

> **Coverage notes:** The lecture covers SMBUD-07 from the CRUD slides (p.29) to the sharding strategies (p.46–50), after a short recap of the data model. Several topics the professor explained (projection, dot notation, array conditions, `$elemMatch`, `$unwind`, the car-crash examples) have no slide in the mapped deck. He said the projection was missing from the slides and that the `$unwind` material would also be given and repeated in the practical sessions. Indexes, map-reduce and the CAP slide were not discussed.

## No Query Language: You Query MongoDB Through a Library in Your Own Language

**Reference:** SMBUD-07-document-db.pdf, p.29

- Unlike SQL or Cypher, document databases have no dedicated declarative query language. The database is an external system, but you interact with it by writing code in your own programming language (Python, Java, C, Scala…) through an API, that is, a library of functions. In Python this library is **PyMongo**.
- The API covers the standard **CRUD** operations (create, read, update, delete), which any data API provides. It has tens of functions. The lecture showed only the basic ones; for the rest, see the documentation.
- First step in any language: import the library and connect, which gives you a database object (called `db` in the examples). Everything is then done on this object.
- `createCollection` needs only a name, since a collection is just an empty container. The options are optional and let you limit the amount of data or number of documents, or set where the collection is located.

## Insert: Object-Oriented Calls That Take the JSON Document Directly

**Reference:** SMBUD-07-document-db.pdf, p.29

- Everything is object-oriented: to add a student you call `db.students.insert(...)`, so the insertion applies directly to the collection named in the code. A document can only be added inside one collection.
- The parameter is the JSON document itself, written with its curly brackets inside the function's round parentheses. This shows the compatibility between objects and documents: what you pass is a map/object in the programming language and is exactly equivalent to the document that gets saved. More complex documents (sub-documents, arrays) are passed the same way.
- Variants such as `insertOne` and `insertMany` (seen in the practical session) are only different syntax for inserting one or many documents.

## Find Conditions Are a Template Document, Not Predicates

**Reference:** SMBUD-07-document-db.pdf, p.30

- Read operations also work on **one collection at a time**: `db.<collection>.find(...)` searches only inside that collection. `find()` with no parameter returns the whole collection content.
- The condition is passed *in the shape of a document*. `gender: "female"` is not an equality test: it defines an attribute of a document. The system uses this document as a **template** and returns the documents compatible with it, which is pattern matching, similar to what Neo4j does on graphs.
- This is why you cannot write `age <= 20`: it would not be valid document syntax. The "trick" is to make the value a sub-document with a special attribute name starting with `$`: `age: {$lte: 20}`. The professor called this solution "not really nice" and "quite annoying", since writing a normal comparison would be easier. The other operators (`$eq`, `$gt`, `$ne`, `$in`, `$or`…) are the same kind of syntax to remember.

## Why MongoDB Keeps Even Conditions in JSON Shape

**Reference:** None (not in slides)

The professor asked the class why the designers insisted on document shape for conditions instead of accepting a condition string. The answer is that everything ends up being JSON, so there is only **one syntax**. About 90–95% of web APIs and third-party services talk JSON: you send a request and get back a JSON answer. Being able to send a query that is itself a piece of JSON text to an API, and get JSON back, makes everything homogeneous: it is just serialized text in the request and in the answer. The cost is that JSON must be parsed, but on the web data always travels as text anyway.

## Find Returns Whole Main Documents (findOne Picks an Arbitrary One)

**Reference:** None (not in slides)

- The output of `find` is always the **entire main document**, not its sub-documents, even when the conditions are on atomic attributes, arrays or sub-elements. The result is in effect a sub-collection of the documents that match.
- `findOne` returns only one matching document, and you cannot know which one: if 20 match, you get one of them. The professor explained that this is a way to make things fast, because the system returns the first one it catches.

## Projection: The Second Parameter of find Shapes the Output

**Reference:** None (not in slides)

The professor said he forgot to put this in the slides; it is shown in the practice sessions. A document may have 50 or 100 attributes plus sub-documents, and you may need only, say, the student ID and last name. `find` takes two parameters:
- the **condition document** (the pattern to look for);
- the **output specification**, which reduces or changes the shape of the output.

A plain list of attribute names would not be JSON, so the trick is to give each wanted attribute the value `1` (think "true, I want it"); `0` means not wanted, but you normally just leave those out. For example: `find({...}, {student_id: 1, last_name: 1})`.

## Conditions on Sub-Documents Use Dot Notation

**Reference:** None (not in slides)

- To put a condition inside a sub-document, use the object-oriented **dot notation**. Example: students with an expired credit card, where `credit_card` is a sub-document with `number`, `expiration`, …: `"credit_card.expiration": 2025`, here combined with an "age below 20" condition. Several conditions in the same document are in AND.
- A student asked whether nesting curly brackets (a sub-document inside the condition) would also work. The professor said he had never seen it used and did not think it works, but would check; people use the dot notation.

## Array Conditions Apply Independently to Elements: The Citroën Trap

**Reference:** None (not in slides)

- Example: a New York car-crash collection with one document per crash and an array of sub-documents for the other vehicles involved (each with year, maker, model…). Query: find crashes where the vehicles have production year < 1995 and model Citroën.
- The two conditions are still in AND, but **not on the same array element**. The query finds crashes that contain *a* car older than 1995 *and* *a* Citroën. A crash with a 1993 car and a 2010 Citroën matches.
- Correct reading: return the main documents whose array contains at least one element satisfying the first condition and at least one element satisfying the second condition.
- The professor called this misleading and "a typical error" that many people make. If you are asked for crashes involving a Fiat Panda from 2020, you cannot write it this way, or you will also get any crash with a Fiat Panda plus some other car from 2020.

## Use `$elemMatch` to Force All Conditions onto the Same Array Element

**Reference:** None (not in slides)

To require that all the conditions hold on the **same** element of the array (e.g. only crashes with a Citroën older than 1995), apply the `$elemMatch` operator to the array attribute. Then at least one element must satisfy all the conditions together. Without it, the conditions are ANDed but each is checked independently on any element.

## Searching Inside Arrays Still Returns Documents, Not Array Elements

**Reference:** None (not in slides)

Another common misunderstanding: even when your conditions are on array elements, `find` is not an array search and does not return the matching elements. It returns the whole documents that contain them, or only the attributes chosen with the second parameter. The granularity is always the document.

## `$unwind`: One New Document per Array Element

**Reference:** None (not in slides)

- To work at the granularity of array elements you must change the query: call `aggregate` instead of `find`, with `{$unwind: "$other_vehicles_involved"}`.
- For each element of the array, `$unwind` creates a separate, independent document. The array attribute becomes a single-valued attribute holding that one element, and all the other attributes (e.g. the main crashed vehicle) are copied as they are. A document whose array has three sub-documents becomes three documents.
- Asked why the function is `aggregate`: this is not finding things but reshaping documents. Here it is actually a *disaggregation*, but the function is called `aggregate`.
- The professor said these slides would be given and covered in the practical session as well, and that he repeated it in theory because people make mistakes here.

## Why Operators and Field Paths Get a `$` Prefix

**Reference:** SMBUD-07-document-db.pdf, p.33

- Operators (`$unwind`, `$elemMatch`, `$lte`, `$group`, `$max`…) start with `$` so that they are parsed as keywords to interpret. Otherwise `unwind` could simply be the name of an attribute.
- In `$unwind` and `$group`, the **attribute name** also gets a `$` (e.g. `"$crash_date"`). There it is not just a name whose value is taken: it is a path to be explored and operated on (looped over, aggregated), so it must be interpreted too.
- Whenever you run functions over attributes, prefix them with `$`. If you forget, you get an error and it does not work.

## `$group`: The Output Document Shape, with `_id` as the Grouping Key

**Reference:** SMBUD-07-document-db.pdf, p.33

- Example: 1,000 car crashes over 5 days, grouped by date. In SQL: `SELECT date, COUNT(...) FROM crashes GROUP BY date`. Group-by is a general operation over a collection's documents and has nothing to do with sub-attributes.
- In `db.crashes.aggregate({$group: {...}})`, the content of `$group` describes the **shape of the document produced for each group**. The output is one document per group (5 documents for 5 days).
- Each output document must have an `_id`. Setting `_id: "$crash_date"` *means* "group by crash date": if each output's ID is the date, then each output is the group of that day. To group by car brand or anything else, put that attribute there.
- The other fields hold the aggregates (max, min, average, count, as in SQL). The professor's example was the maximum number of persons killed per day: a field whose value is `{$max: "$<persons killed attribute>"}` (field names approximate).

## Documents Missing an Attribute Do Not Match

**Reference:** None (not in slides)

- A student asked what happens when an attribute used in a condition is missing from a document. The document is simply not returned. This holds for simple conditions (a student with no `age` is not returned by an age condition), array conditions (a vehicle element with no model is not considered) and grouping.
- This matters because documents can have different shapes. Typically, if a value is null you do not write `age: null`; you just leave the attribute out.
- So read every condition as "the attribute exists **and** satisfies the condition", e.g. "age exists and is more than 20".

## Queries Are Pipelines of Chained Calls

**Reference:** SMBUD-07-document-db.pdf, p.31, p.33

- The `object.object.function.function` syntax is no accident: it is a **pipeline**. You start from the database, go into the collection, then into the search operation, and the output of each step flows into the next one, like a pipe.
- You can make the pipeline as long as you like, e.g. `find(...).sort(...)`: sort is ORDER BY applied to the output of the find. The same applies to `distinct`. Multi-step pipelines can transform data until the final output.
- Asked whether you can apply a find over a find: yes, but it is usually not done, because it becomes very hard to debug and understand. Writing the condition in a single `find` is usually enough.

## Joins and Transactions Exist but Signal a Design Problem

**Reference:** SMBUD-07-document-db.pdf, p.14

The "no joins, no transactions" principle still holds: you should always be able to write read or write operations on individual documents. MongoDB does have functions for joins and transactions, but they are much slower and not advisable. If you start needing joins, links between documents, or multi-step transactions, you probably did not design your documents properly, since they are meant to be self-standing.

## Update: Non-Matching Documents Are Skipped, `$set` Can Add New Attributes

**Reference:** SMBUD-07-document-db.pdf, p.35

- `update` takes two parameters: the selection criteria (a pattern) and the update rule. Example: students named Gwen get `$set: {age: 20}`.
- A student with **no name** is not affected, because pattern matching cannot match a missing attribute.
- A matched student with **no age** gets a new `age` attribute set to 20. So `$set` is also how you **change the shape** of a document. Even if no student in the collection has an age, adding it only to the matching ones is fine, because the collection is agnostic and enforces no structure.
- `save` does almost the same thing but replaces the whole document instead of modifying it. The professor said it is "not so useful".

## updateOne vs updateMany

**Reference:** None (not in slides)

`updateMany` updates every document that matches the condition. `updateOne` updates only one, and which one is non-deterministic: you cannot control it. The same holds for `findOne`.

## Dropping a Non-Empty Collection or Database Is Usually Blocked

**Reference:** SMBUD-07-document-db.pdf, p.36

According to the professor, it depends on the deployment, but usually you cannot delete a collection or a database that is not empty. The system first checks that it is empty. This is a safety net against deleting a full database by mistake. `remove` deletes every document matching the pattern you pass.

## MongoDB Is the Most Important NoSQL Technology to Master

**Reference:** None (not in slides)

- The professor said that all models matter, but this one is **more important**. Document databases, and JSON-based representations in particular, are by far the most adopted NoSQL implementation at the moment, so "make sure you are pretty good at managing this kind of data".
- Two exercise sessions on MongoDB have been scheduled, with plenty of examples and exercises on the language.

## History and Positioning: CouchDB First, MongoDB the Most Adopted

**Reference:** SMBUD-07-document-db.pdf, p.2, p.9

- MongoDB was not the first document database. The first ones were **CouchDB** (the logo with a guy on a couch) and **Couchbase**. The "couch" name came from the idea that these technologies should be very comfortable for software developers: "you can program on the couch".
- MongoDB became so well accepted that it is by far the most adopted document database, which is why the course uses it. It is open source, developed by the MongoDB company, which also sells cloud-based services.
- It is extremely well implemented and scalable, from very small use cases to huge data problems. You can install the free open-source version on your machine easily, with few resources, or deploy it on a cloud cluster over hundreds of servers in parallel.

## mongod Alone Is Enough Locally; mongos Is Only for Distributed Deployments

**Reference:** SMBUD-07-document-db.pdf, p.37, p.45

- `mongod` is the database server: the process you switch on to run a database. It receives and executes queries and manages storage. For a local database, that is all you need.
- For a distributed, scalable deployment (cloud, cluster, multiple servers) you also need `mongos`, where the "s" stands for sharding.
- A small deployment with little data, e.g. installed on your own machine, needs no sharding. This configurability is part of what the professor meant by MongoDB being flexible.

## Sharding = Horizontal Partitioning That Never Breaks a Document

**Reference:** SMBUD-07-document-db.pdf, p.3

- Sharding is almost a synonym of **horizontal partitioning**, applied with modern technology so that it is more convenient, practical and efficient.
- On a table, horizontal partitioning cuts the table horizontally and puts each slice on a different server. For documents (discussed with the class), it means splitting the *set of documents*, placing some on one server and some on another.
- It is still called "horizontal" because it does the same thing: just as a row is never broken into pieces, **a document is never split**. Both a row and a document are an instance. Breaking documents would make no sense, since they were built big on purpose to keep things together; splitting them would only do damage.

## Request Flow: mongos Router, Config Server, mongod Shards

**Reference:** SMBUD-07-document-db.pdf, p.41–42

- The `mongos` is in practice a **router**. A query arrives at `mongos`, which looks up where the needed data is and forwards the request to the right shard (shard = partition). The `mongod` there runs the query and sends the data back to `mongos`, which returns the results.
- If the needed data is in several shards, the request is sent to all of them, and the results are collected, combined and returned.
- `mongos` knows where the data is thanks to the **configuration server**, a third component that stores all the metadata: indexes, pointers, records and the tracking of where the data is.
- Data is grouped into chunks. When shards get too full, the system automatically deploys a new one and starts filling it, or migrates some data to it to free space on the others and rebalance.

## Replica Sets: Default Three Copies, Requests Load-Balanced Across Them

**Reference:** SMBUD-07-document-db.pdf, p.43

- For each shard you choose either a single copy (one `mongod`) or a **replica set**, a bundle of copies of the same data. The default is **three copies**, physically in different locations to avoid damage.
- Full path of a request: application (via library/drivers) → `mongos` router → config server lookup → right shard → one of its copies.
- The system also does load balancing: if one copy is already getting many requests, new ones are sent to a less loaded copy. In principle all the copies are equal, so which one serves the request does not matter.

## Sharding Strategies: Why Range Sharding Can Unbalance, and When to Use Hash or Tag

**Reference:** SMBUD-07-document-db.pdf, p.44, p.46–50

- **Auto-sharding:** you delegate everything to the database ("I don't care, just deal with the splitting"). No effort from the developer. You are transparent with respect to distribution both when querying and when placing data.
- **Range sharding:** you choose a shard key (e.g. device ID) and set static rules, e.g. IDs 0–1000 on one shard, 1000–3000 on another, the rest on a third. The risk: you cannot know how the data will evolve, so fixed ranges can unbalance the system, leaving one shard almost empty and another very full or overloaded with requests.
- **Hash sharding** fixes this. You still choose the key (ID, year, date, brand, country…), but placement follows a hash function. Even if the data is very unevenly distributed over the key's range, the hash output tends to be uniform, so coverage across shards is much more likely to be even.
- **Tag sharding** is typically used on categorical attributes such as countries or provinces. A typical motivation is legal: customers' personal data must stay in the customer's country.

## First Mid-Term Test (5 November) Covers Only Neo4j

**Reference:** None (not in slides)

Answering a question at the very end, the professor said the topic of the test on 5 November is only Neo4j.
