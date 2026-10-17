# ANN2DL-Lab-20261008-Session2-Archetti — Additional Professor Notes

**Transcripts:** Alberto Archetti's Personal Room-20261008 1413-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\Lecture 2\Overfitting and Regularisation.ipynb

## GPU Non-Determinism and Weight Saving Guidance

Fixing random seeds on a CPU guarantees full code reproducibility. On GPUs, however, reproducibility is not guaranteed due to hardware-level execution differences. Because re-training with identical seeds on GPU can yield different weights and altered performance, the instructor explicitly advises always saving model weights immediately after training (especially for competitive course challenges).

## Stakeholder Intuition for Precision vs. Recall

**Reference:** Cell 12

Precision and recall can be understood through the differing questions asked by distinct stakeholders in a diagnostic scenario: precision is the metric of interest to an individual patient (answering 'Given that the doctor diagnosed me as having a disease, what is the probability that I actually have it?'), whereas recall is of primary interest to a health ministry or public health authority (answering 'What fraction of all truly diseased individuals in the population were correctly detected by the doctors?').

## Purpose of Shuffling Training Batches vs. Fixed Evaluation Sets

**Reference:** Cell 18

Evaluation (validation and test) loaders do not require shuffling because evaluation computes a fixed deterministic average over identical data points regardless of order. In contrast, shuffling the training set per epoch ensures that mini-batches contain different random combinations of samples (sampling without replacement across each epoch), which continuously injects stochastic variability into the gradient directions across iterations, assisting non-linear optimization.

## Manual Parameter Counting for Dense Layers

**Reference:** Cell 22

To manually compute parameter counts in fully connected (dense) layers (highlighted as a frequent exam-style question), multiply the number of inputs by the number of outputs and crucially remember to add one bias parameter per output neuron: $(\text{in\_features} + 1) \times \text{out\_features}$, or $(\text{in\_features} \times \text{out\_features}) + \text{out\_features}$. For example, connecting 2,000 inputs to 512 outputs yields $2000 \times 512 + 512 = 1,024,512$ parameters.

## Internal Mechanics of PyTorch Computational Graph and Tensors

**Reference:** Cell 28

Under the hood in C-level execution, PyTorch represents each tensor node in a dynamic computational graph using a data structure containing three key elements: (1) the raw values/data of the tensor cells, (2) the tensor's accumulated gradient/partial derivative computed via the chain rule during the backward pass, and (3) backward connections/pointers to parent nodes and the operations that generated it.

## Advanced Generalization Phenomena: Double Descent and Grokking

**Reference:** Cell 35

While classical machine learning models follow a standard U-shaped bathtub curve where excessive complexity increases generalization error, the instructor notes advanced phenomena: (1) Double Descent, where scaling model capacity/parameters far beyond interpolation threshold causes the test error curve to peak and descend again; and (2) Grokking, where a network that is severely overfitting at 100% training accuracy with poor validation loss will suddenly generalize after being left to train for vast numbers of extra epochs.

## Distributed Redundancy and Fault Tolerance Analogy of Dropout

**Reference:** Cell 40

Dropout enforces generalization through an architectural analogy to internet network fault tolerance: by randomly dropping connections/neurons during each training step, information paths can fail at any time. Consequently, the network cannot rely on single pathways and is forced to learn redundant parallel paths for every feature computation, effectively reducing model capacity without changing physical layer dimensions.

## Adam vs. AdamW Weight Decay Interaction Intuition

**Reference:** Cell 48

In standard Adam, adding an L2 penalty term directly to the objective function feeds the weight penalty into the adaptive first and second gradient moments ($m_t, v_t$), which effectively penalizes weight magnitudes twice and distorts regularization scaling. AdamW solves this by decoupling the penalty from gradient moment updates, applying weight decay directly to the weights as a flat, uniform percentage tax per iteration.
