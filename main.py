from smg import SMG

def main():
    with open("data.txt", "r") as f:
        dataset = f.read()

    ai = SMG(dataset)
    ai.setup(lookback_characters=20, max_response_length=100, start_tag="<START>", seperator_tag="<SEP>", end_tag="<END>")
    ai.set_dataset(dataset)

    while True:
        prompt = input(">>: ")
        response = ai.generate(prompt)
        print(response)

if __name__ == "__main__":
    main()
