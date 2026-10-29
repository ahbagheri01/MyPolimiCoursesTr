# SMBUD-Ex-20261008-Neo4j-Introduction — Additional Professor Notes

**Transcripts:** Neo4J_introduction_Ettori_08-10-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j Sandbox Setup Guide.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

## When Graph Databases Fit, and Why You Must "Think in Graphs"

**Reference:** E02 - Neo4j.pdf p.2; SMBUD-06-graphDB-neo4j.pdf p.37

- The TA said graph databases are widely used in the real world, for example in banking systems, fraud detection and cryptocurrencies. The rule he gave: use them when the relationships matter as much as the nodes, or more.
- Mindset warning: with SQL you reasoned in tables. To understand Cypher queries you have to imagine yourself inside the graph, following nodes and arrows. "Otherwise, you're not going to get it."

## Reading Cypher Visually: Bracket Types and Temporary Variables

**Reference:** E02 - Neo4j.pdf p.4–5, p.13

- Cypher was designed so the query looks like a graph, with dashes and arrows. The bracket type tells you what kind of object you are looking at: **round brackets = nodes**, **curly brackets = properties/attributes**, **square brackets = relationships**.
- A variable such as `ee` in `(ee:Person …)` is only a temporary name for the current query and is forgotten when the query ends. The label (`Person`) is the node's type.
- You can count the round brackets to know how many nodes the pattern matches. `(js)-[:KNOWS]-()-[:KNOWS]-(surfer)` has three, so it matches only paths of exactly three nodes (Johan, an intermediate person, the surfer). The TA said to picture placing the pattern on the graph: it counts only where it fits exactly. So a surfer who is a *direct* friend of Johan is not matched. For other lengths you add more brackets or use the `*` variable-length syntax.

## Neo4j's Flexibility Compared With the ER Model

**Reference:** E02 - Neo4j.pdf p.5, p.8

- A node can have **any number of labels** (e.g. `Person:Student:Teenager`). In the ER model an entity's type is fixed.
- **Attributes can be arrays**, e.g. `from: ["Sweden","UK"]`. The TA stressed this cannot be done in the ER model.
- Relationship attributes are optional: you can create one `KNOWS` without attributes and another with `since: 2015`, and add attributes later.
- `CREATE (a)` (no label, no properties) is legal, but the TA called it useless because there is then no way to find that node again. Neo4j lets you do almost anything, so you have to keep track of what you created.

## Why CREATE Is Usually Followed by RETURN

**Reference:** E02 - Neo4j.pdf p.5, p.7

`CREATE (a {name:'Andy'}) RETURN a.name` looks pointless, but in practice you insert thousands or millions of nodes at once and need to see whether it worked. Neo4j is permissive and accepts almost anything, so you return the result to check what actually happened. For the same reason, relationship creation ends with `RETURN type(r)`.

## MATCH … WHERE as Cypher's SELECT … WHERE

**Reference:** E02 - Neo4j.pdf p.6–7; SMBUD-06-graphDB-neo4j.pdf p.41, p.58

- The TA said every Neo4j query is pattern matching on the graph. `MATCH … WHERE` plays the role of SQL's `SELECT … WHERE`. There is no `FROM`, because the graph itself is the "from". He recommended following this match-then-filter structure.
- Student question: can the filter go inside the pattern, e.g. `(a:Person {name:'Mike'})`, instead of in `WHERE`? Yes, it is equivalent. The TA said this is what is usually done and is usually better (also faster). He used `WHERE` on the slides only because it is clearer step by step.

## MATCH Returns Sets: An Unfiltered CREATE Builds Every Combination

**Reference:** E02 - Neo4j.pdf p.7

`MATCH (a:Person), (b:Person)` does not bind one node each: `a` and `b` are each the **set** of all matching nodes. With only Mark and Mike in the graph and no `WHERE`, `CREATE (a)-[:KNOWS]->(b)` creates relationships for every combination, i.e. **four**: Mark→Mark, Mark→Mike, Mike→Mike, Mike→Mark. When creating relationships, always filter down to exactly the pair you want. Otherwise you silently create far more relationships than intended.

## DELETE: Why DETACH Exists and What an Unconditioned Delete Does

**Reference:** E02 - Neo4j.pdf p.9–10; E02 - Neo4j Sandbox Setup Guide.pdf p.3–4

- In Neo4j you **cannot delete a node that still has relationships**; plain `DELETE` gives an error. `DETACH` works like a confirmation that you really want it gone: it removes all of the node's relationships and then the node.
- Class question: what does `MATCH (n) DETACH DELETE n` delete? **Everything**. There is no condition and every node matches `(n)`, so all nodes and relationships are removed. The TA said this is normally not a query you want to run; usually you restrict it (e.g. `(n:Person {name:'Ben'})`).

## Deleting Relationships: The Arrow Decides What Is Removed

**Reference:** E02 - Neo4j.pdf p.11; SMBUD-06-graphDB-neo4j.pdf p.60

`MATCH (n {name:'Ben'})-[r:KNOWS]->() DELETE r` (class question) deletes **all** `KNOWS` relationships going *out* of Ben, not just one. The target node `()` has no label and no properties, so any target is accepted. If the arrow is replaced by a plain dash (`-[r:KNOWS]-`), the pattern accepts both directions, so both outgoing and incoming `KNOWS` relationships of Ben are deleted. In general, a dash instead of an arrow matches much more.

## Unlabeled Variables Match Any Node Type: When to Add the Label

**Reference:** E02 - Neo4j.pdf p.12, p.19, p.25, p.30, p.39

- In the Emil query, `(ee:Person)-[:KNOWS]-(friends)` is undirected, so it returns both the people Emil knows and the people who know Emil. `friends` has no label. That is fine only while the graph contains just `Person` nodes. If it also had, say, animals and buildings, you would have to write `(friends:Person)`.
- In the movie graph, the unlabeled `(hollywood)` in the Kevin Bacon query returns both movies and actors. Now that there are several node types "the label really makes a difference": to get only actors you must add the label.
- In `(person:Person)-[:ACTED_IN]->(movie)`, `movie` is just a name, not a type constraint (class discussion). In this dataset only movies have incoming `ACTED_IN`, so only movies match. In general, other nodes could match. The TA's example: if dogs also acted in movies and you dropped `:Person`, dogs would be returned too. In the recommendation query, `m` could be a cartoon.
- His advice: if you are not sure, enforce the label (e.g. `m:Movie`). The slides use as few constraints as possible, but "if in the exam or in the exercise you are more specific, it's just better for you", because it is not an error and avoids mistakes.

## Returning the Anchor Node Repeats It Once per Match

**Reference:** E02 - Neo4j.pdf p.12

In `… WHERE ee.name = "Emil" RETURN ee, friends`, `ee` is not one node. MATCH stores one entry for every matched pair (Emil–Mike, Emil–Mark, …). With five friends, `friends` holds five nodes and `ee` holds **Emil five times**. Returning `ee` is therefore pointless, because its content is predictable. (The TA set aside the case of several distinct people named Emil.)

## Friend-of-a-Friend Surfer: Why DISTINCT and What the Query Does Not Enforce

**Reference:** E02 - Neo4j.pdf p.13–14

- Finding "a friend who can introduce Johan to a surfer" is usually hard in other query languages, but in Cypher it is one line. This is the kind of hop-by-hop relationship query Neo4j is built for.
- DISTINCT is needed because a surfer with many friends can be reached through several intermediate people. If the surfer has three friends who know Johan, `COUNT(surfer)` gives **3** but `COUNT(DISTINCT surfer)` gives **1**: it is the same node found through three paths.
- Student question: the query does **not** check that the surfer is a *new* friend. If Johan already knows the surfer directly, nothing excludes that result. The query only assumes it.

## Cycles: Avoided Automatically Inside One Pattern, Not Across Several

**Reference:** None (not in slides)

- The TA stated that within a single MATCH pattern Neo4j automatically discards cycles. If Johan is a surfer, the pattern will not go Johan → friend → back to Johan and return Johan as his own surfer friend.
- When the pattern is split across several matches (several pattern lines), Neo4j no longer checks this, and the same node can be matched again (e.g. Tom Hanks showing up as his own co-co-actor). In that case you must exclude it yourself in `WHERE` (see the recommendation query below).

## PROFILE: How to Read the Plan and Why the TA Recommends It

**Reference:** E02 - Neo4j.pdf p.15–16; SMBUD-06-graphDB-neo4j.pdf p.65

- `PROFILE` does not change the query or its result. It shows, as a flowchart, what Cypher does under the hood and how many rows flow between steps. The TA strongly advised using it, calling it the best way to learn to "reason like Cypher". He suggested running the recommendation queries with it in particular.
- Reading the surfer plan:
  - The `Filter js.name = $autostring_0` step comes right after the `Person` label scan. Neo4j saw the later `WHERE` and checks the name while it searches the pattern, instead of collecting all candidate nodes and filtering at the end, which is much more efficient. You cannot see this optimization from the query text.
  - `$autostring_…` is simply the string literal from the query.
  - `anon_…` ("anonymized") names are given to nodes and relationships that you left without a variable.

## ER-to-Neo4j Mapping: ISA Hierarchies and N:N Relationships

**Reference:** E02 - Neo4j.pdf p.17

- Entities (ER rectangles) become nodes. Relationships stay relationships ("Neo4j was built for relationships").
- Overlapping ISA: since a node can have several labels, someone who is both a student and a worker becomes one node labeled `:Student:Worker`. For an exclusive hierarchy the TA said multiple labels are not needed, and that "you don't even need the parent node in that case". This remark is brief and partly unclear in the recording, and the slide describes parent entities becoming nodes, so treat it with caution.
- N:N relationships need an extra table in SQL and, he anticipated, are complicated in MongoDB (covered in later weeks). In Neo4j they need no special treatment because a node can have any number of incoming and outgoing arrows.

## Variable-Length Patterns: Bounds and the Risk of Explosion

**Reference:** E02 - Neo4j.pdf p.25; SMBUD-06-graphDB-neo4j.pdf p.61, p.65

- The alternative to `[*1..4]` would be four separate matches (1, 2, 3 and 4 hops), which the TA called very ugly.
- Bound semantics he gave: only `*` = any number of hops, no limit. Only a minimum = it goes as far as it can find. Without a maximum the query may "explode", because Neo4j tries all paths of any length and their number can be exponential in the graph. So it is better to always give a maximum.

## DISTINCT Is Not a Shortest-Path Operator

**Reference:** E02 - Neo4j.pdf p.25–26

Student question: does `RETURN DISTINCT` give the shortest path? No. `hollywood` is the set of all nodes reachable within four hops, and DISTINCT only removes duplicates from that set. For example, Kevin Bacon may reach Robert De Niro in two hops through two films, and again in four hops through other films going the other way. DISTINCT keeps De Niro once but says nothing about which path or length was the shortest. For that you use the `shortestPath` function.

## Direction in shortestPath and Variable-Length Patterns

**Reference:** E02 - Neo4j.pdf p.25–27

The Bacon→Meg Ryan pattern uses plain dashes, so the path may cross relationships in either direction. With arrows, the hops must all follow the arrow direction and cannot go backwards. Arrows can also be put on variable-length patterns. The TA said you usually do not put arrows when looking for a shortest path, but you should remember that relationships can be traversed both ways and that this matters for some queries.

## all(), any(), IN and relationships(p): How the Path Predicate Works

**Reference:** E02 - Neo4j.pdf p.27–28

- `[:ACTED_IN*]` lets the path cross any number of relationships, but only `ACTED_IN` ones, in either direction.
- `all(r IN relationships(p) WHERE r.role IS NOT NULL)` is built in three steps:
  1. `relationships(p)` gives the list of relationships in the path.
  2. `IN` iterates over that list, "like in Python".
  3. The inner `WHERE` turns each relationship into a Boolean. With four relationships you get an array of four true/false values.
- `all()` is a **logical AND** over that Boolean array: true only if every element is true. The TA also mentioned **`any()`**, the **logical OR** (true if at least one element is true).
- Why the check is needed: the role attribute is not mandatory, so some `ACTED_IN` relationships may lack it. The query therefore enforces two conditions in two places: "only ACTED_IN" in the pattern, and "role not null" in the WHERE.
- `all`/`any` are typically used on paths such as shortest paths, where you have lists of nodes or relationships.

## WITH: GROUP BY Analogue, Free Clause Order, and the Visibility Barrier

**Reference:** E02 - Neo4j.pdf p.29–31; SMBUD-06-graphDB-neo4j.pdf p.59

- The TA compared `WITH` to SQL's `GROUP BY`. It is the place to aggregate (count, max, min, …), often together with `ORDER BY` and `LIMIT`.
- Unlike SQL, Cypher has no fixed clause order. You can write `MATCH`, `WHERE`, `MATCH` again, `WHERE` again, and so on, and `WHERE` can appear both before and after a `WITH` (answer to a student question).
- The one hard constraint: `WITH` is a barrier. Variables not listed in it are invisible afterwards. The TA said a frequent mistake is using, after the `WITH`, a variable that was bound in the `MATCH` but not passed through. Put everything you will need later into the `WITH`.

## Choosing Grouping Keys in WITH; Aliases; collect()

**Reference:** E02 - Neo4j.pdf p.30–31

- In `WITH person, count(*) AS movieCount`, `count(*)` counts everything associated with each person, i.e. their movies. An alias is usually optional, but it is **mandatory here** because `movieCount` is filtered in the following `WHERE`. After this `WITH`, `movie` is no longer available.
- Class question: what does `WITH person, movie, count(*)` count? Each (person, movie) pair, so the count is essentially always 1. The TA said it could only be higher if the same person had more than one acting relationship to the same movie, e.g. multiple roles, which is rare. The grouping keys you list in `WITH` decide what is counted.
- `collect()` changes only the output format. Instead of a table with one name per row (as shown in the Neo4j app), you get a single list/array of strings.

## Why the Fast Shortest-Path Search Can Prune Some Conditions but Not Path Length

**Reference:** E02 - Neo4j.pdf p.33–37

- With a condition like "all nodes on the path must be `Person`", the breadth-first search expands node by node. As soon as it reaches a `Movie` node it **cuts that branch**, even if the target lies beyond it. Likewise, a relationship with a null role can be discarded the moment it is traversed.
- A condition like `length(p) > 1` cannot be checked during the search. While searching, Neo4j does not know how long the path will end up (it would have to keep a count of hops, which this search does not do). It must complete a path and only then count its length, which is why the exhaustive algorithm is planned.

## The WITH p Trick: Hiding a Predicate Changes Both Speed and Meaning

**Reference:** E02 - Neo4j.pdf p.37–38

- Why adding `WITH p` before `WHERE length(p) > 1` removes the exhaustive fallback: `WITH` is a barrier, so when Neo4j plans `shortestPath` it cannot "look down" at the condition below. It believes there is no condition at all and happily uses the fast algorithm.
- Consequence: suppose the true shortest path has length 1 and a valid path of length 2 (or 5) exists.
  - **Without** `WITH`, Neo4j sees the condition, skips the length-1 path and returns the length-2 one.
  - **With** `WITH`, it returns the length-1 path, the later `WHERE` discards it, and the query returns **nothing**, even though a valid longer path exists.
- So `WITH` changes the question. Without it: "find the shortest path whose length is > 1" (the shortest *with respect to the condition*). With it: "give me the shortest path, but only if its length is > 1".
- The TA said this is sometimes done on purpose: hide an expensive condition behind `WITH` to force the fast algorithm, and accept that a result may not be found even if it exists. It is a speed-versus-exhaustiveness trade-off.

## Recommendation Query: Direction, Self-Matches and "Hidden" WHERE Conditions

**Reference:** E02 - Neo4j.pdf p.39

- The arrows matter here: `-[:ACTED_IN]->(m)<-[:ACTED_IN]-` is the only correct form, because it forces both people to have acted in the *same* movie. A bidirectional pattern would be wrong.
- Only variables you reuse need names: `tom` is named because it is filtered later, while the `ACTED_IN` relationships stay anonymous because any one will do.
- Because the co-actor step and the co-co-actor step are two separate matches, Tom Hanks himself can come back as a "co-co-actor" (three hops and back to the start), and Neo4j does not prevent it. Hence `tom <> cocoActors` (`<>` is Cypher's not-equal). `WHERE NOT (tom)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors)` also shows that patterns can be used inside `WHERE`, not only in `MATCH`.
- Warning: these conditions are not stated in the question. You have to work them out yourself from the cycles your pattern can create. The TA said students typically forget them. The query still runs, but returns extra, wrong results (Tom Hanks recommended to himself).

## Aggregating in RETURN Without WITH

**Reference:** E02 - Neo4j.pdf p.39

`RETURN cocoActors.name AS Recommended, count(*) AS Strength` aggregates without a `WITH`, which the TA had said was the only way to aggregate. Aggregating directly in `RETURN` is the one exception. It is fine when you do not need to filter on the aggregate, because `RETURN` is the last clause and nothing can follow it. If you need to filter (e.g. `> 1`), you must use `WITH`. `Strength` measures how many times the co-co-actor was reached through Tom Hanks's co-actors, i.e. how strong the collaboration is.

## Tom Hanks → Tom Cruise: Why No Cycle Check Is Needed, and m vs m2

**Reference:** E02 - Neo4j.pdf p.40

- Class question: why is there no anti-cycle `WHERE` here? Both ends are fixed by different names (Tom Hanks and Tom Cruise), so the end cannot loop back to the start.
- Returning `tom, m, coActors, m2, cruise` is more than needed (`coActors` alone answers the question). Returning everything shows how each path was built.
- Student question: different variable names (`m`, `m2`) do **not** force different nodes, so `m` and `m2` can be the same film, e.g. if the co-actor was in one film with both Toms. To forbid that, add `WHERE m <> m2`. (This exchange is partly garbled in the recording.)

## Expected Level of Detail in Exercise/Exam Queries

**Reference:** E02 - Neo4j.pdf p.39–40

Asked how far edge cases must be handled, the TA said the graph has endless edge cases and loops. The queries shown, which exclude the obvious loop (e.g. Tom Hanks ≠ co-co-actor) but not every possible one, are "usually the right level of complexity" and "what we expect" from students. Where the slide leaves an assumption implicit, you may state it.
