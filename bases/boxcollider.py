from bases.vector2d import Vector2D
from bases.gameobject import GameObject
from bases.renderer import RectRenderer

class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self)
        self.width = width
        self.height = height
        self.renderer = RectRenderer(width, height)

    def left(self):
        return self.position.x - self.width / 2

    def right(self):
        return self.position.x + self.width / 2

    def top(self):
        return self.position.y - self.height / 2

    def bottom(self):
        return self.position.y + self.height / 2

    def collideWith(self, other):
        x_overlap = other.right() >= self.left() and other.left() <= self.right();
        y_overlap = other.bottom() >= self.top() and other.top() <= self.bottom();
        return x_overlap and y_overlap;
