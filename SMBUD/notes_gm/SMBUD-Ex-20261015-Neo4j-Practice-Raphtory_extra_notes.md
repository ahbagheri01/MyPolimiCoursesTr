# SMBUD-Ex-20261015-Neo4j-Practice-Raphtory — Additional Professor Notes

**Transcripts:** Neo4J_practice_and_raphtory_Ettori_15-10-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j Exercises.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 Extra - Introduction to Raphtory.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 - Neo4j.pdf

## Exam Scope for Cypher and Raphtory

The hands-on query exercises shown in class reflect the exact query problems tested on the exam. Conversely, Raphtory will not have practical query exercises in the exam, but only theoretical questions.

## Simulating 'Top N' or 'Last N' Queries in Cypher

**Reference:** E02 - Neo4j.pdf page 31

Cypher lacks a dedicated 'top N' or 'bottom N' operator. To achieve this, queries must combine ORDER BY (which defaults to ascending order) and LIMIT.

## Counting Non-Null Attributes vs Nodes

**Reference:** E02 - Neo4j Exercises.pdf page 2

Cypher's `count()` ignores null values. Counting a node property (e.g., `count(p.born)`) counts only nodes where that property exists/is not null, whereas `count(p)` or `count(*)` counts all matched nodes.

## Equality Operator Syntax in Cypher

**Reference:** E02 - Neo4j Exercises.pdf page 1

Unlike most programming languages that use `==` for comparisons, Cypher uses a single `=` for equality checks.

## Self-Match Prevention Across Independent MATCH Clauses

**Reference:** E02 - Neo4j Exercises.pdf page 2

When multiple MATCH clauses (or multiple comma-separated node declarations) match the same entity label without structural connection, they can bind to the identical node; an explicit inequality predicate (e.g., `WHERE matrix <> m`) is necessary to prevent self-matches.

## Underlying Mechanics of Aggregation and WITH/RETURN in Cypher

**Reference:** E02 - Neo4j.pdf page 29-30

Cypher groups implicitly by all non-aggregate projections in a WITH or RETURN clause, functioning like an automatic SQL GROUP BY over graph patterns. While RETURN performs this grouping as a syntactic shorthand, subsequent filtering (WHERE) or graph pattern matching requires an explicit WITH clause.

## Deduplicating Symmetric Undirected Co-Occurrence Pairs Using Lexicographical Comparison

**Reference:** E02 - Neo4j Exercises.pdf page 3

Finding co-acting pairs through an undirected movie bridge creates mirrored duplicates (A-B and B-A) with identical counts. Enforcing a lexicographical inequality on node properties (such as `a1.name < a2.name`) halves the symmetric results and ensures each distinct pair appears exactly once.

## Naming Complete Path Matches in Cypher

**Reference:** E02 - Neo4j.pdf page 26

To return both a path and derived metrics (such as `length(p)`), the pattern match itself must be assigned to an identifier variable prefixing the pattern (e.g., `p = shortestPath(...)`).

## Raphtory Temporal Reachability vs Static Graph Reachability

**Reference:** E02 Extra - Introduction to Raphtory.pdf page 4

In static graph databases like Neo4j, path reachability between nodes depends solely on topological structure. In Raphtory, reachability is strictly constrained by edge timestamp order: if edge A->B occurs after B->C, no temporal information flow can reach C from A, despite the static graph topology being identical.

## Raphtory Properties vs Metadata Rationale

**Reference:** E02 Extra - Introduction to Raphtory.pdf page 7

Raphtory separates temporal dynamic properties from constant metadata to avoid storing unnecessary update events. Static fields (like customer role) are kept as metadata without history tracking, whereas dynamic values (like bank balances) are stored as properties with event history.

## Zero-Copy Nature of Raphtory Views

**Reference:** E02 Extra - Introduction to Raphtory.pdf page 9

Raphtory views (temporal snapshots across point-in-time or window ranges) are read-only lenses that do not create deep copies of the underlying graph data, conserving memory.

## Exclusive Upper Bound in Raphtory Python Window Querying

**Reference:** E02 Extra - Introduction to Raphtory.pdf page 14

In Raphtory's Python API, `window(start, end)` follows standard Python half-open interval conventions [start, end), where the upper bound `end` is excluded. For example, `window(1, 3)` includes events at t=1 and t=2, but excludes t=3.

## Relationship Count Invariance: Temporal Edges vs Distinct Structural Edges

**Reference:** E02 Extra - Introduction to Raphtory.pdf page 14

In Raphtory, multi-event edges between the same endpoints collapse to 1 under `count_edges()`, but count each occurrence under `count_temporal_edges()`. Consequently, `count_temporal_edges()` can never be less than `count_edges()`.
