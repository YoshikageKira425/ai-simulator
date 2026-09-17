import arcade
from src.constant import CAR_IMAGE_PATH


class Car(arcade.Sprite):
    def __init__(self, spawn_x: float, spawn_y):
        super().__init__(path_or_texture=CAR_IMAGE_PATH,
                         center_x=spawn_x, center_y=spawn_y)
