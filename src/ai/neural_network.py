import numpy
from ..model.neural_network_model import NeuralNetworkModel


class NeuralNetwork:
    def __init__(self, model: NeuralNetworkModel):
        self.model = model

    def foward_pass(self, input: list[float]):
        z1 = numpy.dot(input, self.model.hidden_weight_1) + self.model.hidden_bias_1
        a1 = numpy.tanh(z1)

        z2 = numpy.dot(a1, self.model.output_weight) + self.model.output_bias
        y = numpy.tanh(z2)

        return y
