import arcade
from ..core.map_manager import MapManager
from ..ai.simulation_environment import SimulationEnvironment
from ..ai.checkpoint import Checkpoint
from ..ai.breed import breed
from ..ui.simulation_information_ui import SimulationInformationUi
from ..constant import KILL_TIMER


class SimulationView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        arcade.enable_timings()

        self.ui = SimulationInformationUi()

        self.sprite_list = arcade.SpriteList(True)

        self.map_index = 0
        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        self.simulation_enviroment = SimulationEnvironment(
            self.map_manager, Checkpoint.load_generation()
        )
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())

        self.generation_count = 1

        self.debug_mode = False
        self.game_speed = 1

        self.wait = 2
        self.kill_timer = KILL_TIMER

        self.pause = False

    def new_generation_spawn(self):
        for sprite in self.simulation_enviroment.get_sprites():
            self.sprite_list.remove(sprite)

        new_generation = breed(self.simulation_enviroment.highest_fitness)

        self.simulation_enviroment.spawn(new_generation)
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())
        
        self.generation_count += 1

    def on_update(self, delta_time):
        if self.pause:
            return

        for _ in range(self.game_speed):
            self.step(delta_time)

    def step(self, delta_time: float):
        self.update_ui()

        if self.wait > 0:
            self.wait -= delta_time
            return

        if self.simulation_enviroment.all_dead:
            self.kill_generation()

        if self.kill_timer <= 0:
            self.kill_generation()
        else:
            self.kill_timer -= delta_time

        self.simulation_enviroment.update(delta_time)

    def update_ui(self):
        self.ui.set_fps()
        self.ui.set_generation(self.generation_count)
        self.ui.set_time_remaining(self.kill_timer)
        self.ui.set_alive_counter(
            self.simulation_enviroment.active_agents_count,
            self.simulation_enviroment.population,
        )
        self.ui.set_the_highest_fitness(
            self.simulation_enviroment.highest_fitness[0].fitness
        )

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.debug_mode = not self.debug_mode

        if symbol == arcade.key.KEY_1:
            self.update_game_speed(1)

        if symbol == arcade.key.KEY_2:
            self.update_game_speed(2)

        if symbol == arcade.key.KEY_3:
            self.update_game_speed(3)

        if symbol == arcade.key.S:
            self.save()

        if symbol == arcade.key.R:
            self.kill_generation()

        if symbol == arcade.key.SPACE:
            self.pause = not self.pause

        if symbol == arcade.key.M:
            self.map_index = (self.map_index + 1) % self.map_manager.map_limit()
            
            self.change_map(self.map_index)

    def update_game_speed(self, speed: int):
        self.game_speed = speed
        self.ui.set_game_speed(self.game_speed)

    def save(self):
        generation = self.simulation_enviroment.get_all_models()
        best_one = generation[0]

        Checkpoint.save_generation(generation)
        Checkpoint.save(best_one)

    def kill_generation(self):
        self.new_generation_spawn()
        self.kill_timer = KILL_TIMER

    def change_map(self, index: int):
        self.sprite_list.remove(self.map_manager.get_map())
        self.map_manager.change_map(index)
        self.sprite_list.append(self.map_manager.get_map())

        self.kill_generation()

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()

        if self.debug_mode:
            for agent in self.simulation_enviroment.agents:
                agent.debug()

        self.ui.draw()
