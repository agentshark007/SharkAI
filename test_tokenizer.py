from tiktoktoken import tokenize, detokenize, tokens

not_changed = input("text: ")
tokenized = tokenize(not_changed)
detokenized = detokenize(tokenized)

print(detokenized)
