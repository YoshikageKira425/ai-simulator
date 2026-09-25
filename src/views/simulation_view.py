import arcade
from ..core.map_manager import MapManager
from ..ai.simulation_environment import SimulationEnvironment
from ..ai.checkpoint import Checkpoint
from ..ai.breed import breed
from ..constant import KILL_TIMER


class SimulationView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager(5)
        self.sprite_list.append(self.map_manager.get_map())

        self.simulation_enviroment = SimulationEnvironment(self.map_manager, Checkpoint.load_generation())
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())

        self.wait = 2
        self.kill_timer = KILL_TIMER

    def new_generation_spawn(self):
        Checkpoint.save_generation(self.simulation_enviroment.get_all_models())
        
        for sprite in self.simulation_enviroment.get_sprites():
            self.sprite_list.remove(sprite)

        new_generation = breed(self.simulation_enviroment.highest_fitness)

        self.simulation_enviroment.spawn(20, new_generation)
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())

    def on_update(self, delta_time):
        if self.wait > 0:
            self.wait -= delta_time
            return

        if self.simulation_enviroment.all_dead:
            self.new_generation_spawn() 
            self.kill_timer = KILL_TIMER

        if self.kill_timer <= 0:
            self.new_generation_spawn()
            self.kill_timer = KILL_TIMER
        else:
            self.kill_timer -= delta_time

        self.simulation_enviroment.update(delta_time)

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()
