# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learning_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LearningWindow(object):
    def setupUi(self, LearningWindow):
        LearningWindow.setObjectName("LearningWindow")
        LearningWindow.resize(1200, 800)
        LearningWindow.setStyleSheet("background-color: rgb(205, 213, 255);")
        self.centralwidget = QtWidgets.QWidget(LearningWindow)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 160, 91, 91))
        self.pushButton.setStyleSheet("border-style: outset; \n"
"background-color: rgb(96, 138, 228);\n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 310, 91, 91))
        self.pushButton_2.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 460, 91, 91))
        self.pushButton_9.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 610, 91, 91))
        self.pushButton_10.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 160, 91, 91))
        self.pushButton_3.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 310, 91, 91))
        self.pushButton_4.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 460, 91, 91))
        self.pushButton_5.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 610, 91, 91))
        self.pushButton_6.setStyleSheet("border-style: outset; \n"
"border-width: 1px; \n"
"border-radius: 7px; \n"
"border-color: black; \n"
"padding: 4px; \n"
"background-color: rgb(96, 138, 228);\n"
"font: 87 16pt \'Segoe UI Grey\'; \\n ")
        self.pushButton_6.setObjectName("pushButton_6")
        LearningWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LearningWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        LearningWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LearningWindow)
        self.statusbar.setObjectName("statusbar")
        LearningWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LearningWindow)
        QtCore.QMetaObject.connectSlotsByName(LearningWindow)

    def retranslateUi(self, LearningWindow):
        _translate = QtCore.QCoreApplication.translate
        LearningWindow.setWindowTitle(_translate("LearningWindow", "MainWindow"))
        self.pushButton.setText(_translate("LearningWindow", "2"))
        self.pushButton_2.setText(_translate("LearningWindow", "3"))
        self.pushButton_9.setText(_translate("LearningWindow", "4"))
        self.pushButton_10.setText(_translate("LearningWindow", "5"))
        self.pushButton_3.setText(_translate("LearningWindow", "6"))
        self.pushButton_4.setText(_translate("LearningWindow", "7"))
        self.pushButton_5.setText(_translate("LearningWindow", "8"))
        self.pushButton_6.setText(_translate("LearningWindow", "9"))
