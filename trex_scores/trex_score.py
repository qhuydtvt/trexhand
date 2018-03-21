from bases.gameobject import GameObject
from bases.counter import Counter
from bases.renderer import TextRenderer

class Score(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.score = 0
        self.counter = Counter(109)
        self.renderer = TextRenderer()
        self.renderer.text = "Score: 0"

    def run(self, parent):
        GameObject.run(self, parent)
        if self.counter.run():
            self.counter.reset()
            self.score += 10
            self.renderer.text = "Score: {0}".format(self.score)
