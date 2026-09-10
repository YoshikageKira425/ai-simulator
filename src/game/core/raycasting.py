import arcade
from game.entity.car import Car
from game.core.map_manager import MapManager
import math
from typing import List

class Raycasting:
    def __init__(
        self,
        car: Car,
        map: MapManager,
        ray_angles: List[float] = None,
        max_distance: float = 100.0,
        step_size: float = 0.6,
    ):
        self._car = car
        self._map = map

        self._ray_angles = (
            ray_angles if ray_angles is not None else [-60, -30, 0, 30, 60]
        )
        self._max_distance = max_distance
        self._step_size = step_size
        
    def cast_rays(self) -> List[float]:
        origin_x = self._car.center_x
        origin_y = self._car.center_y

        sensor_inputs: List[float] = []

        for rel_angle in self._ray_angles:
            total_angle = -self._car.angle + rel_angle
            ray_rad = math.radians(total_angle)

            dx = -math.sin(ray_rad)
            dy = math.cos(ray_rad)

            distance = 0.0

            while distance < self._max_distance:
                distance += self._step_size

                sample_x = origin_x + (dx * distance)
                sample_y = origin_y + (dy * distance)

                if self._map.is_on_track(sample_x, sample_y):
                    break

            actual_distance = min(distance, self._max_distance)
            normalized_dist = actual_distance / self._max_distance

            danger_score = 1.0 - normalized_dist
            sensor_inputs.append(danger_score)

        return sensor_inputs

    def debug_cast_rays(self):
        origin_x = self._car.center_x 
        origin_y = self._car.center_y

        for rel_angle in self._ray_angles:
            total_angle = -self._car.angle + rel_angle
            ray_rad = math.radians(total_angle)

            dx = -math.sin(ray_rad)
            dy = math.cos(ray_rad)

            distance = 0.0

            while distance < self._max_distance:
                distance += self._step_size
                
                sample_x = origin_x + (dx * distance)
                sample_y = origin_y + (dy * distance)

                if self._map.is_on_track(sample_x, sample_y):
                    break

            actual_distance = min(distance, self._max_distance)
            
            end_x = origin_x + (dx * actual_distance)
            end_y = origin_y + (dy * actual_distance)
            
            arcade.draw_line(origin_x, origin_y, end_x, end_y, arcade.color.WHITE, 3)