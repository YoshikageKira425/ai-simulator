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
        self.car_controller.apply_action(self.throttle, self.steering, delta_time)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
