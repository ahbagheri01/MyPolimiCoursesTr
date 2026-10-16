# DM2026-05-Clustering — Additional Professor Notes

**Transcripts:** DM2026-05-Clustering.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-05-Clustering.pdf

## Implementation-Specific Behavior of Jaccard Distance with Continuous/Real Values

**Reference:** Slide 19

While standard theoretical definitions treat Jaccard distance strictly over binary sets where (0,0) pairs are ignored, standard library implementations (such as scikit-learn) extend Jaccard distance to real-valued data. Specifically, attributes with matching non-zero continuous values are counted toward the numerator (intersection), while non-matching values still enter the denominator (union), demonstrating how library implementations may silently diverge from textbook definitions.

## Semantic Asymmetry of Zero: One-Hot Dummy Variables vs. Categorical Codings

**Reference:** Slide 18, 20-22

Zero holds fundamentally distinct semantic meanings depending on encoding context: in one-hot encoded dummy attributes, zero signifies the complete absence of a value (making Jaccard distance semantically appropriate by ignoring joint zeros), whereas in binary/ordinal encodings of attributes (e.g., humidity low vs. high encoded as 0/1), zero represents an active, observed measurement state (making Hamming distance or matching metrics relevant).

## Consistency Requirements for Pre-processing and Scaling State Across Batches and Deployment

**Reference:** Slide 30

Any data transformation or scaling mapping (e.g., category-to-integer mappings, MinMaxScaler bounds, or StandardScaler mean and variance) constitutes learned state that must be stored and reused consistently on newly incoming batches during deployment. Fitting a new scaler on subsequent operational data breaks coordinate comparability.

## Outlier Truncation via Standard Deviation Bounds in Pre-processing

**Reference:** Slide 30

Standard score (Z-score) normalization enables systematic outlier filtering prior to distance computation by evaluating points against sigma multiples under normal distribution assumptions; observations falling outside extreme thresholds (e.g., beyond ±6 standard deviations from the zero-mean center) are formally trimmed as non-representative outliers.

## Practical Upper Bound on Cluster Cardinality for Business Reporting

**Reference:** Slide 7

Although hierarchical agglomerative clustering mathematically yields a full continuum down to individual data instances or any fine-grained K, actionable customer segmentation in industry cannot absorb large numbers of partitions. Business and marketing requirements dictate pruning the hierarchy to display no more than 15–20 top-level clusters.

## Hierarchical Clustering Sampling Strategy for Large Datasets

**Reference:** Slide 33

Because agglomerative hierarchical clustering requires O(N^2) memory for pairwise distance storage and O(N^3) execution time, it cannot scale directly to large datasets (e.g., millions of records). In practice, practitioners run the deterministic hierarchical method on a representative sample of the data to extract the underlying structural taxonomy and discover hierarchy before applying scalable partitioning methods.

## Geometric Mechanics and Objective of Ward's Linkage Method

**Reference:** DM2026-05-Clustering.pdf

Ward's hierarchical clustering linkage quantifies proximity not by geometric point separation, but by the net increase in Sum of Squared Errors (SSE / variance) resulting from merging two clusters. Merging two tight clusters that are distant from one another incurs a large SSE penalty due to the displaced shared centroid, meaning the algorithm prioritizes unions that maintain cluster compactness.

## Lance-Williams Generalized Update Recurrence Intuition

**Reference:** DM2026-05-Clustering.pdf

Rather than necessitating distinct algorithmic procedures for single linkage, complete linkage, average linkage, and Ward's method, all classical inter-cluster update metrics can be computed via a single parameterized algebraic recurrence formula by setting specific parameter weights.
