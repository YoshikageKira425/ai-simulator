import arcade
from ..core.car_agent import CarAgent
from ..core.map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel

class AiGameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        self.car = CarAgent(70, 200, self.map_manager, NeuralNetworkModel.random())
        self.sprite_list.append(self.car.car_enity)
        
        self.wait = 2

    def on_update(self, delta_time):
        if self.wait > 0:
            self.wait -= delta_time
            return
        
        self.car.update(delta_time)

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()