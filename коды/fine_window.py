# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fine_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fine_window(object):
    def setupUi(self, fine_window):
        fine_window.setObjectName("fine_window")
        fine_window.resize(600, 500)
        fine_window.setStyleSheet("background-color: rgb(103, 255, 205);\n"
"")
        self.pushButton = QtWidgets.QPushButton(fine_window)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(79, 123, 170);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(fine_window)
        QtCore.QMetaObject.connectSlotsByName(fine_window)

    def retranslateUi(self, fine_window):
        _translate = QtCore.QCoreApplication.translate
        fine_window.setWindowTitle(_translate("fine_window", "Form"))
        self.pushButton.setText(_translate("fine_window", "Я МОЛОДЕЦ!"))
