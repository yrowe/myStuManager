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
import about
from newUser import Ui_register
from choose_dialog import Ui_choose

class set_slot_signal(Ui_MainWindow):
	#信号与槽，对应登陆后的界面
    def __init__(self):
        super().__init__()
        authority_name = ['管理员','学生']
        self.setWindowTitle("学生成绩管理系统-用户名:{}-权限:{}".format(globalVar.uname,authority_name[globalVar.authority]))
        #菜单，创建档案选项
        self.createNewAction.triggered.connect(self.createNewFunction)
        #菜单，打开数据库选项
        self.openDataBaseAction.triggered.connect(self.openDBFunction)
        #菜单，关闭选项
        self.fileCloseAction.triggered.connect(self.close)
        #菜单，关于选项
        self.openAbout.triggered.connect(self.openAboutFunction)
        #按钮，创建档案
        self.createButton.clicked.connect(self.createNewFunction)
        #按钮，查询按钮
        self.queryButton.clicked.connect(self.queryFunction)
        #按钮，修改按钮
        self.modifyButton.clicked.connect(self.modifyFunction)
        #按钮，删除按钮
        self.deleteButton.clicked.connect(self.deleteFunction)
        self.flushButton.clicked.connect(self.flushFunction)
        #get table item
        #self.stuInfoList.itemClicked.connect(self.getItem)
        self.findDisqualified.triggered.connect(self.findDisFunction)
        self.createNewAccount.triggered.connect(self.newAccountFunction)

        header = self.stuInfoList.horizontalHeader()
        header.sectionClicked.connect(self.HorSectionClicked)
        
        #如果登录时候，得到的权限只是学生，则使增删改功能失效
        if globalVar.authority is 1:
            self.deleteButton.setEnabled(False)
            self.modifyButton.setEnabled(False)
            self.createButton.setEnabled(False)
            self.queryButton.setDefault(True)
            self.createNewAction.setEnabled(False)
            self.createNewAccount.setEnabled(False)

    def modifyFunction(self):
        #TODO if there is no selected row , what will happen
        #修改按钮对应的函数
        #得到选中的行
        select_row = self.stuInfoList.currentRow()
        #如果，没有选中行，此时值为-1， 显示警告
        if(select_row is -1):
            self.warning(1)
            return
        #新建一个学生实例，方便传数据
        collectStu = Students()
        #把修改前的值记录下来，方便在窗口显示
        collectStu.id = self.stuInfoList.item(select_row, 0).text()
        collectStu.name = self.stuInfoList.item(select_row, 1).text()
        collectStu.gender = self.stuInfoList.item(select_row, 2).text()
        collectStu.grade = self.stuInfoList.item(select_row, 3).text()
        collectStu.major = self.stuInfoList.item(select_row, 4).text()
        collectStu.score1 = self.stuInfoList.item(select_row, 5).text()
        collectStu.score2 = self.stuInfoList.item(select_row, 6).text()
        collectStu.score3 = self.stuInfoList.item(select_row, 7).text()
        collectStu.score4 = self.stuInfoList.item(select_row, 8).text()
        #设置是否修改的标志位
        globalVar.hasEdited = 0
        #打开修改窗口对话框
        dialog = EditClass(collectStu)
        dialog.exec_()
        
        #如果没有修改，则直接返回
        if globalVar.hasEdited is 0:
            return
        
        #有对信息修改的话，修改UI界面对应的显示
        self.stuInfoList.setItem(select_row, 0,QTableWidgetItem(globalVar.editStu.id))
        self.stuInfoList.setItem(select_row, 1,QTableWidgetItem(globalVar.editStu.name))
        self.stuInfoList.setItem(select_row, 2,QTableWidgetItem(globalVar.editStu.gender))
        self.stuInfoList.setItem(select_row, 3,QTableWidgetItem(globalVar.editStu.grade))
        self.stuInfoList.setItem(select_row, 4,QTableWidgetItem(globalVar.editStu.major))
        self.stuInfoList.setItem(select_row, 5,QTableWidgetItem(str(globalVar.editStu.score1)))
        self.stuInfoList.setItem(select_row, 6,QTableWidgetItem(str(globalVar.editStu.score2)))
        self.stuInfoList.setItem(select_row, 7,QTableWidgetItem(str(globalVar.editStu.score3)))
        self.stuInfoList.setItem(select_row, 8,QTableWidgetItem(str(globalVar.editStu.score4)))
        total_score = globalVar.editStu.score1+globalVar.editStu.score2+globalVar.editStu.score3+globalVar.editStu.score4
        self.stuInfoList.setItem(select_row, 9,QTableWidgetItem(str(globalVar.editStu.score5)))
        
        #修改数据库对应的项
        database.modify_item_by_id(globalVar.editStu)


    def createNewFunction(self):
        #TODO more rule to define input! the number of input id, non-blank text
        #新建对话框
        self.newDialog()
        if(globalVar.status == 0):
            # id conflict
            #如果，新建的学生学号重复，则已经显示过警告了，此处就直接退出了
            return
        
        #为UI界面新增项准备工作，把当前表项数+1
        self.stuInfoList.setRowCount(globalVar.stuNum+1)
        #得到需要增加的学生档案的值
        student = globalVar.newStu
        #同步增加到数据库上
        database.add_new_item(student)
        #在UI界面新增项
        self.stuInfoList.setItem(globalVar.stuNum,0,QTableWidgetItem(student.id))
        self.stuInfoList.setItem(globalVar.stuNum,1,QTableWidgetItem(student.name))
        self.stuInfoList.setItem(globalVar.stuNum,2,QTableWidgetItem(student.gender))
        self.stuInfoList.setItem(globalVar.stuNum,3,QTableWidgetItem(student.grade))
        self.stuInfoList.setItem(globalVar.stuNum,4,QTableWidgetItem(student.major))
        self.stuInfoList.setItem(globalVar.stuNum,5,QTableWidgetItem(str(student.score1)))
        self.stuInfoList.setItem(globalVar.stuNum,6,QTableWidgetItem(str(student.score2)))
        self.stuInfoList.setItem(globalVar.stuNum,7,QTableWidgetItem(str(student.score3)))
        self.stuInfoList.setItem(globalVar.stuNum,8,QTableWidgetItem(str(student.score4)))
        total_score = student.score1+student.score2+student.score3+student.score4
        self.stuInfoList.setItem(globalVar.stuNum,9,QTableWidgetItem(str(total_score)))
        #同步全局变量，+1，新增一个学生
        globalVar.stuNum = globalVar.stuNum + 1
    
    def getfiles(self):
        #打开数据库操作，在下面的openDBFunction用到
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open database', 
        	'.', "database file(*.db)")
        #得到数据库地址，同步到全局变量
        globalVar.dbPath = fname

    def HorSectionClicked(self, index):
        #print(index)
        if(index < 5):
            return
        #print(globalVar.col_index, index)
        if globalVar.col_index != index:
            globalVar.col_index = index
            globalVar.ascend = 0

        header = self.stuInfoList.horizontalHeader()
        header.setSortIndicator(index, QtCore.Qt.AscendingOrder)
        if globalVar.ascend == 0:
            self.stuInfoList.sortByColumn(index, QtCore.Qt.AscendingOrder)
        else:
            self.stuInfoList.sortByColumn(index, QtCore.Qt.DescendingOrder)
        globalVar.ascend = (globalVar.ascend+1)%2

    def openDBFunction(self):
        #对应，打开数据选项函数
        #打开数据库
        #self.getfiles()
        #得到数据库中所有项
        allStu = database.get_all_item()
        #获得需要显示的项目个数，同步全局变量
        globalVar.stuNum = len(allStu)
        #更新UI界面显示
        self.stuInfoList.setRowCount(globalVar.stuNum)
        for i in range(globalVar.stuNum):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(allStu[i][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(allStu[i][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(allStu[i][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(allStu[i][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(allStu[i][4]))
            self.stuInfoList.setItem(i, 5, QTableWidgetItem(str(allStu[i][5])))
            self.stuInfoList.setItem(i, 6, QTableWidgetItem(str(allStu[i][6])))
            self.stuInfoList.setItem(i, 7, QTableWidgetItem(str(allStu[i][7])))
            self.stuInfoList.setItem(i, 8, QTableWidgetItem(str(allStu[i][8])))
            total_score = allStu[i][5]+allStu[i][6]+allStu[i][7]+allStu[i][8]
            self.stuInfoList.setItem(i, 9, QTableWidgetItem(str(total_score)))

    def newDialog(self):
        #对接创建新档案用到的，新窗口
        globalVar.newStu = Students()
        dialog = StudentBox()
        dialog.exec_()

    def deleteFunction(self):
        #删除按钮对应的函数
        #获取目前选中的行号
        select_row = self.stuInfoList.currentRow()
        #如果，没有选中行，则显示警告，并直接退出
        if select_row is -1:
            self.warning(2)
            return
        #获取选中行的ID
        select_id = self.stuInfoList.item(select_row, 0).text()
        #删除选中行
        self.stuInfoList.removeRow(select_row)
        #同步更新到数据库
        database.delete(select_id)
        globalVar.stuNum = globalVar.stuNum - 1


    def queryFunction(self):
        #查询操作对应的函数
        #用全局变量记录查询条件
        globalVar.condition = Students()
        #是否进行了查询标志位
        globalVar.hasQuery = 0
        
        #点击查询按钮弹出的页面
        dialog = QueryStudent()
        dialog.exec_()
        
        #点了查询，但是输入全部为空
        if globalVar.condition.id is '' and globalVar.condition.name is '' \
        and globalVar.condition.gender is '' and globalVar.condition.grade is ''\
        and globalVar.condition.major is '' and globalVar.condition.score is ''\
        and globalVar.hasQuery is 1:
            self.warning(3)
            return
        #点了查询，但是无合适结果
        result = database.query(globalVar.condition)
        if len(result) is 0 and globalVar.hasQuery is 1:
            globalVar.condition = Students()
            self.warning(0)
            return
        #点了查询按钮，但是没查，直接退出的情况
        if len(result) is 0:
            return
        
        #获得符合条件的结果个数
        globalVar.stuNum = len(result)
        #清空UI界面，好进行显示
        self.stuInfoList.clearContents()
        #显示查询结果，在UI界面上
        self.stuInfoList.setRowCount(globalVar.stuNum)

        for i in range(globalVar.stuNum):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(result[i][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(result[i][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(result[i][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(result[i][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(result[i][4]))
            self.stuInfoList.setItem(i, 5, QTableWidgetItem(str(result[i][5])))
            self.stuInfoList.setItem(i, 6, QTableWidgetItem(str(result[i][6])))
            self.stuInfoList.setItem(i, 7, QTableWidgetItem(str(result[i][7])))
            self.stuInfoList.setItem(i, 8, QTableWidgetItem(str(result[i][8])))
            total_score = result[i][5]+result[i][6]+result[i][7]+result[i][8]
            self.stuInfoList.setItem(i, 9, QTableWidgetItem(str(total_score)))

    def warning(self, typeError):
    	#不同的警告
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

    def openAboutFunction(self):
    	#菜单，关于选项
        dialog = QtWidgets.QDialog()
        window = about.Ui_Dialog()
        window.setupUi(dialog)
        dialog.setWindowTitle("关于")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        dialog.exec_()

    def flushFunction(self):
        allStu = database.get_all_item()
        #获得需要显示的项目个数，同步全局变量
        globalVar.stuNum = len(allStu)
        #更新UI界面显示
        self.stuInfoList.setRowCount(globalVar.stuNum)
        for i in range(globalVar.stuNum):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(allStu[i][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(allStu[i][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(allStu[i][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(allStu[i][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(allStu[i][4]))
            self.stuInfoList.setItem(i, 5, QTableWidgetItem(str(allStu[i][5])))
            self.stuInfoList.setItem(i, 6, QTableWidgetItem(str(allStu[i][6])))
            self.stuInfoList.setItem(i, 7, QTableWidgetItem(str(allStu[i][7])))
            self.stuInfoList.setItem(i, 8, QTableWidgetItem(str(allStu[i][8])))
            total_score = allStu[i][5]+allStu[i][6]+allStu[i][7]+allStu[i][8]
            self.stuInfoList.setItem(i, 9, QTableWidgetItem(str(total_score)))

    def findDisFunction(self):
    	#查询不及格学生
        diglog = Ui_choose()
        diglog.exec_()

        allStu = database.get_all_item()
        #globalVar.stuNum = len(allStu)
        #self.stuInfoList.setRowCount(globalVar.stuNum)
        #遍历的索引值
        nowIndex = 0
        #该循环I为当前显示的索引值，不同于之前的类似结构里的I
        i = 0
        #不同科目，为60和90
        if globalVar.disqualified == 5 or globalVar.disqualified == 6:
            thresh = 60
        else:
            thresh = 90

        for nowIndex in range(globalVar.stuNum):
            if(int(allStu[nowIndex][globalVar.disqualified]) >= thresh):
                continue
            
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(allStu[nowIndex][0]))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(allStu[nowIndex][1]))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(allStu[nowIndex][2]))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(allStu[nowIndex][3]))
            self.stuInfoList.setItem(i, 4, QTableWidgetItem(allStu[nowIndex][4]))
            self.stuInfoList.setItem(i, 5, QTableWidgetItem(str(allStu[nowIndex][5])))
            self.stuInfoList.setItem(i, 6, QTableWidgetItem(str(allStu[nowIndex][6])))
            self.stuInfoList.setItem(i, 7, QTableWidgetItem(str(allStu[nowIndex][7])))
            self.stuInfoList.setItem(i, 8, QTableWidgetItem(str(allStu[nowIndex][8])))
            total_score = allStu[nowIndex][5]+allStu[nowIndex][6]+allStu[nowIndex][7]+allStu[nowIndex][8]
            self.stuInfoList.setItem(i, 9, QTableWidgetItem(str(total_score)))
            i = i + 1
            
        #删除多余网格
        self.stuInfoList.setRowCount(i)
        globalVar.stuNum = i

    def newAccountFunction(self):
        dialog = Ui_register()
        dialog.exec_()


if __name__ == '__main__':
    #这样 python slot_signal.py就可以直接运行，方便调试，把这段删了，就必须先登录
    app = QApplication(sys.argv)
    win = set_slot_signal()
    win.show()
    sys.exit(app.exec_())