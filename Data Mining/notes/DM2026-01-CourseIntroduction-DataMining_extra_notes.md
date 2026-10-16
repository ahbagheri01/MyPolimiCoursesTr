# DM2026-01-CourseIntroduction-DataMining — Additional Professor Notes

**Transcripts:** DM2026-01-CourseIntroduction-DataMining.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-00-CourseIntroduction.pdf, E:\amirhossein\Polimi\POLIMI\Data Mining\Syllabus-20260914\Slides\DM2026-2027-01-DataMining.pdf

## Exam structure, grading rules, and mandatory enrollment

**Reference:** DM2026-2027-00-CourseIntroduction.pdf, slides 7-8

The written exam structure typically consists of five 6-point problems; the professor strictly enforces the enrollment deadline with zero exceptions under any circumstances.

## Course focus vs. Machine Learning and Deep Learning

**Reference:** DM2026-2027-00-CourseIntroduction.pdf, slides 20-21

Linear regression is treated primarily through interpretation of results rather than theoretical derivations; deep learning is explicitly omitted as a dedicated core topic and restricted to pre-processing stages (e.g., text or graph representations).

## Historical motivation for Data Mining (Basket data and storage costs)

**Reference:** DM2026-2027-01-DataMining.pdf, slides 3-4, 7

Data mining and association rules took off in the mid-1990s largely because plunging hard drive storage costs made storing previously discarded transactional receipts ('basket data') economically viable.

## Pattern criteria: Explainability as a prerequisite for actionability

**Reference:** DM2026-2027-01-DataMining.pdf, slide 23

In business churn contexts, explainability is a direct operational prerequisite for actionability; knowing churn probability alone provides no actionable marketing retention intervention without knowing the underlying reason.

## Descriptive vs. Predictive mining and deployment costs

**Reference:** DM2026-2027-01-DataMining.pdf, slides 21-22

In descriptive mining on historical data, overfitting is less of a concern than in predictive settings; predictive mining represents forward commitments where prediction errors can incur contractual financial penalties, and deployed models cannot be patched quickly like software.

## Time distribution in data mining and necessity of algorithmic understanding

**Reference:** DM2026-2027-01-DataMining.pdf, slide 29

Despite data preparation taking 80-90% of pipeline effort, data mining education must emphasize downstream algorithms because data cannot be effectively preprocessed or engineered without knowing the specific biases and operational mechanics of the algorithms receiving it.

## Practical utility of sampling in massive data workflows

**Reference:** DM2026-2027-01-DataMining.pdf, slide 34

Practical big data prototyping involves downsampling to representative subsets to evaluate models rapidly before scaling data volume, alongside domain-specific temporal compression (such as aggregating satellite telemetry from millisecond rates to seconds to reduce training runtimes drastically).

## Trade-offs between linear regression, k-NN, and decision/regression trees

**Reference:** DM2026-2027-01-DataMining.pdf, slides 36-42

For numeric regression tasks, the sample average serves as the simplest baseline; linear regression provides a parametric equation, k-NN memorizes data without an explicit explanatory formula (losing explainability), and regression trees partition space into stepwise rule regions.

## Geometric interpretation and intrinsic difficulty of clustering

**Reference:** DM2026-2027-01-DataMining.pdf, slides 48-51

Clustering is fundamentally the most difficult core mining task because it lacks objective ground-truth feedback, and geometric proximity as a proxy for similarity is heavily task-dependent (e.g., determining whether two retail customer purchase histories are truly similar).
