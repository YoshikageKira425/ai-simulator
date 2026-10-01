import arcade
from ..core.car_agent import CarAgent
from ..core.map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel
from ..ai.checkpoint import Checkpoint


class AiGameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_index = 0
        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        self.brain = (
            Checkpoint.load() if Checkpoint.load() else NeuralNetworkModel.random()
        )

        self.car = CarAgent(self.map_manager, self.brain)
        self.sprite_list.append(self.car.car_enity)

        self.wait = 2

        self.pause = False
        self.debug_mode = False
        self.game_speed = 1

    def on_update(self, delta_time):
        if self.pause:
            return

        for _ in range(self.game_speed):
            self.step(delta_time)

    def step(self, delta_time: float):
        if self.wait > 0:
            self.wait -= delta_time
            return

        self.car.update(delta_time)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.debug_mode = not self.debug_mode

        if symbol == arcade.key.KEY_1:
            self.game_speed = 1

        if symbol == arcade.key.KEY_2:
            self.game_speed = 2

        if symbol == arcade.key.KEY_3:
            self.game_speed = 3

        if symbol == arcade.key.R:
            self.reset()

        if symbol == arcade.key.SPACE:
            self.pause = not self.pause

        if symbol == arcade.key.M:
            self.map_index = (self.map_index + 1) % self.map_manager.map_limit()

            self.change_map(self.map_index)

    def change_map(self, index: int):
        self.sprite_list.remove(self.map_manager.get_map())
        self.map_manager.change_map(index)
        self.sprite_list.append(self.map_manager.get_map())

        self.reset()

    def reset(self):
        self.wait = 2

        self.sprite_list.remove(self.car.car_enity)
        self.car = CarAgent(self.map_manager, self.brain)
        self.sprite_list.append(self.car.car_enity)

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()

        if self.debug_mode:
            self.car.debug()
