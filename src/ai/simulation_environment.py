import arcade
from ..core.car_agent import CarAgent
from ..core.map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel


class SimulationEnvironment:
    def __init__(self, map_manager: MapManager, new_generation: list[NeuralNetworkModel] = None, population: int = 20):
        self.map_manager = map_manager
        self.population = population

        self.spawn(new_generation)

    def spawn(self, new_generation: list[NeuralNetworkModel] | None = None):
        self.agents = [
            CarAgent(self.map_manager, NeuralNetworkModel.random()
                     if not new_generation else new_generation[i])
            for i in range(self.population)
        ]

    def get_sprites(self) -> list[arcade.Sprite]:
        return [car.car_enity for car in self.agents]

    def update(self, delta_time: float):
        if self.all_dead:
            return

        for car in self.agents:
            car.update(delta_time)

    def kill_every_agents(self):
        for agent in self.agents:
            agent.is_alive = False

    def get_all_models(self) -> list[NeuralNetworkModel]:
        return [car.brain.model for car in self.highest_fitness]

    @property
    def highest_fitness(self) -> list[CarAgent]:
        return sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)

    @property
    def active_agents_count(self) -> int:
        return sum(1 for agent in self.agents if agent.is_alive)

    @property
    def all_dead(self) -> bool:
        return self.active_agents_count == 0
