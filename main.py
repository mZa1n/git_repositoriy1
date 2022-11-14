import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randrange


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.setWindowTitle('Окружности')

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            draw = QPainter()
            draw.begin(self)
            self.circles(draw)
            draw.end()

    def circles(self, draw):
        draw.setBrush(QColor(255, 255, 0))
        draw.drawEllipse(40, 60, randrange(10, 70), randrange(10, 70))
        draw.drawEllipse(200, 60, randrange(10, 70), randrange(10, 70))
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Form()
    widget.show()
    sys.exit(app.exec())