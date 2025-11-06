from collections import Counter

class TikTokToken:
    def __init__(self, max_seq_len=5, vocab_size=1000):
        self.max_seq_len = max_seq_len
        self.vocab_size = vocab_size
        self.token_dict = {}
        self.inverse_token_dict = {}

    def generate_tokens(self, dataset):
        seq_counter = Counter()
        for text in dataset:
            text = text.strip()
            for n in range(1, self.max_seq_len + 1):
                seq_counter.update(text[i:i+n] for i in range(len(text) - n + 1))

        common = [seq for seq, _ in seq_counter.most_common(self.vocab_size)]

        self.token_dict = {"<START>": 0, "<SEP>": 1, "<END>": 2}
        self.token_dict.update({seq: i + 3 for i, seq in enumerate(common)})
        self.inverse_token_dict = {v: k for k, v in self.token_dict.items()}

    def tokenize(self, text):
        tokens, i = [], 0
        while i < len(text):
            for n in range(self.max_seq_len, 0, -1):
                sub = text[i:i+n]
                if sub in self.token_dict:
                    tokens.append(self.token_dict[sub])
                    i += n
                    break
            else:
                tokens.append(self.token_dict.get(text[i], len(self.token_dict)))
                i += 1
        return tokens

    def detokenize(self, tokens):
        return "".join(self.inverse_token_dict.get(t, "") for t in tokens)

    def generate_token_dataset(self, dataset, start_keyword, sep_keyword, end_keyword):
        s, sep, e = self.token_dict["<START>"], self.token_dict["<SEP>"], self.token_dict["<END>"]
        tokenized_datasets = []
        for text in dataset:
            text = text.replace(start_keyword, "<START>").replace(sep_keyword, "<SEP>").replace(end_keyword, "<END>")
            tokens = []
            for token in text.split():
                if token == "<START>":
                    tokens.append(s)
                elif token == "<SEP>":
                    tokens.append(sep)
                elif token == "<END>":
                    tokens.append(e)
                else:
                    tokens.extend(self.tokenize(token))
            tokenized_datasets.append(tokens)
        return tokenized_datasets

    def prepare_for_response_generation(self, prompt, lookback_characters):
        trimmed_prompt = prompt[-lookback_characters:]
        s, sep, e = self.token_dict["<START>"], self.token_dict["<SEP>"], self.token_dict["<END>"]
        tokens = [s] + self.tokenize("user") + [sep] + self.tokenize(trimmed_prompt) + [e] + [s] + self.tokenize("assistant") + [sep]
        return tokens
