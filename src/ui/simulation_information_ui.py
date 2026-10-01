import arcade
import arcade.gui


class SimulationInformationUi:
    def __init__(self):
        self._manager = arcade.gui.UIManager()

        self._fps = arcade.gui.UILabel("FPS: 99", x=15, y=550, font_size=18)
        self._manager.add(self._fps)

        self._generation = arcade.gui.UILabel(
            "Generation: 100", x=15, y=525, font_size=18
        )
        self._manager.add(self._generation)

        self._alive_counter = arcade.gui.UILabel(
            "Alive: 20 / 20", x=15, y=500, font_size=18
        )
        self._manager.add(self._alive_counter)

        self._highest_fitness = arcade.gui.UILabel(
            "Gen Best Fitness: 1000", x=15, y=475, font_size=18
        )
        self._manager.add(self._highest_fitness)

        self._time_remaining = arcade.gui.UILabel(
            "Time Remaining: 14.2s", x=15, y=450, font_size=18
        )
        self._manager.add(self._time_remaining)

        self._speed_lable = arcade.gui.UILabel("Speed: 1x", x=15, y=25, font_size=18)
        self._manager.add(self._speed_lable)

    def set_fps(self):
        fps = round(arcade.get_fps())
        self._fps.text = f"FPS: {fps}"

    def set_generation(self, count: int):
        self._generation.text = f"Generation: {count}"

    def set_alive_counter(self, alive_counter: int, max_alive_counter: int):
        self._alive_counter.text = f"Alive: {alive_counter} / {max_alive_counter}"

    def set_the_highest_fitness(self, fitness: float):
        self._highest_fitness.text = f"Gen Best Fitness: {round(fitness, 1)}"

    def set_time_remaining(self, timer: float):
        self._time_remaining.text = f"Time Remaining: {round(timer, 1)}s"

    def set_game_speed(self, speed: int):
        self._speed_lable.text = f"Speed: {speed}x"

    def draw(self):
        self._manager.draw()
