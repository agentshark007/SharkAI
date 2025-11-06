import math
from tiktoktoken import *
from network import *

class SLM:
    def __init__(self, dataset):
        self.dataset = dataset
        self.initialized = False
        self.trained = False
        self.network = None

    def initialize_network(self, hidden_layers, lookback_tokens):
        self.network = NeuralNetwork()
        self.network.generate_structure(lookback_tokens, hidden_layers, 1)
        self.initialized = True

    def train(self, epochs, influence):
        if not self.initialized:
            raise Exception("Network not initialized.")
        for _ in range(epochs):
            for i in range(len(self.dataset) - self.network.input_size):
                inputs = self.dataset[i:i + self.network.input_size]
                target = self.dataset[i + self.network.input_size]
                output = self.network.forward(inputs)
                error = target - output
                self.network.backward(error * influence)
        self.trained = True

    def generate_and_print_response(self, prompt, length=20):
        if not self.trained:
            raise Exception("Model not trained.")
        tokens = tokenize(prompt)
        for _ in range(length):
            input_seq = tokens[-self.network.input_size:]
            next_token = self.network.forward(input_seq)
            next_token_rounded = round(next_token)
            tokens.append(next_token_rounded)
            token_str = detokenize([next_token_rounded])
            print(token_str, end='', flush=True)
        response = detokenize(tokens)
        return response
