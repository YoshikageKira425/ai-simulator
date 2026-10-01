from dataclasses import dataclass
import numpy


@dataclass
class NeuralNetworkModel:
    hidden_weight_1: numpy.ndarray
    hidden_bias_1: numpy.ndarray
    hidden_weight_2: numpy.ndarray
    hidden_bias_2: numpy.ndarray
    output_weight: numpy.ndarray
    output_bias: numpy.ndarray

    @classmethod
    def random(cls, hidden_size: int = 6) -> NeuralNetworkModel:
        return cls(
            hidden_weight_1=numpy.random.randn(5, hidden_size) * 0.01,
            hidden_bias_1=numpy.zeros((1, hidden_size)),
            hidden_weight_2=numpy.random.randn(hidden_size, hidden_size) * 0.01,
            hidden_bias_2=numpy.zeros((1, hidden_size)),
            output_weight=numpy.random.randn(hidden_size, 2) * 0.01,
            output_bias=numpy.zeros((1, 2)),
        )

    def copy(self) -> NeuralNetworkModel:
        return NeuralNetworkModel(
            self.hidden_weight_1,
            self.hidden_bias_1,
            self.hidden_weight_2,
            self.hidden_bias_2,
            self.output_weight,
            self.output_bias,
        )
