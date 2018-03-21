from bases.gameobject import *

class Scene:
    def __init__(self):
        pass

    def init_objects(self):
        pass

    def deinit_objects(self):
        clear_all_game_objects()


class SceneManager:
    current_scene = None
    next_scene = None

    @classmethod
    def change_scene(cls, next_scene):
        cls.next_scene = next_scene

    @classmethod
    def change_scence_if_needed(cls):
        if cls.next_scene is None:
            return

        clear_all_game_objects()

        cls.current_scene = cls.next_scene
        cls.next_scene = None

        cls.current_scene.init_objects()
