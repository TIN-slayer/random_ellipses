import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from elip import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = False
        size = self.size()
        self.x, self.y = size.width(), size.height()
        self.pushButton.clicked.connect(self.elipse)

    def elipse(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.qp = QPainter()
            x, y = randint(0, self.x - 1), randint(0, self.y - 1)
            max_cd = randint(1, min(self.x - x, self.y - y))
            self.qp.begin(self)
            self.qp.setPen(color)
            self.qp.drawEllipse(x, y, max_cd, max_cd)
            self.qp.end()
            self.f = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
