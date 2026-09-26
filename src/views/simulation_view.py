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

        self.ui = SimulationInformationUi()

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager(1)
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

        self.simulation_enviroment.spawn(new_generation)
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())

    def on_update(self, delta_time):
        self.ui.set_time_remaining(self.kill_timer)
        self.ui.set_alive_counter(self.simulation_enviroment.active_agents_count, self.simulation_enviroment.population)
        
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
        
        # for agent in self.simulation_enviroment.agents:
                #agent.debug()
        
        self.ui.draw()
