# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_groupgame_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result_groupgame_window(object):
    def setupUi(self, result_groupgame_window):
        result_groupgame_window.setObjectName("result_groupgame_window")
        result_groupgame_window.resize(600, 500)
        result_groupgame_window.setStyleSheet("background-color: rgb(81, 126, 184);")
        self.centralwidget = QtWidgets.QWidget(result_groupgame_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(405, 406, 151, 41))
        self.pushButton.setStyleSheet("font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(184, 86, 117);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 501, 171))
        self.label.setStyleSheet("font: 87 10pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 391, 41))
        self.label_2.setStyleSheet("font: 87 9pt \"Segoe UI Black\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 300, 401, 41))
        self.label_3.setStyleSheet("font: 87 9pt \"Segoe UI Black\";")
        self.label_3.setObjectName("label_3")
        result_groupgame_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(result_groupgame_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        result_groupgame_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(result_groupgame_window)
        self.statusbar.setObjectName("statusbar")
        result_groupgame_window.setStatusBar(self.statusbar)

        self.retranslateUi(result_groupgame_window)
        QtCore.QMetaObject.connectSlotsByName(result_groupgame_window)

    def retranslateUi(self, result_groupgame_window):
        _translate = QtCore.QCoreApplication.translate
        result_groupgame_window.setWindowTitle(_translate("result_groupgame_window", "MainWindow"))
        self.pushButton.setText(_translate("result_groupgame_window", "Хорошо!"))
        self.label.setText(_translate("result_groupgame_window", "TextLabel"))
        self.label_2.setText(_translate("result_groupgame_window", "TextLabel"))
        self.label_3.setText(_translate("result_groupgame_window", "TextLabel"))
