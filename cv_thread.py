from PyQt5.QtCore import QThread
from inputs import input

class CVThread(QThread):

    def run(self):
        count = 0
        while True:
            count += 1
            if count >= 100000:
                input.jump_pressed = not input.jump_pressed
                count = 9
