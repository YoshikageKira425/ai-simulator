import arcade
from .car_agent import CarAgent
from .map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel


class GameManager:
    def __int__(self, map_manager: MapManager, population: int = 20):
        self.agents = [CarAgent(
            70, 200, map_manager, NeuralNetworkModel.random()) for i in range(population)]
        
    def get_sprites(self) -> list[arcade.Sprite]:
        return [car.car_enity for car in self.agents]
    
    def update(self, delta_time: float):
        for car in self.agents:
            car.update(delta_time)
            
    @property
    def active_agents_count(self) -> int:
        return sum(1 for agent in self.agents if agent.is_alive)

    @property
    def all_dead(self) -> bool:
        return self.active_agents_count == 0
            
