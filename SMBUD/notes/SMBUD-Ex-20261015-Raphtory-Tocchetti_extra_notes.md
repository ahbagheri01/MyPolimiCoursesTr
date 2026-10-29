# SMBUD-Ex-20261015-Raphtory-Tocchetti — Additional Professor Notes

**Transcripts:** Andrea Tocchetti's Personal Room-20261015 1602-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E02 - Neo4j\E02 Extra - Introduction to Raphtory.pdf

> **Coverage notes:** The recording starts mid-session, directly on the Raphtory slides (any earlier part of the session is not in the transcript). All slides of the Raphtory deck were discussed.

## Motivating Use Case: Detecting Money Laundering Through Money Cycles

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.2–3

The TA works for the company that develops Raphtory (one reason he chose this technology). A concrete use there is looking for **money cycles between people**: by analysing how money moves across different bank accounts over time, money laundering can be identified. He contrasted this with the Neo4j movie graph used earlier in the course, which is a single static picture with no timeline/history of when nodes and relationships appeared.

## Raphtory Is Natively Temporal, Neo4j Is Not

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.2

According to the TA, Raphtory is currently the only technology that is **native** for temporal graphs. Neo4j has done something similar, but only through an extension: Neo4j is natively static, while Raphtory is designed from the ground up to be temporal. He presented temporal databases as more useful than static ones because they let you identify different types of interactions over time.

## Time Ordering: Context Flow and Snapshots

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.4

- If A talks to B at t=1 and B talks to C at t=2, then when B speaks to C it carries **additional context coming from A**. If instead A→B happens at t=2 and B→C at t=1, B has no context from A when talking to C.
- Observing the graph at a single moment shows only what existed by then. At t=1, the first case contains only A and B, and the second case contains only B and C. The graph should be imagined as something that evolves and expands over time.

## Loading Data: Edges First, Nodes Created Implicitly

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.5

- Compared to Neo4j, the only extra data needed is a **timestamp** for every node and every relationship (above all for relationships).
- Loading order is reversed with respect to Neo4j. In Neo4j you usually import the nodes first. In temporal technologies like Raphtory you define the **relationships first**: adding "t=1, Alice → Bob" creates the relationship *and* the two nodes Alice and Bob. A relationship is created even if its nodes have no data yet, and node data can be populated later.
- To link the two datasets, the relationship dataset's source/destination values must be the IDs used in the node dataset (e.g., node ID "Alice" with all its attributes).
- Every data instance needs a timestamp: if one is missing, the system fails and reports that it cannot load the data.

## Time Comes From the Data, Not From a Clock

Answering a student question on whether time keeps advancing on its own: time is a **property of every entity/relationship** in the graph, and it moves forward only when there are events. If the data spans 2022–2024, the maximum time in the graph is the last date in 2024 present in the data (timestamps are in milliseconds). "Time" in Raphtory is not wall-clock time. It is defined entirely by the data.

## Choosing Between Property and Metadata

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.7

Use metadata for values that will not change regardless of the node's interactions (Bob's `role = customer`). If you think the value **might change in the future**, store it as a (temporal) property instead. The reason given: every update to a node's data is recorded as a separate entry in its timestamped history, which is what properties provide and metadata does not.

## Layers: Baboon Example and Why to Use Them

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.8

- The resting/playing/grooming figure comes from a **public dataset of baboons interacting with each other**, with one layer per kind of behaviour.
- Analogy: layers are like overlaying several transparent film sheets one on top of the other. Over time you see the different behaviours without having them all merged into a single graph.
- Why this helps: to query only how the baboons rest together, you do not need to filter every node/relationship while the query runs. You pick the resting layer and run the query on it, which selects all relationships, across time, stored in that layer. The full graph still contains all layers and all their relationships, at every timestamp.

## Layers Exist Only When They Have Relationships

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.8

A layer starts existing only when there is a relationship on it: you cannot create a layer without relationships. Asked how layers are implemented, the TA said he does not work on Raphtory's low-level core, but he believes layers are stored as properties alongside the data (his tentative answer, not a definite statement).

## Using Views: Snapshot and "Only After" Analyses

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.9

- `at(t)`, e.g. `at(1000)`, returns a **static representation** of the graph as it was at that moment.
- `before(t)` / `after(t)` check what happened before or after a timestamp. Example: to look for money laundering only after 2026, take `graph.after(t)` with t at 2026 and run the analysis on that view.
- These functions let you slice the graph into the part relevant to your analysis.

## Persistent Graph Example: An Engagement

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.11

In a persistent graph, an edge that has not been deleted is considered to keep existing until it is deleted. The TA's example: an "engaged" relationship lasts from when two people get engaged until they are no longer engaged (deletion). If they later get back together, the edge is added again. Event graphs, by contrast, store individual spikes (messages, payments).

## PageRank Over Windows: Finding Important Users Over Time

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.12

Running PageRank per time window shows how important a node was in each window. Suggested application: **online communities** on social media (Facebook, X, etc.). Connect people with their posts, track how they interact over time, and identify the most important node in each window (B in [1,4), C in [4,7), E in [7,10) in the slide example). The ranking changes because it depends on the frequency of each node's incoming and outgoing relationships within the window.

## Building a First Graph: Setup and What You Do Not Need to Add

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.14

- Install with `pip install raphtory`. The library is free to use. There is also an enterprise edition with small differences, aimed at companies.
- `Graph()` creates an **event graph**. For a persistent graph you must import `PersistentGraph` and create `g = PersistentGraph()`.
- The example only calls `add_edge`, never adding nodes, because these nodes have no properties. You add node data only when nodes have properties. Otherwise the nodes are just the IDs used as source and target.
- In `add_edge(time, source, destination, layer=..., properties=...)`, relationships can carry properties, e.g. the amount of money moved in a transaction.

## Reading the Results of the First-Graph Example

**Reference:** E02 Extra - Introduction to Raphtory.pdf, p.14

- `count_edges()` = 3 counts edges as if the graph were static. `count_temporal_edges()` = 4 also counts how many times each interaction happened, so Alice→Bob (t=1 and t=4) is counted twice.
- `window(1, 3)` includes time 1 and **excludes** time 3, so only the t=1 and t=2 edges remain, giving 2.
- `layer("payment")` keeps only the Alice→Carol payment edge, giving 1.
