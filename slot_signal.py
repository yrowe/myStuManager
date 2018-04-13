from mainUI import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, QtGui
import globalVar
import sqlite3
import database
from Student import Students
from boxUI import StudentBox, QueryStudent, EditClass
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
        self.modifyButton.clicked.connect(self.modifyFunction)
        self.deleteButton.clicked.connect(self.deleteFunction)
        #get table item
        self.stuInfoList.itemClicked.connect(self.getItem)
        
        if globalVar.verify is 1:
            self.deleteButton.setEnabled(False)
            self.modifyButton.setEnabled(False)
            self.createButton.setEnabled(False)
            self.queryButton.setDefault(True)
            self.createNewAction.setEnabled(False)
        

    def modifyFunction(self):
    	#TODO if there is no selected row , what will happen
        select_row = self.stuInfoList.currentRow()
        if(select_row is -1):
        	self.warning(1)
        	return
        collectStu = Students()
        collectStu.id = self.stuInfoList.item(select_row, 0).text()
        collectStu.name = self.stuInfoList.item(select_row, 1).text()
        collectStu.gender = self.stuInfoList.item(select_row, 2).text()
        collectStu.grade = self.stuInfoList.item(select_row, 3).text()
        collectStu.major = self.stuInfoList.item(select_row, 4).text()
        
        globalVar.hasEdited = 0

        dialog = EditClass(collectStu)
        dialog.exec_()
        
        if globalVar.hasEdited is 0:
            return

        self.stuInfoList.setItem(select_row, 0,QTableWidgetItem(globalVar.editStu.id))
        self.stuInfoList.setItem(select_row, 1,QTableWidgetItem(globalVar.editStu.name))
        self.stuInfoList.setItem(select_row, 2,QTableWidgetItem(globalVar.editStu.gender))
        self.stuInfoList.setItem(select_row, 3,QTableWidgetItem(globalVar.editStu.grade))
        self.stuInfoList.setItem(select_row, 4,QTableWidgetItem(globalVar.editStu.major))

        database.modify_item_by_id(globalVar.editStu)

    def getItem(self, item):
        #ipdb.set_trace()
        #print('you selected =>'+item.text())

        #print(self.stuInfoList.currentRow())
        pass

    def createNewFunction(self):
    	#TODO more rule to define input! the number of input id, non-blank text
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

    def deleteFunction(self):
        select_row = self.stuInfoList.currentRow()
        if select_row is -1:
            self.warning(2)
            return
        select_id = self.stuInfoList.item(select_row, 0).text()
        self.stuInfoList.removeRow(select_row)
        database.delete(select_id)


    def queryFunction(self):
        globalVar.condition = Students()
        globalVar.hasQuery = 0

        dialog = QueryStudent()
        dialog.exec_()

        if globalVar.condition.id is '' and globalVar.condition.name is '' \
        and globalVar.condition.gender is '' and globalVar.condition.grade is ''\
        and globalVar.condition.major is '' and globalVar.hasQuery is 1:
            self.warning(3)
            return
        
        result = database.query(globalVar.condition)
        if len(result) is 0 and globalVar.hasQuery is 1:
            globalVar.condition = Students()
            self.warning(0)
            return

        if len(result) is 0:
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

    def warning(self, typeError):
        if typeError is 0:
            subdialog = QtWidgets.QMessageBox.warning(self, "查询无效", "无符合条件结果", QtWidgets.QMessageBox.Yes)
            return
        if typeError is 1:
            subdialog = QtWidgets.QMessageBox.warning(self, "修改无效", "未选定行", QtWidgets.QMessageBox.Yes)
            return
        if typeError is 2:
            subdialog = QtWidgets.QMessageBox.warning(self, "删除无效", "未选定行", QtWidgets.QMessageBox.Yes)
            return

        if typeError is 3:
            subdialog = QtWidgets.QMessageBox.warning(self, "查询无效", "至少指定一个条件", QtWidgets.QMessageBox.Yes)
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app.exec_())