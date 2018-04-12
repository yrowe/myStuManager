from dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui
import globalVar
import database

class StudentBox(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("档案信息")
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.id = window.lineEdit_id
        self.id.setText('123')
        self.id.setEnabled(False)
        self.name = window.lineEdit_name
        self.gender = window.lineEdit_gender
        self.grade = window.lineEdit_grade
        self.major = window.lineEdit_major
        self.okButton = window.buttonBox.accepted
        self.cancelButton = window.buttonBox.rejected

        self.okButton.connect(self.getValue)

    def show(self):
    	self.dialog.show()

    def exec_(self):
        self.dialog.exec_()

    def getValue(self):
        globalVar.newStu.id = self.id.text()
        globalVar.newStu.name = self.name.text()
        globalVar.newStu.gender = self.gender.text()
        globalVar.newStu.grade = self.grade.text()
        globalVar.newStu.major = self.major.text()
        if database.check_unique_id(globalVar.newStu):
            globalVar.status = 1
            self.dialog.accepted
        else:
            globalVar.status = 0
            self.showWarning()

    def showWarning(self):
        subdialog = QtWidgets.QMessageBox.warning(self.dialog, "警告！", "学号重复！", QtWidgets.QMessageBox.Yes)



class QueryStudent(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("学生查询")
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.id = window.lineEdit_id
        self.name = window.lineEdit_name
        self.gender = window.lineEdit_gender
        self.grade = window.lineEdit_grade
        self.major = window.lineEdit_major
        self.okButton = window.buttonBox.accepted
        self.cancelButton = window.buttonBox.rejected

        self.okButton.connect(self.getValue)

    def exec_(self):
        self.dialog.exec_()

    def getValue(self):
        globalVar.condition.id = self.id.text()
        globalVar.condition.name = self.name.text()
        globalVar.condition.gender = self.gender.text()
        globalVar.condition.grade = self.grade.text()
        globalVar.condition.major = self.major.text()
        self.dialog.accepted
        