import math
import random

class Node:
    def __init__(self, id, node_type):
        self.id = id
        self.node_type = node_type
        self.value = 0.0

class Connection:
    def __init__(self, from_node, to_node, weight=0.1):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

class NeuralNetwork:
    def __init__(self):
        self.nodes = {}  # id -> Node
        self.connections = []
        self.input_nodes = []
        self.output_nodes = []

    def generate_structure(self, input_size, hidden_layers, output_size):
        self.input_nodes = [self.add_node(f"input-{i}", "input") for i in range(input_size)]
        prev_layer = self.input_nodes

        hidden_node_layers = []
        for l_idx, size in enumerate(hidden_layers):
            layer = [self.add_node(f"hidden-{l_idx}-{i}", "hidden") for i in range(size)]
            hidden_node_layers.append(layer)
            self._fully_connect(prev_layer, layer)
            prev_layer = layer

        self.output_nodes = [self.add_node(f"output-{i}", "output") for i in range(output_size)]
        self._fully_connect(prev_layer, self.output_nodes)

        if not hidden_layers:
            self._fully_connect(self.input_nodes, self.output_nodes)

    def add_node(self, id, node_type):
        node = Node(id, node_type)
        self.nodes[id] = node
        return node

    def add_connection(self, from_node, to_node, weight=0.1):
        if isinstance(from_node, str):
            from_node = self.nodes[from_node]
        if isinstance(to_node, str):
            to_node = self.nodes[to_node]
        self.connections.append(Connection(from_node, to_node, weight))

    def _fully_connect(self, from_layer, to_layer, weight=0.1):
        for f in from_layer:
            for t in to_layer:
                self.add_connection(f, t, weight)

    def forward(self):
        # Reset non-input node values
        for node in self.nodes.values():
            if node.node_type != "input":
                node.value = 0

        # Simple feedforward (ignores layers, works recursively)
        for node in self.nodes.values():
            if node.node_type != "input":
                total_input = sum(conn.weight * conn.from_node.value for conn in self.connections if conn.to_node == node)
                node.value = 1 / (1 + math.exp(-total_input))

    def get_output(self):
        # Return all output node values
        return [node.value for node in self.output_nodes]

    def map_output_to_token(self, vocab_size):
        # Simple mapping: scale sigmoid output to token range
        output_val = self.output_nodes[0].value  # assume 1 output for now
        token_id = int(output_val * (vocab_size - 1))
        token_id = max(0, min(token_id, vocab_size - 1))
        return token_id
