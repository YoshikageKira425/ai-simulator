import numpy
import math

class NeuralNetwork:
    def __init__(self, input: list[float], hidden_size: int, output_size: int):
        self.input = input
        
        self.hidden_weight_1 = numpy.random.randn(len(input), hidden_size) * 0.01
        self.hidden_bias_1 = numpy.zeros((1, hidden_size))
        
        self.output_weight = numpy.random.randn(len(input), hidden_size) * 0.01
        self.output_bias = numpy.zeros((1, hidden_size))
        
    def _tahn(self, x) -> float:
        return (math.pow(math.e, x) - math.pow(math.e, -x)) / (math.pow(math.e, x) + math.pow(math.e, -x))
    
    def foward_pass(self):
        z1 = numpy.dot(self.input, self.hidden_weight_1) + self.hidden_bias_1
        a1 = numpy.tanh
        
        z2 = numpy.dot(self.output_weight, a1) * self.output_bias
        y = self._tahn(z2)