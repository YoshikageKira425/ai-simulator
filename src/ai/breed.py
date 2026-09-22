import random
import numpy
from ..core.car_agent import CarAgent
from ..model.neural_network_model import NeuralNetworkModel

ELITISM = 2
MUTATION_CHANCE = 0.1
MUTATION_STRENGTH = 0.1

def breed(agents: list[CarAgent], population:int = 20) -> list[NeuralNetworkModel]:
    results = []
    
    for i in range(ELITISM):
        results.append(agents[i].brain)
    
    for i in range(population - ELITISM):
        parent_a = _tournament_selection(agents)
        parent_b = _tournament_selection(agents)
        
        child = _crossover(parent_a, parent_b)
        
        mutated_child = _mutate(child)
        
        results.append(mutated_child)
        
    return results
        
def _tournament_selection(agents: list[CarAgent]) -> NeuralNetworkModel:
    k_agents = random.sample(agents, k=3)
    
    return max(k_agents, key=lambda agent: agent.fitness).brain

def _mutate(child: NeuralNetworkModel):
    if random.random() > MUTATION_CHANCE:
        return
    
    def mutate_matrix(matrix: numpy.ndarray) -> numpy.ndarray:
        mask = numpy.random.rand(*matrix.shape) < MUTATION_CHANCE
        noise = numpy.random.randn(*matrix.shape) * MUTATION_STRENGTH
        
        return matrix + (mask * noise)

    return NeuralNetworkModel(
        hidden_weight1=mutate_matrix(child.hidden_weight1),
        hidden_bias1=mutate_matrix(child.hidden_bias1),
        output_weight2=mutate_matrix(child.output_weight2),
        output_bias2=mutate_matrix(child.output_bias2),
    )

def _crossover(parent_a: NeuralNetworkModel, parent_b: NeuralNetworkModel) -> NeuralNetworkModel:
    hidden_weight_1 = (parent_a.hidden_weight_1 + parent_b.hidden_weight_1) / 2
    hidden_bias_1 = (parent_a.hidden_bias_1 + parent_b.hidden_bias_1) / 2

    output_weight = (parent_a.output_weight + parent_b.output_weight) / 2
    output_bias = (parent_a.output_bias + parent_b.output_bias) / 2
    
    child = NeuralNetworkModel(hidden_weight_1, hidden_bias_1, output_weight, output_bias)
    
    return child