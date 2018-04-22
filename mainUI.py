from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem
import sys


class Ui_MainWindow(QWidget):
    #登录后的界面，UI设置，不赘述
    def __init__(self):
    	super().__init__()
    	self.initUI()

    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle("毕业设计")
        self.resize(1200,600)

        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.stuInfoList = QTableWidget(self)
        self.stuInfoList.setEditTriggers(self.stuInfoList.NoEditTriggers)
        self.stuInfoList.verticalHeader().setHidden(True)
        self.stuInfoList.setColumnCount(9)
        self.stuInfoList.setHorizontalHeaderLabels(["学号", "姓名", "性别", "年级", "专业", "政治", "英语", "数学", "专业课"])
        #选中条目的动作为选中那一行
        self.stuInfoList.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        #单行选中
        self.stuInfoList.setSelectionMode(Qt.QAbstractItemView.SingleSelection)
        #将每个条目扩展到充满容器
        self.stuInfoList.horizontalHeader().setStretchLastSection(True)
        #将容器宽度平均分给所有条目
        self.stuInfoList.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)

        header = self.stuInfoList.horizontalHeader()
        #header.setSortIndicator(5, QtCore.Qt.AscendingOrder)
        header.setSortIndicatorShown(True)
        header.setSectionsClickable(True)
        #connect(headerGoods, SIGNAL(sectionClicked(int)), _nodeTableWidget, SLOT (sortByColumn(int)))

        self.createButton = Qt.QPushButton(self)
        self.createButton.setText("新建")
        self.createButton.setDefault(True)

        self.deleteButton = Qt.QPushButton(self)
        self.deleteButton.setText("删除")

        self.modifyButton = Qt.QPushButton(self)
        self.modifyButton.setText("修改")

        self.queryButton = Qt.QPushButton(self)
        self.queryButton.setText("查询")

        self.flushButton = Qt.QPushButton(self)
        self.flushButton.setText("后退")
        
        self.menuBar = Qt.QMenuBar(self)

        menu = Qt.QMenu(self.menuBar)
        menu.setTitle("菜单")

        menu_A = Qt.QMenu(self.menuBar)
        menu_A.setTitle("关于")
        self.menuBar.addMenu(menu)
        self.menuBar.addMenu(menu_A)

        self.openAbout = Qt.QAction(menu_A)
        self.openAbout.setText("作品相关")
        menu_A.addAction(self.openAbout)

        self.openDataBaseAction = Qt.QAction(menu)
        self.openDataBaseAction.setText("打开数据库")
        menu.addAction(self.openDataBaseAction)

        self.createNewAction = Qt.QAction(menu)
        self.createNewAction.setText("新建档案")
        #self.enterAction.triggered.connect(self.enterActionTriggered)
        menu.addAction(self.createNewAction)

        self.createNewAccount = Qt.QAction(menu)
        self.createNewAccount.setText("新建学生账户")
        menu.addAction(self.createNewAccount)

        self.findDisqualified = Qt.QAction(menu)
        self.findDisqualified.setText("查询不及格")
        menu.addAction(self.findDisqualified)

        self.fileCloseAction = Qt.QAction(menu)
        self.fileCloseAction.setText("关闭")
        menu.addAction(self.fileCloseAction)

        '''
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_E.setTitle(_translate("MainWindow", "编辑(&E)"))
        '''
        layout = Qt.QGridLayout(self)
        layout.addWidget(self.stuInfoList,3,0,5,-1)
        layout.addWidget(self.queryButton,8,9,1,1)
        layout.addWidget(self.createButton,8,6,1,1)
        layout.addWidget(self.modifyButton,8,8,1,1)
        layout.addWidget(self.deleteButton,8,7,1,1)
        layout.addWidget(self.flushButton,8,10,1,1)
        layout.setMenuBar(self.menuBar)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Ui_MainWindow()
	win.show()
	sys.exit(app.exec_())

