# ANN2DL-20260923-FeedForward-ErrorFunctions — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20260923 1623-2.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\02 - Perceptron2NeuralNetworks.pdf

## Historical Breakdown of Hebbian Learning in Multilayer Networks

**Reference:** Slide 16

Hebbian learning requires synchronous or concordant/discordant activation between the known input and target ($x_i$ and $t$). In a multilayer architecture, intermediate hidden layers lack known input and target signals, making classical Hebbian learning inapplicable. This limitation, highlighted by Minsky and Papert in 1969, stalled multilayer models until backpropagation and differentiable continuous neurons were introduced (around 1985–1986).

## Quadratic Growth of Parameter Counts in Dense Layers

**Reference:** Slide 17

Dense (fully connected) layers scale roughly quadratically with layer width. Two hidden layers of 10 neurons yield ~110 parameters, two hidden layers of 100 neurons yield ~10,000 parameters, and two hidden layers of 1,000 neurons yield on the order of 1,000,000 parameters. This illustrates how quickly parameter count inflates in fully connected networks compared to convolutional architectures.

## Limitations of Step/Sign Functions vs. Continuous Activations in Optimization

**Reference:** Slide 17

The step and sign functions fail under gradient descent because their derivative is zero almost everywhere and undefined at the origin, halting gradient-based weight updates. Conversely, non-differentiability at a single point (such as in ReLU at zero) is not fatal because a single point has measure zero on the real line.

## Derivative Upper Bounds of Sigmoid and Tanh

**Reference:** Slide 18

Computing derivatives at the origin demonstrates their maximal bounds: for sigmoid, $g(0) = 0.5$ and $g'(0) = 0.5(1 - 0.5) = 0.25$ (maximum derivative is 0.25). For tanh, $g(0) = 0$ and $g'(0) = 1 - 0^2 = 1$ (maximum derivative is 1). The fact that the sigmoid derivative is bounded strictly below 0.25 becomes a critical factor in the vanishing gradient problem in deep networks.

## Why Purely Linear Networks Collapse to Linear Regression

**Reference:** Slide 18

If all layers employ linear activation functions, the entire deep network algebraically collapses into a single linear combination of linear combinations, reducing to simple linear regression from input dimension $I+1$ to output dimension $K$. This renders the intermediate layers and excess parameters completely redundant and ill-conditioned.

## Pitfalls of Min-Max Normalization with Sigmoid Output in Regression (Tallest Person Example)

**Reference:** Slide 19

Using a sigmoid output for regression by normalizing target values to [0, 1] using sample minimum and maximum is dangerous unless the absolute physical bounds are known. For example, if predicting human height using a dataset of people in the classroom, a person encountered in the general population taller than the tallest student in the room cannot be predicted correctly; the network saturates at 1.0, underestimating their height.

## Network Output as Uncalibrated Probability and Overconfidence

**Reference:** Slide 19

A sigmoid or softmax output represents mathematical values between 0 and 1, but cannot automatically be trusted as true, calibrated real-world probabilities. Deep neural networks often suffer from overconfidence—for instance, outputting a probability of 0.95 while exhibiting an empirical error rate of 20% rather than 5%—requiring explicit probability calibration post-processing.

## Multi-Class (Softmax) vs. Multi-Label (Independent Sigmoids) Architectures

**Reference:** Slide 19

While multi-class classification enforces mutually exclusive categories using a softmax layer across classes, multi-label classification (e.g., an image simultaneously containing a person and a dog, but not a car) uses $K$ independent sigmoid output units, predicting separate binary probabilities for each label independently.

## Standard Historical Activation Architecture Templates

**Reference:** Slide 19

Before the widespread adoption of ReLU, standard network design followed clear templates: regression used a linear output with tanh for all hidden neurons; binary classification used a sigmoid output with tanh for all hidden neurons; multi-class classification used a softmax output with tanh for all hidden neurons.

## Universal Approximation Theorem vs. Practical Deep Hierarchies

**Reference:** Slide 20

Kurt Hornik's 1991 theorem proved that a single hidden layer can approximate any measurable function on a compact set, but this does not imply that gradient descent can find the weights, nor does it prevent overfitting; it may also require exponentially many neurons. In practice, deeper networks train much more effectively through hierarchical feature representation, which was under-explored in the early 1990s because training algorithms struggled with deep architectures.

## Physical Rolling Stone Analogy for Momentum

**Reference:** Slide 24

Gradient descent often behaves like a rolling object that abruptly stops the moment the gradient levels out, trapping it in local minima. Momentum models physical inertia—allowing the update to retain velocity along its prior direction of travel, carrying it across flat spots and small bumps on the loss surface and accelerating progress down steep, sustained slopes.

## Loss Surface Geometry in Massive Models vs. Multiple Restarts

**Reference:** Slide 24

While multi-start random initialization was traditionally necessary to avoid getting stuck in poor local minima, modern massive models (e.g., LLMs) avoid multi-start regimes due to extreme computational costs. Theoretical and empirical insights show that in very high-dimensional parameter spaces, the number of local minima proliferates, but nearly all of them converge to similarly low loss values, making single-run optimization viable.

## Backpropagation as the Rediscovery of Gradient Descent Chain Rule

**Reference:** Slide 25

Backpropagation (popularized in 1985/1986) is fundamentally the chain rule of calculus applied to non-linear optimization via gradient descent, rather than a fundamentally distinct paradigm. Recognizing it as standard non-linear function optimization opens the door to using generalized numerical solvers (such as Quasi-Newton, Polak-Ribière, or Levenberg-Marquardt).

## Step-by-Step Chain Rule Isolation of Specific Weight $w_{3,5}^{(1)}$

**Reference:** Slide 26

In differentiating the sum of squared errors with respect to an internal first-layer weight $w_{3,5}^{(1)}$, almost all terms in the summation $\sum_{j} w_{1,j}^{(2)} h_j$ vanish because there are no lateral connections between neurons in the same layer. Only the term passing through the third hidden neuron $h_3$ depends on $w_{3,5}^{(1)}$, directly isolating $w_{1,3}^{(2)} \cdot h'_3(\cdot) \cdot x_5$ as the backpropagated path.
