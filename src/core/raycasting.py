import arcade
from ..entity.car import Car
from .map_manager import MapManager
import math
from typing import List
from ..constant import RAY_ANGLES, RAY_MAX_DISTANCE, RAY_STEP_SIZE

class Raycasting:
    def __init__(
        self,
        car: Car,
        map: MapManager
    ):
        self._car = car
        self._map = map
        
    def cast_rays(self) -> List[float]:
        origin_x = self._car.center_x
        origin_y = self._car.center_y

        sensor_inputs: List[float] = []

        for rel_angle in RAY_ANGLES:
            total_angle = -self._car.angle + rel_angle
            ray_rad = math.radians(total_angle)

            dx = -math.sin(ray_rad)
            dy = math.cos(ray_rad)

            distance = 0.0

            while distance < RAY_MAX_DISTANCE:
                distance += RAY_STEP_SIZE

                sample_x = origin_x + (dx * distance)
                sample_y = origin_y + (dy * distance)

                if not self._map.is_on_track(sample_x, sample_y):
                    break

            actual_distance = min(distance, RAY_MAX_DISTANCE)
            normalized_dist = actual_distance / RAY_MAX_DISTANCE

            danger_score = 1.0 - normalized_dist
            sensor_inputs.append(danger_score)

        return sensor_inputs

    def debug_cast_rays(self):
        origin_x = self._car.center_x 
        origin_y = self._car.center_y

        for rel_angle in RAY_ANGLES:
            total_angle = -self._car.angle + rel_angle
            ray_rad = math.radians(total_angle)

            dx = -math.sin(ray_rad)
            dy = math.cos(ray_rad)

            distance = 0.0

            while distance < RAY_MAX_DISTANCE:
                distance += RAY_STEP_SIZE
                
                sample_x = origin_x + (dx * distance)
                sample_y = origin_y + (dy * distance)

                if not self._map.is_on_track(sample_x, sample_y):
                    break

            actual_distance = min(distance, RAY_MAX_DISTANCE)
            
            end_x = origin_x + (dx * actual_distance)
            end_y = origin_y + (dy * actual_distance)
            
            arcade.draw_line(origin_x, origin_y, end_x, end_y, arcade.color.WHITE, 3)