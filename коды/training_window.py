# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'training_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainingWindow(object):
    def setupUi(self, TrainingWindow):
        TrainingWindow.setObjectName("TrainingWindow")
        TrainingWindow.resize(1200, 800)
        TrainingWindow.setStyleSheet("background-color: rgb(205, 213, 255);")
        self.centralwidget = QtWidgets.QWidget(TrainingWindow)
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
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 340, 431, 101))
        self.label.setStyleSheet("font: 87 26pt \'Segoe UI Black\'; \\n ")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(740, 340, 151, 101))
        self.lineEdit.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 26pt \'Segoe UI Black\'; \\n ")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 680, 291, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(79, 123, 170);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 991, 121))
        self.label_2.setStyleSheet("font: 87 12pt \'Segoe UI Grey\'; \\n ")
        self.label_2.setObjectName("label_2")
        TrainingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrainingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        TrainingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TrainingWindow)
        self.statusbar.setObjectName("statusbar")
        TrainingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrainingWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainingWindow)

    def retranslateUi(self, TrainingWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainingWindow.setWindowTitle(_translate("TrainingWindow", "MainWindow"))
        self.label.setText(_translate("TrainingWindow", "TextLabel"))
        self.pushButton.setText(_translate("TrainingWindow", "ЗАВЕРШИТЬ ТРЕНИРОВКУ"))
        self.label_2.setText(_translate("TrainingWindow", "Вводи ответ и нажимай Enter. \n"
"При неверном ответе ты получишь подсказку, а при верном тренировка продолжится.\n"
"Для окончания тренировки нажми кнопку \"Завершить тренировку\"."))
