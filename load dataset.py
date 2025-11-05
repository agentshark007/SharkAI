from datasets import load_dataset

# Maximum number of characters to collect
max_chars = 1_000_000

# Output text file to save collected data
output_file = "data.txt"

# Load the "codeparrot-clean" dataset in streaming mode (no full download)
ds = load_dataset("codeparrot/codeparrot-clean", split="train", streaming=True)

char_count = 0
samples = []

# Iterate through samples from the dataset
for sample in ds:
    code = sample["content"]  # Extract code content from sample
    samples.append(code)
    char_count += len(code)   # Track total number of characters collected
    if char_count >= max_chars:
        break  # Stop once character limit reached

# Write collected code samples to file, separated by blank lines
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(samples))

# Display completion summary
print(f"Saved {char_count} characters to {output_file}")
