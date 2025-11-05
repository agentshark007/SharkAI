from datasets import load_dataset

# Parameters
max_chars = 1_000_000
output_file = "data.txt"

# Load the dataset (streaming mode)
ds = load_dataset("codeparrot/codeparrot-clean", split="train", streaming=True)

char_count = 0
samples = []

# Collect code until reaching ~1 million characters
for sample in ds:
    code = sample["content"]  # use "content" key
    samples.append(code)
    char_count += len(code)
    if char_count >= max_chars:
        break

# Write to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(samples))

print(f"Saved {char_count} characters to {output_file}")
