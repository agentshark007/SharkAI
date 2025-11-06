from slm import SLM  # make sure SLM class is in slm.py

def main():
    # Load dataset from file
    dataset_file = "data.txt"
    with open(dataset_file, "r") as f:
        dataset = f.read().splitlines()  # treat each line as separate entries

    # Initialize SLM and configure parameters
    ai = SLM(dataset)
    lookback_tokens = 10
    hidden_layers = [20]  # example hidden layer configuration
    ai.initialize_network(hidden_layers=hidden_layers, lookback_tokens=lookback_tokens)
    ai.train(epochs=5, influence=0.1)  # very simple naive training

    # Interactive text generation loop
    print("SharkAI is ready. Type 'exit' to exit the program. Type your prompt below:")
    while True:
        try:
            prompt = input(">>: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if prompt.strip().lower() == "exit":
            print("Exiting.")
            break

        response = ai.generate_and_print_response(prompt, length=50)
        print("\n")  # newline after output

if __name__ == "__main__":
    main()
