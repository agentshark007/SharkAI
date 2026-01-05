def add_tokens_to_dataset(dataset, start_tag, sep_tag, end_tag):

    def add_tokens_to_string(string, id, start_tag, sep_tag, end_tag):
        return f"{start_tag}{id}{sep_tag}{string}{end_tag}"

    lines = dataset.split("\n")

    for i, line in enumerate(lines):
        if i % 2 == 0:
            lines[i] = add_tokens_to_string(
                line, "user", start_tag, sep_tag, end_tag)
        else:
            lines[i] = add_tokens_to_string(
                line, "assistant", start_tag, sep_tag, end_tag)

    return "\n".join(lines)


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read()

    processed = add_tokens_to_dataset(data, "<START>", "<SEP>", "<END>")

    with open("data.txt", "w") as f:
        f.write(processed)
