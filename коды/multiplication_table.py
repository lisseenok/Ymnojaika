# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplication_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_multiplication_table(object):
    def setupUi(self, multiplication_table):
        multiplication_table.setObjectName("multiplication_table")
        multiplication_table.resize(650, 550)
        multiplication_table.setStyleSheet("background-color: rgb(36, 161, 189);")
        self.centralwidget = QtWidgets.QWidget(multiplication_table)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 480, 171, 31))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(79, 123, 170);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.pushButton.setObjectName("pushButton")
        multiplication_table.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(multiplication_table)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 18))
        self.menubar.setObjectName("menubar")
        multiplication_table.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(multiplication_table)
        self.statusbar.setObjectName("statusbar")
        multiplication_table.setStatusBar(self.statusbar)

        self.retranslateUi(multiplication_table)
        QtCore.QMetaObject.connectSlotsByName(multiplication_table)

    def retranslateUi(self, multiplication_table):
        _translate = QtCore.QCoreApplication.translate
        multiplication_table.setWindowTitle(_translate("multiplication_table", "MainWindow"))
        self.pushButton.setText(_translate("multiplication_table", "Повторил(а)"))
