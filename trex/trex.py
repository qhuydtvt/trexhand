from bases.gameobject import *
from bases.renderer import *
from inputs import input
from bases.vector2d import Vector2D

from trex.state import TRexState
from trex.animator import TRexAnimator
from trex.physics import TRexPhysics

class TRex(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.velocity = Vector2D(0, 0)
        self.renderer = TRexAnimator()
        self.state = TRexState.IDLE
        self.jump_speed = 14
        self.gravity = 1
        self.base_y = 0
        self.setup_physics()

    def setup_physics(self):
        self.physics = TRexPhysics(self)

    def play_dead(self):
        self.state = TRexState.DEAD

    def run(self, parent):
        GameObject.run(self, parent)
        if self.state != TRexState.DEAD:
            self.move_vertical()
            self.physics.update(self)
        self.renderer.update(self)

    def move_vertical(self):
        if self.state == TRexState.IDLE or self.state == TRexState.RUNNING:
            if input.jump_pressed:
                self.velocity.y = -self.jump_speed
                self.state = TRexState.JUMPING
            elif input.duck_pressed:
                self.state = TRexState.DUCKING
        if self.state == TRexState.DUCKING:
            if input.jump_pressed:
                self.velocity.y = -self.jump_speed
                self.state = TRexState.JUMPING
            elif not input.duck_pressed:
                self.state = TRexState.RUNNING

        self.velocity.y += self.gravity

        if self.state == TRexState.JUMPING:
            if self.position.y + self.velocity.y >= self.base_y:
                self.position.y = self.base_y
                self.velocity.y = 0
                self.state = TRexState.RUNNING
            else:
                self.position.y += self.velocity.y


    def set_initial_position(self, x, y):
        self.position = Vector2D(x, y)
        self.base_y = y

trex = TRex()

def instance():
    return trex
