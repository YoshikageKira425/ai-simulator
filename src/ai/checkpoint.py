import numpy
from ..model.neural_network_model import NeuralNetworkModel


class Checkpoint:
    @staticmethod
    def save(
        model: NeuralNetworkModel,
        file_name: str = "best_results",
    ):
        file_path = f"checkpoints/{file_name}"

        numpy.savez_compressed(
            file=file_path,
            hidden_weight_1=model.hidden_weight_1,
            hidden_bias_1=model.hidden_bias_1,
            hidden_weight_2=model.hidden_weight_2,
            hidden_bias_2=model.hidden_bias_2,
            output_weight=model.output_weight,
            output_bias=model.output_bias,
        )

    @staticmethod
    def load(file_name: str = "best_results") -> NeuralNetworkModel | None:
        file_path = f"checkpoints/{file_name}.npz"

        try:
            result = numpy.load(file_path)
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

    @classmethod
    def save_generation(
        generation: list[NeuralNetworkModel],
        file_name: str = "best_generation",
    ):
        file_path = f"checkpoints/{file_name}.npz"

        numpy.savez_compressed(
            file_path,
            hidden_weight_1=numpy.array(
                [m.hidden_weight_1 for m in generation]
            ),
            hidden_bias_1=numpy.array([m.hidden_bias_1 for m in generation]),
            hidden_weight_2=numpy.array(
                [m.hidden_weight_2 for m in generation]
            ),
            hidden_bias_2=numpy.array([m.hidden_bias_2 for m in generation]),
            output_weight=numpy.array([m.output_weight for m in generation]),
            output_bias=numpy.array([m.output_bias for m in generation]),
        )

    @classmethod
    def load_generation(file_name: str = "best_generation") -> list[NeuralNetworkModel] | None:
        file_path = f"checkpoints/{file_name}.npz"

        try:
            with numpy.load(file_path) as data:
                pop_size = len(data["hidden_weight_1"])
                return [
                    NeuralNetworkModel(
                        hidden_weight_1=data["hidden_weight_1"][i],
                        hidden_bias_1=data["hidden_bias_1"][i],
                        hidden_weight_2=data["hidden_weight_2"][i],
                        hidden_bias_2=data["hidden_bias_2"][i],
                        output_weight=data["output_weight"][i],
                        output_bias=data["output_bias"][i],
                    )
                    for i in range(pop_size)
                ]
        except Exception:
            return None
