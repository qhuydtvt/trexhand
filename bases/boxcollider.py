from bases.vector2d import Vector2D
from bases.gameobject import GameObject
from bases.renderer import RectRenderer
from settings import SHOW_BOX_COLLIDER

class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self)
        self.width = width
        self.height = height
        if SHOW_BOX_COLLIDER:
            self.renderer = RectRenderer(width, height)

    def left(self):
        return self.screen_position.x - self.width / 2

    def right(self):
        return self.screen_position.x + self.width / 2

    def top(self):
        return self.screen_position.y - self.height / 2

    def bottom(self):
        return self.screen_position.y + self.height / 2

    def __str__(self):
        return "".join(str(x) for x in [self.left(), self.right(), self.top(), self.bottom()])

    def collide_with(self, other):
        x_overlap = other.right() >= self.left() and other.left() <= self.right();
        y_overlap = other.bottom() >= self.top() and other.top() <= self.bottom();
        return x_overlap and y_overlap

    def run(self, parent):
        GameObject.run(self, parent)
        if SHOW_BOX_COLLIDER:
            self.renderer.width = self.width
            self.renderer.height = self.height
