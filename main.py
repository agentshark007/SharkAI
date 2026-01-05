from neural_network import NeuralNetwork, InputLayer, HiddenLayer, OutputLayer
from tiktoktoken import tokenize, detokenize, tokens


class SharkAI:
    def __init__(self, lookback_tokens):
        self.lookback_tokens = lookback_tokens

        self.network = NeuralNetwork()
        self.network.add_layer(InputLayer(self.lookback_tokens))
        self.network.add_layer(HiddenLayer(128))
        self.network.add_layer(OutputLayer(len(tokens)))
        self.network.generate_connections()

    def train(self, dataset, epochs=10, learning_rate=0.05):
        for epoch in range(epochs):
            total_loss = 0.0
            count = 0
            failures = 0

            for input_tokens, target_vector in dataset:
                inputs = input_tokens[-self.lookback_tokens:]
                while len(inputs) < self.lookback_tokens:
                    inputs = [0] + inputs

                outputs = self.network.generate(inputs)

                # loss
                sample_loss = sum(
                    (outputs[i] - target_vector[i])**2 for i in range(
                        len(target_vector))) / len(target_vector)
                total_loss += sample_loss
                count += 1

                # failure check
                predicted = outputs.index(max(outputs))
                target = target_vector.index(1.0)
                if predicted != target:
                    failures += 1

                self.network.backward(target_vector, learning_rate)

            avg_loss = total_loss / count if count else 0.0
            print(
                f"Epoch {epoch + 1}/{epochs} - Loss: {avg_loss:.6f} - Failures: {failures}/{count}")

    def generate_response(self, prompt, max_length=50):
        input_tokens = tokenize(prompt)
        clipped_tokens = input_tokens[-self.lookback_tokens:]
        while len(clipped_tokens) < self.lookback_tokens:
            clipped_tokens = [0] + clipped_tokens

        output_sequence = []
        for _ in range(max_length):
            for i, token in enumerate(clipped_tokens):
                self.network.set_input(i, token)
            output_probs = self.network.generate(clipped_tokens)
            next_token_index = output_probs.index(max(output_probs))
            output_sequence.append(next_token_index)
            clipped_tokens = clipped_tokens[1:] + [next_token_index]

        return detokenize(output_sequence)


def build_dataset_from_file(file_path, lookback_tokens):
    """
    Reads a text file and converts it into a dataset of (input_tokens, target_vector) pairs.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    tokenized_text = tokenize(text)
    dataset = []

    for i in range(len(tokenized_text) - 1):
        # Input sequence
        input_seq = tokenized_text[max(0, i - lookback_tokens + 1):i + 1]

        # Target as one-hot vector
        target_index = tokenized_text[i + 1]
        target_vector = [0.0] * len(tokens)
        target_vector[target_index] = 1.0

        dataset.append((input_seq, target_vector))

    return dataset


if __name__ == "__main__":
    lookback = 10
    ai = SharkAI(lookback)

    # Build dataset from data.txt
    dataset = build_dataset_from_file("data.txt", lookback)

    # Train the AI
    ai.train(dataset, epochs=100, learning_rate=0.5)

    print("\nHello, i am an AI. Type \"exit\" to exit.\n")
    while True:
        prompt = input(">>> ")
        if prompt.lower() == "exit":
            break
        response = ai.generate_response(prompt)
        print(response)

    print("\nGoodbye!\n")
