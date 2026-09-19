from dataclasses import dataclass
import numpy


@dataclass
class NeuralNetworkModel:
    hidden_weight_1: numpy.ndarray
    hidden_bias_1: numpy.ndarray
    output_weight: numpy.ndarray
    output_bias: numpy.ndarray
