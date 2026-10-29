# SMBUD03-20260922-DataArchitectures-TowardsBigData — Additional Professor Notes

**Transcripts:** SMBUD03-Marco Brambilla PoliMi-20260922 1407-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-04-data-architectures.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-05-nosql.pdf

## Set-Theoretic Definition and Core Rules of Horizontal vs. Vertical Partitioning

**Reference:** SMBUD-04-data-architectures.pdf, slides 10-12

Data partitioning is formally defined as dividing a set such that the union of all partitions equals the entire set and the pairwise intersection of any two distinct partitions is null (empty). Arbitrary partitioning is impractical because locating data becomes unpredictable. Thus, systems use horizontal partitioning (preserving intact records with all columns for a row subset, avoiding row splitting and allowing single-location writes) or vertical partitioning (splitting columns across partitions while retaining all rows). In vertical partitioning, at least one common key attribute must be preserved across partitions to perform the join required to reconstruct the original tuple. Furthermore, if the number of rows grows beyond single-server capacity, vertical partitioning eventually forces either further vertical splits or secondary horizontal partitioning.

## Use Cases for Vertical Partitioning

**Reference:** SMBUD-04-data-architectures.pdf, slide 11

Although horizontal partitioning (and sharding) is the default in modern databases, vertical partitioning is suitable for specific niche scenarios: (1) workloads where transactions access only a few specific attributes together, ensuring those columns reside locally; (2) analytical queries and aggregations over single columns (e.g., computing the average of an attribute across all entities); and (3) heavy write workloads where splitting columns across different partitions allows parallelized, faster write throughput.

## Trade-offs and Operational Realities of Combining Partitioning and Replication

**Reference:** SMBUD-04-data-architectures.pdf, slides 13-15

Replication creates multiple copies of data for fault tolerance and availability. Systems typically use odd replication factors (most commonly 3, or 5, 7, 9) because 2 copies risk simultaneous failure while odd numbers balance availability against storage overhead (e.g., replicating 20 TB three times requires 60 TB). Real-world distributed architectures apply both partitioning and replication simultaneously, resulting in multiple replicated copies of each partition distributed across physical nodes, often co-locating multiple distinct partition replicas on a single physical node depending on hardware capacity. Partitioning improves scalability and query distribution, whereas replication speeds up reads (load balancing identical requests across copies) but introduces high network overhead and slows down writes due to multi-copy propagation.

## Distinction Between Data Cleaning and Data Enrichment in Data Wrangling

**Reference:** SMBUD-04-data-architectures.pdf, slide 19; SMBUD-05-nosql.pdf, slide 12

Data wrangling prepares incoming ingestion streams before storage. The professor clearly distinguishes cleaning from enrichment: cleaning/validation is subtractive (eliminating dirty, noisy, missing, or mismatched data), whereas enrichment/augmentation is additive (enhancing data value by precomputing derived attributes, especially useful for machine learning, or linking with external/public datasets such as standardized location catalogs).

## Architectural Mechanism of Data Lake Zones as Asynchronous Multi-Step Buffers

**Reference:** SMBUD-05-nosql.pdf, slide 12

Data lake zones (transient, raw, trusted, refined) function internally as asynchronous intermediate storage buffers. Because massive ingestion volumes make synchronous end-to-end processing infeasible, data is dumped into staging queues/stacks, and distinct background worker processes asynchronously pick up, clean, standardize, and advance data from one zone to the next.

## Organizational Justification and Pitfalls of Data Lakes

**Reference:** SMBUD-05-nosql.pdf, slides 10-12

A data lake does not replace operational databases; operational systems continue running as before while concurrently feeding a copy into the lake. The paramount organizational value is centralized discoverability and access: in large enterprises with hundreds of siloed departmental databases, analysts often waste months trying to locate who owns data and obtaining access permissions. A centralized data lake provides a single corporate repository. However, without strict automated cataloging, metadata tagging, and wrangling pipelines, a data lake quickly degenerates into an unusable 'data dump'.

## Schema-on-Write vs. Schema-on-Read: University Transcripts Concrete Example and Quality Trade-offs

**Reference:** SMBUD-05-nosql.pdf, slides 8-10

To illustrate the paradigm shift, consider submitting bachelor's degree exam records (as CSV, JSON, or Word): Under schema-on-write, data must be parsed, transformed, and mapped into rigid tables upfront—wasting engineering effort, discarding original raw details, and risking data loss if requirements change. Under schema-on-read, the raw file is stored as-is; when a specific query arises (e.g., listing course titles), a lightweight, tailored schema/view is created just for that query. This keeps writes simple and fast and preserves the full raw data for future unknown queries. The major downside is that moving away from strict relational constraints shifts all data quality and schema enforcement responsibility entirely onto the software developer or data ingestion pipeline.

## Root Cause of the Object-Relational Mismatch (ORM)

**Reference:** SMBUD-05-nosql.pdf, slide 13

The impedance mismatch occurs because relational database queries return a tabular 'result set' (a collection of relation tuples) rather than instantiated programming objects. Developers in languages like Java or Python are forced to write procedural loops over result sets to manually instantiate objects. Historical Object-Oriented Databases (OODB) in the 1990s attempted to solve this but failed commercially. Modern NoSQL document stores (like MongoDB) succeeded because they store serialized document structures directly aligning with programming objects.

## Non-Obvious Drawbacks and Cost Dynamics of Vertical Scalability

**Reference:** SMBUD-05-nosql.pdf, slides 16-17

Vertical scaling (scaling up) has severe practical drawbacks beyond physical hardware ceilings: (1) costs scale exponentially rather than linearly when entering appliance and specialized hardware tiers; (2) it requires sizing machines for anticipated future peaks, meaning expensive capacity sits idle and wasted; (3) scaling down when demand drops is economically and practically impossible; (4) it creates a single point of failure; and (5) it introduces expensive downtime and operational migration burdens.

## Horizontal Scalability Setup Overhead and Historical Shift of the Cost Threshold

**Reference:** SMBUD-05-nosql.pdf, slides 20-23

Horizontal scaling features linear cost per node, but has a higher initial entry cost and setup complexity due to the infrastructure needed to support distributed clustering and node networking. The economic break-even crossover ('grey area') between vertical and horizontal scaling is dynamic and has dropped dramatically over time: around 2006 (on-premises Hadoop), horizontal scaling was justifiable only at hundreds of petabytes; by 2010 (cloud Hadoop), around tens of petabytes; by 2013 (Spark), at hundreds of terabytes; and currently, horizontal scaling is cost-effective starting at just a few terabytes.

## Business Elasticity and Downscaling Illustrated by E-Commerce Peaks

**Reference:** SMBUD-04-data-architectures.pdf, slide 17

Scalability encompasses both expanding and shrinking dynamically ('elasticity'). Downscaling is not an indication of business failure, but an operational requirement for seasonal business models. For example, Amazon makes a massive share of its annual sales during the two-month Christmas holiday peak; sizing infrastructure permanently to that peak would be economically unviable, requiring dynamic scaling up and down of compute instances and temporary resources.

## Granular Semantic Mapping and Failure Cases in the CAP Theorem

**Reference:** SMBUD-05-nosql.pdf, slides 34-37

The CAP theorem maps across three distinct system layers: Consistency is a property of the data (all copies identical and aligned), Availability is a property of the system (every operational node returns a non-error response), and Partition Tolerance is a property of the network (handling severed communications). A network partition can arise from physical cable cuts during roadworks or major catastrophic events (e.g., during 9/11 when Ground Zero routing hubs collapsed and severed national networks). Because network partitions in large distributed systems are inevitable, Partition Tolerance (P) is mandatory, reducing the real design choice to CP vs. AP. In an AP system, sacrificing consistency explicitly means the database returns incorrect or stale data to queries for the sake of staying online.

## Commercial Rationale for AP Systems: Brand Awareness and Approximate Queries in Web Platforms

**Reference:** SMBUD-05-nosql.pdf, slides 35, 41-43

Modern web companies choose AP (Availability over Consistency) because platform outages cause severe reputational and brand damage, whereas stale or approximate answers go largely unnoticed. For example, when searching for 'dogs' on Instagram or TikTok, returning 9.9 million posts instead of 10 million due to delayed cross-datacenter replication is harmless to user experience. Similarly, Amazon's displayed stock counts (e.g., 'only 7 items left') are often regional approximations. In contrast, total outages (such as Meta's major multi-hour service outage) are catastrophic for brand perception, making high availability the top commercial priority.
