import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):
        self.w1 = np.random.randn(layer_sizes[1], layer_sizes[0]) * 0.01
        self.w2 = np.random.randn(layer_sizes[2], layer_sizes[1]) * 0.01
        self.b1 = np.zeros((layer_sizes[1], 1))
        self.b2 = np.zeros((layer_sizes[2], 1))

    def activation(self, x):
        a = 1 / (1 + np.exp(-x))
        return a

    def forward(self, x):
        z1 = np.dot(self.w1, x) + self.b1
        a1 = self.activation(z1)
        z2 = np.dot(self.w2, a1) + self.b2
        a2 = self.activation(z2)
        return a2
