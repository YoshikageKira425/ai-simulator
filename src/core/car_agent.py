import math
from typing import Optional
from ..entity.car import Car
from .car_controller import CarController
from .raycasting import Raycasting
from .map_manager import MapManager
from ..model.neural_network_model import NeuralNetworkModel
from ..ai.neural_network import NeuralNetwork


class CarAgent:
    def __init__(
        self,
        map: MapManager,
        model: Optional[NeuralNetworkModel] = None,
    ):
        spawn_x, spawn_y = map.car_spawn_point()

        self.car_enity = Car(spawn_x, spawn_y)
        self._car_controller = CarController(self.car_enity)
        self._raycast = Raycasting(self.car_enity, map)
        self._map_manager = map

        self.model = model
        self.brain = NeuralNetwork(model) if model else None

        self.is_alive = True
        self.sensor_inputs: list[float] = []
        
        self.prev_x = self.car_enity.center_x
        self.prev_y = self.car_enity.center_y
        self.distance_traveled = 0.0
        
        self.max_distance_reached = 0.0
        self.stagnation_timer = 0.0
        self.MAX_STAGNATION_TIME = 2.0
        self.MIN_PROGRESS_THRESHOLD = 35.0

    def update(
        self, delta_time: float, manual_actions: Optional[tuple[float, float]] = None
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
            return

        dx = self.car_enity.center_x - self.prev_x
        dy = self.car_enity.center_y - self.prev_y
        self.distance_traveled += math.hypot(dx, dy)

        if (
            self.distance_traveled - self.max_distance_reached
            > self.MIN_PROGRESS_THRESHOLD
        ):
            self.max_distance_reached = self.distance_traveled
            self.stagnation_timer = 0.0 
        else:
            self.stagnation_timer += delta_time
            if self.stagnation_timer >= self.MAX_STAGNATION_TIME:
                self.is_alive = False  
                return
            
        self.prev_x = self.car_enity.center_x
        self.prev_y = self.car_enity.center_y

    @property
    def fitness(self):
        return self.distance_traveled 

    def debug(self):
        if not self.is_alive:
            return
        
        self._raycast.debug_cast_rays()
