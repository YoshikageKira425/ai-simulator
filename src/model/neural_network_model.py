from dataclasses import dataclass
import numpy


@dataclass
class NeuralNetworkModel:
    hidden_weight_1: numpy.ndarray
    hidden_bias_1: numpy.ndarray
    output_weight: numpy.ndarray
    output_bias: numpy.ndarray
    
    @classmethod
    def random(
        cls, input_size: int, hidden_size: int, output_size: int
    ) -> NeuralNetworkModel:
        return cls(
            hidden_weight_1=numpy.random.randn(input_size, hidden_size) * 0.01,
            hidden_bias_1=numpy.zeros((1, hidden_size)),
            output_weight=numpy.random.randn(hidden_size, output_size) * 0.01,
            output_bias=numpy.zeros((1, output_size)),
        )
    
    def copy(self) -> NeuralNetworkModel:
        return NeuralNetworkModel(
            self.hidden_weight_1,
            self.hidden_bias_1,
            self.output_weight, 
            self.output_bias
        )
