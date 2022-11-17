import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from UI import Ui_Form


class Form(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.setWindowTitle('Окружности')
        self.pushButton.clicked.connect(self.paint)

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
        rad = randrange(10, 100)
        draw.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
        draw.drawEllipse(40, 60, rad, rad)
        draw.drawEllipse(200, 60, rad, rad)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Form()
    widget.show()
    sys.exit(app.exec())
