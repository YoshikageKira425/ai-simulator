import arcade
from game.entity.car import Car

class GameView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)
        
        self.sprite_list = arcade.SpriteList(True)
        
        self.car = Car()
        self.sprite_list.append(self.car)
        
    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        