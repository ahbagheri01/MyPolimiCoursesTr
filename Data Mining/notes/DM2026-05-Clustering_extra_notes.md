# DM2026-05-Clustering — Additional Professor Notes

**Transcripts:** DM2026-05-Clustering.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-05-Clustering.pdf

## Tabular Behavioral Patterns vs. High-Level Aggregates

While grouping raw images or text can be intuitive, tabular behavioral data complicates similarity definitions because identical high-level aggregates can conceal opposing underlying behaviors. For example, two grocery shoppers may both spend 200 euros a week, but one buys fresh groceries daily (around 25–30 euros per day) while the other buys everything in a single weekend trip. Similarly, spending 10,000 euros on technology over six years could occur as a single infrequent hardware purchase or distributed across recurring insurance and media subscriptions. High-level aggregates mask temporal and structural nuances that require deliberate distance metric design.

## Jaccard vs. Hamming Semantics on Zeros and One-Hot Encoding

**Reference:** DM2026-2027-05-Clustering.pdf#page=18

The choice between Jaccard distance and Hamming distance hinges on the domain semantics of the value zero. In Jaccard distance, double zeros do not count; zero represents the absence of a measurement or an unpurchased item (crucial in sparse settings like Amazon recommendations where unbought items are practically infinite). In contrast, Hamming distance considers matching zeros as equal positive matches. When categorical features are one-hot encoded (creating dummy variables across mutually exclusive values), Jaccard distance treats zeroes as non-events across sparse options, whereas Hamming counts all shared zeroes as similarity matches. If an attribute has meaningful binary states (like humidity=low vs high encoded as 0 and 1), treating zero as absence alters the intended semantics.

## Scikit-Learn Implementation Nuance for Jaccard Distance with Real Values

**Reference:** DM2026-2027-05-Clustering.pdf#page=19

While textbook definitions of Jaccard distance define it strictly on binary sets, scikit-learn's implementation accepts continuous/real-valued variables. In its calculation, columns where both entries are zero are ignored. When continuous attributes are included (e.g., temperature = 1.0 vs 1.0 or 1.0 vs 2.0), matching non-zero values contribute to the intersection numerator, whereas differing non-zero values count only in the union denominator. Thus, when temperature matches, distance is 1 - 2/3 ≈ 0.333, and when it differs, distance is 1 - 1/3 ≈ 0.667.

## Cosine Similarity Invariance to Document Length Duplication

**Reference:** DM2026-2027-05-Clustering.pdf#page=25

A primary geometric intuition for using cosine similarity in text frequency vectors is scale invariance under document repetition. If an entire text document is duplicated by concatenating it to itself (document + document), the raw word counts double, but the relative frequencies remain unchanged, keeping the document vector pointing in the exact same geometric direction (along the same ray from the origin). Cosine similarity evaluates the angle/projection between vectors, remaining entirely unaffected by document length expansion.

## Preserving Normalization Parameters for Pipeline Deployment vs. Outlier Filtering

**Reference:** DM2026-2027-05-Clustering.pdf#page=30

Whenever data normalization (MinMaxScaler, StandardScaler) is performed, the computed parameters (min, max, mean, standard deviation) must be stored and reused on subsequent incoming data batches to maintain semantic consistency across the pipeline. Furthermore, standard score normalization (StandardScaler) provides an intuitive basis for outlier filtering: data points falling beyond ±6 standard deviations (or 6 to 8 sigma) can be identified as extreme outliers and filtered out before downstream modeling.

## Ratio of Distance Range to Minimum Distance Under the Curse of Dimensionality

**Reference:** DM2026-2027-05-Clustering.pdf#page=37

The plot illustrating the curse of dimensionality plots (d_max - d_min) / d_min against feature count. As the number of dimensions increases (e.g., towards 100 dimensions and beyond), the difference between the maximum distance and the minimum distance between any pair of points rapidly approaches zero relative to the minimum distance. Consequently, the most dissimilar pair of points and the most similar pair of points end up at almost the identical distance, rendering proximity metrics ineffective for partitioning clusters in very high dimensions.

## Practical Usability Limit on Number of Customer Clusters

Although hierarchical agglomerative clustering can mathematically produce any number of clusters from N down to 1, in practical business and marketing deployments, presenting more than 15 to 20 clusters is useless. Marketing agencies cannot operationalize campaigns targeting dozens or hundreds of micro-segments. Practitioners typically prune or inspect only the top levels of the dendrogram to identify between 10 and 15 actionable customer groups.

## Ward's Hierarchical Linkage and Cluster Compactness via SSE Increase

Ward's distance, the default linkage criterion in scikit-learn, measures the proximity between two candidate clusters as the increase in total Sum of Squared Errors (SSE) that would result from merging them. If two compact clusters that are far apart are merged, their combined centroid falls in the empty space between them, leading to a massive increase in SSE. By minimizing the change in SSE at each step, Ward's method favors merging clusters that keep the resulting merged group as compact as possible around its new centroid.

## Generalized Lance-Williams Matrix Update Formula for Hierarchical Linkages

Rather than writing separate update algorithms for each cluster linkage type (single, complete/max, average, centroid, Ward's), practitioners and libraries use a unified recurrence equation (the Lance-Williams formula). By adjusting four parameters in this single update formula, all standard linkage measures can be computed uniformly when updating distance matrices during agglomerative clustering.
