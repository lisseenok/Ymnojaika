pyuic5 group_game_window.ui -o group_game_window.py
pyuic5 training_window.ui -o training_window.py
pyuic5 explanation_window.ui -o explanation_window.py
pyuic5 main_window.ui -o main_window.py
pyuic5 fine_window.ui -o fine_window.py
pyuic5 multiplication_table.ui -o multiplication_table.py
pyuic5 game_window.ui -o game_window.py
pyuic5 rules_group_game.ui -o rules_group_game.py
pyuic5 errors_window.ui -o errors_window.py
pyuic5 group_game_window_RUN.ui -o group_game_window_RUN.py
pyuic5 result_groupgame_window.ui -o result_groupgame_window.py
pyuic5 explanation_window_training.ui -o explanation_window_training.py
pyuic5 learning_window.ui -o learning_window.py

self.labels = [self.label, self.label_2, self.label_3, self.label_4, self.label_5]

C:\Users\miair\Documents\проект\коды

self.labels = [self.label, self.label_2, self.label_3, self.label_4, self.label_5]


icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("4.png"))
self.pushbutton_menu.setIcon(icon)
self.pushbutton_menu.setIconSize(QtCore.QSize(35, 35))


icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("21.png"))
self.pushButton_2.setIcon(icon)
self.pushButton_2.setIconSize(QtCore.QSize(25, 25))

icon3 = QtGui.QIcon()
icon3.addPixmap(QtGui.QPixmap("22.png"))
self.pushButton_3.setIcon(icon3)
self.pushButton_3.setIconSize(QtCore.QSize(25, 25))  