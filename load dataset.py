from datasets import load_dataset

max_chars = 1_000_000
output_file = "data.txt"

ds = load_dataset("codeparrot/codeparrot-clean", split="train", streaming=True)

char_count = 0
samples = []

for sample in ds:
    code = sample["content"]
    samples.append(code)
    char_count += len(code)
    if char_count >= max_chars:
        break

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(samples))

print(f"Saved {char_count} characters to {output_file}")
