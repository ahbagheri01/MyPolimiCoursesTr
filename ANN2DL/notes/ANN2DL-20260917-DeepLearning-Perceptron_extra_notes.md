# ANN2DL-20260917-DeepLearning-Perceptron — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20260917 1415-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\01 - DeepLearningIntro.pdf, E:\amirhossein\Polimi\POLIMI\ANN2DL\02 - Perceptron2NeuralNetworks.pdf

## The Core Shift from ML to Deep Learning: End-to-End Hierarchical Representation Learning

**Reference:** 01 - DeepLearningIntro.pdf, slides 24-26, 36

The fundamental distinction between traditional machine learning and deep learning is not merely the specific implementation technique, but the pushing of learning deep into the data representation itself. Traditional ML pipelines hit a performance ceiling because they rely on hand-crafted, domain-specific features (e.g., MFCCs via Fourier transforms of Fourier transforms for audio, or SIFT/HOG edge/corner pixel descriptors for images). In contrast, deep learning jointly trains a hierarchical feature extractor alongside the classifier or regressor end-to-end, learning simple features first and hierarchically aggregating them into complex patterns directly optimized for the task.

## Deep Learning Without Neural Networks: The Brain-Computer Interface Counterexample

Deep learning does not conceptually equal neural networks; deep learning fundamentally means learning data representations/features so that the downstream classifier improves. As a concrete counterexample, the professor describes a brain-computer interface project he worked on with a PhD student where a genetic algorithm was used to learn features from brain signals prior to classification. Although implemented with genetic algorithms rather than neural networks, this two-stage representation-learning process was conceptually deep learning.

## The 'Perfect Storm' of 2012 vs. 1998 LeNet: Why Data and Hardware Mattered

**Reference:** 01 - DeepLearningIntro.pdf, slides 27-29

While MIT Technology Review initially attributed the deep learning breakthrough purely to massive computational power, the professor clarifies that 2012 was a 'perfect storm' of three concurrent elements: massive user-generated data (terabytes produced and labeled for free via Web 2.0 and social media), the right computing hardware (GPUs repurposed from 3D graphic rendering matrix math), and novel algorithmic techniques. CNNs were introduced back in 1998 (LeCun's LeNet), but failed to revolutionize AI then because Web 1.0 lacked user-generated data and GPUs did not yet exist to process it.

## ImageNet 2012 Nuances: Multi-class vs. Multi-label Failures and Surprising Predictions

**Reference:** 01 - DeepLearningIntro.pdf, slide 30

When discussing AlexNet on the 1000-class ImageNet challenge (achieving an unprecedented >10% improvement over the previous year's incremental 0.8–1.2% gains), the professor highlights specific qualitative error patterns: the model predicted 'Dalmatian' on an image containing both cherries and a dog because the challenge is formulated as single-label multi-class rather than multi-label. Other errors stem from overly specific classes (confusing a koala with a wombat, though koala was the 5th guess), while other predictions like 'seat belt' surprisingly captured subtle objects humans would easily overlook.

## Early Computer Vision Milestone: Super-Resolution in 1980s Video Games

**Reference:** 01 - DeepLearningIntro.pdf, slide 34

To illustrate super-resolution before modern generative models, the professor notes one of NVIDIA's earliest super-resolution implementations, which was specifically created to upscale 1980s retro video games (such as Pac-Man) by a factor of 8 so they could be played on modern consoles without blocky pixelation.

## Repurposing GPUs: From Shadow Calculations to Neural Network Matrix Algebra

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slides 7-8

GPUs were not originally designed for artificial intelligence; they were engineered for 3D graphic rendering tasks like polygon meshing, projections, and shadow rendering. Because shadow computation in graphics engines reduces to massive parallel matrix-vector multiplications, GPUs turned out to be the exact hardware required to accelerate neural network forward and backward passes.

## Hardware Evolution: The Mark 1 Perceptron Potentiometers and Widrow's Learnable Bias

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 9

In Rosenblatt's 1957 Mark 1 Perceptron, weights were physically implemented as potentiometers (variable resistors), adjusted mechanically by electric motors (the large bundles of wires were the motor power and control lines). Furthermore, the original perceptron had a fixed bias; it was Bernard Widrow in 1960 who introduced the innovation of treating the bias as an additional input fixed to 1 with an associated weight w0 that is learned alongside the other weights.

## Exam Warning: Counting Network Weights and Never Forgetting the Bias

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 8

The professor issues an explicit exam warning: a standard exam question requires calculating the total number of weights in a neural network architecture. Students frequently forget the bias term. For a neuron with I inputs, the number of weights is strictly I + 1 (the I inputs plus the bias weight w0).

## Hebbian Plasticity Analogy: Manual Gearbox, Double-Clutching, and Electric Car Braking

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 11

To explain Hebbian learning ('cells that fire together, wire together' reinforcing pathways through synchronous activation), the professor presents an analogy of learning to drive a manual car. Beginners must execute conscious, uncoordinated steps (clutch, gear, release clutch, press gas). In older cars like the classic Fiat 500, unsynchronized gearboxes required double-clutching ('doppietta': clutch, neutral, gas to synchronize gearbox speeds, clutch, shift, gas). Repetition strengthens this neural pathway into an automatic reflex. This reinforced connection is exposed when driving an electric car for the first time: when a traffic light turns red, the driver reflexively stamps the leftmost pedal expecting the clutch, which is actually the brake, slamming it with the heavy muscular force normally used for the clutch pedal.

## Role of Learning Rate in Perceptron vs. Non-linear Deep Networks

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 11

In the perceptron learning algorithm, the learning rate (eta) does not fundamentally matter—setting it to 1, 0.5, or 10,000 only scales the resulting weight vector without changing the separating decision boundary (which is defined by w^T x = 0). This is because the perceptron is a linear classifier. However, the professor stresses that as soon as models transition beyond linear boundaries into non-linear multilayer neural networks, eta becomes the single most critical hyperparameter, and is frequently tested on the exam.

## Handling Discontinuities at the Decision Boundary in Perceptron Learning

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 12

During the manual walk-through of the perceptron learning algorithm on the Boolean OR problem (coded with inputs/targets in {-1, +1}), when initial weights w = [0, 0, 0] yield a weighted sum of exactly 0, the sign activation is mathematically discontinuous/undefined. The convention adopted is to treat an output of 0 as an incorrect prediction, forcing a weight update.

## Perceptron Convergence: Initializations and the Multi-Pass 'Epoch' Requirement

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slide 12

The professor clarifies two essential convergence properties via classroom questions: (1) Running one pass across the training records (one epoch) and obtaining correct predictions at the end of the pass does not mean training is finished—earlier samples may have been invalidated by subsequent weight updates, requiring repeated epochs until an entire epoch completes with zero errors. (2) Starting from different initial weights does not guarantee convergence to the same final weights; because an infinite number of separating hyperplanes exist for linearly separable data, the algorithm converges to different valid solutions depending on initialization, but it is guaranteed to converge without oscillating provided the problem is linearly separable.

## Deriving the 2D Line Equation from the Perceptron Hyperplane

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slides 13-14

The perceptron decision boundary is w0 + w1*x1 + w2*x2 = 0. Solving explicitly for x2 yields x2 = -(w0/w2) - (w1/w2)*x1. Applying the weights found during the lecture OR exercise (w0 = 1/2, w1 = 1/2, w2 = 1/2), this directly yields x2 = -1 - x1, demonstrating geometrically how the learned hyperplane separates (-1, -1) from the remaining three positive points in {-1, 1}^2.

## Why Changing the Activation Function Cannot Solve Non-Linear Separability

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slides 15, 18

In response to a student question about whether changing the activation function (e.g., substituting the step/sign with a smooth Sigmoid or Tanh) resolves the XOR problem for a single neuron, the professor demonstrates geometrically that it cannot. The activation function acts orthogonally to the hyperplane: applying a Sigmoid or Tanh creates a smooth 3D sigmoidal wave rather than an abrupt vertical step, but the decision boundary (intersecting the surface with a classification threshold like z = 0) remains identical to w^T x = 0—strictly a linear line/hyperplane. A single neuron is a linear classifier because its decision boundary is linear, not because its activation function is linear.

## The Breakdown of Hebbian Learning in Multi-Layer Networks

**Reference:** 02 - Perceptron2NeuralNetworks.pdf, slides 16, 30-32

While multi-layer perceptrons (MLPs) overcome the XOR limitation by cascading linear boundaries into convex or arbitrary regions, Hebbian learning completely breaks down for MLPs. Hebb's rule (Delta w_i = eta * x_i * t) fundamentally requires access to both the presynaptic activation (input x) and postsynaptic activation (target t) for every connection. In an MLP, there is no known target signal for intermediate hidden neurons, nor does an output neuron have direct access to the raw input features. This credit assignment failure caused the AI winter following Minsky and Papert's 1969 book until Rumelhart et al. formalized backpropagation in 1986.
