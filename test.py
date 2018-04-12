import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("Test", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: red;}")

        self.button = QPushButton("Test", self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)

        self.setLayout(self.layout)
        self.show()

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())