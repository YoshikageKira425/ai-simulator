import arcade
from PIL import Image
from ..constant import MAPS


class MapManager:
    def __init__(self, map_index: int = 0):
        self._map_data = MAPS[map_index]
        
        self._map_sprite = arcade.Sprite(self._map_data["path"], center_x=400, center_y=300)

        self._pil_image = Image.open(self._map_data["path"]).convert("RGB")
        self.width, self.height = self._pil_image.size

    def car_spawn_point(self) -> tuple:
        return self._map_data["spawn_point"]

    def get_map(self) -> arcade.Sprite:
        return self._map_sprite

    def is_on_track(self, x: float, y: float) -> bool:
        new_y = self.height - y

        if 0 <= x < self.width and 0 <= new_y < self.height:
            r, g, b = self._pil_image.getpixel((x, new_y))
            return not (r > 0 and g > 0 and b > 0)

        return False
