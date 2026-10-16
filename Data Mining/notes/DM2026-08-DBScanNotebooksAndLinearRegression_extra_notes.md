# DM2026-08-DBScanNotebooksAndLinearRegression — Additional Professor Notes

**Transcripts:** DM2026-08-DBScanNotebooksAndLinearRegression.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-08-DensityBasedClustering.pdf, E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-09-LinearRegression.pdf

## Density-based Clustering (DBSCAN)

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 7

Including the point x itself within its own epsilon neighborhood is a computational simplification rather than a mathematical quirk, avoiding edge/special-case handling during spatial queries and searches.

## Clustering Algorithms Choice & Practical Advice

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 19

K-means is often used blindly without verifying cluster stability, and in practice, if cluster stability testing is applied to typical K-means outputs, reliable solutions are rarely found.

## Silhouette Analysis

A silhouette coefficient can reach -1 in the extreme scenario where a point is an isolated centroid of its assigned cluster (a=0) or when distance to an alternative cluster is drastically smaller than to its assigned cluster, proving severe misassignment.

## Silhouette Analysis

Silhouette analysis inherently favors convex clusters because it relies on nearest neighboring cluster distance, mirroring K-means geometric assumptions.

## Silhouette Analysis

True silhouette analysis relies on inspecting cluster-wise silhouette band plots and checking for values dipping below the average or into negative territory, rather than merely relying on a 2D scatter plot or a scalar average.

## Hierarchical Clustering with Connectivity Constraints

Connectivity constraints (e.g., using a k-neighbors graph) in agglomerative clustering restrict merges to an instance's k nearest neighbors, preventing unnatural distant jumps between structures (such as concentric circles).

## Linear Regression Baseline

**Reference:** DM2026-2027-09-LinearRegression.pdf, slides 4-6, 22

The sample mean represents the minimal baseline predictor, establishing the Total Sum of Squares (TSS) against which the regression model's RSS must improve.

## Evaluation and Model Validation

**Reference:** DM2026-2027-09-LinearRegression.pdf, slides 30, 34-35

A single train/test split risks pessimistic evaluation if difficult edge cases end up in the test set without being trained on, or overly optimistic evaluation if difficult cases are trained on and the test set contains only easy samples; K-fold cross-validation ensures every difficult case is tested objectively.
