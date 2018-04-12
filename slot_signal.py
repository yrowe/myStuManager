from mainUI import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem
import globalVar
import sqlite3
import database
from Student import Students

class set_slot_signal(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.createNewAction.triggered.connect(self.createNewFunction)
        self.openDataBaseAction.triggered.connect(self.openDBFunction)
        self.fileCloseAction.triggered.connect(self.close)
        self.createButton.clicked.connect(self.createNewFunction)

    def createNewFunction(self):
        
        self.stuInfoList.setRowCount(globalVar.stuNum+1)
        student = Students('10','2','3','4','5')
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app.exec_())