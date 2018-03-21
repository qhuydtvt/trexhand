from bases.scenes import *
from bases.counter import *
from inputs import input
from bases.gameobject import *
from trex.trex import *
from cactus.cactus import *
from trex_scores.trex_score import Score
from game_restarter import GameRestarter

def restart_play_scene():
    SceneManager.change_scene(PlayScene())

class PlayScene(Scene):

    def init_objects(self):
        self.init_cactus()
        self.init_trex()
        self.init_score()

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


    def init_score(self):
        score = Score()
        add_game_object(score)
