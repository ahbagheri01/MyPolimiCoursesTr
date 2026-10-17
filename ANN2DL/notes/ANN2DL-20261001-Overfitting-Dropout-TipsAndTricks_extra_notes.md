# ANN2DL-20261001-Overfitting-Dropout-TipsAndTricks — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20261001 1421-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\03 - NeuralNetworksTraining.pdf

## Overfitting Definition vs. Model Complexity & Underfitting

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 3, 11

Overfitting strictly denotes the divergence/difference between training performance and test performance, not whether the overall performance is intrinsically good or bad. If training and test performance are both equally poor, the model is underfitting and complexity should be increased. If increasing complexity improves both in lockstep, it is safe to keep increasing it; overfitting only manifests when training and test performance diverge.

## Architectural vs. Training Procedure Regularization

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 12-17

Early stopping and weight decay do not modify the network architecture or reduce its structural parameter count; early stopping modifies the training loop/epochs, and weight decay modifies the loss function. Dropout differs fundamentally because it enforces stochastic structural regularization on the network itself.

## Dropout Implementation and Backpropagation Mechanics

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 17

Dropout applies an element-wise product (Hadamard product) between activations and a binary Bernoulli mask vector. Backpropagation through a dropout layer is non-differentiable in the classical sense, but operates via a simple gating pass-through: if the mask is 1, gradient flows through with derivative 1; if the mask is 0, the gradient is blocked (derivative 0). The professor notes that while libraries may vary, practical implementations generate the mask per iteration/mini-batch rather than per sample to preserve parallel GPU computation.

## Weight Rescaling Mechanism in Dropout

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 22

At inference time, all neurons are active simultaneously, meaning incoming sum inputs receive more accumulated signals (e.g., ~30% more if dropout probability is 0.3) than during training. To compensate for this shift and treat the network as an aggregate ensemble average, weights are rescaled (e.g., dividing by 1.3 / multiplying by 1 - p).

## Empirical Dropout (Monte Carlo Dropout) for Uncertainty Estimation

An advanced use of dropout (referred to by the professor as empirical dropout) keeps dropout active during inference and passes the same input multiple times under different sampled masks. This yields a distribution of predictions, allowing the estimation of predictive variance and confidence intervals (output uncertainty).

## Vanishing Gradient in Deep Networks via Chain Rule Derivatives

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 24-25

Sigmoid and hyperbolic tangent derivatives are strictly less than 1 everywhere across their domains (maximum 0.25 for sigmoid and 1.0 at origin for tanh, falling off rapidly). When backpropagating through deep architectures (e.g., 10 layers), chained multiplication of values <= 0.1 drives the gradient exponentially toward zero, preventing earlier layers from updating and leaving them trapped near random initialization.

## ReLU6 for Embedded and Quantized Systems

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 27

To mitigate unbounded activation outputs in hardware with low bit-depth, systems often adopt ReLU6, which clips the maximum activation at 6. In embedded systems limited to 4-bit or 8-bit precision (256 discrete values), placing an upper bound allows the full numerical resolution of the integer quantization grid to be utilized effectively without overflow.

## Dying ReLU vs. Dropout Irreversibility and Large Learning Rates

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 27-28

While dying ReLUs and dropout both cause inactive neurons, dropout is temporary and stochastic per iteration, whereas a dying ReLU is permanently deactivated because both its output and gradient evaluate to zero. High initial learning rates are dangerous with ReLUs because a large gradient step can throw neuron pre-activations into the negative region, permanently killing parameters and irreversibly shrinking model capacity.

## Derivation Intuition for Xavier/Glorot Initialization and the He Factor

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 31-32

Xavier initialization derives from requiring the variance of a neuron's output to match its input variance under zero-mean i.i.d. assumptions: Var(output) = I * Var(w) * Var(x), requiring Var(w) = 1 / n_in. Glorot & Bengio reasoned backwards for gradient propagation, requiring Var(w) = 1 / n_out, motivating the harmonic/average compromise 2 / (n_in + n_out). For ReLU, He initialization multiplies the variance by 2 (Var(w) = 2 / n_in) because approximately half the neurons are inactive (clipped at zero) at initialization.

## Batch Normalization Placement and Parameter Learning via Backprop

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 34-36

Batch normalization is conventionally placed after dense/convolutional linear operations and before the non-linearity (e.g., ReLU), because pre-activations span (-inf, +inf) whereas post-ReLU activations are non-negative [0, +inf). The scale (gamma) and shift (beta) are learnable parameters that allow the network to adapt or invert the normalization; during backpropagation, gradients with respect to gamma (x_hat) and beta (1) are computed cleanly through the linear transformation.

## Batch Normalization Inference vs. Training Discrepancy

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 35

At inference time, inputs often arrive individually (batch size = 1), making sample batch mean and variance meaningless. Instead of calculating batch statistics, inference uses global population statistics (or running averages) tracked during training, combined with learned parameters gamma and beta, to perform a fixed linear rescaling.

## Nesterov Accelerated Gradient (NAG) Look-Ahead Mechanics

**Reference:** 03 - NeuralNetworksTraining.pdf, slide 40

Standard momentum takes a step combining the current gradient with the accumulated velocity from the previous gradient. Nesterov Accelerated Gradient improves this by first making the jump along the direction of the momentum vector, computing the gradient at that projected look-ahead position, and then applying the correction step.
