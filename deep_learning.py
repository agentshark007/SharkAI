import math

class NeuralNetwork():
    def sigmoid(self, x):
        return 1 / (1 + math.pow(math.e, -x))
