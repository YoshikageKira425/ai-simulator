import arcade


class Car(arcade.Sprite):
    def __init__(self, spawn_x: float, spawn_y):
        super().__init__(path_or_texture="src/assets/sprites/placeholder_car_sprite.png",
                         center_x=spawn_x, center_y=spawn_y)
