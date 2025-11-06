from smg import SMG

if __name__ == "__main__":
    # Load dataset from file
    dataset_file = "data.txt"
    with open(dataset_file, "r") as f:
        dataset = f.read()

    # Initialize SharkAI and configure parameters
    ai = SMG(dataset)
    ai.setup(lookback_characters=10, max_response_length=100)

    # Interactive text generation loop
    print("SharkAI is ready. Type 'exit' to exit the program. Type your prompt below:")
    while True:
        prompt = input(">>: ")
        if prompt.lower() == "exit":
            break
        ai.print(prompt)
