from bases.gameobject import GameObject
from bases.counter import Counter
from bases.scenes import SceneManager
from inputs import input

class GameRestarter(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.enabled = False
        self.counter = Counter(20)

    def enable(self):
        self.enabled = True

    def restart(self):
        pass

    def run(self, parent):
        GameObject.run(self, parent)
        if self.enabled:
            if self.counter.run():
                if input.jump_pressed:
                    self.restart()
                    self.enabled = False
