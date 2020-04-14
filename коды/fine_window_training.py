# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fine_window_training.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fine_window_training(object):
    def setupUi(self, fine_window_training):
        fine_window_training.setObjectName("fine_window_training")
        fine_window_training.resize(600, 500)
        fine_window_training.setStyleSheet("background-color: rgb(103, 255, 205);\n"
"")
        self.centralwidget = QtWidgets.QWidget(fine_window_training)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(79, 123, 170);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 70, 421, 31))
        self.label.setStyleSheet("font: 87 12pt \"Segoe UI Black\";\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        fine_window_training.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fine_window_training)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        fine_window_training.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fine_window_training)
        self.statusbar.setObjectName("statusbar")
        fine_window_training.setStatusBar(self.statusbar)

        self.retranslateUi(fine_window_training)
        QtCore.QMetaObject.connectSlotsByName(fine_window_training)

    def retranslateUi(self, fine_window_training):
        _translate = QtCore.QCoreApplication.translate
        fine_window_training.setWindowTitle(_translate("fine_window_training", "MainWindow"))
        self.pushButton.setText(_translate("fine_window_training", "Я МОЛОДЕЦ!"))
