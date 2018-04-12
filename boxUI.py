from dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui

class StudentBox(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("档案信息")
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.id = window.lineEdit_id
        self.name = window.lineEdit_name
        self.gender = window.lineEdit_gender
        self.grade = window.lineEdit_grade
        self.major = window.lineEdit_major
        self.okButton = window.buttonBox.accepted
        self.cancelButton = window.buttonBox.rejected 

    def show(self):
    	self.dialog.show()

    def exec_(self):
    	self.dialog.exec_()