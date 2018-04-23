# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chooseDialog(object):
    def setupUi(self, chooseDialog):
        chooseDialog.setObjectName("chooseDialog")
        chooseDialog.resize(273, 320)
        self.pushButton = QtWidgets.QPushButton(chooseDialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(chooseDialog)
        self.widget.setGeometry(QtCore.QRect(101, 61, 61, 126))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton1 = QtWidgets.QRadioButton(self.widget)
        self.radioButton1.setObjectName("radioButton1")
        self.verticalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton2.setObjectName("radioButton2")
        self.verticalLayout.addWidget(self.radioButton2)
        self.radioButton3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton3.setObjectName("radioButton3")
        self.verticalLayout.addWidget(self.radioButton3)
        self.radioButton4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton4.setObjectName("radioButton4")
        self.verticalLayout.addWidget(self.radioButton4)

        self.retranslateUi(chooseDialog)
        QtCore.QMetaObject.connectSlotsByName(chooseDialog)

    def retranslateUi(self, chooseDialog):
        _translate = QtCore.QCoreApplication.translate
        chooseDialog.setWindowTitle(_translate("chooseDialog", "Dialog"))
        self.pushButton.setText(_translate("chooseDialog", "确认"))
        self.radioButton1.setText(_translate("chooseDialog", "政治"))
        self.radioButton2.setText(_translate("chooseDialog", "英语"))
        self.radioButton3.setText(_translate("chooseDialog", "数学"))
        self.radioButton4.setText(_translate("chooseDialog", "专业课"))

