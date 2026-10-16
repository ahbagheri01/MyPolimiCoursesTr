# DM2026-02-DataRepresentation — Additional Professor Notes

**Transcripts:** DM2026-02-DataRepresentation.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-02-DataRepresentation.pdf

## Association Rules

Association analysis originated in the database community driven by the emergence of cheap disk storage for basket data; the widely repeated beer-and-diapers story is an urban legend.

## Association Rules Metrics

Lift measures surprise or unexpectedness of a rule, where values significantly greater than 1 indicate an unexpected association, complementing frequency (support) and certainty (confidence).

## Data Mining Landscape & Competitors

Outlier analysis can be conceptualized as the inverse of clustering; while deep learning handles unstructured data preprocessing, gradient boosting and random forests are its main competitors on tabular tasks.

## Subjectivity and Search in Data Mining

Evaluation of pattern interestingness is frequently subjective rather than objective depending on the user; modeling in machine learning operates as a search across a space of models, analogously to AI state-space search.

## Spurious Correlations and p-value Pitfalls

Relying purely on low p-values across large public datasets can prove completely absurd spurious correlations (e.g., correlating pizza consumption with PhD conferrals), illustrating how statistics can be manipulated without domain validity.

## Data Representation: Tabular Universality

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 3

Unstructured data (sound, images, text) must ultimately be converted into tabular representations because virtually no native learning algorithms operate without tabular input.

## Terminology & Field Identification

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 3

Terminology reflects field background: 'instances' denotes traditional ML, 'data points' reflects statistics, 'observations' indicates empirical/field research, and 'cases/records' points to medicine or databases.

## Attribute Types: Scale Context and Semantics

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 6-8

Categorical strings serve only as human-readable labels that algorithms treat as arbitrary tokens; interpreting numerical properties requires understanding domain context (such as whether zero is arbitrary or meaningful).

## Ordinal vs Categorical Encoding Risks

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 43

Encoding nominal categories as integer ranks introduces an artificial ordering and numerical distance that distorts distance- and weight-based models (like linear models and neural networks), whereas decision trees remain invariant to monotonic orderings.

## Domain Context in Outlier Detection

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 11-12, 36

Outliers are context- and domain-dependent ('in the eye of the beholder'); e.g., large family sizes may appear as statistical outliers in modern Western contexts but remain regular observations in other settings.

## Cyclic Attributes Representation

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 14, 20

To preserve uniform distance between cyclical categories (e.g. Sunday to Monday), attributes can be projected onto a 2D unit circle using sine and cosine coordinates, and these two derived variables must remain paired during feature selection.

## Hierarchical Attributes

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 22

Hierarchical geographic attributes (such as street addresses) can be handled either by choosing a specific categorical granularity level or by converting them into continuous spatial coordinates (latitude and longitude).

## Missing Value Mechanisms & Meaning

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 26-27

Missing values may represent valid informative responses (e.g., undecided voters). MNAR occurs when missingness depends on the unobserved value itself, whereas MAR depends on other observed features.

## Handling Missing Values: First Principle

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 34

When encountering missing data, the primary and preferred initial step is to consult the data owner/client directly about why the data is missing before attempting automated imputation.

## Clustering Limitations

Clustering should generally be avoided or treated as a last resort because cluster definition and evaluation are inherently subjective and prone to unvalidated assumptions.

## Imputation Indicator (Dummy Variables)

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 33

Standard imputation overwrites the signal that a value was missing; pairing imputed values with a binary dummy indicator (1 if imputed, 0 if observed) retains this metadata for the learning algorithm.

## Risks of Listwise Deletion

**Reference:** DM2026-2027-02-DataRepresentation.pdf, page 30

Illustrating the risk of listwise deletion under MNAR: removing incomplete rows in an Italian regional dataset resulted in completely deleting data from two entire geographic regions.

## Library Implementations vs Algorithmic Theory

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 28, 40

While algorithms like decision trees theoretically handle missing or categorical data directly, Scikit-Learn's implementations strictly mandate numerical inputs and do not natively tolerate missing values or strings.

## Label Encoding vs One-Hot Encoding

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 40-46

Label encoding requires saving the fitted mapping dictionary for future test data and risks unintended ordering effects in linear models; one-hot encoding circumvents ordering and mapping retention at the expense of creating high-dimensional sparse representations.

## Discretization by Clustering

**Reference:** DM2026-2027-02-DataRepresentation.pdf, pages 39, 47

Discretization deliberately discards unnecessary continuous precision when minute variations do not impact the target decision; binning values using clustering is considered by the professor to be one of the rare justifiable applications of clustering.
