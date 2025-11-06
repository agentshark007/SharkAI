from tiktoktoken import TikTokToken

if __name__ == "__main__":
    # Sample dataset
    dataset = [
        "hello world",
        "hi there",
        "hello there",
        "world of ai",
        "hi world"
    ]

    tokenizer = TikTokToken()
    tokenizer.generate_tokens(dataset)

    print("Token dictionary sample (first 10):")
    for k, v in list(tokenizer.token_dict.items())[:10]:
        print(f"{k}: {v}")

    # Generate tokenized dataset
    token_dataset = tokenizer.generate_token_dataset(dataset)
    print("\nTokenized dataset:")
    for td in token_dataset:
        print(td)

    # Test prompt preparation
    prompt = "hello world"
    tokens_for_prompt = tokenizer.prepare_for_response_generation(prompt, lookback_characters=8)
    print("\nTokens for response generation:")
    print(tokens_for_prompt)

    # Tokenize and detokenize a string
    text = "hi world"
    tokens = tokenizer.tokenize(text)
    reconstructed = tokenizer.detokenize(tokens)

    print("\nOriginal text:", text)
    print("Tokens:", tokens)
    print("Reconstructed:", reconstructed)
