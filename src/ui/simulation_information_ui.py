import arcade
import arcade.gui


class SimulationInformationUi:
    def __init__(self):
        self._manager = arcade.gui.UIManager()

        self._generation_counter = arcade.gui.UILabel(
            "Generation: 99",
            x=15,
            y=550,
            font_size=18
        )
        self._manager.add(self._generation_counter)

        self._alive_counter = arcade.gui.UILabel(
            "Alive: 20 / 20",
            x=15,
            y=525,
            font_size=18
        )
        self._manager.add(self._alive_counter)

        self._time_remaining = arcade.gui.UILabel(
            "Time Remaining: 14.2s",
            x=15,
            y=500,
            font_size=18
        )
        self._manager.add(self._time_remaining)

        self._speed_lable = arcade.gui.UILabel(
            "Speed: 1x",
            x=15,
            y=25,
            font_size=18
        )
        self._manager.add(self._speed_lable)

    def set_alive_counter(self, alive_counter: int, max_alive_counter: int):
        self._alive_counter.text = f"Alive: {alive_counter} / {max_alive_counter}"

    def set_time_remaining(self, timer: float):
        self._time_remaining.text = f"Time Remaining: {round(timer, 2)}s"

    def set_game_speed(self, speed: int):
        self._speed_lable.text = f"Speed: {speed}x"

    def draw(self):
        self._manager.draw()
