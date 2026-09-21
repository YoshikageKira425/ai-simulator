import random
from ..core.car_agent import CarAgent
from ..model.neural_network_model import NeuralNetworkModel

ELITISM = 0.5

def breed(agents: list[CarAgent], popullation:int = 20) -> list[NeuralNetworkModel]:
    top_1_agent = agents[0]
    top_2_agent = agents[1]
    
    for i in range(popullation - 2):
        parent_a = _tournament_selection(agents)
        parent_b = _tournament_selection(agents)
        
        
def _tournament_selection(agents: list[CarAgent]) -> CarAgent:
    k_agents = random.choices(agents, k=3)
    
    return max(k_agents, key=lambda agent: agent.fitness)

def _breed(parent_a: CarAgent, parent_b: CarAgent) -> NeuralNetworkModel:
    pass