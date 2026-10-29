# SMBUD-Ex-20261008-Neo4j-Introduction — Additional Professor Notes

**Transcripts:** Neo4J_introduction_Ettori_08-10-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j Sandbox Setup Guide.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf

## Querying and Cartesian Product Traps with Unfiltered MATCH Clauses

**Reference:** E02 - Neo4j.pdf, slide 7

In Cypher, MATCH produces a set of matching nodes. When multiple nodes are matched independently without sufficient filtering (e.g., `MATCH (a:Person), (b:Person)`), combining them in a subsequent `CREATE (a)-[:REL]->(b)` will generate a full Cartesian product of relationships (including self-loops and cross-links, such as Mark with himself, Mark with Mike, Mike with himself, Mike with Mark). The WHERE clause or inlined property constraints are essential to restrict the binding to exactly the desired pairs.

## Query Optimization: Inlining Property Filters in MATCH vs. WHERE

**Reference:** E02 - Neo4j.pdf, slides 6-7

Filtering properties can either be written inside the `MATCH` pattern directly (e.g., `(a:Person {name: 'Mike'})`) or deferred to a subsequent `WHERE` clause (`WHERE a.name = 'Mike'`). While functionally equivalent, collapsing the property constraint directly into the `MATCH` pattern is standard practice and often faster because Neo4j can evaluate the predicate directly during pattern traversal rather than matching all candidates first.

## Mandatory Deletion of Relationships via DETACH DELETE

**Reference:** E02 - Neo4j.pdf, slide 9

Neo4j enforces referential graph integrity by disallowing the direct deletion of any node that still possesses incident relationships; attempting to execute `DELETE n` on a connected node triggers an error. `DETACH DELETE` explicitly confirms the cascading deletion of both the node and all attached incoming/outgoing edges.

## Internal Optimization Observed via PROFILE: Filter Pushdown via autostring

**Reference:** E02 - Neo4j.pdf, slide 16

When using `PROFILE`, Cypher execution plans show internal operators like `auto_string` where Cypher optimizes execution by pushing down WHERE predicates directly into the pattern scan (`NodeByLabelScan` / expanding steps). Instead of retrieving every node of a label and then filtering, Neo4j checks node properties while expanding candidates.

## Cycle Prevention: Single MATCH vs. Multi-Match Statements

**Reference:** E02 - Neo4j.pdf, slides 13, 39, 40

Within a single `MATCH` clause, Neo4j automatically enforces relationship uniqueness across the pattern, preventing repeated traversal of the same relationship and avoiding trivial cycles. However, when multiple distinct `MATCH` clauses are chained sequentially (e.g., matching Tom Hanks to co-actors, and in a second MATCH connecting co-actors to co-coactors), Neo4j evaluates them independently. This allows cycles where paths can traverse back to the origin node unless explicit inequality predicates (e.g., `WHERE tom <> cocoActors` and `NOT (tom)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors)`) are defined.

## ShortestPath Algorithm Planning: Fast BFS vs. Exhaustive DFS and the WITH Barrier Trick

**Reference:** E02 - Neo4j.pdf, slides 36-38

For `shortestPath()`, Cypher defaults to a fast bidirectional BFS if the condition can be evaluated step-by-step during traversal (such as filtering relationship types or non-null edge properties). If the condition inspects global properties only verifiable on complete paths (such as `length(p) > 1`), Cypher must plan a slower exhaustive DFS. Placing a `WITH` barrier before the `WHERE` clause (`WITH p WHERE length(p) > 1`) hides the predicate from the planner during path search; Cypher executes fast BFS blindly and returns only the single shortest path, which then gets discarded if it does not satisfy the length condition, resulting in an empty result even if valid longer paths exist.

## Grouping Semantics with WITH: Impact of Preserving Grouping Keys

**Reference:** E02 - Neo4j.pdf, slide 30

Like SQL `GROUP BY`, variables listed before aggregation functions in a `WITH` clause define the grouping key. If both `person` and `movie` are placed in `WITH` (e.g., `WITH person, movie, count(*) AS c`), Cypher groups by the unique (person, movie) pair, yielding a count of 1 in virtually all standard cases unless an actor played multiple roles in the same movie. To count movies per person, `movie` must be omitted from the grouping key in `WITH`.

## Aggregation in RETURN Without a WITH Clause

**Reference:** E02 - Neo4j.pdf, slide 39

While multi-step pipeline aggregations generally require an explicit `WITH` clause to project and group variables, Cypher permits direct aggregation inside the `RETURN` statement (e.g., `RETURN cocoActors.name, count(*)`). This acts as a shorthand aggregation when no subsequent filtering on the aggregated result is needed.

## Exam Advice: Explicit Labeling in Cypher Queries

**Reference:** E02 - Neo4j.pdf, slides 23, 39

Although slide examples often omit entity labels on intermediate nodes (relying on domain assumptions such as only Person having `ACTED_IN`), in exams and complex databases students should explicitly specify node labels (e.g., `(m:Movie)` or `(m:Film)` instead of `(m)`). Explicitly defining labels prevents unwanted matches and accidental grading deductions.
