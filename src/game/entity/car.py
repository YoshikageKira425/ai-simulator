import arcade

class Car(arcade.Sprite):
    def __init__(self):
        super().__init__(path_or_texture="src/game/assets/sprites/placeholder_car_sprite.png", center_x=100, center_y=200)