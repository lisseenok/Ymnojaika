# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_game_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_group_game_window(object):
    def setupUi(self, group_game_window):
        group_game_window.setObjectName("group_game_window")
        group_game_window.resize(1200, 800)
        group_game_window.setStyleSheet("background-color: rgb(205, 213, 255);")
        self.centralwidget = QtWidgets.QWidget(group_game_window)
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
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 30, 291, 71))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 551, 61))
        self.label.setStyleSheet("font: 87 14pt \'Segoe UI Black\'; \\n ")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 240, 211, 51))
        self.lineEdit.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 390, 551, 61))
        self.label_3.setStyleSheet("font: 87 14pt \'Segoe UI Black\'; \\n ")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 520, 211, 51))
        self.lineEdit_2.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 680, 231, 61))
        self.pushButton_2.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"background-color: rgb(118, 55, 68);\n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 12pt \'Segoe UI Black\'; \\n \n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        group_game_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(group_game_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        group_game_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(group_game_window)
        self.statusbar.setObjectName("statusbar")
        group_game_window.setStatusBar(self.statusbar)

        self.retranslateUi(group_game_window)
        QtCore.QMetaObject.connectSlotsByName(group_game_window)

    def retranslateUi(self, group_game_window):
        _translate = QtCore.QCoreApplication.translate
        group_game_window.setWindowTitle(_translate("group_game_window", "MainWindow"))
        self.pushButton.setText(_translate("group_game_window", "Правила командной игры"))
        self.label.setText(_translate("group_game_window", "Введите название первой команды:"))
        self.label_3.setText(_translate("group_game_window", "Введите название второй команды:"))
        self.pushButton_2.setText(_translate("group_game_window", "Поехали!"))
