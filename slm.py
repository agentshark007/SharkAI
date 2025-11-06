from tiktoktoken import TikTokToken
from network import NeuralNetwork

class SLM:
    def __init__(self, dataset):
        self.dataset = dataset
        self.tokenizer = TikTokToken()
        self.network = None
        self.initialized = False
        self.trained = False
        self.lookback_tokens = None

    def initialize_network(self, hidden_layers, lookback_tokens):
        # Use the dataset as-is, including literal <START>, <SEP>, <END>
        self.tokenizer.generate_tokens(self.dataset)
        self.lookback_tokens = lookback_tokens

        self.network = NeuralNetwork()
        self.network.generate_structure(lookback_tokens, hidden_layers, 1)
        self.network.input_size = lookback_tokens
        self.initialized = True

    def train(self, epochs, influence=0.1):
        if not self.initialized:
            raise Exception("Network not initialized.")

        # Tokenize the entire dataset
        token_dataset = []
        for text in self.dataset:
            token_dataset.extend(self.tokenizer.tokenize(text))

        # Simple naive online training
        for _ in range(epochs):
            for i in range(len(token_dataset) - self.network.input_size):
                inputs = token_dataset[i:i + self.network.input_size]
                target = token_dataset[i + self.network.input_size]

                # Set input node values
                for idx, node in enumerate(self.network.input_nodes):
                    node.value = inputs[idx]

                # Forward pass
                self.network.forward()
                output_val = self.network.get_output()[0]

                # Naive weight adjustment
                error = target - output_val
                for conn in self.network.connections:
                    conn.weight += influence * error

        self.trained = True

    def generate_and_print_response(self, prompt, length=20):
        if not self.trained:
            raise Exception("Model not trained.")

        tokens = self.tokenizer.tokenize(prompt)
        vocab_start = self.tokenizer.token_dict["<START>"]

        for _ in range(length):
            input_seq = tokens[-self.network.input_size:]
            # pad if sequence is too short
            if len(input_seq) < self.network.input_size:
                input_seq = [vocab_start] * (self.network.input_size - len(input_seq)) + input_seq

            for idx, node in enumerate(self.network.input_nodes):
                node.value = input_seq[idx]

            self.network.forward()
            next_token_id = self.network.map_output_to_token(len(self.tokenizer.token_dict))
            tokens.append(next_token_id)

            token_str = self.tokenizer.detokenize([next_token_id])
            print(token_str, end='', flush=True)

        print()
        return self.tokenizer.detokenize(tokens)

