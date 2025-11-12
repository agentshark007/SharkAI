import random
import time

class SMG:
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
            # for i in range(self.max_response_length):
            #     next_char = self._next_char(prompt, self.lookback_characters)
            #     prompt += next_char
            # return prompt

            prompt = f"<START>user<SEP>{prompt}<END><START>assistant<SEP>"
            original_prompt = prompt

            end_sequence = False

            while not (end_sequence or len(prompt.removeprefix(original_prompt)) > self.max_response_length):
                next_char = self._next_char(prompt, self.lookback_characters)
                prompt += next_char

                if prompt.endswith("<END>"):
                    end_sequence = True

            prompt = prompt.removeprefix(original_prompt)
            prompt = prompt.removesuffix("<END>")

            return prompt

        else:
            return "Error: SharkAI not configured. Please run setup() before generating text."
