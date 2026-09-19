import numpy
from ..model.neural_network_model import NeuralNetworkModel


class Checkpoint:
    @staticmethod
    def save(hidden_weight_1, hidden_bias_1, output_weight, output_bias, file_name: str = "best_results"):
        file = f"checkout/{file_name}"

        numpy.savez_compressed(
            file=file,
            hidden_weight_1=hidden_weight_1,
            hidden_bias_1=hidden_bias_1,
            output_weight=output_weight,
            output_bias=output_bias
        )

    @staticmethod
    def load(file_name: str = "best_results") -> NeuralNetworkModel:
        file = f"checkout/{file_name}.npz"

        result = numpy.load(file)

        return NeuralNetworkModel(
            result["hidden_weight_1"],
            result["hidden_bias_1"],
            result["output_weight"],
            result["output_bias"],
        )
