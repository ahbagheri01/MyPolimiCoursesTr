# SMBUD05-20261006-GraphDB-Neo4j — Additional Professor Notes

**Transcripts:** SMBUD05-Marco Brambilla PoliMi-20261006 1410-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

## Labels vs. Types in Neo4j

**Reference:** Slide 49 ('Data Model: Nodes – with labels (type) and attributes; Edges; Indexes'), Slide 52 ('Multiple labels: Create (n:Actor:Director ...)')

There is a strict notational and conceptual distinction between labels (applied to nodes) and types (applied to relationships/edges). A primary conceptual and practical reason for this distinction is that nodes can have multiple labels simultaneously (e.g., categorizing an entity as both an actor and a director), whereas edges have a single type.

## Nature and Scope of Aliases in Cypher

**Reference:** Slide 51, Slide 52, Slide 60, Slide 61

Aliases (such as variable names assigned to nodes or edges during creation or matching) are strictly temporary in-memory identifiers during the execution of a single command. They are not stored as attributes or persistent identifiers in the graph database, and future queries cannot reference past aliases to find entities.

## Defining Source and Target Aliases Before Creating Relationships

**Reference:** Slide 51 ('(Neo)-[:KNOWS]->(Morpheus)')

When creating a relationship in Cypher, both endpoint nodes must already be identified via aliases defined beforehand in the operation; attempting to connect to an alias that was not defined results in an error. If a relationship is created using an empty node descriptor as target, Neo4j will create a completely empty node (no labels, no attributes), which is syntactically valid but problematic because it cannot be retrieved directly later except via graph traversal from the connected node.

## Data Ingestion via LOAD CSV and Row Aliasing

**Reference:** Slide 52 ('LOAD CSV WITH HEADERS FROM "file:customers.csv" AS row')

The LOAD CSV WITH HEADERS command behaves like an iterative loop over a tabular file, reading one row at a time and binding it to an alias (e.g., 'row'). Developers have full flexibility over the resulting graph schema: a single row can be mapped to one node, multiple nodes, or relationships with attributes.

## CREATE vs. MERGE for Idempotency and Duplication Control

**Reference:** Slide 53 ('Cypher - Merge', 'MERGE (player:Player {id: row.playerUri}) ON CREATE SET...')

Repeated executions of CREATE blindly generate duplicate nodes and edges because graph databases lack built-in relational uniqueness checks by default. MERGE replaces CREATE to provide idempotency: it first checks if a pattern/node matching the specified identifier exists; if it exists, it aborts creation/duplication; if not, it creates the node and applies ON CREATE SET properties.

## Multi-Step Graph Ingestion Pattern (Player Transfers Example)

**Reference:** Slide 54 ('Importing Edges')

To import complex relationships where the related entities already exist (e.g., football player transfers between seller and buyer clubs), the query pattern uses MATCH to bind aliases to existing nodes (player, source club, target club via their URIs from the row), then uses MERGE to create the intermediate event node (the transfer), and finally creates the connecting relationships between the event node and the matched entities.

## Purpose of Indexes in Graph DBs vs. Relational DBs

**Reference:** Slide 35 ('Provides index-free adjacency', 'Every node is a pointer to its adjacent element'), Slide 55 ('Cypher - indexes', 'Only for access to initial node of the query')

In relational databases, indexes are critically required on foreign keys to accelerate expensive join operations between tables. In graph databases, relationships act as direct pointers (index-free adjacency), so relationship traversals need no indexes and are inherently fast. Indexes in graph databases are instead access structures primarily used for initial node lookup (entry points) based on property values (e.g., finding John or a customer by ID) to avoid full-graph scans.

## Comparison of Cypher MATCH-WHERE-RETURN to SQL SELECT-FROM-WHERE

**Reference:** Slide 50 ('Many features stem from improving on pain points with SQL such as join tables'), Slide 57 ('Cypher - Queries: MATCH Pattern Matching, WHERE Expressions, RETURN Output')

Cypher's MATCH-WHERE-RETURN corresponds conceptually to SQL's SELECT-FROM-WHERE: MATCH replaces FROM (searching for structural graph patterns/shapes rather than listing flat tables), WHERE retains the exact same filtering role on predicates, and RETURN replaces SELECT (with RETURN being strictly more flexible because it can output scalar values, property lists, or entire subgraphs and newly formed graph topologies).

## Recursive / Multi-Step Navigation Syntax and Exponential Search Risk

**Reference:** Slide 58, Slide 61 ('(n)-[*1..5]->(m)', '(n)-[*]->(m)'), Slide 65 ('Always set an upper limit for your variable length patterns. It’s easy to have a query touch all nodes in a graph by mistake.')

Adding an asterisk (e.g., [:KNOWS*]) denotes recursive multi-step traversal across relationships. While Cypher automatically detects and breaks cycles/loops so traversal does not spin infinitely, multi-step queries carry an extreme performance risk of exponential explosion (e.g., the 'six degrees of separation' phenomenon reaching billions of nodes in 4-5 steps in social graphs). Traversals should always be bounded by specifying explicit min/max step limits (e.g., *1..5).

## Directionality in Queries vs. Physical Graph Storage

**Reference:** Slide 60 ('(n)--(m) Relationship in any direction between n and m')

All relationships in Neo4j are stored with a mandatory direction in the database. However, in Cypher queries, indicating an arrow direction enforces matching only that specific direction, whereas omitting the arrow in the query pattern instructs the engine to traverse edges in either direction. It does not mean the underlying graph is undirected, but that the query accepts either incoming or outgoing edges.

## Scope of Conditions in Multi-Step Recursive Paths

**Reference:** Slide 58, Slide 61

In a multi-step path expression like (n:Crew)-[:KNOWS*]->(m), node labels/properties placed on the endpoints apply strictly to the start node (n) and end node (m), but intermediate traversed nodes are unconstrained and do not need to satisfy those conditions. Conversely, relationship constraints specified on the edge type apply universally to every single traversed step along the path.

## Inline Property Matching vs. WHERE Clause and Optimizer Role

**Reference:** Slide 57, Slide 58, Slide 60, Slide 61

Specifying properties inline within MATCH (e.g., `(n {name: 'Neo'})`) vs. specifying them in WHERE (e.g., `WHERE n.name = 'Neo'`) are conceptually different (pattern definition vs. post-filtering predicate), but because Cypher is declarative and utilizes a cost-based query optimizer, both execute in the exact same execution plan and time. However, inline syntax only supports exact equality matching on single attribute values; range conditions (e.g., `age > 20`), composite logical operators (`OR`), and inequalities cannot be written inline and strictly require the WHERE clause.

## Handling Missing Attributes and NULL Values in Graph DBs

**Reference:** Slide 46 ('Neo4j is schema free – Data does not have to adhere to any convention')

Unlike relational databases which store explicit NULL markers in missing table cells, Neo4j simply omits the attribute from the node entirely (schema-free property graph). When filtering with a condition like `WHERE n.age = 20`, nodes lacking the `age` attribute are automatically excluded. To check for attribute absence/presence without value equality, use `IS NULL` or `IS NOT NULL`. Crucially, you must never write `= null` because two nulls cannot be equated.

## Exam Example: Querying Current Status via Absence of End Date

The professor provides a concrete exam example: finding current employees in an employment relationship with `start_date` and `end_date` attributes. A current employee is modelled not by a specific value, but by an active relationship where `end_date IS NULL` (i.e. the attribute has not been assigned).

## The WITH Clause and Why Graph DBs Lack GROUP BY

**Reference:** Slide 59 ('WITH separates query parts explicitly, to declare the variables for the next part', 'Aggregation can be used (count)')

Neo4j does not have a SQL `GROUP BY` keyword. In relational databases, `GROUP BY` is necessary because tuples reside in a flat table and must be partitioned before aggregation. In a graph, aggregation is naturally anchored to a node: Cypher uses the `WITH` clause to focus on an entity (e.g., `WITH user, count(friend) AS friends`), effectively behaving like a 'for-each' context switch that passes projected aliases, aggregations, and filtered variables into subsequent query stages.

## Expressing Non-Linear and Complex Graph Topologies in Cypher

**Reference:** Slide 60, Slide 61, Slide 64

To represent non-linear patterns (e.g., graphs with branching, cycles, or multiple connections between non-consecutive nodes like A->B->C->D alongside B->D and C->F), queries cannot be written as a single linear chain. Instead, separate path fragments are joined with commas, reusing the same node aliases across fragments. In Cypher, the comma in a MATCH statement functions as a logical AND, enforcing that the entire composite pattern matches collectively.

## Matching Isolated Nodes vs. Connected Subgraphs

**Reference:** Slide 60 ('(n)--(m) Relationship in any direction between n and m')

Querying for a bare node pattern `MATCH (n) RETURN n` retrieves all nodes in the database, including completely isolated nodes. In contrast, querying with a pattern that specifies any connection, such as `MATCH (n)--() RETURN n`, filters out isolated nodes and strictly returns only those nodes that participate in at least one relationship.

## Interpretation of Query Output Identifiers (0) and (1)

**Reference:** Slide 58 ('[(0)-[0:KNOWS]->(1)]')

In Cypher query output representations showing relationships connecting entities (e.g., `[(0)-[0:KNOWS]->(1)]`), the numbers (0 and 1) are not the actual persistent database IDs of the nodes. They are temporary visualization and formatting placeholders used by the interface to clarify which endpoints correspond to each other without conflating them.
