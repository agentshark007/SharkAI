import math
from tiktoktoken import TikTokToken
from network import NeuralNetwork

class SLM:
    def __init__(self, dataset):
        self.dataset = dataset
        self.tokenizer = TikTokToken()
        self.network = None
        self.initialized = False
        self.trained = False

    def initialize_network(self, hidden_layers, lookback_tokens):
        # Generate tokenizer on dataset
        self.tokenizer.generate_tokens(self.dataset)
        self.lookback_tokens = lookback_tokens
        self.network = NeuralNetwork()
        self.network.generate_structure(lookback_tokens, hidden_layers, 1)
        self.network.input_size = lookback_tokens  # for training loop
        self.initialized = True

    def train(self, epochs, influence=0.1):
        if not self.initialized:
            raise Exception("Network not initialized.")

        # Tokenize entire dataset
        token_dataset = []
        for text in self.dataset:
            token_dataset.extend(self.tokenizer.tokenize(text))

        # Simple online training
        for _ in range(epochs):
            for i in range(len(token_dataset) - self.network.input_size):
                inputs = token_dataset[i:i + self.network.input_size]
                target = token_dataset[i + self.network.input_size]

                # Set input values
                for idx, node in enumerate(list(self.network.nodes.values())[:self.network.input_size]):
                    node.value = inputs[idx]

                # Forward pass
                output = self.network.determine_value(f"output-0")

                # Backward placeholder: simple weight adjustment for demonstration
                # A real backprop is not implemented in the previous network class
                error = target - output
                for conn in self.network.connections:
                    conn.weight += influence * error  # very naive adjustment

        self.trained = True

    def generate_and_print_response(self, prompt, length=20):
        if not self.trained:
            raise Exception("Model not trained.")

        tokens = self.tokenizer.prepare_for_response_generation(prompt, self.lookback_tokens)

        for _ in range(length):
            input_seq = tokens[-self.lookback_tokens:]

            # Set input values
            for idx, node in enumerate(list(self.network.nodes.values())[:self.network.input_size]):
                node.value = input_seq[idx]

            # Forward pass
            next_token_val = self.network.determine_value("output-0")
            next_token_id = round(next_token_val)
            tokens.append(next_token_id)

            token_str = self.tokenizer.detokenize([next_token_id])
            print(token_str, end='', flush=True)

        print()  # newline at the end
        return self.tokenizer.detokenize(tokens)
