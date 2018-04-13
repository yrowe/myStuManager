import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets, QtCore, QtGui
from welcome import Ui_Dialog
from slot_signal import set_slot_signal
import globalVar

class logWin(Ui_Dialog):
	#TODO ! rewrite this UI, because buttonBox accepted func is not what i expected!
    def __init__(self):
        super().__init__()
        self.dialog = QtWidgets.QDialog()
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("登录")
        self.userLine = window.lineEdit
        self.passwd = window.lineEdit_2

        self.okButton = window.buttonBox.accepted
        self.okButton.connect(self.verifyFunction)
        #window.buttonBox.accepted.connect(self.verifyFunction)

    def show(self):
        self.dialog.show()

    def exec_(self):
        self.dialog.exec_()

    def verifyFunction(self):
        #TODO transform this func to database version
        if self.userLine.text() == 'wuziqiang' and self.passwd.text() == '123':
            globalVar.verify = 1
        elif self.userLine.text() == 'admin' and self.passwd.text() == '123':
        	globalVar.verify = 2
        else:
            self.warning()

    def warning(self):
        subdialog = QtWidgets.QMessageBox.warning(self.dialog, "错误", "用户名或密码错误", QtWidgets.QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    winLog = logWin()
    winLog.show()

    winLog.exec_()
    
    if(globalVar.verify is 0):
        sys.exit(0)
    
    app2 = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app2.exec_())