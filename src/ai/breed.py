import random
from ..core.car_agent import CarAgent
from ..model.neural_network_model import NeuralNetworkModel

ELITISM = 2

def breed(agents: list[CarAgent], popullation:int = 20) -> list[NeuralNetworkModel]:
    results = []
    
    for i in range(ELITISM):
        results.append(agents[i].brain)
    
    for i in range(popullation - ELITISM):
        parent_a = _tournament_selection(agents)
        parent_b = _tournament_selection(agents)
        
        results.append(_crossover(parent_a, parent_b))
        
    return results
        
def _tournament_selection(agents: list[CarAgent]) -> CarAgent:
    k_agents = random.choices(agents, k=3)
    
    return max(k_agents, key=lambda agent: agent.fitness)

def _crossover(parent_a: CarAgent, parent_b: CarAgent) -> NeuralNetworkModel:
    pass