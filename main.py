from neural_network import *

# Create a neural network
nn = NeuralNetwork()

# Add layers: 2 inputs, 3 hidden nodes, 1 output
nn.add_layer(InputLayer(2))
nn.add_layer(HiddenLayer(3))
nn.add_layer(OutputLayer(1))

# Generate random weights
nn.generate_connections()

# Set inputs
nn.set_input(0, 0.5)
nn.set_input(1, -0.7)

# Run forward propagation
outputs = nn.generate([0.5, -0.7])

# Print outputs
print("Network output:", outputs)

# Optional: print weights and biases
print("\nWeights:")
for i, layer_conn in enumerate(nn.connections):
    print(f"Layer {i} to {i+1}: {layer_conn}")

print("\nBiases:")
for i, layer in enumerate(nn.layers):
    print(f"Layer {i} biases: {layer.nodes}")
