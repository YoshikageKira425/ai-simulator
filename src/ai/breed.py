import random
import numpy
from ..core.car_agent import CarAgent
from ..model.neural_network_model import NeuralNetworkModel

ELITISM = 2

def breed(agents: list[CarAgent], population:int = 20) -> list[NeuralNetworkModel]:
    results = []
    
    for i in range(ELITISM):
        results.append(agents[i].brain)
    
    for i in range(population - ELITISM):
        parent_a = _tournament_selection(agents)
        parent_b = _tournament_selection(agents)
        
        results.append(_crossover(parent_a, parent_b))
        
    return results
        
def _tournament_selection(agents: list[CarAgent]) -> NeuralNetworkModel:
    k_agents = random.sample(agents, k=3)
    
    return max(k_agents, key=lambda agent: agent.fitness).brain

def _crossover(parent_a: NeuralNetworkModel, parent_b: NeuralNetworkModel) -> NeuralNetworkModel:
    hidden_weight_1 = (parent_a.hidden_weight_1 + parent_b.hidden_weight_1) / 2
    hidden_bias_1 = (parent_a.hidden_bias_1 + parent_b.hidden_bias_1) / 2

    output_weight = (parent_a.output_weight + parent_b.output_weight) / 2
    output_bias = (parent_a.output_bias + parent_b.output_bias) / 2
    
    child = NeuralNetworkModel(hidden_weight_1, hidden_bias_1, output_weight, output_bias)
    
    return child