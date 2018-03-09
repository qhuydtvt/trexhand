from trex.state import TRexState
from bases.boxcollider import BoxCollider

class TRexPhysics:
    def __init__(self, trex):
        trex.box_collider = BoxCollider(40, 40)
        trex.children.append(trex.box_collider)

    def update(self, trex):
        state = trex.state
        box_collider = trex.box_collider

        if state == TRexState.DUCKING:
            box_collider.position.x = 16
            box_collider.position.y = 4
            box_collider.height = 20
        else:
            box_collider.position.x = 0
            box_collider.position.y = 0
            box_collider.height = 40
