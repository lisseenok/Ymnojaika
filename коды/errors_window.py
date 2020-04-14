# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errors_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errors_window(object):
    def setupUi(self, errors_window):
        errors_window.setObjectName("errors_window")
        errors_window.resize(500, 200)
        errors_window.setStyleSheet("background-color: rgb(197, 90, 92);")
        self.centralwidget = QtWidgets.QWidget(errors_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 111))
        self.label.setStyleSheet("font: 87 9pt \'Segoe UI Black\'; \\n ")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 129, 71, 31))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.pushButton.setObjectName("pushButton")
        errors_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(errors_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        errors_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(errors_window)
        self.statusbar.setObjectName("statusbar")
        errors_window.setStatusBar(self.statusbar)

        self.retranslateUi(errors_window)
        QtCore.QMetaObject.connectSlotsByName(errors_window)

    def retranslateUi(self, errors_window):
        _translate = QtCore.QCoreApplication.translate
        errors_window.setWindowTitle(_translate("errors_window", "MainWindow"))
        self.label.setText(_translate("errors_window", "TextLabel"))
        self.pushButton.setText(_translate("errors_window", "ОК"))
