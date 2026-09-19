import numpy
from ..model.neural_network_model import NeuralNetworkModel


class NeuralNetwork:
    def __init__(self, input: list[float], model: NeuralNetworkModel):
        self.input = input

        self.model = model

    def foward_pass(self):
        z1 = numpy.dot(self.input, self.model.hidden_weight_1) + \
            self.model.hidden_bias_1
        a1 = numpy.tanh(z1)

        z2 = numpy.dot(self.model.output_weight, a1) * self.model.output_bias
        y = numpy.tanh(z2)

        return y
