from mainUI import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, QtGui
import globalVar
import sqlite3
import database
from Student import Students
from boxUI import StudentBox, QueryStudent
from dialog import Ui_Dialog
import ipdb

class set_slot_signal(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.createNewAction.triggered.connect(self.createNewFunction)
        self.openDataBaseAction.triggered.connect(self.openDBFunction)
        self.fileCloseAction.triggered.connect(self.close)
        self.createButton.clicked.connect(self.createNewFunction)
        self.queryButton.clicked.connect(self.queryFunction)
        #get table item
        self.stuInfoList.itemClicked.connect(self.getItem)
        self.modifyButton.connect(self.modifyFunction)

    def modifyFunction(self):
    	select_row = self.stuInfoList.currentRow()
    	


    def getItem(self, item):
        #ipdb.set_trace()
        #print('you selected =>'+item.text())

        #print(self.stuInfoList.currentRow())
        pass

    def createNewFunction(self):
        self.newDialog()
        if(globalVar.status == 0):
            # id conflict
            return

        self.stuInfoList.setRowCount(globalVar.stuNum+1)
        student = globalVar.newStu
        database.add_new_item(student)
        
        self.stuInfoList.setItem(globalVar.stuNum,0,QTableWidgetItem(student.id))
        self.stuInfoList.setItem(globalVar.stuNum,1,QTableWidgetItem(student.name))
        self.stuInfoList.setItem(globalVar.stuNum,2,QTableWidgetItem(student.gender))
        self.stuInfoList.setItem(globalVar.stuNum,3,QTableWidgetItem(student.grade))
        self.stuInfoList.setItem(globalVar.stuNum,4,QTableWidgetItem(student.major))
        
        globalVar.stuNum = globalVar.stuNum + 1


    def openDBFunction(self):
        allStu = database.get_all_item()
        
        globalVar.stuNum = len(allStu)
        self.stuInfoList.setRowCount(globalVar.stuNum)
        for i in range(globalVar.stuNum):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(allStu[i][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(allStu[i][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(allStu[i][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(allStu[i][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(allStu[i][4]))

    def newDialog(self):
        '''
        dialog = QtWidgets.QDialog()
        btn = QtWidgets.QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.exec_()
        '''
        globalVar.newStu = Students()
        dialog = StudentBox()
        dialog.exec_()

    def queryFunction(self):
        globalVar.condition = Students()
        dialog = QueryStudent()
        dialog.exec_()
        
        result = database.query(globalVar.condition)
        if len(result) is 0:
            globalVar.condition = Students()
            self.warning()
            return

        globalVar.stuNum = len(result)
        self.stuInfoList.clearContents()
        self.stuInfoList.setRowCount(globalVar.stuNum)

        for i in range(globalVar.stuNum):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(result[i][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(result[i][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(result[i][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(result[i][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(result[i][4]))

    def warning(self):
        subdialog = QtWidgets.QMessageBox.warning(self, "查询无效", "无符合条件结果", QtWidgets.QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app.exec_())