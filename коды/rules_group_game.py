# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules_group_game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rules_group_game(object):
    def setupUi(self, rules_group_game):
        rules_group_game.setObjectName("rules_group_game")
        rules_group_game.resize(748, 408)
        rules_group_game.setStyleSheet("background-color: rgb(36, 161, 189);")
        self.centralwidget = QtWidgets.QWidget(rules_group_game)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 330, 201, 41))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"background-color: rgb(53, 117, 173);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px;\n"
"font: 87 10pt \'Segoe UI Black\'; \\n ")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -40, 741, 221))
        self.label.setStyleSheet("font: 87 9pt \'Segoe UI Black\'; \\n ")
        self.label.setObjectName("label")
        rules_group_game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rules_group_game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 18))
        self.menubar.setObjectName("menubar")
        rules_group_game.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rules_group_game)
        self.statusbar.setObjectName("statusbar")
        rules_group_game.setStatusBar(self.statusbar)

        self.retranslateUi(rules_group_game)
        QtCore.QMetaObject.connectSlotsByName(rules_group_game)

    def retranslateUi(self, rules_group_game):
        _translate = QtCore.QCoreApplication.translate
        rules_group_game.setWindowTitle(_translate("rules_group_game", "MainWindow"))
        self.pushButton.setText(_translate("rules_group_game", "Понятно!"))
        self.label.setText(_translate("rules_group_game", "Сперва введите названия двух команд, причем они должны быть различны. \n"
"Далее выполните задания, перетащив ответы к соответствующим примерам. \n"
"После выполнения всех заданий вы увидите результаты командной игры."))
