# SMBUD06-20261013-GraphDB-Wrapup-DocumentDB — Additional Professor Notes

**Transcripts:** SMBUD06-Marco Brambilla PoliMi-20261013 1405-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-06-graphDB-neo4j.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-07-document-db.pdf

## Neo4j Physical Storage Architecture: Separation of Topology from Values

**Reference:** SMBUD-06-graphDB-neo4j.pdf, page 47

Neo4j's native storage architecture strictly separates the physical files that define graph topology from the files that contain descriptive attributes/values. Nodes, relationships, and relationship types are persisted in dedicated files to define graph shape and enable topology pattern matching, whereas properties are stored in separate files. Furthermore, because files on disk are sequential while graphs inherently have a topological structure, the execution engine heavily exploits multi-layer caching across disk, the operating system file cache, and the Java Virtual Machine (JVM) object cache to keep direct adjacency structures and query processing in main memory.

## ACID Log Management and Transaction Guarantee in Neo4j

**Reference:** SMBUD-06-graphDB-neo4j.pdf, page 47

To provide full ACID transactional guarantees, Neo4j incorporates a write-ahead transaction log where every operation is logged sequentially step-by-step prior to physical execution, allowing operations to be recovered or rerun. The dedicated transaction management layer coordinates these logs to guarantee transaction properties across the system.

## APOC Library and User-Defined Stored Procedures in Cypher

**Reference:** SMBUD-06-graphDB-neo4j.pdf, page 62

Neo4j supports user-defined business logic via stored procedures (implemented in languages such as Java and packaged into JAR files placed in the database environment), invoked directly inside Cypher queries via the CALL operator. The professor highlights APOC (Awesome Procedures on Cypher) as a standard extension library providing utility procedures for data import/export, data management, graph transformations, and light graph analysis, noting this expands expressive power even though custom stored procedures will not be tested in the exam.

## Duality Between Graph Databases and Document Databases

**Reference:** SMBUD-07-document-db.pdf, page 2

Graph databases and document-oriented databases represent exact opposite (dual) design philosophies. Graph databases are required when information and value reside predominantly in complex relationships and topological connections between objects. In contrast, document databases are optimal when data value resides inside comprehensive, complex, self-standing business objects where users work atomically on one document at a time without traversing external relationships.

## Motivating Business Objects and Relational Granularity Mismatch

**Reference:** SMBUD-07-document-db.pdf, page 7

Document databases are motivated by real-world business objects (such as invoices, purchase orders, product sheets, or customer profiles). In relational databases, normalized schemas decompose a single business object across tens of granular tables (e.g., separate tables for orders, order lines, customers, credit cards, addresses), forcing the system to perform expensive multi-table joins every time an object is viewed or printed. Even relational views fail to solve the underlying performance penalty because the underlying storage remains fragmented and non-native.

## Mapping Business Objects into JSON: Modeling Array of Subdocuments

**Reference:** SMBUD-07-document-db.pdf, page 7

When converting a complex business object into JSON, hierarchical multi-valued components are modeled through combinations of arrays and nested subdocuments. For example, order line items must be represented as an array of subdocuments (`line_items: [ {productId, quantity, price}, ... ]`) using square brackets enclosing curly brackets. In contrast, payment details (e.g., credit card number, expiration) are modeled as a single nested subdocument or flat properties depending on design choices.

## Subdocuments Lack Technical Identifiers

**Reference:** SMBUD-07-document-db.pdf, page 20

In document databases like MongoDB, embedded subdocuments are strictly property values within the parent document rather than independent entities. As a consequence, embedded subdocuments do not possess their own unique `_id` field; the `_id` is an exclusive technical requirement of the top-level root document.

## Practical Guideline for Nesting Depth in Document Databases

**Reference:** SMBUD-07-document-db.pdf, page 20

While document databases technically permit arbitrary levels of document nesting, practical usability dictates keeping embedding shallow. The professor provides an explicit rule of thumb: embed at one, two, or three levels, and typically never exceed four levels of nesting, as deeper hierarchies become unmanageable and impractical to query and update.

## Embedded Documents vs. Document References: Trade-Offs and Philosophy

**Reference:** SMBUD-07-document-db.pdf, page 23

Choosing between embedding subdocuments and referencing separate documents via IDs involves critical trade-offs. Embedding optimizes read performance and atomicity when documents are read whole, but it introduces severe data duplication (denormalization) and consistency update hazards (e.g., modifying a shared credit card across multiple orders). Conversely, using references avoids duplication but essentially reconstructs the relational model and violates the core document database principle of self-contained, self-standing documents. If an application requires frequent cross-document joins, updates across shared data, and full domain modeling, a relational database is appropriate instead.

## Design Philosophy: Domain Modeling (Relational) vs. 90% Query Probability (Document)

**Reference:** SMBUD-07-document-db.pdf, page 23

Relational schema design focuses on modeling the general real-world domain independently of future queries, providing flexibility to answer any query via arbitrary joins. In contrast, document database schema design requires knowing the application workload in advance: the designer chooses a fixed composite document shape based on the 'maximality of usage probability' (optimizing for the 90–95% predominant read pattern), intentionally accepting suboptimal performance for the remaining 5–10% of access patterns.

## Philosophical Rejection of Joins and Multi-Document Transactions

**Reference:** SMBUD-07-document-db.pdf, page 14

Although document databases may add support for joins or multi-document transactions at the technical level, the underlying philosophy strongly discourages their use. A document system achieves maximum efficiency when queries and updates operate atomically on a single self-contained document. If an architecture routinely relies on multi-document transactions and joins, system performance collapses and the design negates the core purpose of adopting a document store.

## Historical Genesis of JSON from Web Standards

**Reference:** SMBUD-07-document-db.pdf, page 7

The professor explains why JSON originated as a textual format rather than a binary format common to databases: it was invented specifically for the web browser ecosystem. Early web architecture had HTML for structure, CSS for presentation, and JavaScript for client-side logic, but lacked a native lightweight data representation. JSON (JavaScript Object Notation) was conceived as a text-based object serialization format native to JavaScript in the textual web environment, and its subsequent success in eliminating object-relational impedance mismatch led to its adoption in databases.

## BSON Role: Internal Engine Optimization vs. User JSON Interface

**Reference:** SMBUD-07-document-db.pdf, page 17

While JSON serves as the human-readable text exchange format between clients and MongoDB, disk storage and query execution internally rely on BSON (Binary JSON). BSON overcomes the substantial parsing overhead and ASCII byte bloat of text files, and incorporates features like length prefixing to accelerate document scanning. However, language drivers handle the translation transparently, meaning software developers work entirely with JSON objects in code and never directly interact with raw BSON files.
