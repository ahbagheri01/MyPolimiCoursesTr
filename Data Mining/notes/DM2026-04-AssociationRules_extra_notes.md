# DM2026-04-AssociationRules — Additional Professor Notes

**Transcripts:** DM2026-04-AssociationRules.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-04-AssociationRules.pdf

## Sequence Mining vs. Sequential Pattern Mining

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 70, 72, 78-80

Sequence mining searches sequences of individual symbols/items (order matters, leading to combinatorial explosion across permutations), whereas sequential pattern mining searches ordered sequences of unordered itemset events over time.

## Practical Advice: Never Re-implement Standard Data Mining Algorithms

Practitioners should avoid re-implementing established data mining and clustering algorithms from scratch in commercial work because standard libraries (e.g., scikit-learn) absorb technical risk and maintenance liabilities that otherwise fall entirely on the developer.

## Clustering: Benchmarking Against Existing Labels

Benchmarking unsupervised clustering against pre-existing ground-truth labels validates whether external labels genuinely reflect the intrinsic geometric or statistical structure of the underlying data.

## Clustering: Distance Matrix vs. Similarity Matrix Conventions

In pairwise data matrix representations, check the main diagonal to determine matrix type: a diagonal of zeros denotes a distance matrix, whereas a diagonal of ones indicates a similarity matrix.

## Graph Bipartite Clique Trawling via Frequent Itemsets

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 65-69

Finding complete bipartite subgraphs K_{s,t} (communities of s sources sharing t targets) can be modeled as frequent itemset mining: mapping each node to the set of outgoing edges treats nodes as transactions and targets as items, where minsup = s and frequent itemset size = t.
