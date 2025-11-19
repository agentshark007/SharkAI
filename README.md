# Neural Network Experiment

This project is a basic feedforward neural network for experimentation with biases, weights, and forward propagation. It is designed for learning and testing neural network concepts with simple datasets.

---

## Features

* Fully connected feedforward network
* Input, hidden, and output layers
* Randomized weights and biases
* Forward propagation using sigmoid activation
* Access and modification of nodes, weights, and biases
* Lightweight and easy to extend
* Forward generation from input to output

---

## Installation

1. Clone or download the project.
2. Ensure Python 3 is installed.
3. Provide a dataset file named `data.txt` in the project folder (optional, for experiments).

---

## Usage

```python
from neural_network import *

# Create a neural network
nn = NeuralNetwork()

# Add layers: 2 inputs, 3 hidden nodes, 1 output
nn.add_layer(InputLayer(2))
nn.add_layer(HiddenLayer(3))
nn.add_layer(OutputLayer(1))

# Generate random connections
nn.generate_connections()

# Set input values
nn.set_input(0, 0.5)
nn.set_input(1, -0.7)

# Run forward propagation
outputs = nn.generate([0.5, -0.7])
print("Network output:", outputs)

# Optional: inspect weights and biases
print("\nWeights:")
for i, layer_conn in enumerate(nn.connections):
    print(f"Layer {i} to {i+1}: {layer_conn}")

print("\nBiases:")
for i, layer in enumerate(nn.layers):
    print(f"Layer {i} biases: {layer.nodes}")
```

---

## Neural Network API

* `add_layer(layer)` – Add `InputLayer`, `HiddenLayer`, or `OutputLayer`
* `generate_connections()` – Randomly initialize weights between layers
* `forward()` – Compute outputs from current inputs
* `get_input(node)` / `set_input(node, value)` – Access input nodes
* `get_output(node)` – Access output nodes
* `get_value(layer, node)` / `set_value(layer, node, value)` – Access any node
* `get_weight(start_layer, start_node, end_layer, end_node)` / `set_weight(...)` – Access weights
* `get_bias(layer, node)` / `set_bias(layer, node, value)` – Access biases
* `nudge_weight` / `nudge_bias` – Increment weights or biases
* `randomize_weight` / `randomize_bias` – Randomize weights or biases

---

## Example Dataset Format (optional)

```
<START>user<SEP>Hello<END>
<START>assistant<SEP>Hi there!<END>
```

---

## Related Tools and Resources

* [BNF Generator](https://baturin.org/tools/bnfgen/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* [GSM8K Dataset Viewer](https://huggingface.co/datasets/openai/gsm8k/viewer)

---

## License

**CC BY-NC 4.0** – Share and adapt with attribution. No commercial use.
