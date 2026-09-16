from typing import List, Tuple
from game.entity.car import Car
from game.core.car_controller import CarController
from game.core.raycasting import Raycasting
from game.core.map_manager import MapManager


class CarAgent:
    def __init__(self, spawn_x: float, spawn_y: float, map: MapManager):
        self.car_enity = Car(spawn_x, spawn_y)
        self._car_controller = CarController(self.car_enity)
        self._raycast = Raycasting(self.car_enity, map)
        self._map_manager = map

        self.is_alive = True
        self.fitness = 0.0
        self.sensor_inputs = []

    def update(self, delta_time: float, actions: tuple[float, float]):
        if not self.is_alive:
            return

        if actions:
            throttle, steering = actions

            self._car_controller.apply_action(throttle, steering, delta_time)

        self.sensor_inputs = self._raycast.cast_rays()

        if not self._map_manager.is_on_track(self.car_enity.center_x, self.car_enity.center_y):
            self.is_alive = False

    def debug(self):
        self._raycast.debug_cast_rays()