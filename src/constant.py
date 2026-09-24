SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CAR"

CAR_MAX_SPEED = 400.0
CAR_MAX_REVERSE_SPEED: float = -150.0
CAR_ACCELERATION = 300.0
CAR_FRICTION = 0.98
CAR_TURN_SPEED = 120.0

RAY_ANGLES = [-60.0, -30.0, 0.0, 30.0, 60.0]
RAY_MAX_DISTANCE = 250.0
RAY_STEP_SIZE = 3.0

ELITISM = 2
MUTATION_CHANCE = 0.3
MUTATION_STRENGTH = 0.05

MAPS = [
    {
        "path": "src/assets/maps/map01.png",
        "spawn_point": (70, 200),
    },
    {
        "path": "src/assets/maps/map02.png",
        "spawn_point": (240, 120),
    },
    {
        "path": "src/assets/maps/map03.png",
        "spawn_point": (200, 140),
    },
    {
        "path": "src/assets/maps/map04.png",
        "spawn_point": (200, 140),
    },
    {
        "path": "src/assets/maps/map05.png",
        "spawn_point": (250, 480),
    },
    {
        "path": "src/assets/maps/map06.png",
        "spawn_point": (200, 140),
    },
    {
        "path": "src/assets/maps/map07.png",
        "spawn_point": (250, 150),
    },
    {
        "path": "src/assets/maps/map08.png",
        "spawn_point": (200, 130),
    },
    {
        "path": "src/assets/maps/map09.png",
        "spawn_point": (200, 220),
    },
]
CAR_IMAGE_PATH = "src/assets/sprites/placeholder_car_sprite.png"
