from bases.renderer import *
from trex.state import TRexState

class TRexAnimator:
    def __init__(self):
        self.idle_anim = ImageRenderer("images/t-rex/idle.png")
        self.run_anim = Animation("images/t-rex/run1.png", "images/t-rex/run2.png")
        self.duck_anim = Animation("images/t-rex/duck1.png", "images/t-rex/duck2.png")
        self.anim = self.idle_anim

    def render(self, qp, position):
        self.anim.render(qp, position)

    def update(self, trex):
        if trex.state == TRexState.IDLE:
            self.anim = self.idle_anim
        elif trex.state == TRexState.RUNNING:
            self.anim = self.run_anim
        elif trex.state == TRexState.DUCKING:
            self.anim = self.duck_anim
