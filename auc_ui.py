# Form implementation generated from reading ui file 'auc1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #line to remove below if wrong
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.centralwidget.setLayout(self.layout)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuArea_Color = QtWidgets.QMenu(parent=self.menubar)
        self.menuArea_Color.setObjectName("menuArea_Color")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon1)
        self.actionClear.setObjectName("actionClear")
        self.action3px = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Three.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action3px.setIcon(icon2)
        self.action3px.setObjectName("action3px")
        self.action5px = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Five.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action5px.setIcon(icon3)
        self.action5px.setObjectName("action5px")
        self.action7px = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Seven.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action7px.setIcon(icon4)
        self.action7px.setObjectName("action7px")
        self.action9px = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Nine.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action9px.setIcon(icon5)
        self.action9px.setObjectName("action9px")
        self.actionBlack = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Solid_black.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBlack.setIcon(icon6)
        self.actionBlack.setObjectName("actionBlack")
        self.actionRed = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Solid_red.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRed.setIcon(icon7)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Solid_green.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionGreen.setIcon(icon8)
        self.actionGreen.setObjectName("actionGreen")
        self.actionYellow = QtGui.QAction(parent=MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/1024px-Solid_yellow.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionYellow.setIcon(icon9)
        self.actionYellow.setObjectName("actionYellow")
        self.actionWhite = QtGui.QAction(parent=MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/Resources/Icons/Solid_white.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWhite.setIcon(icon10)
        self.actionWhite.setObjectName("actionWhite")
        self.action_color_red = QtGui.QAction(parent=MainWindow)
        self.action_color_red.setObjectName("action_color_red")
        self.action_color_green = QtGui.QAction(parent=MainWindow)
        self.action_color_green.setObjectName("action_color_green")
        self.action_color_yellow = QtGui.QAction(parent=MainWindow)
        self.action_color_yellow.setObjectName("action_color_yellow")
        self.menuFile.addAction(self.actionClear)
        self.menuArea_Color.addAction(self.action_color_red)
        self.menuArea_Color.addSeparator()
        self.menuArea_Color.addAction(self.action_color_green)
        self.menuArea_Color.addSeparator()
        self.menuArea_Color.addAction(self.action_color_yellow)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuArea_Color.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuArea_Color.setTitle(_translate("MainWindow", "Area Color"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action3px.setText(_translate("MainWindow", "3px"))
        self.action3px.setShortcut(_translate("MainWindow", "Alt+3"))
        self.action5px.setText(_translate("MainWindow", "5px"))
        self.action5px.setShortcut(_translate("MainWindow", "Alt+5"))
        self.action7px.setText(_translate("MainWindow", "7px"))
        self.action7px.setShortcut(_translate("MainWindow", "Alt+7"))
        self.action9px.setText(_translate("MainWindow", "9px"))
        self.action9px.setShortcut(_translate("MainWindow", "Alt+9"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionBlack.setShortcut(_translate("MainWindow", "Alt+B"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionRed.setShortcut(_translate("MainWindow", "Alt+R"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionGreen.setShortcut(_translate("MainWindow", "Alt+G"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionYellow.setShortcut(_translate("MainWindow", "Alt+Y"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.actionWhite.setShortcut(_translate("MainWindow", "Alt+W"))
        self.action_color_red.setText(_translate("MainWindow", "Red"))
        self.action_color_green.setText(_translate("MainWindow", "Green"))
        self.action_color_yellow.setText(_translate("MainWindow", "Yellow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
