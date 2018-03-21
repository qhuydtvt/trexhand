from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QImage, QFontMetrics
from PyQt5.QtCore import QPoint, QRect, Qt

class ImageRenderer:
    def __init__(self, image_url):
        self.image = QImage(image_url)

    def render(self, qp, position):
        qp.drawImage(QPoint(position.x - self.image.width() / 2, position.y  - self.image.height() / 2), self.image)


class Animation:
    def __init__(self, *args, **kwargs):
        self.images = [QImage(arg) for arg in args]
        self.image_index = 0
        self.frame_count = 0
        self.loop = True
        self.frame_multiplier = 5
        self.playing = True

        if "loop" in kwargs:
            self.loop = kwargs["loop"]
        if "frame_multiplier" in kwargs:
            self.frame_multiplier = kwargs["frame_multiplier"]

    def pause(self):
        self.playing = False

    def play(self):
        self.playing = True

    def render(self, qp, position):
        image = self.images[self.image_index]
        qp.drawImage(QPoint(position.x - image.width() / 2, position.y - image.height() / 2), image)
        if self.playing:
            self.frame_count += 1
            if self.frame_count >= self.frame_multiplier:
                self.frame_count = 0
                self.image_index = (self.image_index + 1) % len(self.images)

class RectRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self, qp, position):
        brush = QBrush(QColor('red'))
        qp.drawRect(position.x - self.width / 2, position.y - self.height / 2, self.width, self.height)


class TextRenderer:
    def __init__(self):
        self.text = ""

    def render(self, qp, position):
        font = QFont('Consolas', 16)
        metrics = QFontMetrics(font)
        rect = metrics.boundingRect(self.text)

        qp.setFont(font)
        qp.drawText(QRect(position.x, position.y, rect.width(), rect.height()), Qt.AlignLeft, self.text)
