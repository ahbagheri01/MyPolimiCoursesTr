# DM2026-06-HierarchicalClusteringAndNotebooks — Additional Professor Notes

**Transcripts:** DM2026-06-HierarchicalClusteringAndNotebooks.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-06-HierarchicalClustering.pdf

## Post-Processing Single Linkage Hierarchical Clusters via Merge Numerosities

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=47

Relying strictly on automated cutoffs or standard knee/elbow heuristics in single linkage hierarchical clustering can be misleading because single linkage often peels off tiny clusters or single points (noise) one by one. By inspecting the hierarchy/linkage matrix (Z) for the numerosity (sizes) of merged clusters at each step, an analyst can detect when real macro-clusters are truly formed (e.g., stopping at k=10 where three substantial clusters of ~500 points exist alongside single-point noise clusters). The practical post-processing step is to retain the macro-clusters and reassign the isolated singleton/noise points to their nearest substantial cluster.

## Intuition of Between-Cluster Sum of Squares (BSS) as Center of Mass

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=41

In response to a student question about why BSS measures distance between cluster centroids and the overall dataset centroid rather than pairwise cluster distances, the professor explains that BSS views the overall dataset mean as the global 'center of mass' (analogizing it to finding the center of mass in the lecture room). BSS increases when cluster centroids are placed far outward from this central reference point, whereas pairwise separation across clusters is handled by metrics such as the silhouette coefficient.

## Structure and Interpretation of SciPy Hierarchical Clustering Linkage Matrix Z

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=14

When performing hierarchical clustering in Python (SciPy/scikit-learn), the output linkage table Z is an (N-1) by 4 matrix representing the full dendrogram merge sequence. Each row contains four elements: cluster ID 1, cluster ID 2 (the two clusters merged), the distance between them at the time of merging, and the resulting cluster size (number of original points contained). This structure allows programmatic post-processing to inspect cluster numerosity and calculate metrics like inconsistency across rolling merge windows without relying solely on visual dendrogram plots.

## Heuristics for Cutting Dendrograms: Acceleration and Inconsistency

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=44

Automated cut recommendations in libraries like SciPy/scikit-learn often use inconsistency (comparing the merge height against the mean and standard deviation of a window of previous merges) or acceleration (the second derivative of merge distances across steps). A sharp spike or high acceleration indicates a jump in merge distance compared to preceding steps, which the library uses to suggest cluster counts (e.g., suggesting k=2).

## Failure of Unsupervised Iris Clustering to Separate Versicolor and Virginica

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=40

When evaluating clustering on Iris data externally against ground-truth labels, single and complete linkage cleanly isolate Iris Setosa (50 pure instances) because the raw features distinctly separate it. However, they consistently fail to cleanly partition Versicolor and Virginica into separate 50-item clusters, splitting them into uneven mixtures or singleton splits. This demonstrates that if an unsupervised pipeline cannot recover known labels across multiple linkage variations, the raw feature space itself lacks sufficient discriminatory information to distinguish those classes without transformation or supervised guidance.

## Visualizing High-Dimensional Cluster Profiles with Snake Plots

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=59

To describe and interpret clusters when datasets have many attributes, analysts can use snake plots. In a snake plot, the x-axis represents the normalized attributes (typically standardized via Z-score so variables with different units/ranges can be compared on the same scale), the y-axis represents the attribute values/distributions, and each line or profile is colored by cluster. Distinct, non-overlapping profiles indicate clear cluster separation, whereas crisscrossing lines highlight attributes where clusters overlap.

## Clustering as an Enumerative Labeling and the Need for Cluster Descriptors

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf#page=59

Hierarchical clustering only assigns arbitrary numeric partition labels (e.g., 0, 1, ..., k-1) without providing an intrinsic semantic explanation or description of what each cluster represents. In practical domains like marketing or student dropout prevention, enumerating members without explaining cluster characteristics leaves stakeholders unable to act. Analysts must therefore post-process clusters to derive profiles—such as persona narratives (e.g., 'DINKs'), feature means in Euclidean spaces, or medoids in non-Euclidean spaces—functioning as a form of cluster explainability.
