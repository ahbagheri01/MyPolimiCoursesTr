# SMBUD02-20260917-RelationalDBs-SchemaTransactions — Additional Professor Notes

**Transcripts:** SMBUD02-Marco Brambilla PoliMi-20260917 1546-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-03-ER-Relational.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-04-data-architectures.pdf

## Persistence of Relational Databases and Market Context

Despite the industry focus on big data and NoSQL technologies, roughly 90% of the market is still dominated by relational databases and SQL, particularly within large and highly structured enterprise environments.

## Domain-Dependent Modeling: Address Attribute vs. Entity

**Reference:** SMBUD-03-ER-Relational.pdf, page 15

Design choices such as whether a concept is modeled as an attribute or an entity depend directly on application requirements. For example, an address is naturally modeled as an attribute in a university student system, but becomes a primary entity in a geospatial platform like Google Maps.

## Attribute Cardinalities and Temporal Absence of Values

**Reference:** SMBUD-03-ER-Relational.pdf, page 18

Cardinalities can be placed directly on attributes to reflect real-world lifecycles; for instance, assigning a cardinality of (0,1) to an exam grade ('mark') captures the fact that the grade does not exist during the course and only appears once the course edition finishes.

## Pre-Relational Database History: IBM Hierarchical Model and NASA

**Reference:** SMBUD-03-ER-Relational.pdf, page 26

Prior to Codd's 1970 introduction of the relational model, database systems used hierarchical models (such as IBM's), which were originally funded and developed to track millions of missile subcomponents for NASA.

## Semantic Difference Between 'Relationship' and 'Relation'

**Reference:** SMBUD-03-ER-Relational.pdf, pages 10, 26-27

Despite sharing the same root, an ER 'relationship' denotes a semantic association between conceptual entities, whereas a relational 'relation' refers strictly to the mathematical definition of a relation as a subset of a Cartesian product of domains (implemented as a table).

## Codd's Intuition: Eliminating Positional Dependencies with Named Attributes

**Reference:** SMBUD-03-ER-Relational.pdf, pages 29-30

In raw mathematical relations, attributes are strictly positional, meaning columns are identified purely by index. Codd's breakthrough was adding explicit attribute names (column headers) so tuples became non-positional, enabling columns to be reordered without losing semantic meaning.

## Real-World Anomaly of Null Values: The 'NULL' Vanity License Plate

**Reference:** SMBUD-03-ER-Relational.pdf, page 34

The real-world ambiguity of null values is illustrated by a driver who registered the custom license plate 'NULL'; when police departments recorded citations with missing plate numbers as NULL, the integration software converted these into string literals matching his plate, directing thousands of nationwide fines to his address.

## Bidirectional Foreign Keys in (1,1)-(1,1) Mappings Cause Dangerous Redundancy

**Reference:** SMBUD-03-ER-Relational.pdf, pages 49-50

In a strict one-to-one (1,1)-(1,1) relationship (e.g., Sale and Cash Receipt), posting foreign keys in both directions is dangerous because dual storage risks data misalignment and inconsistency during updates. Only one direction must be chosen.

## ER Decomposition Resolving Star Trek Drinkers Redundancy

**Reference:** SMBUD-03-ER-Relational.pdf, pages 65-66

The unnormalized Star Trek table (Janeway living on Voyager liking Budweiser and WickedAle, Spock liking Budweiser) produces update anomalies because functional dependencies (name->addr, name->favdrink, drinkLiked->manf) cause redundant repetitions. Modeling through ER entities (Person, Drink, Manufacturer) decomposes this cleanly into three entity tables and one many-to-many relationship table ('likes'), eliminating all duplication.

## Long Lifespan of Relational Schemas in Enterprise Systems

**Reference:** SMBUD-04-data-architectures.pdf, page 3

The strict typing and rigidity of relational schemas were deliberately engineered to safeguard enterprise data integrity across decades. Many core institutional databases (such as banking systems built around 1980) remain in active production without schema alterations because their rules prevent user error over 20 to 50 years.

## Data Locking and Race Conditions in Multi-User Concurrency

**Reference:** SMBUD-04-data-architectures.pdf, page 4

Concurrent read operations do not compromise data integrity, but overlapping write operations create race conditions where execution order becomes non-deterministic and values can be silently overwritten. To prevent this, systems enforce data locking, serializing concurrent writes into sequential operations.

## Rollback and Redo Mechanics in Transactional Atomicity

**Reference:** SMBUD-04-data-architectures.pdf, pages 5, 9

If a transaction is interrupted mid-execution (e.g., system crash), the recovery process first attempts a redo operation upon restart. If completion remains impossible, it performs an undo (rollback) of all partial operations to guarantee that intermediate, broken states never persist.

## Isolation Violation and Cascading Domino Effects

**Reference:** SMBUD-04-data-architectures.pdf, page 9

Transaction isolation ensures intermediate uncommitted states remain invisible to other concurrent transactions. Without isolation, a transaction reading uncommitted data that subsequently rolls back creates cascading aborts (the domino effect), potentially crashing millions of concurrent processes.

## Computational and Metadata Overhead of ACID Guarantees

**Reference:** SMBUD-04-data-architectures.pdf, page 4

ACID compliance is computationally expensive: maintaining atomicity, consistency, and isolation requires substantial metadata tracking and internal lock management subsystems, resulting in significant system overhead that NoSQL databases specifically aim to relax for performance.
