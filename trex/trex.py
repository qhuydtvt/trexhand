from bases.gameobject import *
from bases.renderer import *
from trex.state import TRexState
from trex.animator import TRexAnimator

class TRex(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.renderer = TRexAnimator()
        self.state = TRexState.IDLE

    def run(self):
        GameObject.run(self)
        self.renderer.update(self)

trex = TRex()
