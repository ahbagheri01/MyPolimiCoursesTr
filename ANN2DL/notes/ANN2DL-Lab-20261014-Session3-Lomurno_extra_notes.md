# ANN2DL-Lab-20261014-Session3-Lomurno — Additional Professor Notes

**Transcripts:** Eugenio Lomurno's Personal Room-20261014 1558-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\Lecture 3\Cross Validation and Tuning.ipynb

## Limitations of Stratified Splitting in Real Feature Spaces

**Reference:** Cell 16

While stratified splitting preserves target class proportions across train, validation, and test sets, the professor highlights that stratification operates on target labels (or regression targets), not on the feature space. In real-world, noisy datasets with skewed or complex feature distributions, stratified splits can still end up with poorly matched feature distributions between splits. Consequently, a model might perform well on validation yet behave inconsistently on test data purely due to unrepresentative feature partitioning.

## Extreme Batch Size Trade-offs: Outlier Sensitivity vs. Convergence to Dataset Mean

**Reference:** Cell 40

To provide intuition on batch size tuning, the professor examines theoretical boundary conditions: setting batch size to 1 results in very slow, noisy training where the final update could steer model parameters entirely in the direction of an outlier. Conversely, setting batch size to the full dataset size computes only one update per epoch along the exact average gradient, causing the model to converge directly toward the average sample and preventing the beneficial stochastic exploration of loss surfaces.

## Grokking Phenomenon in Extended Training

The professor describes 'grokking' as an unexpected phenomenon observed when training very simple networks on simple (often synthetic) problems for extreme epoch counts far past zero training loss. Contrary to standard overfitting expectations—where validation loss permanently diverges after training loss hits zero—extended training can suddenly exhibit a sharp drop in validation loss as the network abruptly reorganizes its weights into structured geometric patterns.

## Handling Layer-Dependent Search Spaces in Hyperparameter Optimization

**Reference:** Cell 60

When optimizing architectures where each layer could independently have a different number of neurons, dynamic variable counts bias meta-models (like Optuna's surrogate models) because the initial layers are sampled in every trial while deeper layers appear rarely. The professor advises either fixing the search variable count or running separate parallel optimization studies for each specific network depth to avoid injecting structural bias into the meta-model.

## Categorical vs. Integer Hyperparameter Representations in Surrogate Models

**Reference:** Cell 60

When answering a student inquiry regarding specifying search options via `suggest_categorical` versus numerical ranges (like integers), the professor clarifies that categorical encoding strips ordinal relationships (greater-than or less-than comparisons) from the optimization meta-model. Even though discrete grids often use categorical suggestions in practice, numerical scales allow Bayesian optimizers to construct smoother, ordered models of the hyperparameter response surface.

## Suboptimality Mindset and Acceptance in Deep Learning

The professor stresses a fundamental philosophical and operational difference between deep learning and fields like operations research (e.g., solving Sudoku, where exact algorithms guarantee finding the global optimum given sufficient steps). In deep learning, practitioners must accept that solutions will virtually always be suboptimal, and tuning procedures are about finding reasonable, robust configurations rather than guaranteed mathematical optima.

## Retraining on Full Data vs. Model Ensembling Trade-offs Post-CV

**Reference:** Cell 70

After identifying the best hyperparameters through cross-validation, the professor presents two main deployment strategies and their caveats: 1) Retraining a single model on 100% of the available data (train + validation + test), which utilizes all information but introduces uncertainty because the optimal epoch identified on smaller splits might not transfer to a larger dataset, and no independent validation set remains to verify stopping; 2) Ensembling the K cross-validation models by averaging their softmax outputs, which eliminates retraining uncertainty but linearly multiplies inference compute and memory requirements.

## Coherence Check Between Validation and Test Splits to Detect Data Leakage or Misalignment

**Reference:** Cell 67

The professor warns that practitioners should examine the coherence between validation and test scores rather than cherry-picking test results. A large discrepancy (e.g., >10%) indicates that split distributions do not align well with unseen data or that data leakage/experimental errors have occurred. In such cases, one must increase the split count (e.g., from 3 to 10) or audit the preprocessing pipeline rather than using the test set to choose the winning model.
