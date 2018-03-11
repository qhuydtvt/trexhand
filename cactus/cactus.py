from bases.gameobject import *
from bases.boxcollider import *
from bases.vector2d import *
from bases.renderer import *
from bases.counter import *

from settings import *
from inputs import input

class Cactus(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.velocity = ZERO()
        self.renderer = ImageRenderer('images/cactus/cactus.png')
        self.speed = 5
        self.setup_physics()

    def setup_physics(self):
        self.box_collider = BoxCollider(12, 36)
        self.children.append(self.box_collider)

    def run(self, parent):
        GameObject.run(self, parent)
        self.position.x -= self.speed
        if self.position.x < 0:
            self.active = False

class CactusSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.counter = Counter(200)
        self.enabled = False

    def start(self):
        self.enabled = True

    def spawn(self):
        cactus = recycle(Cactus)
        cactus.position = Vector2D(SCREEN_WIDTH, BASE_Y + 4)

    def run(self, parent):
        GameObject.run(self, parent)

        if self.enabled:
            if self.counter.run():
                self.spawn()
                self.counter.reset()
        elif input.jump_pressed or input.duck_pressed:
            self.spawn()
            self.enabled = True
