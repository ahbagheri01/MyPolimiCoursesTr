# DM2026-07-RepresentationBasedClustering — Additional Professor Notes

**Transcripts:** DM2026-07-RepresentationBasedClustering.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-07-RepresentativeBasedClustering.pdf

## Cluster Characterization and Personas

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 2-3

While slides state that each cluster is summarized by a point or parameter vector, the oral lecture contextualizes why this is necessary: raw cluster output is just numeric label vectors across millions of points, which cannot be presented directly to stakeholders without synthesizing them into personas or parameter summaries.

## Centroids vs. Medoids

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 2-3

Centroids represent the mathematical average feature vector of the points, whereas medoids correspond to an actual, existing data point within the dataset nearest to all other points in the cluster.

## Greedy / Hill-Climbing Nature of Partitioning Algorithms

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 4, 6, 15

Partitioning methods act as greedy hill-climbing heuristics navigating towards local optima because evaluating all O(k^N / k!) possible partitions for a global optimum is computationally intractable.

## K-Means Geometric Assumption and Spherical Clusters

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 52, 54, 57, 79

K-Means' geometric limitation to spherical/globular shapes directly stems from assignment via Euclidean distance to a single central point, causing it to fail on elongated or non-axis-aligned structures.

## K-Means Stopping Criteria and Oscillation Handling

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 14

Beyond standard centroid convergence, practical K-Means implementations apply an oscillation tolerance threshold (e.g., stopping when <0.1% of boundary points swap between clusters).

## K-Means Initialization Heuristics and Dendrogram Seeding

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 18, 47

A concrete hybrid initialization method involves hierarchically clustering a small data sample, cutting the resulting dendrogram at K, and computing the centroids of those sample clusters as seeds for K-Means.

## Bisecting K-Means

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 36

Bisecting K-Means iteratively selects the cluster with the largest sum of squared errors (SSE) and splits it using 2-means, progressively increasing clusters until reaching K.

## Why Outlier Removal / Heuristics Are Done in Pre/Post-Processing

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 50

Outlier detection and cluster merging/splitting are performed as pre- or post-processing steps because production data science relies on standardized, verified libraries (e.g., scikit-learn); modifying core library source code introduces unacceptable liability and bug risks.

## Stochastic Elbow Analysis Bumps

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 62

Elbow plots of WCSS/SSE across increasing K should theoretically decrease monotonically; non-monotonic bumps in empirical curves indicate single stochastic runs getting trapped in inferior local minima, highlighting the necessity of multiple runs per K.

## Mean Shift Clustering

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 66, 79, 81

Mean Shift originated in computer vision for image segmentation, operating as a non-parametric mode-seeking density algorithm with O(N^2) complexity.

## Mean Shift Bandwidth Selection and Overlap

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 80

Bandwidth in Mean Shift can be tuned via an elbow-style curve against validation metrics; when search windows overlap across boundaries, point assignment is determined by the update order of the specific implementation.

## Expectation-Maximization and Gaussian Mixture Models

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slides 83-84

GMM/EM conceptually generalizes K-Means from rigid spherical boundaries to soft probabilistic clustering by optimizing not just cluster positions (means) but also cluster geometry (covariance matrices) and component proportions (priors).
