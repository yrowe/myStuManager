import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets, QtCore, QtGui
from welcome2 import Ui_Dialog
from slot_signal import set_slot_signal
import globalVar
import database

class logWin(Ui_Dialog):
	#登录界面UI
    def __init__(self):
        super().__init__()
        self.dialog = QtWidgets.QDialog()
        #这个Ui_Dialog和boxUI.py的Ui_Dialog不一样，是在welcome.py里定义的，不一样
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("登录")
        self.userLine = window.lineEdit
        self.passwd = window.lineEdit_2

        self.okButton = window.pushButton
        self.okButton.clicked.connect(self.verifyFunction)
        self.exitButton = window.pushButton_2
        self.exitButton.clicked.connect(self.exitFunction)

        self.comboBox = window.comboBox
        #window.buttonBox.accepted.connect(self.verifyFunction)

    def show(self):
        self.dialog.show()

    def exec_(self):
        self.dialog.exec_()

    def verifyFunction(self):
        #TODO transform this func to database version
        #登录暂时没有接数据库，简单的判断。。
        globalVar.okPush = 1
        #print(self.comboBox.currentText())  #管理员/学生
        globalVar.authority = self.comboBox.currentIndex()   #0 for manager / 1 for student

        #print(type(globalVar.authority))
        ans = database.check_authority(self.userLine.text())
        if(len(ans) == 0):
            #无对应用户名
            globalVar.okPush = 0
            self.warning()
            return

        ans = ans[0]  #列表转元组，因为ans不为空，则必为1
        if self.passwd.text() == ans[1] and self.comboBox.currentIndex() == ans[2]:
            globalVar.authority =  self.comboBox.currentIndex()
            globalVar.uname = self.userLine.text()
            self.dialog.close()
        else:
            globalVar.okPush = 0
            self.warning()
    
    def exitFunction(self):
        sys.exit(0)

    def warning(self):
        subdialog = QtWidgets.QMessageBox.warning(self.dialog, "错误", "用户名或密码错误", QtWidgets.QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    winLog = logWin()
    winLog.show()
    app.exec_()

    if(globalVar.okPush is 0):
        sys.exit(0)
    
    app2 = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app2.exec_())