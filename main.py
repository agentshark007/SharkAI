import random

class SharkAI:
    def __init__(self, dataset):
        self.dataset = dataset
        self.ready = False

    def setup(self, lookback_characters, lookback_influence, max_response_length):
        self.lookback_characters = lookback_characters
        self.lookback_influence = lookback_influence
        self.max_response_length = max_response_length
        self.ready = True

    def next(self, prompt, lookback_characters, lookback_influence, dataset):
        def find_sequence_end_indices(data, seq):
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
        while lookback_characters > 0 and end_indices == []:
            end_indices = find_sequence_end_indices(dataset, prompt[-lookback_characters:])
            lookback_characters -= 1

            if random.random() < lookback_influence:
                if random.random() < lookback_characters / lookback_characters_original:
                    end_indices = []

        if end_indices:
            character_index = random.choice(end_indices) + 1

            if character_index >= len(dataset):
                character_index = 0

            return dataset[character_index]
        else:
            return random.choice(dataset)

    def generate(self, prompt):
        if self.ready:
            for i in range(self.max_response_length):
                next_char = self.next(prompt, self.lookback_characters, self.lookback_influence, self.dataset)
                prompt += next_char
        else:
            return "Not ready to generate"
        
        return prompt

if __name__ == "__main__":
    dataset_file = "data.txt"
    with open(dataset_file, "r") as f:
        dataset = f.read()

    ai = SharkAI(dataset)
    ai.setup(lookback_characters=5, lookback_influence=1, max_response_length=50)

    while True:
        prompt = input(">>: ")
        print(ai.generate(prompt))
