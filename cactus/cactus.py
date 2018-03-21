from bases.gameobject import *
from bases.boxcollider import *
from bases.vector2d import *
from bases.renderer import *
from bases.counter import *

from settings import *
from inputs import input

from trex.trex import TRex

class Cactus(GameObject):
    move_lock = False

    @classmethod
    def lock_move(cls):
        cls.move_lock = True

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
        if not Cactus.move_lock:
            self.position.x -= self.speed
            if self.position.x < 0:
                self.active = False

            self.run_physics()

    def run_physics(self):
        if self.box_collider.collide_with(TRex.instance.box_collider):
            TRex.instance.play_dead()
            Cactus.lock_move()


class CactusSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.counter = Counter(200)
        self.enabled = False
        Cactus.move_lock = False

    def start(self):
        self.enabled = True

    def spawn(self):
        cactus = recycle(Cactus)
        cactus.position = Vector2D(SCREEN_WIDTH, BASE_Y + 4)

    def run(self, parent):
        GameObject.run(self, parent)

        if self.enabled and not Cactus.move_lock:
            if self.counter.run():
                self.spawn()
                self.counter.reset()
        elif input.jump_pressed or input.duck_pressed:
            self.spawn()
            self.enabled = True
