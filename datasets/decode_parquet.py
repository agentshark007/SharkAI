import pandas as pd

df = pd.read_parquet("train.parquet")  # local file path

with open("data.txt", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        f.write(row["question"].strip() + "\n")
        f.write(row["answer"].strip() + "\n")
