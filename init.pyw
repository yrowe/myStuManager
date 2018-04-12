# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:34:45 2018

@author: 91243
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem
from dialog import *

class MyMainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())