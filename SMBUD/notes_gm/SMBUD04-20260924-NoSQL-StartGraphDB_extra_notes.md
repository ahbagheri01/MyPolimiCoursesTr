# SMBUD04-20260924-NoSQL-StartGraphDB — Additional Professor Notes

**Transcripts:** SMBUD04-Marco Brambilla PoliMi-20260924 1611-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-05-nosql.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

## CAP Trade-offs: Split Architectures and Consistency vs. Performance

**Reference:** SMBUD-05-nosql.pdf, slides 36-37

Applications need not apply a uniform CAP property across all sub-components. In an e-commerce platform, the product catalog and browsing pages prioritize high availability (even with stale or slightly inconsistent stock levels), whereas the payment and order submission pipeline strictly enforces high consistency to prevent financial and inventory errors. Furthermore, consistency trades off against performance (speed) because maintaining ACID/consistent replicas requires costly inter-server synchronizations, version checks, and reduced parallelization, prompting services to trade consistency for speed to prevent user drop-off.

## BASE Eventual Consistency: Mechanics and User-Facing Consequences

**Reference:** SMBUD-05-nosql.pdf, slide 42

Eventual consistency is a liveness guarantee about the future, meaning it implicitly provides no safety guarantees in the present. From a user's perspective, this means the system can serve stale or wrong data (e.g., showing 7 items available when only 5 exist, or booking an unavailable hotel room), leaving the user to deal with real-world compensations like returns or rebooking. In real systems, convergence delays typically range from milliseconds to a few minutes and stem from network latency, replica synchronization, or node rebalancing rather than transaction failure.

## Industrial Origins and Open Source Dynamics of NoSQL

**Reference:** SMBUD-05-nosql.pdf, slides 44, 46, 53

NoSQL platforms were not developed by incumbent database vendors (e.g., Oracle, IBM, Microsoft), who were bound by existing RDBMS monopolies and heavy past investments. Instead, Web 2.0 giants (Google, Facebook, Twitter, LinkedIn, Netflix) were forced to build their own systems internally to satisfy massive data scale. Because these companies did not monetize database software, they collaborated—even among direct competitors like Facebook and Twitter—to split engineering costs and released approximately 90–95% of NoSQL platforms as open-source software.

## NoSQL Families: Classification and Modern Additions

**Reference:** SMBUD-05-nosql.pdf, slides 47, 50-52

The term 'NoSQL' is fundamentally a negative definition (defining systems by what they are not) and carries multiple historical meanings (from Carlo Strozzi's lightweight RDBMS without SQL syntax, to 'Not Only SQL' and 'NewSQL'). While four classical NoSQL families exist—Key-Value, Columnar/BigTable, Documental, and Graph—modern non-relational database curricula must also include Information Retrieval-based (IR / search-based) databases and Vector databases arising from AI and machine learning requirements.

## Graph DBs vs. Relational: Pointer-Level Navigation vs. Cross-Table Joins

**Reference:** SMBUD-06-graphDB-neo4j.pdf, slides 34, 35, 37, 39, 40

Relational databases struggle with highly connected data because relating entities (such as a sailor renting a boat) necessitates artificial intermediate join tables and expensive foreign key join operations. Graph databases store connections directly with the data via index-free adjacency. The edges behave as direct memory pointers between objects, enabling direct traversal in constant time without scanning index trees or joining separate tables.

## Graph Pattern Matching: Lens Search and Query Pruning

**Reference:** SMBUD-06-graphDB-neo4j.pdf, slides 41, 55, 57

Because graph databases are schemaless and lack fixed relational tables or columns, query evaluation is formulated as graph pattern matching (subgraph isomorphism). The query defines a target subgraph pattern, conceptualized as a lens traversing the database graph. To avoid scanning the entire database graph, the query engine prunes the search space by anchoring the pattern match at specific starting nodes matching the query's node labels and attribute filters, followed by traversing direct adjacent pointers.

## Neo4j Design Choices: Java Implementation, ACID Compliance, and Historical Naming

**Reference:** SMBUD-06-graphDB-neo4j.pdf, slides 45, 46, 48

Neo4j is an ACID-compliant transactional graph database developed by Neo Technologies (Silicon Valley), making it suitable for business applications requiring strict correctness. Its naming and query language (Cypher) are cultural references to the movie *The Matrix*—symbolizing Neo breaking free from the tabular 'matrix' of relational databases. Despite the traditional preference for C/C++ in database development, Neo4j was written in Java (the '4j' suffix) to align with the open-source and open-language movements of around 2000–2001.

## Cypher Syntax: Temporary Aliases vs. Persistent Node Attributes

**Reference:** SMBUD-06-graphDB-neo4j.pdf, slide 51

In Cypher syntax, variables placed before node definitions (e.g., `neo` in `CREATE (neo:Crew {name: 'Neo'})`) are purely temporary aliases scoped to the single query execution to allow local chaining and referencing across clauses. They are not stored in the database. To retrieve an entity in subsequent transactions, persistent attributes (such as unique IDs or names) must be explicitly indexed and queried. Any referenced alias within a statement must be defined prior to use, or execution will fail.

## Cypher Labels vs. Data Types: Multi-Labeling and Schema Discipline

**Reference:** SMBUD-06-graphDB-neo4j.pdf, slide 52

In Cypher, labels (e.g., `:Actor:Director`) should not be confused with classical computer science data types. Data types enforce rigid structural shapes and allow only single instantiation. Labels in Neo4j function like descriptive, non-restrictive tags; a single node can have multiple labels simultaneously (e.g., Clint Eastwood having both `:Actor` and `:Director`), enabling discovery across multiple search contexts. However, this flexibility requires strict design discipline to avoid graph disorder and untraceable data.
