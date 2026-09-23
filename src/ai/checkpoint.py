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
            hidden_weight_2=model.hidden_weight_2,
            hidden_bias_2=model.hidden_bias_2,
            output_weight=model.output_weight,
            output_bias=model.output_bias,
        )

    @staticmethod
    def load(file_name: str = "best_results") -> NeuralNetworkModel | None:
        file = f"checkpoints/{file_name}.npz"

        try:
            result = numpy.load(file)
        except:
            return None
        
        if not result:
            return None

        return NeuralNetworkModel(
            result["hidden_weight_1"],
            result["hidden_bias_1"],
            result["hidden_weight_2"],
            result["hidden_bias_2"],
            result["output_weight"],
            result["output_bias"],
        )
