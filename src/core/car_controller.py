import math
from ..entity.car import Car
from ..constant import (
    CAR_ACCELERATION,
    CAR_FRICTION,
    CAR_MAX_SPEED,
    CAR_TURN_SPEED,
    CAR_MAX_REVERSE_SPEED,
)


class CarController:
    def __init__(self, car: Car):
        self.car = car

        self.current_speed: float = 0.0

    def apply_action(self, throttle: float, steering: float, delta_time: float):
        if throttle > 0:
            self._forward(delta_time)
        elif throttle < 0:
            self._reverse(delta_time)

        if steering > 0:
            self._turn_right(delta_time)
        elif steering < 0:
            self._turn_left(delta_time)

        self._update_car(delta_time)

    def _forward(self, delta_time: float):
        self.current_speed += delta_time * CAR_ACCELERATION
        if self.current_speed >= CAR_MAX_SPEED:
            self.current_speed = CAR_MAX_SPEED

    def _reverse(self, delta_time: float):
        self.current_speed -= delta_time * CAR_ACCELERATION
        if self.current_speed <= CAR_MAX_REVERSE_SPEED:
            self.current_speed = CAR_MAX_REVERSE_SPEED

    def _turn_left(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle -= CAR_TURN_SPEED * delta_time * direction

    def _turn_right(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle += CAR_TURN_SPEED * delta_time * direction

    def _update_car(self, delta_time):
        self.current_speed *= CAR_FRICTION

        if abs(self.current_speed) < 0.1:
            self.current_speed = 0.0

        rad = math.radians(self.car.angle)
        change_x = self.current_speed * math.sin(rad) * delta_time
        change_y = self.current_speed * math.cos(rad) * delta_time

        self.car.center_x += change_x
        self.car.center_y += change_y
