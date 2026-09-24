import arcade
from ..core.car_agent import CarAgent
from ..core.map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel
from ..ai.checkpoint import Checkpoint


class AiGameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        brain = Checkpoint.load() if Checkpoint.load() else NeuralNetworkModel.random() 

        spawn_x, spawn_y = self.map_manager.car_spawn_point()

        self.car = CarAgent(spawn_x, spawn_y, self.map_manager, brain)
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
