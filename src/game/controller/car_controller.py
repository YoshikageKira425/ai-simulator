import math
from game.entity.car import Car


class CarController:
    def __init__(self, car: Car):
        self.car = car

        self.current_speed: float = 0.0
        self.max_speed: float = 400.0
        self.max_reverse_speed: float = -150.0
        self.acceleration: float = 300.0
        self.friction: float = 0.98
        self.turn_speed: float = 120.0

    def apply_action(self, throttle: float, steering: float, delta_time: float):
        if throttle == 1:
            self._forward(delta_time)
        elif throttle == -1:
            self._reverse(delta_time)

        if steering == 1:
            self._turn_right(delta_time)
        elif steering == -1:
            self._turn_left(delta_time)

        self._update_car(delta_time)

    def _forward(self, delta_time: float):
        self.current_speed += delta_time * self.acceleration
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed

    def _reverse(self, delta_time: float):
        self.current_speed -= delta_time * self.acceleration
        if self.current_speed <= self.max_reverse_speed:
            self.current_speed = self.max_reverse_speed

    def _turn_left(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle -= self.turn_speed * delta_time * direction

    def _turn_right(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle += self.turn_speed * delta_time * direction

    def _update_car(self, delta_time):
        self.current_speed *= self.friction

        if abs(self.current_speed) < 0.1:
            self.current_speed = 0.0

        rad = math.radians(self.car.angle)
        change_x = self.current_speed * math.sin(rad) * delta_time
        change_y = self.current_speed * math.cos(rad) * delta_time

        self.car.center_x += change_x
        self.car.center_y += change_y

#  Rework how the actions are handle, make one function that handles it
