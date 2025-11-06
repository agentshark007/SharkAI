from slm import SLM

def main():
    with open("data.txt", "r") as f:
        dataset = f.read().splitlines()

    ai = SLM(dataset)
    ai.initialize_network(hidden_layers=[20], lookback_tokens=10)
    ai.train(epochs=5, influence=0.1)

    print("SharkAI is ready. Type 'exit' to quit.")
    while True:
        prompt = input(">>: ")
        if prompt.lower() == "exit":
            break
        ai.generate_and_print_response(prompt, length=50)

if __name__ == "__main__":
    main()
