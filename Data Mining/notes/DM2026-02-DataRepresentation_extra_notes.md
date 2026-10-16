# DM2026-02-DataRepresentation — Additional Professor Notes

**Transcripts:** DM2026-02-DataRepresentation.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-02-DataRepresentation.pdf

## Sine and Cosine Encoding for Cyclic Attributes

**Reference:** Slide 20

Cyclic ordinal/numerical attributes (like days of the week, where Sunday loops back to Monday) present a distance discontinuity if encoded linearly (e.g., 0 to 6). To preserve uniform distances between adjacent points on the cycle, map the domain onto a unit circle divided into equal angles (e.g., 360°/7 for days of the week) and represent each day as a pair of coordinates using sine and cosine. A critical modeling consequence of this transformation is that the single original attribute is replaced by two attributes that must always remain together and cannot be separated during feature selection.

## Contextual Definition of Outliers: Domain Relativity in CMC Dataset

**Reference:** Slide 11-12

Identifying whether a value is an outlier requires domain knowledge and cultural context rather than purely statistical filtering. In the Contraceptive Method Choice (CMC) dataset, European students frequently flagged 8 or 10 children as outliers based on European demographics; however, in other countries and historical demographics, families of 8 to 13 children are not abnormal. Outliers are strictly 'in the eye of the beholder.'

## Practical Protocol for Missing Data: Source Inquiry over Modeling and Clustering

**Reference:** Slide 28, 34

Before attempting complex mathematical imputation or clustering, the primary real-world engineering response to missing data is to contact the data provider/client directly and ask why the data is missing. The professor specifically warns against using clustering to handle missing data or discover missingness scenarios ('I would die before I'm doing clustering'), as clustering customer behavior is highly subjective and leaves full responsibility for artifacts on the practitioner.

## Theoretical vs. Practical Library Capabilities for Missing and Categorical Data

**Reference:** Slide 28, 38, 40

Theoretically, algorithms like decision trees and Naive Bayes natively handle missing values and categorical attributes without preprocessing. However, practical software implementations differ sharply: scikit-learn's implementations of decision trees and Naive Bayes historically mandate numerical input and reject missing values, forcing manual preprocessing. In contrast, standard implementations in Java or libraries like LightGBM/CatBoost natively handle them, whereas XGBoost strictly requires numerical data.

## Dummy Variable Tracking for Single Imputation

**Reference:** Slide 33

When imputing missing values with a single summary statistic (like replacing missing temperature readings with the mean), the preprocessed feature appears complete, but information about uncertainty is lost. To preserve the fact that an entry was synthesized rather than observed, practitioners add a binary dummy indicator variable (0 for originally observed, 1 for imputed), allowing downstream models to distinguish actual observations from imputed approximations.

## Practical Differences Between Label Encoding and One-Hot Encoding Pipelines

**Reference:** Slide 43, 46

Label encoding assigns an arbitrary integer (0 to n-1) to categorical levels. If applied, the mapping dictionary must be persistently stored; reapplying label encoding to newly arriving batches risks assigning different numbers to the same categories, creating feature misalignment. Conversely, one-hot encoding produces independent binary columns per category, meaning new data batches can be deterministically encoded without needing to remember an arbitrary integer key mapping.

## Discretization by Clustering in Practice

**Reference:** Slide 39, 47

Discretizing continuous numbers into categorical/ordinal buckets is useful to suppress irrelevant fine-grained noise and variance. A primary legitimate use case for clustering is discretization, where continuous variables naturally cluster into actionable segments (e.g., car rental age groups under 24 and over 70, or extreme income tiers where differences like one million vs. one million and one euro are practically irrelevant).
