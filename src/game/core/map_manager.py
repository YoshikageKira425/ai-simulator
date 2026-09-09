import arcade
from PIL import Image


class MapManager:
    def __init__(self):
        self._map = arcade.Sprite("src/game/assets/maps/map01.png", center_x=400, center_y=300)

        self._pil_image = Image.open(
            "src/game/assets/maps/map01.png").convert("RGB")
        self.width, self.height = self._pil_image.size

    def get_map(self) -> arcade.Sprite:
        return self._map

    def is_on_track(self, x: float, y: float) -> bool:
        new_y = self.height - y
        
        if 0 <= x < self.width and 0 <= new_y < self.height:
            r, g, b = self._pil_image.getpixel((x, new_y))
            return r > 0 and g > 0 and b > 0

        return False
