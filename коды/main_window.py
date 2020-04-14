# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(205, 213, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushbutton_training = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_training.setGeometry(QtCore.QRect(350, 650, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbutton_training.sizePolicy().hasHeightForWidth())
        self.pushbutton_training.setSizePolicy(sizePolicy)
        self.pushbutton_training.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushbutton_training.setObjectName("pushbutton_training")
        self.pushbutton_game = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_game.setGeometry(QtCore.QRect(630, 650, 201, 41))
        self.pushbutton_game.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushbutton_game.setObjectName("pushbutton_game")
        self.pushbutton_group_game = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_group_game.setGeometry(QtCore.QRect(910, 650, 201, 41))
        self.pushbutton_group_game.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushbutton_group_game.setObjectName("pushbutton_group_game")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 20, 311, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushButton.setObjectName("pushButton")
        self.pushbutton_learning = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_learning.setGeometry(QtCore.QRect(70, 650, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbutton_learning.sizePolicy().hasHeightForWidth())
        self.pushbutton_learning.setSizePolicy(sizePolicy)
        self.pushbutton_learning.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushbutton_learning.setObjectName("pushbutton_learning")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushbutton_training.setText(_translate("MainWindow", "ТРЕНИРОВКА"))
        self.pushbutton_game.setText(_translate("MainWindow", "ИГРА"))
        self.pushbutton_group_game.setText(_translate("MainWindow", "КОМАНДНАЯ ИГРА"))
        self.pushButton.setText(_translate("MainWindow", "Повториить таблицу умножения"))
        self.pushbutton_learning.setText(_translate("MainWindow", "ИЗУЧЕНИЕ"))
