import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QImage
from PyQt5.QtCore import Qt, QRectF, QTimer, QPoint
from PyQt5.QtMultimedia import QSound
from random import choice

from bases.gameobject import add_game_object, render_all

from trex.trex import *

class GameWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.t_rex_idle = QImage('images/trex-idle.png')
        self.initSound()
        self.setup_trex()
        self.initTimer()
        self.initUI()

    def initSound(self):
        self.correctSound = QSound('sound/correct.wav')
        self.incorrectSound = QSound('sound/incorrect.wav')

    def setup_trex(self):
        add_game_object(trex)

    def initTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(17)
        self.timer.timeout.connect(self.timerTick)
        self.timer.start()


    def timerTick(self):
        self.repaint()


    def initUI(self):
        self.text = "Back color"
        self.setFixedSize(800, 300)
        self.show()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, self.width(), self.height(), QColor(255, 255, 255))
        run_all()
        render_all(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GameWindow()
    sys.exit(app.exec_())
