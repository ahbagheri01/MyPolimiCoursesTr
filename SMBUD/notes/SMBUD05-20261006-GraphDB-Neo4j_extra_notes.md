# SMBUD05-20261006-GraphDB-Neo4j — Additional Professor Notes

**Transcripts:** SMBUD05-Marco Brambilla PoliMi-20261006 1410-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

> **Coverage notes:** This lecture covered only the Cypher part of the shared deck (about p.50–61), with a reference back to the graph-matching figure on p.41. The graph-theory and graph-DB intro slides and p.62–65 (stored procedures, paths, core operators, hints) were not presented. The transcript ends partway through the answer to a student question about the number of evaluations (three announced vs. two in the schedule), so that answer is missing.

## Labels Classify Nodes, Types Belong to Edges — and Why the Distinction Matters

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.49 (Data Model), p.51 (multiple labels)

The professor stressed that the difference between node **labels** and edge **types** is more than notation. The name after `:` in a node `( )` is a label, and the name inside `[ ]` on an edge is a type. A node can have several labels (`:Label1:Label2`), which is unusual for "typing" in data models and programming languages. A label is a **categorization** of nodes. An edge type says what the connection actually **is**. Note that slide p.49 writes "labels (type)" for nodes; the professor kept the two terms separate.

## Aliases Are Temporary Names That Exist Only During One Operation

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.50

- Cypher (originally Neo4j's proprietary language) is used both to **define/create** data and to **query** it.
- The professor called aliases (`Neo`, `n`, `row`, …) the key ingredient for building complex structures. An alias is a temporary identifier that lets you refer to the same object in other parts of the **same** operation.
- Aliases are **not stored**. Only labels, attributes, relationships and their types end up in the database. The names themselves don't matter: using `X`, `Y`, `Z` instead of `Neo` creates exactly the same data. You can never use an alias later to search for the data.
- Inside one command, two different elements cannot share an alias; to add another node, give it a new alias.
- A `CREATE` returns nothing to the user. Its only result is new data in the database.
- His example: create `X:Crew {name:'Neo'}`, an unlabelled `Y`, another `W:Crew`, then `X-[:KNOWS]->Y` and `W-[:WORKS_FOR]->Y`. The graph grows through such sequences of creates. There are no constraints: new labels, types and attributes can be introduced at any moment.

## The Slide's `(Neo)-[:KNOWS]->(Morpheus)` Creates an Empty, Unfindable Node

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.50

- To create a relationship, both endpoints must be identified first, through aliases defined in the operation. On the slide, `Morpheus` is never defined. The professor first said the command as shown is incomplete/wrong (there's no way to know who Morpheus is), and that you should define Morpheus first, e.g. create it as well. Nothing forces Morpheus to be `:Crew`: it could be a Person or anything you like.
- He then pointed out the subtler problem. If the line runs within the creation, it is syntactically fine, but `Morpheus` becomes a **brand-new node with no label and no attributes**. In the future it can't be fetched directly. The only way to reach it is to find Neo first and follow the `KNOWS` relationship. "It works … but it's probably doing something you don't want."
- A student also noted that a relationship must always be given a direction when created. The professor confirmed that Neo4j requires one, and agreed this can be a limitation when the real relationship has no direction.

## `LOAD CSV` Is a Loop Over Rows, and You Choose the Graph Shape It Produces

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.51

- In practice data is rarely created node by node. It is imported from existing sources, e.g. a CSV exported from Excel or from a relational table.
- `AS row` is again an alias, assigned to each line as it is read (the professor compared this to SQL aliasing). The statement is effectively a loop: read one row, create one `Customer` node, copy `CompanyName`, `CustomerID` and `Phone` from the matching columns. A 10,000-line file therefore gives 10,000 nodes in one shot. This assumes the file has exactly those column headers.
- The CSV is just flat lines, but the **shape** you build from each row is up to you: one node, several nodes, relationships, any operation you like.

## `CREATE` Duplicates on Every Run; `MERGE` Checks Existence First

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.51–52

- `CREATE` always creates what you ask for, and there is no check for duplicates. If you import 10,000 customers and then re-run the import by mistake, you get 10,000 more identical customers, because the database has no way to know they are the same.
- `MERGE` replaces `CREATE` when you want to create something only if it doesn't already exist.
- In `MERGE (player:Player {id: row.playerUri})`, the `id` is the property used to check existence. If a player with that id exists, **nothing is done**. A student asked whether it updates or aborts: there is no update. If it does not exist, the node is created and then `ON CREATE SET` fills in `name` and `position`.
- The professor called this a first, "soft" uniqueness constraint, because it lives in the operation rather than in the database.

## Walk-Through of the Transfers Import (Edges)

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.53

- **Scenario:** the graph already holds players and clubs. In the transfer market, clubs buy and sell players. Each row of `transfers.csv` describes one transfer: `playerUri`, `sellerClubUri`, `buyerClubUri`, `transferUri`, plus season, rank and fee.
- **Step zero is binding aliases with `MATCH`**, which looks in the existing data to *find* something. For the current row, find the player with that URI (e.g. P1) and call it `player`. Find the seller club (e.g. C2) and call it `source`. Find the buyer club (e.g. C3) and call it `destination`.
- Then `MERGE` a `Transfer` node `t` with the transfer URI as id, and `ON CREATE SET` season, rank and fee. Then merge the three relationships `OF_PLAYER` (carrying the player's `age`), `FROM_CLUB` and `TO_CLUB`.
- Result: for every row, one transfer node plus three connections, repeated for each transfer in the file.
- **Q&A — could `CREATE` be used for the relationships?** Yes. `MERGE` is the safe choice if you never want duplicates, but here duplicates are essentially impossible: if the transfer node is new, its relationships cannot already exist.
- The same `MATCH`/`MERGE` operations also work for a single element without `LOAD CSV`.

## Constraints Add a Little Design Discipline to a Schema-Free Database

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.55

Because you are otherwise totally free to create any structure at any time, constraints let you enforce "a little bit of proper design". The typical one is uniqueness (`customerID` unique for `Customer` nodes). The professor added that you can also assert other rules, e.g. that `customerID` must be both **unique and not null**, i.e. a value is required. The slide shows only the uniqueness form.

## Why Relational Databases Need Indexes (Especially for Joins)

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.54

Indexes are **access structures** that speed up access to data on chosen attributes. In relational databases you typically create them on primary keys, on attributes you search frequently, and above all on the keys used in **joins**. A join between a primary key and a foreign key must find, for every element on one side, the matching element on the other side, which is expensive. Indexes on the join keys make this much faster.

## In a Graph Database, Indexes Only Serve to Find Starting Nodes

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.54

- Following a relationship needs no index: an edge is like a pointer to the next element, with no join, no matching and no search, so traversal is already fast.
- What is slow is **finding where to start**. Example: searching for students named John. Without an index you would have to start somewhere and move around the whole structure, i.e. scan all nodes: on average half the dataset if you are "average lucky", and the very last node if you are unlucky.
- Think of an index (e.g. on `:Customer(customerID)`) as a **dictionary**: value → pointers to the matching nodes. There may be many: "John" → node 1, node 2, node 25.
- Practical advice: if queries that search by value are slow, create an index on that attribute of those nodes.

## `MATCH–WHERE–RETURN` Mapped Against SQL's `SELECT–FROM–WHERE`

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.56, p.41

- SQL cannot be reused because there are no tables, so `FROM` (a list of tables) makes no sense.
- `MATCH` takes the place of `FROM`. Instead of naming tables, it describes the **shape** (pattern) to look for, since graph queries run by pattern matching (the query-shape-in-the-graph picture on p.41).
- `WHERE` is essentially the same as in SQL: simple or composite conditions on the data matched.
- `RETURN` plays the role of `SELECT` (a description of the output), but it is more powerful. `SELECT` can only list attributes, while `RETURN` can return nodes, relationships, paths/subgraphs, lists, or even new graphs built from the data. This flexibility was one of the requirements for graph DBs.
- The professor said to "print it in your head and keep it forever": match, where, return are the three steps always needed.

## Reading the Basic Neo Query and Its Output

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.57

- The professor first ran the query **without** the star: `MATCH (n:Crew)-[r:KNOWS]-(m) WHERE n.name='Neo' RETURN n AS Neo, r, m`.
- `n`, `r`, `m` are again just aliases. A node with no label or condition (`m`) means **any** node.
- In the Matrix graph the only result is Neo –KNOWS– Morpheus. `n AS Neo` just renames the output column, since n is always Neo.
- **Q&A:** the `(0)`, `(1)` … numbers in the output's `r` column are only a visualization trick to tell the nodes apart in the printed result. They are **not** the actual node IDs. In the real system you get the full node data, including the actual ID.

## Variable-Length `*`: Output Explosion, Loops, and Why Limits Are Not Enough

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.57, p.61, p.65

- Adding `*` makes the navigation of `KNOWS` recursive. From Neo you reach Morpheus at 1 step, Trinity and Cypher at 2, and Agent Smith at 3.
- **Risk 1, explosion:** the query may end up exploring the entire graph, because graphs grow roughly exponentially with each step.
- **Risk 2, loops:** if I know you and you know me, we "know each other" at any number of steps. The language handles this: when it detects a loop during multi-step navigation it breaks it rather than repeating forever. But in a graph with billions of nodes and relationships, *detecting* a loop can itself take a while.
- Use `*` with extreme care, only if really needed, and as constrained as possible. Bounding it with `[*1..5]` (min..max) is always a good idea; another syntax would be shown in the exercise class.
- **A limit is still not safe.** Example: on social media about 4.5 steps reach everyone on Earth. With 4 steps on the Facebook/Instagram graph you are connected to Trump and Putin, and could extract around 3 billion nodes. If you have 100 friends and each has 100 friends, a few steps already give billions of results.

## In a Variable-Length Pattern, Node Conditions Apply Only to the Endpoints

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.57, p.61

In `(n:Crew)-[:KNOWS*]-(m)`, the label or conditions on `n` apply only to the **first** node, and those on `m` only to the **last** node. Intermediate nodes are unconstrained: even after 10 steps they don't need to be `Crew`. The relationship condition works the opposite way: the type `KNOWS` must hold on **every** hop of the path.

## Directions in Queries: Omitted Means "Any Direction", Not "Undirected"

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.60–61

- Stored relationships always have a direction. In a **query**, the direction is optional.
- Writing a direction asks only for patterns with that direction. Omitting it means you accept **either direction**, which is not the same as the graph being undirected.
- In the Matrix example, `(n:Crew)-[:KNOWS]->(m)` gives the same output as the undirected version. Reversing it (looking for an `m` that KNOWS Neo) returns the **empty set**, because no `KNOWS` edge points into Neo.

## `MATCH (n)` vs `MATCH (n)--()` Return Different Sets

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.60

Patterns can be as loose as you like. `MATCH (n) RETURN n` returns every node in the database: technically feasible, though rarely sensible. `MATCH (n)--() RETURN n` is **not** the same: it returns only nodes connected to at least one other node, so isolated nodes are excluded.

## Inline Property vs `WHERE`: Logically Different, but the Optimizer Makes Them Equal

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.49 (declarative), p.60

- `MATCH (n) WHERE n.name='Neo'` and `MATCH (n {name:'Neo'})` give the same output, but conceptually they say different things. The first matches every node and then filters it with a condition. The second directly searches for nodes having that name.
- The professor asked the class which one runs faster. Answer: **the same**. Cypher is declarative, so you state what data you need, not how to get it. An optimizer turns any syntax into the best execution algorithm, much like compiling, and for such simple conditions it easily finds the same plan.
- Only a naive translation would make one of them faster.
- A student noted that an index would make the search faster; the professor agreed, but that holds for both forms.

## `:` (Definition) vs `=` (Predicate), and What Can Go Inside the Pattern

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.60

- `{name: 'Neo'}` inside `MATCH` uses the same **definitory** syntax as node creation. It describes a node shape: "a node n with name Neo, find everything like that."
- `n.name = 'Neo'` in `WHERE` is a **predicate** (a condition).
- Using the wrong symbol simply doesn't work. The professor warned to be careful when writing queries on paper.
- **Consequence:** inside the pattern you can only state **equality to a single value per attribute**. Several equalities side by side are fine. You cannot write `age > 20` there, and you cannot write disjunctions such as "20 years old OR from Milan", because OR is not part of a definitory description. Those must go in `WHERE`.

## Missing Attributes and `IS NULL` in a Graph Database

**Reference:** None (not in slides)

- A condition like `age = 20` (inline or in `WHERE`) is strict. It implicitly requires that the node **has** the attribute. Since every node can have different attributes, nodes without `age` are simply not returned.
- Unlike relational tables with null cells, a graph DB does not store a null for a missing value: the attribute is just **absent** from the node.
- `IS NULL` / `IS NOT NULL` look the same as in SQL but mean "the attribute is absent / present". Example: `n.age = 20 AND n.city IS NULL` finds 20-year-olds whose city is unknown.
- Never write `city = null`. Two nulls are not the same thing, so you cannot test equality with null, only whether something is null or not.

## Last-Exam Example: Current Employees via a Missing End Date

**Reference:** None (not in slides)

The professor gave "a case from the last exam". `Employee` (a person) –`WORKS`→ `Company`, with `startDate` and `endDate` stored on the `WORKS` relationship. To find the **current** employees of a company, match the `WORKS` relationships whose `endDate` is null: no end date means the person still works there. (ASR has "end date … is now"; from context this is "is null".)

## `WITH` Replaces `GROUP BY`: Focus on a Node and Aggregate

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.58

- `WITH` lets you write multi-step queries, feeding the output of one `MATCH` into later steps. It acts as a definitory step where you can create new aliases and values. Its typical use is aggregation (`count`, max, min, sum, …), and you can keep adding `MATCH` clauses incrementally afterwards.
- **Why there is no GROUP BY.** Relational data sits in tables, so you must first group a bunch of rows before computing count/average/max. In a graph, what is connected to a node can be counted directly at that node: there is nothing to group. `WITH user, count(friend) AS friends` means "focus on each user and count its friends", which is more like a **for-each** than a group-by.
- A student suggested picturing the match result as a table and grouping it. The professor said the result is the same, but that view pulls you back into relational thinking, which is less appropriate.
- **Reading the slide query:** count the friends per user, `ORDER BY friends DESC` (most friends first), `SKIP 1`, `LIMIT 3`. The result is the top three users by number of friends, **excluding the first**, i.e. ranks 2–4.

## Writing Non-Linear Patterns: Comma-Separated Pieces Sharing Aliases

**Reference:** SMBUD-06-graphDB-neo4j.pdf, p.60–61

Text syntax naturally writes linear chains such as `A→B→C→D→E`. To also say that B is connected to D (a pattern that is not a line), you cannot draw it. Instead, split the pattern into pieces separated by **commas**, reusing the **same aliases**: e.g. `(a)-->(b)-->(c)-->(d)-->(e), (b)-->(d), (c)-->(f)`.

- The comma means **AND**: the whole picture must hold together.
- Pieces may use different directions (e.g. B–C reversed).
- Each node or relationship can still carry its own label, attribute and relationship conditions.
- With this you can express any topology.
