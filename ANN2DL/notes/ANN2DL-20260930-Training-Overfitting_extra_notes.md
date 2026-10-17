# ANN2DL-20260930-Training-Overfitting — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20260930 1617-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\03 - NeuralNetworksTraining.pdf

## Limitations and Practical Reality of the Universal Approximation Theorem

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 2

While Hornik's theorem guarantees that a single hidden layer can approximate any continuous function, it provides an existence proof rather than a constructive guide. In practice, finding weights via gradient descent yields only local minima, approximating arbitrary datasets directly could require placing roughly a neuron per data point, and without explicit regularization, such maximum-capacity networks completely lose generalization on unseen data.

## Stratified Sampling Strategy for Continuous Regression

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 4

Stratified sampling is standard in classification to preserve label distributions, but when stratifying continuous target values in regression, a practical procedure is to sort the dataset by the continuous target output and uniformly sample (e.g., every 10th item across the sorted range) into splits. This guarantees balanced coverage across low and high values.

## Temporal Splitting Constraints and Failure of Shuffling in Time Series

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 4

Random shuffling and sampling cannot be applied to time series data because taking points indiscriminately across the timeline converts a forecasting/prediction problem into an interpolation task. Validation and test sets must strictly be reserved from the final contiguous segments of the chronological timeline to simulate predicting the future, which inherently exposes the model to temporal distribution shift.

## Diagnosis and Actionability when Validation and Test Metrics Diverge

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 5

If validation and test performance diverge significantly, the root cause is almost invariably a dataset partition failure—such as neglecting stratified sampling or failing to shuffle—which breaks the assumption of identical underlying distributions. Because the test set must remain untouched, the only valid remedy is to re-inspect the raw data distributions/preprocessing and re-partition from scratch.

## End-Stage Training Retraining Protocol on Combined Train and Validation Sets

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 5

Once all structural hyperparameters and training schedules (exact number of epochs, learning rate) are finalized via validation, standard competitive practice permits merging the validation set back into the training data to squeeze maximum signal from available samples. Crucially, the model must be trained for the exact number of epochs found during model selection rather than retrained indefinitely.

## Scalability Trade-Offs in Resampling: Why Modern Deep Learning Relies on Hold-Out Sets

**Reference:** 03 - NeuralNetworksTraining.pdf, slides 6-10

Techniques like Leave-One-Out (LOOCV) and K-fold cross-validation do not scale to large neural networks, as training five folds that take hours or months each multiplies computational overhead linearly. In modern deep learning with large datasets, standard industry methodology defaults to a single random initialization run using a hold-out validation set rather than multiple restarts or K-fold ensembles.

## Computational and Statistical Dynamics of Early Stopping

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 12

Beyond preventing overfitting, early stopping drastically reduces computational training budget (e.g., stopping at epoch 27 instead of a planned 300 epochs). Instead of post-hoc evaluating checkpoints, practitioners monitor a validation patience window (5–20 epochs) to avoid premature termination during temporary loss plateaus while ensuring training terminates when generalization degrades.

## Bayesian Derivation and Log-Posterior Formulation of Weight Decay

**Reference:** 03 - NeuralNetworksTraining.pdf, slides 14-15

Weight decay mathematically emerges from Maximum A Posteriori (MAP) estimation under a zero-mean Gaussian weight prior. In MAP optimization, the denominator evidence term (the marginal likelihood integral over all parameters) can be omitted via the argmax trick because it is strictly independent of the weights. When taking the negative log-likelihood, scaling by 2*sigma^2 yields the hyperparameter gamma = sigma^2 / sigma_w^2, directly balancing data error against weight magnitude.

## Full-Epoch Training Requirement of Weight Decay vs. Modern Layer-Wise Regularization

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 16

Pure weight decay was originally intended to train networks for full duration without early stopping by mathematically constraining the weight space. In modern deep learning practice, practitioners prefer early stopping as the primary defense and selectively add small weight decay per-layer, or use L1 regularization to induce sparsity (zero-valued weights) to accelerate matrix multiplications.
