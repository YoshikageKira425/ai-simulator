import arcade
from PIL import Image
from ..constant import MAP_IMAGE_PATH


class MapManager:
    def __init__(self):
        self._map = arcade.Sprite(MAP_IMAGE_PATH, center_x=400, center_y=300)

        self._pil_image = Image.open(MAP_IMAGE_PATH).convert("RGB")
        self.width, self.height = self._pil_image.size

    def get_map(self) -> arcade.Sprite:
        return self._map

    def is_on_track(self, x: float, y: float) -> bool:
        new_y = self.height - y
        
        if 0 <= x < self.width and 0 <= new_y < self.height:
            r, g, b = self._pil_image.getpixel((x, new_y))
            return not (r > 0 and g > 0 and b > 0)

        return False
