from bases.gameobject import *
from bases.renderer import *
from trex.state import TRexState
from trex.animator import TRexAnimator
from inputs import input

class TRex(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.renderer = TRexAnimator()
        self.state = TRexState.IDLE

    def run(self):
        GameObject.run(self)
        self.renderer.update(self)
        print(input.jump_pressed, input.duck_pressed)

    def set_initial_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self.base_y = y

trex = TRex()
