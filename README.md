# SharkAI – Sequential Markov Generator (SMG)

SharkAI is a character-level text generator using the Sequential Markov Generator (SMG) method. It predicts the next character in a sequence based on a dataset and configurable parameters for lookback and maximum response length.

## Features

* Character-level generation
* Adjustable lookback for sequence matching
* Configurable maximum response length
* Simple and lightweight design

## Installation

1. Clone the repository or download the script.
2. Ensure Python 3 is installed.
3. Prepare a dataset text file (`data.txt`) containing the text to train on.

## Usage

1. Run the script: python main.py
2. Enter a prompt when prompted (`>>:`).
3. SharkAI will generate text based on your prompt and the dataset.

## Configuration

* `lookback_characters`: Number of previous characters considered when finding a match in the dataset.
* `max_response_length`: Maximum number of characters generated per prompt.

## Notes

* SharkAI generates text by finding sequences in the dataset that match the end of your prompt.
* If no matching sequence is found, it picks a random character from the dataset.
* Ensure your dataset is large enough for meaningful text generation.
