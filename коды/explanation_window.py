# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'explanation_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_explanation_window(object):
    def setupUi(self, explanation_window):
        explanation_window.setObjectName("explanation_window")
        explanation_window.resize(600, 500)
        explanation_window.setStyleSheet("background-color: rgb(184, 86, 117);")
        self.pushButton = QtWidgets.QPushButton(explanation_window)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(79, 123, 170);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(explanation_window)
        self.label.setGeometry(QtCore.QRect(100, 210, 151, 41))
        self.label.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(explanation_window)
        self.label_2.setGeometry(QtCore.QRect(100, 290, 151, 41))
        self.label_2.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(explanation_window)
        self.label_3.setGeometry(QtCore.QRect(100, 370, 151, 41))
        self.label_3.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(explanation_window)
        self.label_5.setGeometry(QtCore.QRect(330, 290, 151, 41))
        self.label_5.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(explanation_window)
        self.label_4.setGeometry(QtCore.QRect(330, 210, 151, 41))
        self.label_4.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(explanation_window)
        self.label_6.setGeometry(QtCore.QRect(260, 90, 161, 31))
        self.label_6.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_6.setObjectName("label_6")
        
        self.labels = [self.label, self.label_2, self.label_3, self.label_4, self.label_5]

        self.retranslateUi(explanation_window)
        QtCore.QMetaObject.connectSlotsByName(explanation_window)

    def retranslateUi(self, explanation_window):
        _translate = QtCore.QCoreApplication.translate
        explanation_window.setWindowTitle(_translate("explanation_window", "Form"))
        self.pushButton.setText(_translate("explanation_window", "ЗАПОМНИЛ(А)!"))
        self.label_6.setText(_translate("explanation_window", "TextLabel"))
