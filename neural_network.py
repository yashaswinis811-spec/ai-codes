import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

# -------------------------------
# PART 1: PERCEPTRON
# -------------------------------

print("===== PERCEPTRON =====")

# Training data for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

# Create Perceptron
perceptron = Perceptron(max_iter=1000, random_state=0)

# Train the model
perceptron.fit(X, y)

# Predict
predictions = perceptron.predict(X)

print("Input:")
print(X)

print("Actual Output:")
print(y)

print("Predicted Output:")
print(predictions)


# -------------------------------
# PART 2: BACKPROPAGATION
# -------------------------------

print("\n===== BACKPROPAGATION NEURAL NETWORK =====")

# XOR dataset
X_xor = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y_xor = np.array([0, 1, 1, 0])

# Create neural network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='logistic',
    solver='lbfgs',
    max_iter=1000,
    random_state=0
)

# Train the network
model.fit(X_xor, y_xor)

# Predict
predictions_xor = model.predict(X_xor)

print("Input:")
print(X_xor)

print("Actual Output:")
print(y_xor)

print("Predicted Output:")
print(predictions_xor)