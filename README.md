# SMG – Sequential Markov Generator

SMG is a character-level text generator that predicts the next character in a sequence by scanning a dataset for matching sequences. It uses a simple Sequential-Markov lookup approach with adjustable lookback and supports conversation-style tagging.

## Features

* Character-level generation
* Adjustable lookback window
* Configurable maximum response length
* Conversation-tag support
* Lightweight implementation

## Installation

1. Clone or download the project.
2. Ensure Python 3 is installed.
3. Provide a dataset file named `data.txt`.

## Usage

1. Run `python main.py`.
2. Enter a prompt when `>>:` appears.
3. SMG generates a response using dataset patterns.

## Configuration

* **lookback_characters** – Number of characters used when searching for matches.
* **max_response_length** – Maximum output length.
* **start_tag**, **seperator_tag**, **end_tag** – Conversation structure tags.

## Notes

* SMG looks for dataset sequences matching the end of your prompt.
* If no match is found, a random dataset character is used.
* Supports user/assistant-style training data.
* Larger datasets improve output quality.

## Example Conversation Format

```
<START>user<SEP>Hello<END>
<START>assistant<SEP>Hi there!<END>
```

## Related Tools and Resources

* [https://baturin.org/tools/bnfgen/](https://baturin.org/tools/bnfgen/)
* [https://pypi.org/project/PyAutoGUI/](https://pypi.org/project/PyAutoGUI/)
* [https://huggingface.co/datasets/openai/gsm8k/viewer](https://huggingface.co/datasets/openai/gsm8k/viewer)

## License

This project is licensed under **CC BY-NC 4.0**.

You may share and adapt the material with attribution.
Commercial use is not permitted.
