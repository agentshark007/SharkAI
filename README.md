# Deep Learning Experement kinda thing...




Alright! We are doing some stuff to turn this thing into a deep learning neural network kinda thing.



...



SMG is a character-level text generator that predicts the next character in a sequence by scanning a dataset for matching sequences. It uses a simple Sequential-Markov lookup approach with adjustable lookback and supports conversation-style tagging.

## Features

* Character-level generation
* Adjustable lookback window
* Configurable maximum response length
* Conversation-tag support (`<START>`, `<SEP>`, `<END>`)
* Lightweight implementation
* Cache for repeated sequence lookups

## Installation

1. Clone or download the project.
2. Ensure Python 3 is installed.
3. Provide a dataset file named `data.txt` in the project folder.

## Usage

1. Run the generator:

```bash
python main.py
```

2. Enter a prompt at the `>>:` prompt.
3. SMG generates a response based on dataset patterns.

## Configuration

When initializing SMG, you can configure:

* `lookback_characters` – Number of characters used to search for sequence matches.
* `max_response_length` – Maximum number of characters in the generated response.
* `start_tag`, `seperator_tag`, `end_tag` – Tags used to structure conversation data.

Example setup:

```python
ai.setup(
    lookback_characters=20,
    max_response_length=100,
    start_tag="<START>",
    seperator_tag="<SEP>",
    end_tag="<END>"
)
```

## How It Works

1. SMG scans the dataset for sequences matching the end of your prompt.
2. If a match is found, the next character after the match is selected.
3. If no match exists, a random character from the dataset is used.
4. Responses are automatically wrapped in `<START>assistant<SEP>` … `<END>` tags.

## Example Dataset Format

```
<START>user<SEP>Hello<END>
<START>assistant<SEP>Hi there!<END>
```

## Notes

* Larger datasets improve response quality.
* The cache speeds up repeated lookups.
* Designed for simple, conversation-style text generation.

## Related Tools and Resources

* [BNF Generator](https://baturin.org/tools/bnfgen/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* [GSM8K Dataset Viewer](https://huggingface.co/datasets/openai/gsm8k/viewer)

## License

This project is licensed under **CC BY-NC 4.0**.
You may share and adapt the material with attribution. Commercial use is not permitted.
