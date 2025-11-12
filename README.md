# SharkAI – Sequential Markov Generator (SMG)

SharkAI is a character-level text generator using the Sequential Markov Generator (SMG) method. It predicts the next character in a sequence based on a dataset and configurable parameters for lookback and maximum response length.

## Features

* Character-level generation
* Adjustable lookback for sequence matching
* Configurable maximum response length
* Simple and lightweight design
* Conversation-style prompts and responses

## Installation

1. Clone the repository or download the script.
2. Ensure Python 3 is installed.
3. Prepare a dataset text file (`data.txt`) containing the text to train on.

## Usage

1. Run the script: `python main.py`
2. Enter a prompt when prompted (`>>:`).
3. SharkAI will generate text based on your prompt.

## Configuration

* `lookback_characters`: Number of previous characters considered when finding a match in the dataset.
* `max_response_length`: Maximum number of characters generated per prompt.
* `start_tag`, `seperator_tag`, `end_tag`: Tags used to structure conversations in the dataset.

## Notes

* SharkAI generates text by finding sequences in the dataset that match the end of your prompt.
* If no matching sequence is found, it picks a random character from the dataset.
* The system supports structured conversation data with user and assistant roles.
* Ensure your dataset is large enough for meaningful text generation.

## Example Conversation Format

```
<START>user<SEP>Hello<END><START>assistant<SEP>Hi there!<END>
<START>user<SEP>How are you?<END><START>assistant<SEP>Doing well, thanks!<END>
```

## License

This work is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

You are free to:

* **Share** — copy and redistribute the material in any medium or format.
* **Adapt** — remix, transform, and build upon the material.

Under the following terms:

* **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
* **NonCommercial** — You may not use the material for commercial purposes.

Full license: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)
