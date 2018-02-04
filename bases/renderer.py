from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QImage
from PyQt5.QtCore import QPoint


class ImageRenderer:
    def __init__(self, image_url):
        self.image = QImage(image_url)

    def render(self, qp, position):
        qp.drawImage(QPoint(position.x, position.y), self.image)


class Animation:
    def __init__(self, *args, **kwargs):
        self.images = [QImage(arg) for arg in args]
        self.image_index = 0
        self.frame_count = 0
        self.loop = True
        self.frame_multiplier = 5

        if "loop" in kwargs:
            self.loop = kwargs["loop"]
        if "frame_multiplier" in kwargs:
            self.frame_multiplier = kwargs["frame_multiplier"]

    def render(self, qp, position):
        image = self.images[self.image_index]
        qp.drawImage(QPoint(position.x, position.y), image)
        self.frame_count += 1
        if self.frame_count >= self.frame_multiplier:
            self.frame_count = 0
            self.image_index = (self.image_index + 1) % len(self.images)
