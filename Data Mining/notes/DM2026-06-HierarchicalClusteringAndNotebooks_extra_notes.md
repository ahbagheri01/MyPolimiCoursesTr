# DM2026-06-HierarchicalClusteringAndNotebooks — Additional Professor Notes

**Transcripts:** DM2026-06-HierarchicalClusteringAndNotebooks.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-06-HierarchicalClustering.pdf

## Hierarchical Clustering Algorithm Trace

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf, slides 14, 22-23, 31

In agglomerative hierarchical clustering, regardless of whether single or complete linkage is used, the next pair of clusters to merge is always selected by identifying the global minimum distance in the active distance matrix. The linkage criterion dictates only how row/column distances are recomputed and updated for the newly formed cluster.

## Cluster Cut Selection & Dendrogram Artifacts

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf, slides 47-49

Standard knee/elbow heuristics or automated dendrogram cutoffs can be artifacts of splitting off single isolated outliers or tiny groups rather than discovering meaningful partitions. Practical clustering workflows require inspecting cluster sizes at each merge step and post-processing the partition by reassigning singleton/noise points to the nearest dense cluster.

## Cluster Stability via Bootstrapping

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf, slides 54-55

To evaluate clustering stability across perturbations, generating subsets via bootstrapping with replacement is preferred over partitioning the dataset (e.g., 50/50 splits), because partitioning halves the effective sample size and introduces statistical dependence between the splits.

## Limitation of Hierarchical Clustering & Cluster Profiling

**Reference:** DM2026-2027-06-HierarchicalClustering.pdf, slide 60

Hierarchical clustering outputs partition labels without providing structural or explanatory descriptions of the clusters. In non-Euclidean spaces where arithmetic means cannot be computed, medoids serve as concrete domain-grounded representatives by minimizing total distance to all points in the cluster.

## Heuristics for Cutting Dendrograms: Inconsistency & Acceleration

Beyond knee/elbow plots, dendrogram cut heuristics include inconsistency—which normalizes the current merge height against the mean and standard deviation of merge distances across a sliding window of prior merges—and acceleration, defined as the second derivative (difference-of-differences) of merge distances.

## Data Inseparability & Visualizing Profiles via Snake Plots

When unsupervised clustering fails to separate known ground-truth classes despite trying various linkages, it demonstrates that the measured attribute space lacks the discriminative signal. Snake plots, which plot Z-score standardized attributes across clusters, provide visual profiling to inspect cluster overlap and distinctiveness across many dimensions.
