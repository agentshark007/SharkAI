from collections import Counter

class TikTokToken:
    def __init__(self):
        self.token_dict = {}
        self.inverse_token_dict = {}

    def generate_tokens(self, dataset):
        # Find common 1–5 character sequences
        seq_counter = Counter()
        for text in dataset:
            for length in range(1, 6):
                for i in range(len(text) - length + 1):
                    seq = text[i:i+length]
                    seq_counter[seq] += 1

        # Keep top 1000 sequences as tokens
        common = [seq for seq, _ in seq_counter.most_common(1000)]

        # Add special tokens
        self.token_dict = {
            "<START>": 0,
            "<SEP>": 1,
            "<END>": 2,
        }
        for i, seq in enumerate(common, start=3):
            self.token_dict[seq] = i

        # Build inverse mapping
        self.inverse_token_dict = {v: k for k, v in self.token_dict.items()}

    def tokenize(self, text):
        tokens = []
        i = 0
        while i < len(text):
            match = None
            for length in range(5, 0, -1):
                sub = text[i:i+length]
                if sub in self.token_dict:
                    match = sub
                    break
            if match:
                tokens.append(self.token_dict[match])
                i += len(match)
            else:
                # fallback to single char
                tokens.append(self.token_dict.get(text[i], len(self.token_dict)))
                i += 1
        return tokens

    def detokenize(self, tokens):
        return "".join(self.inverse_token_dict.get(t, "") for t in tokens)

    def generate_token_dataset(self, dataset, start_token="<START>", separator_token="<SEP>", end_token="<END>"):
        token_datasets = []
        for text in dataset:
            tokenized = [self.token_dict[start_token]] + self.tokenize(text) + [self.token_dict[end_token]]
            token_datasets.append(tokenized)
        return token_datasets

    def prepare_for_response_generation(self, prompt, lookback_characters):
        trimmed_prompt = prompt[-lookback_characters:]
        tokens = [self.token_dict["<START>"]] + self.tokenize(trimmed_prompt)
        return tokens
