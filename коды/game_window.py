# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(1200, 800)
        GameWindow.setStyleSheet("background-color: rgb(205, 213, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushbutton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_menu.setGeometry(QtCore.QRect(40, 40, 31, 31))
        self.pushbutton_menu.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; ")
        self.pushbutton_menu.setText("")
        self.pushbutton_menu.setObjectName("pushbutton_menu")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("4.png"))
        self.pushbutton_menu.setIcon(icon)
        self.pushbutton_menu.setIconSize(QtCore.QSize(35, 35))
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 150, 201, 51))
        self.pushButton_1.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 510, 201, 51))
        self.pushButton_4.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 10pt \'Segoe UI Black\'; \\n")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 630, 201, 51))
        self.pushButton_5.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 10pt \'Segoe UI Black\'; \\n")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 390, 201, 51))
        self.pushButton_3.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 10pt \'Segoe UI Black\'; \\n\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 270, 201, 51))
        self.pushButton_2.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 10pt \'Segoe UI Black\'; \\n\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 150, 131, 51))
        self.frame.setStyleSheet("border-style: outset;\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(410, 270, 131, 51))
        self.frame_2.setStyleSheet("border-style: outset;\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(410, 390, 131, 51))
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; ")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(410, 510, 131, 51))
        self.frame_4.setStyleSheet("border-style: outset;\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; ")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(410, 630, 131, 51))
        self.frame_5.setStyleSheet("border-style: outset;\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; ")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(960, 680, 151, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"background-color: rgb(170, 78, 99);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 10pt \'Segoe UI Black\'; \\n")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 921, 31))
        self.label.setStyleSheet("font: 87 12pt \'Segoe UI Grey\'; \\n ")
        self.label.setObjectName("label")
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("GameWindow", "1"))
        self.pushButton_4.setText(_translate("GameWindow", "4"))
        self.pushButton_5.setText(_translate("GameWindow", "5"))
        self.pushButton_3.setText(_translate("GameWindow", "3"))
        self.pushButton_2.setText(_translate("GameWindow", "2"))
        self.pushButton.setText(_translate("GameWindow", "ГОТОВО"))
        self.label.setText(_translate("GameWindow", "Перетащи правильные ответы к соответствующим примерам и нажми \"Готово\"."))
