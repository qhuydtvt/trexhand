class Vector2D:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return Vector2D(self.x + x, self.y + y)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def multiply(self, m):
        return Vector2D(self.x * m, self.y * m)

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

def ZERO():
    return Vector2D(0, 0)

ONE = Vector2D(1, 1)
UP = Vector2D(0, -1)
DOWN = Vector2D(0, 1)
LEFT = Vector2D(-1, 0)
RIGHT = Vector2D(1, 0)
