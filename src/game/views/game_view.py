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
        
    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        