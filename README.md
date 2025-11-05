# SharkAI – Sequential Markov Generator (SMG)

SharkAI is a character-level text generator using the Sequential Markov Generator (SMG) method. It predicts the next character in a sequence based on a dataset and configurable parameters for lookback and influence.

## Features

* Character-level generation
* Adjustable lookback for sequence matching
* Influence parameter to control randomness
* Configurable maximum response length

## Installation

1. Clone the repository or download the script.
2. Ensure Python 3 is installed.
3. Prepare a dataset text file (`data.txt`) containing the text to train on.

## Usage

1. Run the script.
2. Enter a prompt when prompted.
3. SharkAI will generate text based on your prompt and the dataset.

## Configuration

* `lookback_characters`: Number of previous characters considered for predicting the next character.
* `lookback_influence`: Probability of biasing predictions toward sequences matching the lookback.
* `max_response_length`: Maximum number of characters generated per prompt.
