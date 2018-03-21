from bases.scenes import *
from bases.counter import *
from inputs import input
from bases.gameobject import *
from trex.trex import *
from cactus.cactus import *
from game_restarter import GameRestarter

def restart_play_scene():
    SceneManager.change_scene(PlayScene())

class PlayScene(Scene):

    def init_objects(self):
        self.init_cactus()
        self.init_trex()

    def init_cactus(self):
        cactus_spawner = CactusSpawner()
        add_game_object(cactus_spawner)

    def init_trex(self):
        trex = TRex()
        trex.set_initial_position(60, BASE_Y)
        game_restarter = GameRestarter()
        game_restarter.restart = restart_play_scene
        trex.game_restarter = game_restarter
        add_game_object(trex)
        add_game_object(game_restarter)
