# DM2026-03-AssociationRules — Additional Professor Notes

**Transcripts:** DM2026-03-AssociationRules.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-04-AssociationRules.pdf

## Disciplinary Origins and Uniqueness of Association Rule Mining

**Reference:** Slide 4

Unlike other core data mining tasks (such as anomaly detection or classification) which stem from statistics and machine learning, association rule mining originated directly from the database systems community (specifically IBM Almaden Research Center). It treats patterns fundamentally as combinatorial counting problems over stored transaction receipts rather than statistical parameter fitting.

## Historical Genesis: Bucket Data and Forgotten Receipts

**Reference:** Slide 4

Association rule mining arose when companies initially discarded or only recorded total spent/VAT amounts from retail transactions due to storage costs. Once disk storage permitted retaining itemized 'bucket' receipts, researchers at IBM Almaden explored what value could be extracted from these saved transactions.

## Real-World Cross-Selling Illustrations: Supermarket Placement and Travel/Loans

**Reference:** Slide 4

The professor provides specific tangible cross-selling examples: Esselunga placing whipping cream directly beside strawberries during strawberry season, nuts and party snacks placed beside liquor and beers, airlines (Ryanair) selling hotel/car hire/insurance alongside flights, and Italian banks obligating home loans to include insurance while pushing their own policies.

## High Confidence Failure Mode: Misleading Association with Ubiquitous Baseline Items

**Reference:** Slide 6, 7, 59

A rule having 100% confidence can still be useless or misleading if the consequent is a universally purchased staple (e.g., milk or bread). The high confidence is driven entirely by the item's ubiquitous baseline frequency in the population rather than any meaningful cross-item association.

## Computational Bottleneck: Disk I/O and SQL Query Access Cost

**Reference:** Slide 20, 21, 39

The fundamental computational bottleneck of brute-force itemset counting is that every single candidate frequency check represents a separate SQL query accessing disk or cloud storage to perform an aggregation, making 2^D database queries prohibitively slow in practice.

## Setting Support Thresholds: The Tradeoff of Near-Zero vs Overly High Values

**Reference:** Slide 23, 24, 58

Selecting the minimum support threshold involves a severe practical tradeoff: setting it near zero prevents any pruning and produces an exponential search space, while setting it too high causes the search to discover only small, ubiquitous items, missing interesting multi-item associations.

## Order Invariance in Itemsets vs Sequence Order Relevance

**Reference:** Slide 20, 80

In standard market-basket association rules, itemsets are strictly unordered sets (AB is identical to BA). In contrast, sequential pattern mining treats order as fundamental, both from a commercial/behavioral standpoint (reading book 3 before book 1 of Lord of the Rings) and technical monitoring (order of system alarms occurring).

## Apriori Candidate Generation: Lexicographic Sorting and Prefix Matching

**Reference:** Slide 31

To prevent generating all combinations or creating known-infrequent subsets, candidates are strictly ordered lexicographically. Only itemsets sharing a common prefix of length k-1 are merged. Furthermore, candidates generated this way must have all their other k-1 subsets cross-checked against the frequent set F_{k-1} before running support queries.

## Eclat Tidset Advantage: Replacing Disk Scans with Set Intersections

**Reference:** Slide 34, 35

In the vertical representation (Eclat), each item is associated with its tidset (transaction ID set). The support of an itemset XY is computed strictly by intersecting tidsets t(X) and t(Y), converting expensive SQL queries/scans into in-memory set intersections, at the trade-off of memory consumption.

## FP-Growth Implementation: Frequency Sorting and Node Header Links

**Reference:** Slide 41, 42, 43

When constructing an FP-tree, transactions are re-ordered by descending item frequency (using lexicographic order as a deterministic tiebreaker). In production implementations, an auxiliary linked list (header table) links all tree nodes sharing the same item name, allowing traversal from the least frequent items upward through their prefix paths without re-scanning the database.

## Recursive Mining of Conditional FP-Trees on Multi-Path Branches

**Reference:** Slide 41, 46, 49

While a single-path projected FP-tree directly yields frequent patterns via subset enumeration, a projected tree containing branching paths cannot simply be enumerated. Infrequent nodes within the projection must be pruned, and if multiple paths persist, FP-growth must be recursively reapplied on conditional subtrees.
