from choose import Ui_chooseDialog
from PyQt5 import QtWidgets, QtCore, QtGui
import globalVar

class Ui_choose(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_chooseDialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("选择不及格科目")
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.subject1 = window.radioButton1
        self.subject2 = window.radioButton2
        self.subject3 = window.radioButton3
        self.subject4 = window.radioButton4

        self.okButton = window.pushButton
        self.okButton.clicked.connect(self.getClass)

    def getClass(self):
    	#假如用户一项都没选，特殊情况处理 TODO
        if self.subject1.isChecked():
            globalVar.disqualified = 5
        if self.subject2.isChecked():
            globalVar.disqualified = 6
        if self.subject3.isChecked():
            globalVar.disqualified = 7
        if self.subject4.isChecked():
            globalVar.disqualified = 8
        self.dialog.close()

    def exec_(self):
        self.dialog.exec_()
