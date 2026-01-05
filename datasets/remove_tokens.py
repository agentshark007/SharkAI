import re


def remove_tokens_from_dataset(dataset, start_tag, sep_tag, end_tag):
    pattern = re.compile(
        re.escape(start_tag) +
        r"(user|assistant)" +
        re.escape(sep_tag) +
        r"(.*?)" +
        re.escape(end_tag))
    return pattern.sub(r"\2", dataset)


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read()

    restored = remove_tokens_from_dataset(data, "<START>", "<SEP>", "<END>")

    with open("data.txt", "w") as f:
        f.write(restored)
