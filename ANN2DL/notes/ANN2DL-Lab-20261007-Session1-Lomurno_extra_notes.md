# ANN2DL-Lab-20261007-Session1-Lomurno — Additional Professor Notes

**Transcripts:** Eugenio Lomurno's Personal Room-20261007 1601-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\Lecture 1\Feedforward Neural Networks.ipynb

## GPU Non-Determinism and Model Checkpointing Necessity

**Reference:** Cell 3, Cell 5, Cell 37

Saving trained model checkpoints is critical not only to avoid wasting compute time re-running training, but because training on GPUs introduces non-deterministic execution. Running identical code with the exact same seed on a GPU can yield variable results (e.g., scoring 100% accuracy in one run, but 91%, 92%, or 89% in subsequent runs), meaning a well-performing model cannot be reliably reproduced without saving its weights.

## Feature Scaling Disparities as an Unintended Model Bias

**Reference:** Cell 11, Cell 17

When input features differ substantially in baseline magnitudes or mean values (such as petal width versus sepal length in Iris), a randomly initialized linear combination inherently assigns unequal initial importance to them. In the first batch of the first epoch, larger-scale features can exert an unweighted bias (e.g., five times more weight) over smaller features purely due to magnitude, which justifies normalization to avoid injecting unintentional structural bias into the learning dynamics.

## Why Neural Networks Output Unnormalized Logits Instead of Explicit Softmax

**Reference:** Cell 21, Cell 26, Cell 28

While a Softmax function normalizes network outputs to valid probability distributions summing to one, applying an explicit Softmax before calculating categorical cross-entropy loss causes numerical instability and information loss. Softmax squashes unbounded values, making extreme logits (such as 9, 10, 100) appear identical in ranking to moderate logits, which can mask when a model is completely out of scale and trigger severe gradient explosions resulting in NaN values. Computing loss directly from raw logits preserves magnitude sensitivity and ensures numerical stability.

## Outlier Risk and Instability in Stochastic Single-Sample Weight Updates

**Reference:** Cell 18, Cell 28

Batching data instead of updating weights sample-by-sample (pure SGD) provides crucial stabilization beyond raw computational speedup. If updates occur after every single sample, an outlier encountered at the very end of an epoch will pull the entire network's weights away from the population's optimal region towards an unrepresentative, suboptimal state.

## ReLU Gradient Filtering Rationale in Parameter Histograms

**Reference:** Cell 39, Cell 41, Cell 42

In the gradient histogram visualization function, exact zero gradients must be filtered out rather than plotted. Because the ReLU activation zeroes out negative inputs, a large proportion of neurons in any given batch remain inactive and produce exact zero gradients; retaining them would dwarf the rest of the distribution, resulting in an uninformative plot dominated by a single vertical spike around zero.

## Two Strategies for Model Persistence: State Dict vs. Full Architecture

**Reference:** Cell 37, Cell 44

When saving PyTorch models, there are two distinct workflows: saving the full configuration alongside the weights, which allows direct reloading without redeclaring code, or saving strictly the state dictionary (`state_dict`). When saving weights alone, the identical model architecture class must be instantiated in code before loading the state dictionary to overwrite parameters.
