import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QImage
from PyQt5.QtCore import Qt, QRectF, QTimer, QPoint
from PyQt5.QtMultimedia import QSound
from random import choice


from bases.gameobject import add_game_object, render_all

from trex.trex import *
from inputs import input

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
        trex.set_initial_position(10, 140)
        add_game_object(trex)

    def initTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(17)
        self.timer.timeout.connect(self.timerTick)
        self.timer.start()


    def timerTick(self):
        self.repaint()


    def initUI(self):        
        self.text = "Body T Rex"
        self.setFixedSize(800, 300)
        self.show()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, self.width(), self.height(), QColor(255, 255, 255))
        run_all()
        render_all(qp)
        qp.end()


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space or key == Qt.Key_Up:
            input.jump_pressed = True
        if key == Qt.Key_Down:
            input.duck_pressed = True

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space or key == Qt.Key_Up:
            input.jump_pressed = False
        if key == Qt.Key_Down:
            input.duck_pressed = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GameWindow()
    sys.exit(app.exec_())
