from enum import Enum

class TRexState(Enum):
    IDLE = 0
    RUNNING = 1
    JUMPING = 2
    DUCKING = 3
    DEAD = 4
