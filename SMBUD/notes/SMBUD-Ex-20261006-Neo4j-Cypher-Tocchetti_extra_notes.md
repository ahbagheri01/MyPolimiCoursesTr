# SMBUD-Ex-20261006-Neo4j-Cypher-Tocchetti — Additional Professor Notes

**Transcripts:** Andrea Tocchetti's Personal Room-20261006 1603-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j Sandbox Setup Guide.pdf

> **Coverage notes:** The session covered the Cypher introduction, ER-to-Neo4j mapping, distance, shortest path, `WITH` and the fast/exhaustive shortest-path slides. The Movies exercise slides (p.19–24) and the recommendation queries (p.39–40) were not worked through; the TA left them as homework and planned a hands-on session next time.

## Reading Cypher Syntax: Parentheses, Braces, Labels vs Types, Temporary Variables

**Reference:** E02 - Neo4j.pdf, p.3–5

- Cypher is "visual": round brackets are always nodes, curly brackets are always properties, everywhere in the language. Wording: nodes have **labels**, relationships have a **type**.
- The variable before the label (`ee` in `(ee:Person …)`) is a **temporary name** that exists only within that one query. It is not stored in Neo4j, and the next query can call the same node anything.
- Inside one query you cannot give the same temporary name to two different nodes (as with variables in code). In `CREATE (e:Person {name:"Mark"}), (a:Person {name:"Mike"})` you either use two different names or none at all.
- A label is the colon plus the name, written together. A node can have several labels (e.g. both cat and pet), whereas in a relational DB a table represents one type. A `Person:Fisherman` node is returned when you filter for `Person` and also when you filter for `Fisherman`.
- `from` is highlighted as a reserved keyword in the editor, but inside curly brackets Cypher reads it as a property name.

## Schema-less Nodes: Lists, Missing Attributes, One Workspace

**Reference:** E02 - Neo4j.pdf, p.5; E02 - Neo4j Sandbox Setup Guide.pdf, p.3–4

- Creating several nodes in one `CREATE` is the equivalent of a multi-row `INSERT INTO` in SQL.
- Property values can be lists (Francis is `from: ["Sweden","UK"]`). A relational DB cannot do this unless you store the list as a string.
- Neo4j is not strongly typed: within the same DB, nodes can have any labels or none, and any set of attributes. The first nodes have `name`, `from` and `klout` (a score from the Neo4j tutorial), while others have only `name`. In a relational table, a missing attribute must be set to NULL. Here you just leave it out.
- An empty node (`(a)` or even `()`) can be created, but it is pointless.
- Add `RETURN` after a `CREATE` to check that the operation succeeded. Use dot notation (`a.name`) for properties of both nodes and relationships.
- The free/community deployment has a **single workspace**, so everything you create goes into the same place. Before starting a new project, delete the old data. Otherwise your queries can give strange results.

## How to Reason About a MATCH Query (the Skill Needed for the Exam)

**Reference:** E02 - Neo4j.pdf, p.6

- Read a query as a pipeline. (1) `MATCH (ee:Person)` scans the whole DB and builds the set of nodes that fit the pattern. (2) `WHERE` filters that set. (3) `RETURN` outputs the surviving nodes (shown as label + attributes) or just some of their attributes. The TA said that learning this step-by-step reasoning is what you need "to do good at the exam" and in any Neo4j query. What matters is how the query shapes the data as it runs, not how it is written.
- Board example (Q&A): A, B and C are `Person` and D is `Dog`. We want people with white hair, and C has no hair-colour attribute at all. D is dropped by the label in `MATCH`, and C (plus anyone with a different colour) is dropped by `WHERE`. "Filtered out" applies only to this query: the nodes are **not** removed from the database. (The colours on the board were stated inconsistently in the recording.)
- The real DBMS applies optimizations (e.g. it applies the name filter first instead of scanning all nodes), but the outcome is the same as with the naive explanation.
- With practice you don't need to build every intermediate set. You can read a whole pattern line at once, e.g. "a person who knows a person who knows a surfer".

## MATCH (a:Person),(b:Person) Builds Two Independent Sets, Then CREATE Links Every Surviving Pair

**Reference:** E02 - Neo4j.pdf, p.7, p.32

- With only Mark and Mike in the DB, after `MATCH (a:Person),(b:Person)` and before `WHERE` there are **four** node bindings: set A = {Mark, Mike} and set B = {Mark, Mike}. Each pattern part searches the whole graph on its own.
- `WHERE a.name='Mike' AND b.name='Mark'` keeps only Mike in A and only Mark in B. The names stay bound until the end of the query (it runs as a pipeline), and `CREATE (a)-[r:KNOWS]->(b)` creates a relationship between **every** surviving node in A and **every** surviving node in B. Here that is one relationship.
- Without the `WHERE`, the same query would create **four** KNOWS relationships, one for each A–B combination. Understand what you write instead of just writing it.
- Student question: is `MATCH` a Cartesian product? The TA answered no: `MATCH` builds sets from the pattern. If the pattern itself held conditions on values, it would find Mike and Mark directly. Equality conditions can be moved from `WHERE` into the `MATCH` pattern. (Note: slide p.32 shows this same query among those that can raise warnings, e.g. for Cartesian products.)

## No Bidirectional Relationships; Duplicate Same-Type Relationships Duplicate Results

**Reference:** E02 - Neo4j.pdf, p.8

- One relationship cannot be given both directions, because Neo4j does not support bidirectionality. If you need A→B and B→A, create two separate relationships. The TA warned that how `MATCH` behaves when the direction is **omitted** is one of the trickier things to understand (see the Emil example below).
- Creating `KNOWS {since: 2015}` does not overwrite the existing `KNOWS`; it adds a second one. So a query matching all pairs connected by `KNOWS` returns Mike–Mark **twice**.
- Every node and relationship has a **hidden unique ID**. You cannot access it, and using it directly is pointless, but it is how Neo4j keeps nodes and relationships with identical names and values from being merged. `DISTINCT` also relies on it.

## Why DETACH Is Needed: No Dangling Relationships

**Reference:** E02 - Neo4j.pdf, p.9–11

- A relationship must always connect two nodes, so Neo4j cannot contain dangling relationships. A plain `DELETE` of a node that still has any relationship therefore **fails**. The `DELETE` of Ben on p.10 works only if Ben has no relationships.
- Example: Mark has relationships with Stefan and Ellie. `MATCH (m:Person {name:'Mark'}) DETACH DELETE m` (1) finds Mark, (2) removes all of his relationships, both **incoming and outgoing**, and (3) deletes the node.
- The `MATCH` part can be any filter, e.g. "all people with at least two friends", followed by `DETACH DELETE`.
- Deleting a relationship (p.11) never needs `DETACH`, because you are not removing a node. In `MATCH (n {name:'Ben'})-[r:KNOWS]->() DELETE r`, `n` has no label, so it matches anything named Ben (person, dog…). The end node has no name or constraint because we don't care what Ben is connected to, only that the relationship exists.

## Pattern Matching Method and the Effect of Omitting Direction (Emil's Friends)

**Reference:** E02 - Neo4j.pdf, p.12

- Method: know your data, draw small examples, then think about which pattern must be matched (or built). The TA's analogy is Lego: the database is the yellow blocks and the pattern is a red block that you try to fit onto them.
- Example graph: Emil `KNOWS` Francis and Rick. Mark is also a Person, apparently linked by a different relationship, not `KNOWS` (the recording is unclear here). With the optimization, Neo4j starts from Emil only (filtering early avoids lots of computation on big DBs), follows `KNOWS`, and returns (Emil, Francis) and (Emil, Rick).
- Without the optimization, `ee` = all four Person nodes:
  - With a **directed** pattern `(ee)-[:KNOWS]->(friends)`, only pairs starting at the source node are found: (Emil, Francis) and (Emil, Rick).
  - With the **undirected** pattern on the slide, each relationship is found from both ends, so (Francis, Emil) and (Rick, Emil) are matched as well. They are discarded only because `WHERE` requires the first node to be Emil.
- Lesson: when you read or write a query, pay attention to direction. Leaving the direction out is itself a condition, and it changes what is matched.

## Johan's Surfer: Multiple Paths, Size of an Unfiltered Match, Knowing Your Data

**Reference:** E02 - Neo4j.pdf, p.13

- Board graph: Johan knows Mark, Andrew and Rick, who all know Sasha, the surfer. There are **three different paths** to the same surfer.
- Without filtering first, the bare undirected `MATCH` finds J‑M‑S, J‑A‑S and J‑R‑S, the reversed S‑M‑J, S‑A‑J and S‑R‑J, and many more triples, because "person knows someone who knows someone" is very generic. Students guessed 9, and the real number is higher. Applying the Johan filter first leaves only the first three paths. This is another reason the DBMS optimizes.
- The last node is not checked to be a `Person` because the TA *knows* this DB only contains people who know other people. With a DB you don't know, it is better to add more constraints. The same reasoning applies to `(bacon:Person {name:"Kevin Bacon"})` on p.25: `Person` instead of an actor label is enough, because there is only one Kevin Bacon and he is an actor.
- Student question (partly unclear in the recording): the pattern does not recurse. It looks exactly two `KNOWS` hops away, so a surfer further away is not found.
- Advice: reading a query correctly is only half the job. The other half is understanding what the exam asks and writing queries yourself. The best way to learn is to run the queries yourself at home.

## DISTINCT Works on the Whole Returned Tuple

**Reference:** E02 - Neo4j.pdf, p.13–14

- With the three Johan→?→Sasha paths, `RETURN surfer` gives S, S, S and `RETURN DISTINCT surfer` gives S once. Uniqueness is decided by the hidden node ID.
- `DISTINCT js, surfer` still gives **one** row, because it is the same (Johan, Sasha) pair three times.
- If you name the middle node `jf` (Johan's friend) and write `DISTINCT js, jf, surfer`, you get **three** rows, because each triple is different.
- So `DISTINCT` applies to the set of everything listed after it. Be aware of this, or you may get one result when you need all of them, or the reverse.

## Reading the PROFILE Plan of the Johan Query

**Reference:** E02 - Neo4j.pdf, p.15–16

- `NodeByLabelScan` finds all Person nodes, and `Filter` keeps only Johan (1 row). The first `Expand(All)` follows an unnamed `KNOWS` to an unnamed node (4 rows). The second `Expand(All)` reaches `surfer` (12 rows, i.e. 12 triples). The final `Filter` checks `hobby` and leaves 3 rows, then `Distinct` gives 1 row.
- Elements you leave unnamed get system-generated names (`anon_0`, `anon_1`, …).
- `not anon_0 = anon_2` checks that the second relationship is different from the first, so you cannot go Johan → Mark → back to Johan. The TA put it as "you cannot identify cycles" in Neo4j: the same relationship is not walked back within one pattern.
- Use `PROFILE` on your own queries to check that your mental model matches what the DBMS does. Your reasoning should be very close to the plan, even if it is not identical (e.g. the optimizations).

## ER Model → Neo4j: What the Exam Asks and How ISA Hierarchies Become Labels

**Reference:** E02 - Neo4j.pdf, p.17

- **Exam:** you are given an ER model and asked to produce a sample database (nodes and relationships) for some of its entities. You do not draw an ER-like schema. You show example nodes and how they connect.
- Entities become nodes that keep **all** their attributes and use the entity name as label.
- ISA with parent Pet and children Cat and Dog (the hierarchy itself is lost in the transformation; only the labels remain):
  - Total + exclusive: only children exist, and they inherit the parent's attributes and label: `:Pet:Cat`, `:Pet:Dog`.
  - Partial: plain `:Pet` nodes can also exist.
  - Total + overlapping: `:Pet:Cat`, `:Pet:Dog`, `:Pet:Cat:Dog`.
  - Partial + overlapping (the "worst case"): `:Pet`, `:Pet:Cat`, `:Pet:Dog`, `:Pet:Cat:Dog`. At the exam you would give these four example nodes, then link them to e.g. the owner and the vets.
- Relationships: respect cardinality. With 1:N, the graph should show one node connected to multiple nodes. N:N only means that e.g. two Pets and two Owners can be connected in any combination. No bridge nodes are needed.

## Variable-Length Patterns: Bound Syntax and Why DISTINCT Is Needed

**Reference:** E02 - Neo4j.pdf, p.25

- Distance is counted in relationships (hops). `[*1..4]` matches patterns from 2 nodes (1 relationship crossed) up to 5 nodes (4 relationships crossed).
- The bounds are optional, but the `*` is **always** required:
  - `[*]`: no limit.
  - `[*1..]`: only a lower bound.
  - `[*..4]`: only an upper bound.
- `DISTINCT` matters with distance because paths can split and then converge again on the same person, so the same node is reached several times.

## How to Read all(r IN relationships(p) WHERE …) — and Its Exam Status

**Reference:** E02 - Neo4j.pdf, p.27–28

- Read it as a for-loop. For each relationship in the shortest path's list, compute the boolean `r.role IS NOT NULL`. This gives an array of true/false, and `all()` checks that every entry is true. As soon as any crossed `ACTED_IN` has a null role, the path fails.
- This is one of the few cases where the filter is evaluated **while** the shortest path is computed, not after.
- The TA called this "the most complex stuff" in Neo4j and said it has **never been asked at the exam** ("maybe we'll start this year, I don't know").

## WITH as a "Stop Point" and Where Aggregation Is Allowed

**Reference:** E02 - Neo4j.pdf, p.29–31

- `WITH` is a stop point that carries what the first part computed into the second part. In `WITH person, count(*) AS movieCount`, the grouping keys are whatever comes **before** the aggregate. The (person, movie) pairs are grouped by person, and the remaining rows (the movies) are counted. After `WITH`, only `person` and `movieCount` exist, and `movie` is lost (as in SQL).
- The `*` in `count(*)` is a wildcard, like `SELECT *` in SQL. Do not confuse it with the `*` of variable-length paths.
- Aggregation can also go directly in `RETURN`, e.g. `MATCH (person)-[:ACTED_IN]->(movie) RETURN person, count(*) AS movieCount`.
- **Exam rule:** aggregate only in `WITH` or `RETURN`. Even if you find out that aggregations can be used in `WHERE` conditions, don't do it in the exam. The solutions are designed using only what was taught, so stick to that.
- `collect()` makes one list. `count(person.name)` returns the number of rows, while counting over `collect(person.name)` gives 1, because there is only one collection. `WITH n AS person` on p.31 only demonstrates renaming and is useless in that query (answer to a student question).

## Fast vs Exhaustive Shortest Path: Early Stopping, and Why WITH Can Lose the Result

**Reference:** E02 - Neo4j.pdf, p.33–38

- **Exam:** the TA described this as theory and said it is more likely to appear as a theory question than a practical one, because exercising it in practice is quite challenging.
- The only difference between the two algorithms is **early stopping**:
  - **Fast** (breadth-first): when the condition must hold for every node or relationship on the path (e.g. all nodes are `Person`), it stops expanding a branch the moment it hits a failing node, such as a Movie. Node 7 on p.34 is a Person named Kevin Bacon, but it is never reached because the path to it goes through a Movie.
  - **Exhaustive** (depth-first): with a condition like "at least one node is named Kevin Bacon", you cannot tell until you reach the end of the path. A branch through a Movie cannot be excluded a priori.
- `WHERE length(p) > 1` is evaluated while the shortest path is being searched. So if Kevin Bacon and Al Pacino were directly connected (length 1), that path is discarded and the search continues to find another, longer one.
- With `WITH p` between `MATCH` and `WHERE`, the `WITH` "hides whatever is below it from whatever is above it", so the planner sees no condition and just computes the shortest path with the fast algorithm. If that path has length 1, the later `WHERE` filters it out and the query returns **no paths**, even though a longer path exists.

## Relationship Arrows Can Point Right-to-Left

**Reference:** E02 - Neo4j.pdf, p.39

- In `(tom)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors)`, the first relationship goes left→right and the second goes right→left. Relationships do not have to be written left to right. The pattern links Tom to a movie `m` that his co-actors also acted in. The second pattern then extends from the co-actors to their own co-actors.
