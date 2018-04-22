# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_queryDialog(object):
    def setupUi(self, queryDialog):
        queryDialog.setObjectName("queryDialog")
        queryDialog.resize(338, 407)
        self.buttonBox = QtWidgets.QDialogButtonBox(queryDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 340, 291, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(queryDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 50, 241, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout_2.addWidget(self.lineEdit_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_gender = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_gender.setObjectName("lineEdit_gender")
        self.horizontalLayout_4.addWidget(self.lineEdit_gender)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_grade = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_grade.setObjectName("lineEdit_grade")
        self.horizontalLayout_5.addWidget(self.lineEdit_grade)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_major = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_major.setObjectName("lineEdit_major")
        self.horizontalLayout_6.addWidget(self.lineEdit_major)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(queryDialog)
        self.buttonBox.accepted.connect(queryDialog.accept)
        self.buttonBox.rejected.connect(queryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(queryDialog)

    def retranslateUi(self, queryDialog):
        _translate = QtCore.QCoreApplication.translate
        queryDialog.setWindowTitle(_translate("queryDialog", "Dialog"))
        self.label.setText(_translate("queryDialog", "学号"))
        self.label_2.setText(_translate("queryDialog", "姓名"))
        self.label_3.setText(_translate("queryDialog", "性别"))
        self.label_4.setText(_translate("queryDialog", "年级"))
        self.label_5.setText(_translate("queryDialog", "专业"))

