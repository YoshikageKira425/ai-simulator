import numpy
from ..model.neural_network_model import NeuralNetworkModel


class Checkpoint:
    @staticmethod
    def save(
        model: NeuralNetworkModel,
        file_name: str = "best_results",
    ):
        file = f"checkpoints/{file_name}"

        numpy.savez_compressed(
            file=file,
            hidden_weight_1=model.hidden_weight_1,
            hidden_bias_1=model.hidden_bias_1,
            output_weight=model.output_weight,
            output_bias=model.output_bias,
        )

    @staticmethod
    def load(file_name: str = "best_results") -> NeuralNetworkModel:
        file = f"checkpoints/{file_name}.npz"

        result = numpy.load(file)

        return NeuralNetworkModel(
            result["hidden_weight_1"],
            result["hidden_bias_1"],
            result["output_weight"],
            result["output_bias"],
        )
