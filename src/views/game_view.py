import arcade
from ..core.car_agent import CarAgent
from ..core.map_manager import MapManager


class GameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        self.car = CarAgent(70, 200, self.map_manager)
        self.sprite_list.append(self.car.car_enity)

        self.throttle = 0
        self.steering = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.throttle = 1
        elif symbol == arcade.key.S:
            self.throttle = -1

        if symbol == arcade.key.A:
            self.steering = -1
        elif symbol == arcade.key.D:
            self.steering = 1

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.throttle = 0

        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.steering = 0

    def on_update(self, delta_time):
        self.car.update(delta_time, [self.throttle, self.steering])

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()
        # self.car.debug()
