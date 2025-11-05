import random
import time

class SharkAI:
    def __init__(self, dataset):
        # Initialize SharkAI with a dataset and prepare internal states
        self.dataset = dataset
        self.ready = False
        self.cache = {}
        
    def set_dataset(self, dataset):
        # Replace dataset and reset cache
        self.dataset = dataset
        self.cache = {}

    def clear_cache(self):
        # Clear the cache manually
        self.cache = {}
        pass

    def setup(self, lookback_characters, max_response_length):
        # Configure model parameters
        self.lookback_characters = lookback_characters
        self.max_response_length = max_response_length
        self.ready = True

    def _next_char(self, prompt, lookback_characters):
        # Internal function to predict the next character

        def find_sequence_end_indices(data, seq):
            # Find all indices where a sequence occurs in dataset
            indices = []
            start = 0
            while True:
                idx = data.find(seq, start)
                if idx == -1:
                    break
                indices.append(idx + len(seq) - 1)
                start = idx + 1
            return indices

        lookback_characters_original = lookback_characters
        end_indices = []

        # Use cached indices if available
        if prompt[-lookback_characters_original:] in self.cache:
            end_indices = self.cache[prompt[-lookback_characters_original:]]
        else:
            # Decrease lookback length until sequence is found
            while lookback_characters > 0 and end_indices == []:
                end_indices = find_sequence_end_indices(self.dataset, prompt[-lookback_characters:])
                lookback_characters -= 1

        if end_indices:
            # Pick a random match and get the next character
            character_index = random.choice(end_indices) + 1
            if character_index >= len(self.dataset):
                character_index = 0

            # Cache result for future use
            self.cache[prompt[-lookback_characters_original:]] = end_indices

            return self.dataset[character_index]
        else:
            # Fallback to random character if no match found
            return random.choice(self.dataset)

    def generate(self, prompt):
        # Generate text by repeatedly predicting next characters
        if self.ready:
            for i in range(self.max_response_length):
                next_char = self._next_char(prompt, self.lookback_characters)
                prompt += next_char
            return prompt
        else:
            return prompt
    
    def print(self, prompt, delay=False):
        # Print generated text with optional typing delay
        if self.ready:
            print(prompt, end='', flush=True)

            for i in range(self.max_response_length):
                next_char = self._next_char(prompt, self.lookback_characters)
                prompt += next_char
                if delay:
                    time.sleep(random.randint(5, 50) / 1000)  # Simulate typing
                print(next_char, end='', flush=True)
        else:
            print(prompt)

        print("\n")

if __name__ == "__main__":
    # Load dataset from file
    dataset_file = "data.txt"
    with open(dataset_file, "r") as f:
        dataset = f.read()

    # Initialize SharkAI and configure parameters
    ai = SharkAI(dataset)
    ai.setup(lookback_characters=10, max_response_length=100)

    # Interactive text generation loop
    print("SharkAI is ready. Type 'exit' to exit the program. Type your prompt below:")
    while True:
        prompt = input(">>: ")
        if prompt.lower() == "exit":
            break
        ai.print(prompt)
