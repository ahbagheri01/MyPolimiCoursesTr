# DM2026-07-RepresentationBasedClustering — Additional Professor Notes

**Transcripts:** DM2026-07-RepresentationBasedClustering.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-07-RepresentativeBasedClustering.pdf

## Cluster Characterization and the Concept of Personas

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 2-3

Hierarchical clustering outputs raw cluster label assignments for all data points (e.g., millions of 0s and 1s), which cannot be directly presented to stakeholders. To solve this, practitioners build a 'characterization' of the clusters, such as customer personas in market segmentation (e.g., for supermarket chains like Esselunga or Carrefour). In an academic example, clustering students based on distance from the university, age, and academic score produces distinct personas—such as retired seniors taking degree courses for leisure, or international PhD students who tend to pursue degrees later in life compared to traditional Italian students.

## Centroids vs. Medoids: Synthetic Representations vs. Real Data Points

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 2-3

The representative parameter vector of a cluster differs fundamentally between centroids and medoids. While a centroid is typically the mathematical average across variables and may not correspond to an actual individual in the dataset, a medoid is an actual data point within the cloud that is closest to all other members (e.g., pointing to a specific real student, Giovanni, as the prototypical average student).

## Greedy Nature and Local Optima Terminology

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 4, slide 6

Because exhaustive brute-force evaluation of all O(k^N / k!) partitions is computationally impossible, representative clustering algorithms rely on greedy, hill-climbing heuristics. When discussing optimization pitfalls, the professor emphasizes that the issue should generally be referred to as getting stuck in a 'local optimum' rather than strictly a 'local minimum', as clustering objectives can be formulated as either minimization (SSE) or maximization.

## Oscillation and Convergence Tolerance in K-Means

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 14

In standard implementations, K-Means convergence is not only checked by zero changes in cluster assignments or tiny shifts in centroid locations, but also by stopping when fewer than a specific threshold of points change assignments (e.g., fewer than 0.1% oscillating back and forth between adjacent clusters due to ambiguous borderline positioning).

## Hierarchical Clustering Initialization for K-Means

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 18, slide 47

A powerful initialization strategy for K-Means is to run hierarchical clustering on a small sample of the dataset. Since hierarchical clustering does not assume spherical/globular shapes and the target number of clusters k is already known, one can simply cut the resulting dendrogram at level k and compute the centroids of those sample clusters to initialize K-Means.

## Bisecting K-Means: Splitting Heuristic via Cluster SSE

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 36-46

In bisecting K-Means, the algorithm iteratively splits clusters by applying basic 2-means clustering only to the cluster with the highest Sum of Squared Errors (SSE), as the largest SSE indicates the least compact, most expanded cluster. It halts when further bisections yield negligible decreases in SSE.

## Software Engineering Pragmatics: Modifying Libraries vs. Pre/Post-Processing

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 50

Outlier removal and cluster splitting/merging can theoretically be integrated into the internal iterations of clustering algorithms, but in production data science they are almost always implemented as pre- or post-processing steps. Unless employed in specialized R&D teams building proprietary algorithms from scratch, data scientists should never modify production third-party libraries (such as scikit-learn), as maintaining forks of established libraries introduces immense operational and maintenance liability.

## Non-Monotonicity Artifacts in Single-Run Elbow Plots

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 62-63

While theoretical Within-Cluster Sum of Squares (SSE) should strictly decrease monotonically as k increases (eventually reaching zero when k equals the total number of data points), empirical elbow plots from a single K-Means run frequently exhibit unexpected bumps or increases. This non-monotonic behavior is an artifact of K-Means' stochastic initialization converging to suboptimal local minima at certain values of k, highlighting why multiple runs (or clustering stability methods) are essential before plotting elbow curves.

## Mean Shift: Computer Vision Origins and Basin of Attraction Concept

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 65-76

Mean Shift originated in computer vision for image segmentation, where standard pixel-by-pixel clustering fails because adjacent pixels of varying color intensities within an object (e.g., wood floor, metal, shirts) belong to a single semantic region. Mean Shift operates by treating modal convergence points as 'basins/points of attraction' (drawing an analogy to dynamical control systems), assigning all data points whose trajectory paths lead to the same attraction mode into that cluster.

## Bandwidth Tuning via Knee/Elbow Analysis and Intersection Tie-Breaking in Mean Shift

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 78-81

Selecting the window size (bandwidth h) in Mean Shift cannot be done automatically without trade-offs: setting it too large collapses the entire dataset into one cluster, while setting it too small fragments the data into excessive clusters. Practitioners can tune bandwidth by plotting an internal/external validation metric against bandwidth values to find a 'sweet spot' using knee/elbow analysis. Furthermore, when running Mean Shift in parallel, points caught in intersecting bandwidth windows are typically assigned to whichever shifting window updates first, depending on the software implementation.

## Gaussian Mixture Models vs. K-Means: Shape Adaptation and Soft Assignments

**Reference:** DM2026-2027-07-RepresentativeBasedClustering.pdf, slide 83-99

Gaussian Mixture Models (GMM) via Expectation-Maximization extend K-Means from rigid spherical partitions to probabilistic soft assignments. Whereas K-Means only moves centroid positions to minimize distance, GMM simultaneously shifts the centroids (mean vectors mu_i) and dynamically stretches/reshapes the cluster geometry by adjusting the covariance matrices (sigma_i), assigning each point a posterior probability of belonging to each cluster rather than a binary hard assignment.
