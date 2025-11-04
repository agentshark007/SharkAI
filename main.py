import random
import string
import math
import numpy as np

# Activation functions
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

class Model:
    def __init__(self, dataset, hidden_sizes, learning_rate):
        self.chars = sorted(list(set(dataset + string.printable)))
        self.char_to_idx = {c: i for i, c in enumerate(self.chars)}
        self.idx_to_char = {i: c for i, c in enumerate(self.chars)}
        self.vocab_size = len(self.chars)
        self.learning_rate = learning_rate
        
        # Network architecture
        layer_sizes = [self.vocab_size] + hidden_sizes + [self.vocab_size]
        self.weights = [np.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.01 
                        for i in range(len(layer_sizes)-1)]
        self.biases = [np.zeros(layer_sizes[i+1]) for i in range(len(layer_sizes)-1)]

    def forward(self, x_idx):
        x = np.zeros(self.vocab_size)
        x[x_idx] = 1.0
        self.layer_inputs = []
        self.layer_outputs = [x]

        for i in range(len(self.weights)-1):
            z = np.dot(self.layer_outputs[-1], self.weights[i]) + self.biases[i]
            self.layer_inputs.append(z)
            self.layer_outputs.append(relu(z))

        z = np.dot(self.layer_outputs[-1], self.weights[-1]) + self.biases[-1]
        self.layer_inputs.append(z)
        y_hat = softmax(z)
        self.layer_outputs.append(y_hat)
        return y_hat

    def backward(self, x_idx, y_idx):
        grads_w = [np.zeros_like(w) for w in self.weights]
        grads_b = [np.zeros_like(b) for b in self.biases]

        y_hat = self.forward(x_idx)

        delta = y_hat.copy()
        delta[y_idx] -= 1
        grads_w[-1] = np.outer(self.layer_outputs[-2], delta)
        grads_b[-1] = delta

        delta_prev = delta
        for i in reversed(range(len(self.weights)-1)):
            delta = np.dot(delta_prev, self.weights[i+1].T) * relu_derivative(self.layer_inputs[i])
            grads_w[i] = np.outer(self.layer_outputs[i], delta)
            grads_b[i] = delta
            delta_prev = delta

        for i in range(len(self.weights)):
            self.weights[i] -= self.learning_rate * grads_w[i]
            self.biases[i] -= self.learning_rate * grads_b[i]

        return -math.log(y_hat[y_idx] + 1e-8)

    def train_step(self, dataset):
        loss = 0
        for i in range(len(dataset)-1):
            x_idx = self.char_to_idx[dataset[i]]
            y_idx = self.char_to_idx[dataset[i+1]]
            loss += self.backward(x_idx, y_idx)
        return loss / (len(dataset)-1)

    def predict_next_char(self, char):
        idx = self.char_to_idx.get(char, random.randint(0, self.vocab_size-1))
        probs = self.forward(idx)
        next_idx = np.random.choice(range(self.vocab_size), p=probs)
        return self.idx_to_char[next_idx]

    def generate_text(self, prompt, max_length):
        result = ""
        for _ in range(max_length):
            next_char = self.predict_next_char(prompt[-1])
            result += next_char
            prompt += next_char
        return result

class SharkAI:
    def __init__(self, dataset, hidden_sizes=[128,64], learning_rate=0.05, epochs=200, max_output_length=100):
        self.dataset = dataset
        self.hidden_sizes = hidden_sizes
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.max_output_length = max_output_length
        self.model = Model(dataset, hidden_sizes, learning_rate)

    def train(self):
        print("Training started")
        for epoch in range(self.epochs):
            loss = self.model.train_step(self.dataset)
            if (epoch+1) % 10 == 0 or epoch == 0:
                print(f"Epoch {epoch+1}/{self.epochs} | Loss: {loss:.6f}")
        print("Training done")

    def generate_text(self, prompt):
        return self.model.generate_text(prompt, self.max_output_length)

if __name__ == "__main__":
    dataset_file = "data.txt"
    with open(dataset_file, "r") as f:
        dataset = f.read()

    ai = SharkAI(
        dataset,
        hidden_sizes=[128, 256, 512, 256, 128],
        learning_rate=0.05,
        epochs=300,
        max_output_length=150
    )

    ai.train()

    while True:
        prompt = input(">>: ")
        print(ai.generate_text(prompt))
