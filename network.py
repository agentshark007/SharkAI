import math

class Node:
    def __init__(self, id, node_type):
        self.id = id
        self.node_type = node_type  # 'input', 'hidden', 'output'
        self.value = None

class Connection:
    def __init__(self, from_node, to_node, weight=0.1):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

class NeuralNetwork:
    def __init__(self):
        self.nodes = {}  # id -> Node
        self.connections = []  # list of Connection

    def generate_structure(self, input_size, hidden_layers, output_size):
        input_nodes = [self.add_node(f"input-{i}", "input") for i in range(input_size)]
        hidden_node_layers = []
        for l_idx, size in enumerate(hidden_layers):
            hidden_node_layers.append([self.add_node(f"hidden-{l_idx}-{i}", "hidden") for i in range(size)])
        output_nodes = [self.add_node(f"output-{i}", "output") for i in range(output_size)]

        # Connect layers
        prev_layer = input_nodes
        for layer in hidden_node_layers:
            self._fully_connect(prev_layer, layer)
            prev_layer = layer
        self._fully_connect(prev_layer, output_nodes)

        # If no hidden layers, connect input directly to output
        if not hidden_node_layers:
            self._fully_connect(input_nodes, output_nodes)

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

    def set_weight(self, conn_index, value):
        self.connections[conn_index].weight = value

    def set_value(self, node_id, value):
        self.nodes[node_id].value = value

    def _fully_connect(self, from_layer, to_layer, weight=0.1):
        for f in from_layer:
            for t in to_layer:
                self.add_connection(f, t, weight)

    def determine_value(self, node_id, visited=None):
        if visited is None:
            visited = set()
        if node_id in visited:
            raise RuntimeError("Cycle detected in network")
        visited.add(node_id)

        node = self.nodes.get(node_id)
        if not node:
            return None
        if node.node_type == "input":
            return node.value if node.value is not None else 0

        # Weighted sum of incoming connections
        total_input = 0
        for conn in self.connections:
            if conn.to_node.id == node_id:
                from_val = conn.from_node.value
                if from_val is None:
                    from_val = self.determine_value(conn.from_node.id, visited)
                total_input += conn.weight * from_val

        # Sigmoid activation
        node.value = 1 / (1 + math.exp(-total_input))
        return node.value
