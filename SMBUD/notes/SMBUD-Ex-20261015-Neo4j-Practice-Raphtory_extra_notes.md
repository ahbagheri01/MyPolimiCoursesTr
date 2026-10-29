# SMBUD-Ex-20261015-Neo4j-Practice-Raphtory — Additional Professor Notes

**Transcripts:** Neo4J_practice_and_raphtory_Ettori_15-10-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j Exercises.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 Extra - Introduction to Raphtory.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j.pdf

> **Coverage notes:** This was a hands-on session. The Cypher theory slides were not presented again (the TA said they had been shown in the previous session). Exercises solved or discussed in class: Q1–Q5, Q8, Q11 (briefly, in Italian), Q12, Q15, Q18 and Q39. The last ~20 minutes covered the Raphtory slides.

## Neo4j Exercises Like These Are What the Exam Asks

**Reference:** E02 - Neo4j Exercises.pdf (whole sheet)

- The TA said these Cypher exercises are "exactly what you are going to be asked at the exam", and that doing them is "the way to study for this exam".
- Study advice: exercises within one part are similar to each other. In class, do about four per part and then move on, so you see as many query types as possible. At home, aim to do all 50.

## Top-N / Bottom-N Queries Combine ORDER BY and LIMIT (Q1–Q2)

**Reference:** E02 - Neo4j Exercises.pdf p.2 (Q1–Q2); E02 - Neo4j.pdf slide 31

- Cypher has no single "top N" or "last N" command. The standard trick is to sort with `ORDER BY` and then cut the list with `LIMIT`.
- Q2 (five oldest people): first keep only people whose birth year exists, using `WHERE p.born IS NOT NULL` ("that's how you check if the birth year actually exists"). Then sort by `p.born`, add `p.name` as a second key to break ties, and use `LIMIT 5`. Sorting is ascending (smallest to largest) by default, so the smallest birth years, i.e. the oldest people, come first.
- Check value given in class: Q1 should return **7** movies.

## count() Skips Missing Properties: Count the Attribute, Not the Node (Q3)

**Reference:** E02 - Neo4j Exercises.pdf p.2 (Q3); E02 - Neo4j.pdf slide 21

- `count()` only counts values that exist (non-null). So counting a property instead of the node automatically counts only the nodes that have that property.
- `MATCH (p:Person) RETURN count(p) AS total, count(p.born) AS totalKnown` returns **133** people in total and **128** with a known birth year, so 5 people have no `born`.

## Two Separate Patterns Can Match the Same Node (Q4)

**Reference:** E02 - Neo4j Exercises.pdf p.2 (Q4)

- Work step by step: first match `(matrix:Movie {title: "The Matrix"})`, then a second movie `m`, then compare them with `matrix.released = m.released`. In Cypher, equality is a single `=`, not `==` as in other programming languages.
- The two patterns are independent, so `m` can also bind The Matrix itself. You must add `matrix <> m`. With that condition the query returns 3 movies. Without it, the only difference is that The Matrix also appears in the result.

## Finding Property Names in the Neo4j Browser

- If you don't remember which attributes a node or relationship has, click on it (e.g. the Movie or Person label, or a relationship) in the Neo4j interface. It lists the attributes, e.g. Movie has `title`, `released`, `tagline` and Person has `name`, `born`.

## Recognising When to Use WITH: "For Each X, Count Y" (Q5)

**Reference:** E02 - Neo4j Exercises.pdf p.2 (Q5); E02 - Neo4j.pdf slides 29–30

- A request like "for each release year, count the movies" is an aggregation, and that wording should tell you immediately to use `WITH`.
- Pattern used: `MATCH (m:Movie) WITH m.released AS year, count(m) AS movies WHERE movies >= 3`. Put the grouping key first and then the aggregate. Then sort by `movies` descending ("highest first" is not the default order, so you have to state it) and then by `year`, and return both.

## Counting Relationships per Type, and Why the Count Goes Inside WITH (Q8)

**Reference:** E02 - Neo4j Exercises.pdf p.2 (Q8); E02 - Neo4j.pdf slides 24, 29–30

- A student's attempt matched Tom Hanks with anything and returned the nodes, relationships and movies. The filtering was right, but nothing was counted.
- Leave out the arrow, because the question says "in either direction". Use `type(r)` to get the relationship type.
- Common misreading: the question asks how many relationships there are **of each type**, not how many types there are.
- Solution: `WITH type(r) AS type, count(r) AS total RETURN type, total`. `WITH` acts as a barrier: anything not passed through it is invisible afterwards. So the `count` must be computed inside the `WITH`, not later.
- To filter on a relationship's type, compare it to a string: `type(r) = "ACTED_IN"`.

## Aggregating in RETURN vs WITH, and How Implicit Grouping Works

**Reference:** E02 - Neo4j.pdf slide 29

- You can write the aggregation directly in `RETURN` (e.g. `RETURN type(r), count(r)`) and get the same result. However, nothing can follow `RETURN`. If you need a `WHERE`, another `MATCH`, or other processing after the aggregation, you must use `WITH`. The TA described the `RETURN` form as a syntactic shortcut ("it does the WITH and returns it immediately"). `WITH` is the native construct, and he said it is clearer to use it.
- Grouping rule (explained in Italian to a student; partly ASR unclear): every expression in the `WITH`/`RETURN` that is **not** an aggregate (`count`, `max`, `collect`, …) is treated as the grouping key. If you write the movie title and also the movie's year before `count(...)`, you get a count per (title, year) combination. You can use any number of keys and any number of aggregates. An aggregate itself cannot be the grouping key.
- Mental model he gave: the matched patterns are lined up one after another like rows of a table. The distinct values of the key are taken automatically (an implicit `DISTINCT`), and the number of rows for each value is counted. In effect this is an automatic GROUP BY.

## Reusing the Same Variables Ties Patterns to the Same Person and Movie (Q15)

**Reference:** E02 - Neo4j Exercises.pdf p.3 (Q15)

- Solution built in three steps on the same `p` and `m`: `MATCH (p:Person)-[:DIRECTED]->(m), (p)-[:PRODUCED]->(m) WHERE (p)-[:WROTE]->(m) RETURN p.name, m.title`. Reusing `p` and `m` in every pattern ("fixing every arrow") forces all three relationships to involve the same person and the same movie.
- A student who put all three patterns in the `MATCH` got the same result, and the TA confirmed that this works too.

## Counting Pairs with Two Grouping Keys and Removing Mirror Duplicates (Q18)

**Reference:** E02 - Neo4j Exercises.pdf p.3 (Q18)

- Match every co-acting pair with `(a1:Person)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(a2:Person)`. Then use `WITH a1, a2, count(m) AS total`. Both actors must be in the `WITH` because you are counting occurrences of the **couple**, not of a single actor. Then filter with `total >= 3`.
- Without deduplication every pair appears twice, e.g. Laurence Fishburne–Keanu Reeves and then Keanu Reeves–Laurence Fishburne. The pattern matches both orientations, and each one has the same total of 3.
- Fix: add a string comparison on the names (the TA used `a1.name > a2.name`). This keeps only the pair whose first actor comes later in alphabetical order. You should get **7** pairs instead of 14.

## Filtering Before WITH Is Better, but Efficiency Is Not Graded

**Reference:** E02 - Neo4j Exercises.pdf p.3 (Q18)

- A student suggested putting the name comparison in a `WHERE` right after the `MATCH`, before the `WITH`. The TA agreed this is better: couples you will discard anyway are removed early, so the `WITH` has fewer couples to count. He noted that Neo4j may already do this optimization internally.
- He added: "We are not going to check the efficiency of your queries", because that is not the point of the course.

## Naming a Matched Path, and the Keanu Reeves–Tom Hanks Shortest Path (Q39)

**Reference:** E02 - Neo4j Exercises.pdf p.5 (Q39); E02 - Neo4j.pdf slide 26

- `MATCH p = shortestPath((k:Person {name: "Keanu Reeves"})-[*]-(t:Person {name: "Tom Hanks"})) RETURN p, length(p)`. You have to name the match (`p = …`) because you need to return the path. You can always give a name to what you match. You usually don't, because you usually filter on node names or relationship types instead.
- Result shown in class: Tom Hanks → The Da Vinci Code → Jessica Thompson → The Replacements → Keanu Reeves, with **length 4**.
- The pattern was left undirected on purpose, because the exercise allows any relationship. You can add an arrow to impose a direction, chosen according to what the query asks. In the following Q&A the TA indicated that a directed version may not find the path (ASR unclear).

## Raphtory at the Exam: Theory Questions, No Exercises

**Reference:** E02 Extra - Introduction to Raphtory.pdf

- The TA said there will be no Raphtory exercises at the exam, but there will "probably" be theory questions about Raphtory.

## What Temporality Adds Compared with Neo4j

**Reference:** E02 Extra - Introduction to Raphtory.pdf slides 2–4, 12

- Raphtory does what Neo4j does and adds time on top. It keeps both the structure and the history of the graph. Motivating cases: in a social network or a banking system you want to know **when** a connection or transaction happened, not just that it exists.
- On the "Why Time Matters" slide, Neo4j would see the two A→B→C graphs as exactly the same, because their structure is identical. Raphtory can tell that in the second case A can never reach C, because the A→B link appears after the B→C link.
- Running the same algorithm (e.g. PageRank for the most central node) on different time views and watching the result change is, in the TA's words, something you cannot do in Neo4j.

## Every Creation Is an Event; Repeated Edges and Explode

**Reference:** E02 Extra - Introduction to Raphtory.pdf slides 5–6; E02 - Neo4j.pdf slide 8

- Creating a node and creating an edge are both events, stored with their timestamp in the history. You can create the same link several times, and every creation is kept in that edge's history.
- The TA contrasted this with Neo4j, saying that there "the same relationship is always the same, you cannot create it two times". Note that slide 8 of the Neo4j deck shows that running `CREATE` twice produces two *different* KNOWS relationships. What Neo4j lacks is a single edge that accumulates timestamped updates.
- By default you see one edge carrying all its timestamps. Use explode when a query needs to look at each update separately (e.g. first at t=4, then at t=7).

## Properties vs Metadata: Track Only What Changes

**Reference:** E02 Extra - Introduction to Raphtory.pdf slide 7

- Banking example: the account balance changes, so it is stored as a **property** whose history is tracked. The person's role ("customer") will always stay the same, so it is stored as **metadata**.
- Reason: there is no point spending time and space creating events and history for something you know will never change. You want to track the least data possible.

## Layers and Views Restrict the Graph to the Part You Care About

**Reference:** E02 Extra - Introduction to Raphtory.pdf slides 8–9, 14

- A layer corresponds to a relationship type (in the code example, the `layer=` argument is "basically the type of the relationship"). The TA called layers a visual trick for understanding the graph and for querying more efficiently. For example, if you don't care about grooming at all, query only the resting and/or playing layers.
- Views and layers can be combined, e.g. a snapshot at a given time of the resting layer only. Taking such a picture of the graph at a given time is "the whole point" of Raphtory. A view is not a deep copy, so no space is wasted.

## Rolling vs Expanding Windows: Local vs Cumulative Metrics

**Reference:** E02 Extra - Introduction to Raphtory.pdf slide 10

- **Rolling** example: the number of interactions in a social network each week. Each window is one week, you compute the metric for that week, then move on to the next week. The metric is local.
- **Expanding**: the start time stays fixed and earlier data is never dropped, so the window keeps growing and the metric is cumulative.
- Raphtory has dedicated functions for both, because they are the most common analyses on temporal graphs.

## Persistent Graph: An Edge as a State with a Duration

**Reference:** E02 Extra - Introduction to Raphtory.pdf slide 11

- Example: an employment starts at some point, lasts a long time, and then ends. It is not a single moment. In a persistent graph, a snapshot taken inside the interval shows the employment edge, and a snapshot taken outside it does not. The state lasts until it is deleted and can go on forever.

## Reading the First Raphtory Example: Why the Counts Are 3, 4, 2 and 1

**Reference:** E02 Extra - Introduction to Raphtory.pdf slide 14

- Raphtory is used as a Python library. `add_edge(timestamp, source, destination, layer=...)` can also take properties, just as in Neo4j (e.g. `amount` on the payment edge).
- `count_edges()` = 3: Alice→Bob is added twice (t=1 and t=4), but it is the same edge. `count_temporal_edges()` = 4, because it also counts the second Alice→Bob update. This is "the main difference with Neo4j".
- `window(1, 3).count_edges()` = 2, not 3, even though three edges were created by t=3. As with Python lists, the end of the window is exclusive, so only t=1 (Alice→Bob) and t=2 (Bob→Carol) are counted.
- `layer("payment").count_edges()` = 1 (Alice→Carol). Counting temporal edges on that layer also gives 1. In general the number of temporal edges can never be smaller than the number of edges, only equal or larger.
