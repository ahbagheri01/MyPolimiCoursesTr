# ANN2DL-20260924-Backpropagation-LossFunctions — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20260924 1419-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\02 - Perceptron2NeuralNetworks.pdf, E:\amirhossein\Polimi\POLIMI\ANN2DL\03 - NeuralNetworksTraining.pdf

## Historical 1/2 Factor in Mean Squared Error

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 21-22

The historical convention of multiplying the sum of squared errors by 1/2 (or 1/(2N)) was specifically introduced to cancel out the factor of 2 arising from differentiating the quadratic term, thereby saving a single multiplication operation on computationally constrained legacy hardware.

## GPU Data Transfer Bottleneck and Gradient Accumulation Trick

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 28

On GPUs, transfer overhead dominates computation time; loading individual samples repeatedly is drastically slower than computing updates in parallel. When full-batch gradient descent is desired but cannot fit in GPU VRAM, libraries implement gradient accumulation: evaluating gradients per sample or mini-batch sequentially and summing them in memory before applying a single weight update, trading memory for compute time without altering the gradient direction.

## Distinction Between Epochs and Iterations

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 28

An epoch represents a complete pass through the entire dataset, whereas an iteration denotes a single gradient update. For batch gradient descent, one epoch equals 1 iteration; for SGD, one epoch equals N iterations; for mini-batch gradient descent with batch size B, one epoch requires N/B iterations.

## Extension of Automatic Differentiation Frameworks with Custom Layers

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 30-32

To implement custom non-linearities (such as Gaussian or sinusoidal activation functions) in automatic differentiation engines like PyTorch, the user only needs to define the forward mathematical function and its symbolic first derivative; the engine automatically nests and computes the backwards pass through the chain rule.

## Conceptual Distinction of Maximum Likelihood Estimation

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 34-36

Maximum Likelihood Estimation does not seek the most likely parameter set or probability distribution; rather, it identifies the distribution parameters that maximize the probability of generating the observed empirical data.

## Real-World Intuition for Known-Variance MLE: Sonar Measurement

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 37

Estimating an unknown mean with known variance occurs frequently in hardware sensors: for example, a sonar measuring distance to a wall has fixed, known sensor measurement variance (e.g., 3-4 cm deviation), but the mean (the true wall distance) is unknown and must be estimated via repeated measurements.

## Percentage Error, Heteroscedastic Noise, and Logarithmic Variance Stabilization

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 43-44

Standard squared error assumes additive Gaussian noise with constant variance (homoscedasticity). In real instruments (e.g., car speedometers with ±1% error), error scales proportionally with the measured magnitude. Under squared error, large values disproportionately dominate training; applying a logarithmic transformation to the target converts multiplicative proportional error into additive noise, stabilizing variance.

## Multi-Class Softmax vs. Multi-Label Sigmoid Loss Implementations

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 19, 51

In multi-class classification, classes are mutually exclusive, requiring a Softmax output with categorical cross-entropy where boosting the target class probability implicitly suppresses non-target classes due to normalization. In contrast, multi-label classification permits non-exclusive labels per item, requiring independent sigmoid outputs per class trained simultaneously with binary cross-entropy without Softmax normalization.

## Loss Function Modularity in Backpropagation

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 30-32

Replacing the loss function in backpropagation alters solely the first derivative factor in the chain rule (the derivative of the error with respect to network output, dE/dg); all subsequent downstream layer derivative computations remain entirely identical.

## Real-World Multi-Task Loss Engineering: YOLO, Segmentation, and GANs

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 53

Modern deep learning losses are designed heuristically to match task requirements: YOLO combines SSE for bounding box regression with binary cross-entropy for class and objectness scores; semantic segmentation substitutes non-differentiable Intersection over Union (IoU) with differentiable Dice or Focal losses; and GAN generators optimize by backpropagating through the discriminator to maximize the discriminator's classification error.
