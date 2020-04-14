# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'explanation_window_training.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_explanation_window_training(object):
    def setupUi(self, explanation_window_training):
        explanation_window_training.setObjectName("explanation_window_training")
        explanation_window_training.resize(600, 500)
        explanation_window_training.setStyleSheet("background-color: rgb(184, 86, 117);")
        self.centralwidget = QtWidgets.QWidget(explanation_window_training)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 130, 241, 81))
        self.label.setStyleSheet("font: 87 20pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
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
        explanation_window_training.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(explanation_window_training)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        explanation_window_training.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(explanation_window_training)
        self.statusbar.setObjectName("statusbar")
        explanation_window_training.setStatusBar(self.statusbar)

        self.retranslateUi(explanation_window_training)
        QtCore.QMetaObject.connectSlotsByName(explanation_window_training)

    def retranslateUi(self, explanation_window_training):
        _translate = QtCore.QCoreApplication.translate
        explanation_window_training.setWindowTitle(_translate("explanation_window_training", "MainWindow"))
        self.label.setText(_translate("explanation_window_training", "TextLabel"))
        self.pushButton.setText(_translate("explanation_window_training", "ЗАПОМНИЛ(А)!"))
