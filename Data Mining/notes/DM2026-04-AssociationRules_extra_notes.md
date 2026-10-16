# DM2026-04-AssociationRules — Additional Professor Notes

**Transcripts:** DM2026-04-AssociationRules.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-04-AssociationRules.pdf

## Association Rule Generation Complexity and Anti-monotonicity

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 52-53

While confidence lacks strict anti-monotonicity across different itemsets, when splitting a single fixed frequent itemset into rules, confidence decreases or stays equal as more items are moved from the antecedent to the consequent. Intuitively, predicting fewer items from more known items has higher or equal confidence than predicting more items from fewer known items. Thus, if a rule predicting one item has confidence below the minimum threshold, all rules derived by moving further items into the consequent also fall below the threshold and can be pruned.

## Rule Generation Worked Numerical Example

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 55-56

The professor provides a step-by-step oral trace of candidate rule testing and pruning on frequent itemset ABDE with min_conf = 0.9, computing explicit ratios: ABD -> E (3/3 = 1.0, kept), ABE -> D (3/4 = 0.75, pruned), BDE -> A (3/3 = 1.0, kept), ADE -> B (3/4 = 0.75, pruned), and systematically pruning descendant rules with larger consequents derived from low-confidence branches.

## Limitations of Support/Confidence and Motivation for Lift

**Reference:** DM2026-2027-04-AssociationRules.pdf, slide 59

Very high confidence rules can be trivial and uninformative if the consequent is globally ubiquitous in the dataset (e.g., predicting 'milk' with 100% confidence simply because almost every shopper buys milk weekly regardless of other purchases). Setting support/confidence thresholds arbitrarily high retains obvious rules while setting them low causes rule explosion; Lift resolves this by measuring deviation from stochastic independence, acting as a measure of 'surprise'.

## Compact Itemset Representations: Maximal vs. Closed vs. Minimal Generators

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 61-64

To condense frequent itemsets: (1) Maximal itemsets guarantee all subsets are frequent but lose exact subset support counts. (2) Closed itemsets act as a downward boundary where every superset has strictly less support, preserving exact supports. (3) Minimal generators have no subsets with the same support (every subset strictly above has strictly higher support). Together, closed itemsets and minimal generators form equivalence classes that allow exact support inference across the lattice.

## Non-Standard Modeling Application: Bipartite Community/Subgraphs via Itemset Mining

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 66-68

The professor explains how to transform graph community detection into transaction itemset mining: directed graph source nodes are treated as transactions, and the target nodes they link to are treated as items in that transaction. Finding a complete bipartite subgraph K_{s,t} is thus mathematically equivalent to mining frequent itemsets where the minimum support is s (ensuring at least s sources link to all targets) and the itemset size is t (the number of shared target nodes/topics).

## Sequence Mining with GSP: Candidate Generation Explosion from Item Permutations

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 72-74

In sequence mining on symbol sequences (such as DNA or alarm logs), support requires sequence order matching rather than simple set inclusion, and multiple occurrences of a symbol within a single sequence are not counted as duplicate support. A key driver of search-space explosion compared to standard itemset mining is that candidate generation must evaluate permutations and symbol repetitions at every level (e.g., evaluating both AA, AG, and GA), drastically increasing the candidate branching factor.

## Distinction Between Sequence Mining and Sequential Pattern Mining

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 70, 78-81

A crucial distinction between sequence mining and sequential pattern mining: sequence mining analyzes ordered sequences of individual symbols/items (e.g., DNA sequences like A-C-G-T or alarm logs), whereas sequential pattern mining analyzes chronologically ordered sequences of unordered itemsets (e.g., an Amazon customer purchasing Lord of the Rings Book 1 in one transaction basket, and Book 2 among a basket of items a week later).

## Subsequence Definition and Notation in Sequential Pattern Mining

**Reference:** DM2026-2027-04-AssociationRules.pdf, slide 82

In sequential pattern notation, sequence size corresponds to the number of transaction itemsets, whereas sequence length is the total number of items across all itemsets (e.g., <(3), (4 5), (8)> has size 3 and length 4). Ordering between itemsets matters chronologically: buying item 3 and then item 8 in separate transactions is distinct from buying {3, 8} together in the same basket.

## Practical Application: Generating Website Navigation Shortcuts via Sequential Pattern Mining

**Reference:** DM2026-2027-04-AssociationRules.pdf, slides 80-81

The professor illustrates a concrete real-world application of sequential pattern mining: tracking user web browsing sessions for a computer hardware company in Italy. By mining common sequential navigation patterns (e.g., common paths visitors took from the homepage to specific product pages like the newest iPhone), the website dynamically placed direct UI navigation shortcuts along those multi-step user paths.

## Sequential Pattern Mining Requires Categorical Data Rather than Time Series

**Reference:** DM2026-2027-04-AssociationRules.pdf, slide 83

The professor clarifies a modeling boundary for sequential pattern mining: it operates strictly on sequences of discrete, nominal/categorical objects (e.g., orders, commands, web alerts). If sequential data consists of continuous numerical values over time (such as room temperature logs), it must not be treated with sequential pattern mining, but rather analyzed using time series analysis methods.

## Practical Advice: Re-implementing Standard Algorithms vs. Using Libraries

Practical industry advice regarding algorithm implementation: in enterprise data mining consulting, never re-implement standard algorithms (e.g., FP-growth, k-means) from scratch unless absolutely necessary. Client databases contain billions of records where modifying schemas duplicates massive data, and custom implementations introduce huge legal/business liability ('every mistake scikit-learn makes is scikit-learn's mistake; every mistake I make in my code is my mistake'). The professor shares an industry anecdote of a telecom team spending a year implementing custom hash tables from scratch, discovering a bug a year later, and having to redo the entire project.

## Clustering: Definition of Similarity, Distance, and Geometric vs. Probabilistic Views

Introductory clustering foundations: clustering aims to maximize intra-cluster similarity while minimizing inter-cluster similarity. Data can be interpreted geometrically (points in an m-dimensional Cartesian space evaluated by distance functions) or probabilistically (modeled via probability distributions). The choice of similarity/distance measure is the single most influential modeling decision determining clustering quality.

## Validation of Unsupervised Clustering Against Ground Truth Labels

Clustering algorithms are unsupervised and discover natural groupings without labels, but in practice clustering quality is evaluated via: (1) internal compactness measures, (2) manual stakeholder review, and (3) benchmarking against existing hidden labels. When an unsupervised clustering matches independent ground-truth labels, it proves that the original labels reflect genuine mathematical structure in the feature space rather than arbitrary annotation.

## Similarity Matrix vs. Distance Matrix Structure

Operational properties of pairwise comparison matrices in clustering: a matrix with zeros along the main diagonal represents a distance (dissimilarity) matrix, whereas ones on the diagonal indicate a similarity matrix. For categorical variables where Euclidean distance cannot apply, simple matching distance assigns 0 if values are identical and 1 if different, which can subsequently be weighted across attributes.
