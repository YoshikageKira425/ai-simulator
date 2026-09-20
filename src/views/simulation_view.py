import arcade
from ..core.map_manager import MapManager
from ..ai.simulation_environment import SimulationEnvironment

class SimulationView(arcade.View):
    def __init__(self):
        super().__init__(background_color=arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList(True)

        self.map_manager = MapManager()
        self.sprite_list.append(self.map_manager.get_map())

        self.simulation_enviroment = SimulationEnvironment(self.map_manager)
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())
        
        self.wait = 2

    def spawn(self):
        for sprite in self.simulation_enviroment.get_sprites():
            self.sprite_list.remove(sprite)
            
        self.simulation_enviroment.spawn()
        self.sprite_list.extend(self.simulation_enviroment.get_sprites())

    def on_update(self, delta_time):
        if self.wait > 0:
            self.wait -= delta_time
            return
        
        self.simulation_enviroment.update(delta_time)

    def on_draw(self):
        self.clear()

        self.sprite_list.draw()