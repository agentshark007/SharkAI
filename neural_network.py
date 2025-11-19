import math
import random


def random_list(length, min_value, max_value):
    return [random.uniform(min_value, max_value) for _ in range(length)]


class Layer:
    def __init__(self, nodes, bias_range=(-3, 3)):
        self.nodes = random_list(nodes, *bias_range)  # Random bias initialization


class InputLayer(Layer):
    pass


class HiddenLayer(Layer):
    pass


class OutputLayer(Layer):
    pass


class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.connections = []

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def add_layer(self, layer):
        self.layers.append(layer)

    def generate_connections(self):
        if len(self.layers) < 2:
            return
        self.connections = []
        for i in range(len(self.layers) - 1):
            layer_connections = []
            for _ in range(len(self.layers[i].nodes)):
                node_connections = random_list(len(self.layers[i + 1].nodes), -1, 1)
                layer_connections.append(node_connections)
            self.connections.append(layer_connections)

    def find_layer_type(self, layer_type):
        for layer in self.layers:
            if isinstance(layer, layer_type):
                return layer
        return None

    def forward(self):
        for l in range(1, len(self.layers)):
            current_layer = self.layers[l]
            previous_layer = self.layers[l - 1]
            for n, _ in enumerate(current_layer.nodes):
                total_input = sum(
                    previous_layer.nodes[pn] * self.connections[l - 1][pn][n]
                    for pn in range(len(previous_layer.nodes))
                )
                total_input += current_layer.nodes[n]  # add bias
                current_layer.nodes[n] = self.sigmoid(total_input)

    # Input/Output access
    def get_input(self, node):
        return self.find_layer_type(InputLayer).nodes[node]

    def set_input(self, node, value):
        self.find_layer_type(InputLayer).nodes[node] = value

    def get_output(self, node):
        return self.find_layer_type(OutputLayer).nodes[node]

    # Node access
    def get_value(self, layer, node):
        return self.layers[layer].nodes[node]

    def set_value(self, layer, node, value):
        self.layers[layer].nodes[node] = value

    # Weight access
    def get_weight(self, start_layer, start_node, end_layer, end_node):
        return self.connections[start_layer][start_node][end_node]

    def set_weight(self, start_layer, start_node, end_layer, end_node, value):
        self.connections[start_layer][start_node][end_node] = value

    def randomize_weight(self, start_layer, start_node, end_layer, end_node):
        self.set_weight(start_layer, start_node, end_layer, end_node, random.uniform(-1, 1))

    def nudge_weight(self, start_layer, start_node, end_layer, end_node, amount):
        self.set_weight(
            start_layer, start_node, end_layer, end_node,
            self.get_weight(start_layer, start_node, end_layer, end_node) + amount
        )

    # Bias access
    def get_bias(self, layer, node):
        return self.layers[layer].nodes[node]

    def set_bias(self, layer, node, value):
        self.layers[layer].nodes[node] = value

    def randomize_bias(self, layer, node):
        self.set_bias(layer, node, random.uniform(-3, 3))

    def nudge_bias(self, layer, node, amount):
        self.set_bias(layer, node, self.get_bias(layer, node) + amount)

    # Forward generation
    def generate(self, inputs):
        for i, value in enumerate(inputs):
            self.set_input(i, value)
        self.forward()
        return self.find_layer_type(OutputLayer).nodes
