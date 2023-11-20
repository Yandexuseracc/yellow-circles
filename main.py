import io
import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtGui import QColor


class Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)
        self.createButton.clicked.connect(self.paintCircle)
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setSceneRect(-150, -150, 500, 500)
        self.setCentralWidget(self.view)
        self.layout().addWidget(self.createButton)

    def paintCircle(self):
        self.scene.clear()
        diameter = random.randint(100, 500)
        yellow_circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        yellow_circle.setRect(0, 0, diameter, diameter)
        yellow_circle.setBrush(QColor('yellow'))
        self.view.centerOn(yellow_circle)
        self.scene.addItem(yellow_circle)
        self.scene.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())
