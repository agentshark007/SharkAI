from neural_network import NeuralNetwork, InputLayer, HiddenLayer, OutputLayer

# Create network
nn = NeuralNetwork()
nn.add_layer(InputLayer(2))   # 2 input nodes
nn.add_layer(HiddenLayer(3))  # 3 hidden nodes
nn.add_layer(OutputLayer(2))  # 2 output nodes

# Generate connections
nn.generate_connections()

# Set inputs
nn.set_input(0, 0.5)
nn.set_input(1, -0.5)

# Manually set all weights to fixed values for test
for l in range(len(nn.connections)):
    for sn in range(len(nn.connections[l])):
        for en in range(len(nn.connections[l][sn])):
            nn.set_weight(l, sn, l + 1, en, 0.1 * (sn + 1)
                          * (en + 1))  # example weights

# Manually set all biases to fixed values
for layer_index, layer in enumerate(
        nn.layers[1:], start=1):  # skip input layer
    for node_index in range(len(layer.nodes)):
        nn.set_bias(layer_index, node_index, 0.2 *
                    (node_index + 1))  # example biases

# Forward pass
nn.forward()

# Print results
inputs = [nn.get_input(i) for i in range(2)]
outputs = [nn.get_output(i) for i in range(2)]

print("Inputs:", inputs)
print("Outputs:", outputs)
