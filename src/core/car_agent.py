from typing import List, Tuple, Optional
from ..entity.car import Car
from .car_controller import CarController
from .raycasting import Raycasting
from .map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel
from ..ai.neural_network import NeuralNetwork


class CarAgent:
    def __init__(
        self,
        spawn_x: float,
        spawn_y: float,
        map: MapManager,
        model: Optional[NeuralNetworkModel] = None,
    ):
        self.car_enity = Car(spawn_x, spawn_y)
        self._car_controller = CarController(self.car_enity)
        self._raycast = Raycasting(self.car_enity, map)
        self._map_manager = map

        self.model = model
        self.brain = NeuralNetwork(model) if model else None

        self.is_alive = True
        self.fitness = 0.0
        self.sensor_inputs: List[float] = []

    def update(
        self, delta_time: float, manual_actions: Optional[Tuple[float, float]] = None
    ):
        if not self.is_alive:
            return

        self.sensor_inputs = self._raycast.cast_rays()

        if manual_actions is not None:
            throttle, steering = manual_actions
        elif self.brain is not None:
            steering, throttle = self.brain.foward_pass(self.sensor_inputs)[0]
        else:
            throttle, steering = 0.0, 0.0

        self._car_controller.apply_action(throttle, steering, delta_time)

        if not self._map_manager.is_on_track(
            self.car_enity.center_x, self.car_enity.center_y
        ):
            self.is_alive = False

        if self.is_alive:
            self.fitness += self._car_controller.current_speed * delta_time

    def debug(self):
        self._raycast.debug_cast_rays()