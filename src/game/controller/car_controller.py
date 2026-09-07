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
        
    def forward(self, delta_time: float):
        self.current_speed += delta_time * self.acceleration
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
    
    def reverse(self, delta_time: float):
        self.current_speed += delta_time * self.acceleration
        if self.current_speed <= self.max_reverse_speed:
            self.current_speed = self.max_reverse_speed
    
    def turn_left(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle += self.turn_speed * delta_time * direction

    def turn_right(self, delta_time: float):
        if self.current_speed != 0:
            direction = 1.0 if self.current_speed > 0 else -1.0
            self.car.angle -= self.turn_speed * delta_time * direction
    
    def update(self, delta_time: float):
        self.current_speed *= self.friction
        
        if abs(self.current_speed) < 0.1:
            self.current_speed = 0.0

        rad = math.radians(self.car.angle)
        change_x = -self.current_speed * math.sin(rad) * delta_time
        change_y = self.current_speed * math.cos(rad) * delta_time

        self.car.center_x += change_x
        self.car.center_y += change_y