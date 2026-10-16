# DM2026-08-DBScanNotebooksAndLinearRegression — Additional Professor Notes

**Transcripts:** DM2026-08-DBScanNotebooksAndLinearRegression.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-08-DensityBasedClustering.pdf, E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-09-LinearRegression.pdf

## Eye-tracking trajectory analysis as a real-world application of DBSCAN

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 5

Density-based clustering is particularly effective for analyzing eye-tracking trajectories recorded while human subjects examine images on a screen. Points represent gaze dwell times and fixation locations. DBSCAN clusters these spatial trajectory points to reveal distinct scanning patterns and identify behavioral differences or cognitive/visual conditions.

## Implementation rationale for including a point in its own epsilon neighborhood

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 7

In the formal definition of DBSCAN's epsilon neighborhood, x is explicitly included in N_epsilon(x). Beyond formal convenience, this simplifies search query implementation in code by avoiding edge cases and boundary checks.

## Flood-fill analogy for density-connected component expansion

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 11

The iterative expansion of density-connected points from core objects functions analogously to the 'bucket fill' tool in image editors: it colors a seed point and expands to contiguous matching neighbors, propagating outward across all directly reachable core points.

## Spatial index structures (kd-trees) and Google Maps spatial query analogy

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 12

Computing epsilon neighborhoods naively requires an O(n^2) nested loop. DBSCAN achieves O(n log n) in low-to-moderate dimensions by indexing points in spatial structures like kd-trees. The professor compares this to querying nearby restaurants on Google Maps for Milan: instead of scanning every restaurant citywide, the system queries only within the immediate spatial region.

## HDBSCAN dendrogram construction and cluster stability

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 17

Standard DBSCAN struggles with datasets containing multi-density regions because epsilon is global. HDBSCAN addresses this by transforming pairwise distances into mutual reachability distances, building a hierarchical dendrogram, and extracting a flat clustering based on cluster stability across density scales.

## K-means over-reliance and lack of cluster stability evaluation in practice

**Reference:** DM2026-2027-08-DensityBasedClustering.pdf, slide 19

K-means is heavily overused as a default clustering method. If K-means performs well, the underlying problem is usually trivially easy. In real-world data, practitioners rarely verify cluster stability, which often reveals K-means solutions to be unstable and unreliable.

## Silhouette coefficient interpretation and extreme values (-1, 0, +1)

For point x_i, silhouette s(i) = (b(i) - a(i)) / max(a(i), b(i)), where a is mean intra-cluster distance and b is mean distance to the nearest alternative cluster. A score near +1 indicates tight clustering within its group; near 0 indicates the point is on the decision boundary; and -1 (e.g., when b=0, isolated at the neighbor's centroid) indicates misclassification where the point is closer to an adjacent cluster.

## Visual silhouette analysis using sorted cluster bands

Relying on the average silhouette score alone can be misleading. Practitioners sort silhouette values within each cluster to plot silhouette bands against the dataset's average score. A clustering is considered flawed if cluster bands fall entirely below the average score or feature substantial negative silhouette tails.

## Connectivity constraints in agglomerative clustering via k-nearest neighbor graphs

Standard agglomerative clustering can prematurely bridge separate clusters when individual points are close. Applying connectivity constraints (restricting merges to k-nearest neighbor graph edges, e.g., k=10) prevents long-range merges and preserves non-convex structures like concentric rings.

## The mean as the baseline predictor and minimum RSS benchmark

**Reference:** DM2026-2027-09-LinearRegression.pdf, slides 4-6, 22

In regression, the mean response y_bar serves as the primary baseline predictor, with total sum of squares TSS = RSS(mean). Any acceptable regression model must achieve an RSS significantly lower than TSS; models that underperform the mean are strictly invalid.

## Exam question analogy for training vs. test set evaluation

**Reference:** DM2026-2027-09-LinearRegression.pdf, slide 29

Evaluating a model on the data used to train it gives an overly optimistic performance measure. The professor compares this to testing students on the exact problem solved on the blackboard the previous day: high performance reflects memorization rather than generalization.

## Non-normal response distributions in linear regression and time-to-service

**Reference:** DM2026-2027-09-LinearRegression.pdf, slide 16

While standard linear regression assumes a normally distributed target variable, real-world data often violates this. The professor cites customer 'time-to-service' / waiting time as a classic example of a right-skewed, heavy-tailed non-normal distribution requiring specialized regression models.

## Why k-fold cross-validation eliminates holdout partition luck

**Reference:** DM2026-2027-09-LinearRegression.pdf, slides 34-36

A single train/test holdout split can be biased by luck: an unusually hard sample ending up in the test set produces overly pessimistic scores, while ending up in the training set produces overly optimistic scores. K-fold cross-validation ensures every data point appears in the test set exactly once, making the averaged performance estimate robust.
