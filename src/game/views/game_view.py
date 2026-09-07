import arcade
from game.entity.car import Car
from game.controller.car_controller import CarController


class GameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.car = Car()
        self.sprite_list.append(self.car)

        self.car_controller = CarController(self.car)
        self.keys_held = []

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.keys_held.append("forward")
        if symbol == arcade.key.S:
            self.keys_held.append("reverse")
        if symbol == arcade.key.A:
            self.keys_held.append("left")
        if symbol == arcade.key.D:
            self.keys_held.append("right")

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.keys_held.remove("forward")
        if symbol == arcade.key.S:
            self.keys_held.remove("reverse")
        if symbol == arcade.key.A:
            self.keys_held.remove("left")
        if symbol == arcade.key.D:
            self.keys_held.remove("right")

    def on_update(self, delta_time):
        self.car_controller.update(delta_time, self.keys_held)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
