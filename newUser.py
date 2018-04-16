from reg_dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui
import database


class Ui_register(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_Dialog()
        window.setupUi(self.dialog)
        self.dialog.setWindowTitle("新建学生账户")
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.user = window.lineEdit
        self.passwd = window.lineEdit_2

        self.okButton = window.pushButton
        self.okButton.clicked.connect(self.insertNewAccount)

    def exec_(self):
        self.dialog.exec_()

    def insertNewAccount(self):

        isUnique = database.check_unique_id_authority(self.user.text())
        if isUnique is False:
            self.warning()
        else:
            database.insert_authority(self.user.text(), self.passwd.text())
            self.showMessage(self.user.text())
            self.dialog.close()
            

    def warning(self):
        subdialog = QtWidgets.QMessageBox.warning(self.dialog, "新建无效", "用户名已存在", QtWidgets.QMessageBox.Yes)

    def showMessage(self, uname):
    	subdialog = QtWidgets.QMessageBox.information(self.dialog, "新建成功", "新建用户'{}'".format(uname), QtWidgets.QMessageBox.Yes)