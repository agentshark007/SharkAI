import math
from tiktoktoken import *
from network import *

class SLM:
    def __init__(self, dataset):
        # Initialize SLM with a dataset and prepare internal states
        self.dataset = dataset
        self.initialized = False
        self.trained = False
        self.network = None

    def initialize_network(self, hidden_layers, lookback_tokens):
        # Initialize the neural network structure

        self.network = NeuralNetwork()
        self.network.generate_structure(lookback_tokens, hidden_layers, 1) # input: lookback token. hidden: hidden layers. output: 1 for next token

        self.initialized = True

    def train(self, epochs, influence):
        # For each epoch, change the weights a different amount based on the influence.

        # training code here

        self.trained = True
