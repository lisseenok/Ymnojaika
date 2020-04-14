# coding: utf8

import sys
from random import randint, shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt, QMimeData, QPoint
from main_window import Ui_MainWindow
from training_window import Ui_TrainingWindow
from game_window import Ui_GameWindow
from group_game_window import Ui_group_game_window
from explanation_window import Ui_explanation_window
from fine_window import Ui_fine_window
from explanation_window_training import Ui_explanation_window_training
from fine_window_training import Ui_fine_window_training
from multiplication_table import Ui_multiplication_table
from rules_group_game import Ui_rules_group_game
from errors_window import Ui_errors_window
from group_game_window_RUN import Ui_Group_GameWindow_RUN
from result_groupgame_window import Ui_result_groupgame_window
from learning_window import Ui_LearningWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()   
        
        #flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        #self.setWindowFlags(flags)          
    
    def initUI(self):       
        self.setWindowTitle('УМНОЖАЙКА')
        self.setFixedSize(1200, 800)
        self.load_image('1.png', 200, 150, 300, 361)
        self.load_image('2.png', 500, 200, 600, 200)
        self.load_image('3.png', 500, 300, 600, 50)        
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)     


class Multiplication_table(QMainWindow, Ui_multiplication_table):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
    
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
          
    def initUI(self):
        self.setAcceptDrops(True)
        
        self.load_image('таблица.jpg', 30, 30, 600, 411)
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
 
 
class LearningWindow(QMainWindow, Ui_LearningWindow):
    def __init__(self):
        super(LearningWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setAcceptDrops(True)
        self.setFixedSize(1200, 800)        
        self.setWindowTitle('РЕЖИМ ИЗУЧЕНИЯ')
        
        self.load_image('23.png', 130, 20, 460, 100)
        #self.load_image('14.png', 30,     500, 200, 269)
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)    
    
    
class TrainingWindow(QMainWindow, Ui_TrainingWindow):
    def __init__(self):
        super(TrainingWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
          
    def initUI(self):
        self.setAcceptDrops(True)
        self.setFixedSize(1200, 800)        
        self.setWindowTitle('РЕЖИМ ТРЕНИРОВКИ')
        
        self.load_image('6.png', 1000, 20, 200, 200)
        self.load_image('14.png', 30, 500, 200, 269)
    
    def set_ex(self):
        self.num1 = randint(2, 9)
        self.num2 = randint(2, 9)
        self.answer = self.num1 * self.num2        
        self.label.setText('    {}     *     {}     ='.format(self.num1, self.num2))        
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)

    
class ExplanationWindow_training(QMainWindow, Ui_explanation_window_training):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        
        
    def initUI(self):
        self.setWindowTitle('ОКНО ПОЯСНЕНИЯ')
        self.load_image('7.png', 190, 50, 200, 50)
        self.load_image('19.png', 10, 150, 300, 300)
    
    def set_text(self, text1, text2, text3, object_):
        object_.setText('{} * {} = {}'.format(text1, text2, text3))
             
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)


class FineWindow_training(QMainWindow, Ui_fine_window_training):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        
        
    def initUI(self):       
        self.setWindowTitle('МОЛОДЕЦ!')
        self.load_image('8.png', 180, 10, 200, 50) 
        self.load_image('9.png', 130, 100, 286, 350)
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
    

class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setAcceptDrops(True)
        self.setFixedSize(1200, 800)        
        self.setWindowTitle('РЕЖИМ ИГРЫ')
    
        self.load_image('6.png', 1000, 20, 200, 200)
        
        self.random_choice()
        
        self.ans_buttons = []
        x, y = 750, 100
        for i in range(5):
            button = Button(str(self.answers[i]), self)
            button.setStyleSheet("border-style: outset; \n"
    "border-width: 1px; \n"
    "border-radius: 7px; \n"
    "border-color: black; \n"
    "background-color: rgb(130, 130, 195); \n"
    "font: 87 10pt 'Segoe UI Black'; \n"
    "padding: 4px; ")            
            y += 100
            button.move(x, y)
            self.ans_buttons.append(button)

        self.buttons = [button]
        
        self.pushButton_1.setText('{} * {}'.format(self.factors_1[0], self.factors_2[0]))
        self.pushButton_2.setText('{} * {}'.format(self.factors_1[1], self.factors_2[1]))
        self.pushButton_3.setText('{} * {}'.format(self.factors_1[2], self.factors_2[2]))
        self.pushButton_4.setText('{} * {}'.format(self.factors_1[3], self.factors_2[3]))
        self.pushButton_5.setText('{} * {}'.format(self.factors_1[4], self.factors_2[4]))
    
    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        mime = e.mimeData().text()
        x, y = map(int, mime.split(','))

        if e.keyboardModifiers() & Qt.ShiftModifier:
            button = Button('Button', self)
            button.move(e.pos()-QPoint(x, y))
            button.show()
            self.buttons.append(button)
            e.setDropAction(Qt.CopyAction)
        else:
            e.source().move(e.pos()-QPoint(x, y))
            e.setDropAction(Qt.MoveAction)
        e.accept()
                       
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
    
    def random_choice(self):
        k = 0
        self.factors_1 = []
        while len(self.factors_1) < 5:
            k = randint(2, 9)
            if k not in self.factors_1:
                self.factors_1.append(k) 
                
        k = 0       
        self.factors_2 = []
        while len(self.factors_2) < 5:
            k = randint(2, 9)
            if k not in self.factors_2 or k not in self.factors_1:
                self.factors_2.append(k)
                
        self.ans = [self.factors_1[i] * self.factors_2[i] for i in range(5)]
        self.answers = self.ans[::]        
        shuffle(self.answers)
        
        self.check_ = [self.answers.index(self.ans[i]) + 1 for i in range(5)] 
        check_2 = [i for i in [1, 2, 3, 4, 5] if i not in self.check_]
        for i in range(4, -1, -1):
            if self.check_.count(self.check_[i]) > 1:
                self.check_[i] = check_2[0]
                
            
        coords = [[140, 200], [260, 330], [380, 440], [500, 560], [620, 680]]
        self.coords_y = []
        for i in range(1, 6):
            self.coords_y.append(coords[self.check_.index(i)])

    
    def check(self):
        self.result = []
        self.errors = []
        self.resolution_ = [1 for i in range(5) if 400 <= self.ans_buttons[i].x() <= 550 and 140 <= self.ans_buttons[i].y() <= 680]

        if (400 <= self.ans_buttons[0].x() <= 550) and (self.coords_y[0][0] <= self.ans_buttons[0].y() <= self.coords_y[0][1]):
            self.result.append(1)
        else:
            self.errors.append([self.factors_1[0], self.factors_2[0], self.ans[0]])
            
        if (400 <= self.ans_buttons[1].x() <= 550) and (self.coords_y[1][0] <= self.ans_buttons[1].y() <= self.coords_y[1][1]):
            self.result.append(2) 
        else:
            self.errors.append([self.factors_1[1], self.factors_2[1], self.ans[1]])
        
        if (400 <= self.ans_buttons[2].x() <= 550) and (self.coords_y[2][0] <= self.ans_buttons[2].y() <= self.coords_y[2][1]):
            self.result.append(3)
        else:
            self.errors.append([self.factors_1[2], self.factors_2[2], self.ans[2]])
        
        if (400 <= self.ans_buttons[3].x() <= 550) and (self.coords_y[3][0] <= self.ans_buttons[3].y() <= self.coords_y[3][1]):
            self.result.append(4)
        else:
            self.errors.append([self.factors_1[3], self.factors_2[3], self.ans[3]])
        
        if (400 <= self.ans_buttons[4].x() <= 550) and (self.coords_y[4][0] <= self.ans_buttons[4].y() <= self.coords_y[4][1]):
            self.result.append(5)
        else:
            self.errors.append([self.factors_1[4], self.factors_2[4], self.ans[4]])  
            
        return len(self.result)
    

class ExplanationWindow(QMainWindow, Ui_explanation_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
             
    def initUI(self):
        self.setWindowTitle('ОКНО ПОЯСНЕНИЯ')
        self.load_image('7.png', 190, 150, 200, 50)
        self.load_image('10.png', 150, 10, 300, 80)
    
    def set_text(self, list_text, list_objects):
        if list_text != []:
            for i in range(len(list_text)):
                list_objects[i].setText('{} * {} = {}'.format(list_text[i][0], list_text[i][1], list_text[i][2]))
            
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
        
     
class FineWindow(QMainWindow, Ui_fine_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        
        
    def initUI(self):       
        self.setWindowTitle('МОЛОДЕЦ!')
        self.load_image('8.png', 80, 10, 400, 50) 
        self.load_image('9.png', 150, 70, 286, 350)
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
    

class GroupGameWindow(QMainWindow, Ui_group_game_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.load_image('17.png', 880, 442, 300, 238)
        

    def initUI(self):       
        self.setFixedSize(1200, 800)        
        self.setWindowTitle('РЕЖИМ КОМАНДНОЙ ИГРЫ')
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)

class GroupGameWindow_RUN(QMainWindow, Ui_Group_GameWindow_RUN):
    
    def __init__(self):
        super(GroupGameWindow_RUN, self).__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setAcceptDrops(True)
        self.setFixedSize(1200, 800)        
        self.setWindowTitle('РЕЖИМ КОМАНДНОЙ ИГРЫ')
    
        self.load_image('6.png', 1000, 20, 200, 200)
        
        self.random_choice()
        
        self.ans_buttons = []
        x, y = 750, 100
        for i in range(5):
            button = Button(str(self.answers[i]), self)
            button.setStyleSheet("border-style: outset; \n"
    "border-width: 1px; \n"
    "border-radius: 7px; \n"
    "border-color: black; \n"
    "background-color: rgb(130, 130, 195); \n"
    "font: 87 10pt 'Segoe UI Black'; \n"
    "padding: 4px; ")            
            y += 100
            button.move(x, y)
            self.ans_buttons.append(button)

        self.buttons = [button]
        
        self.pushButton_1.setText('{} * {}'.format(self.factors_1[0], self.factors_2[0]))
        self.pushButton_2.setText('{} * {}'.format(self.factors_1[1], self.factors_2[1]))
        self.pushButton_3.setText('{} * {}'.format(self.factors_1[2], self.factors_2[2]))
        self.pushButton_4.setText('{} * {}'.format(self.factors_1[3], self.factors_2[3]))
        self.pushButton_5.setText('{} * {}'.format(self.factors_1[4], self.factors_2[4]))
    
    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        mime = e.mimeData().text()
        x, y = map(int, mime.split(','))

        if e.keyboardModifiers() & Qt.ShiftModifier:
            button = Button('Button', self)
            button.move(e.pos()-QPoint(x, y))
            button.show()
            self.buttons.append(button)
            e.setDropAction(Qt.CopyAction)
        else:
            e.source().move(e.pos()-QPoint(x, y))
            e.setDropAction(Qt.MoveAction)
        e.accept()
                       
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
    
     
    def random_choice(self):
        k = 0
        self.factors_1 = []
        while len(self.factors_1) < 5:
            k = randint(2, 9)
            if k not in self.factors_1:
                self.factors_1.append(k) 
                
        k = 0       
        self.factors_2 = []
        while len(self.factors_2) < 5:
            k = randint(2, 9)
            if k not in self.factors_2 or k not in self.factors_1:
                self.factors_2.append(k)
                
        self.ans = [self.factors_1[i] * self.factors_2[i] for i in range(5)]
        self.answers = self.ans[::]        
        shuffle(self.answers)
        
        self.check_ = [self.answers.index(self.ans[i]) + 1 for i in range(5)] 
        check_2 = [i for i in [1, 2, 3, 4, 5] if i not in self.check_]
        for i in range(4, -1, -1):
            if self.check_.count(self.check_[i]) > 1:
                self.check_[i] = check_2[0]
                
            
        coords = [[140, 200], [260, 330], [380, 440], [500, 560], [620, 680]]
        self.coords_y = []
        for i in range(1, 6):
            self.coords_y.append(coords[self.check_.index(i)])

    
    def check(self):
        self.result = []
        self.errors = []
        self.resolution_ = [1 for i in range(5) if 400 <= self.ans_buttons[i].x() <= 550 and 140 <= self.ans_buttons[i].y() <= 680]
        if (400 <= self.ans_buttons[0].x() <= 550) and (self.coords_y[0][0] <= self.ans_buttons[0].y() <= self.coords_y[0][1]):
            self.result.append(1)
        else:
            self.errors.append([self.factors_1[0], self.factors_2[0], self.ans[0]])
            
        if (400 <= self.ans_buttons[1].x() <= 550) and (self.coords_y[1][0] <= self.ans_buttons[1].y() <= self.coords_y[1][1]):
            self.result.append(2) 
        else:
            self.errors.append([self.factors_1[1], self.factors_2[1], self.ans[1]])
        
        if (400 <= self.ans_buttons[2].x() <= 550) and (self.coords_y[2][0] <= self.ans_buttons[2].y() <= self.coords_y[2][1]):
            self.result.append(3)
        else:
            self.errors.append([self.factors_1[2], self.factors_2[2], self.ans[2]])
        
        if (400 <= self.ans_buttons[3].x() <= 550) and (self.coords_y[3][0] <= self.ans_buttons[3].y() <= self.coords_y[3][1]):
            self.result.append(4)
        else:
            self.errors.append([self.factors_1[3], self.factors_2[3], self.ans[3]])
        
        if (400 <= self.ans_buttons[4].x() <= 550) and (self.coords_y[4][0] <= self.ans_buttons[4].y() <= self.coords_y[4][1]):
            self.result.append(5)
        else:
            self.errors.append([self.factors_1[4], self.factors_2[4], self.ans[4]])  
        return len(self.result)
    
class Errors_window(QMainWindow, Ui_errors_window):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        

        
class Rules_group_game(QMainWindow, Ui_rules_group_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        
        
    def initUI(self):   
        self.load_image('15.png', 80, 140, 231, 250) 

    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)
        
class Result_groupgame_window(QMainWindow, Ui_result_groupgame_window): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        flags = self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)        
        
    def initUI(self):       
        self.load_image('20.png', 400, 200, 200, 200) 
    
    def load_image(self, file_name, x, y, w, h):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(file_name)
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        lbl.setGeometry(x, y, w, h)

        
class Button(QPushButton):
    
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        mimeData.setText('%d,%d' % (e.x(), e.y()))

        pixmap = QWidget.grab(self)

        painter = QPainter(pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 127))
        painter.end()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(e.pos())

        if drag.exec_(Qt.CopyAction | Qt.MoveAction) == Qt.MoveAction:
            pass
        else:
            pass
    
        
class InvisibleWindow(QMainWindow):
    def __init__(self):
        super(InvisibleWindow, self).__init__()
    
    def show_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.pushbutton_training.clicked.connect(self.show_trainingwindow)
        self.mainwindow.pushbutton_training.clicked.connect(self.mainwindow.close)
        self.mainwindow.pushbutton_game.clicked.connect(self.show_gamewindow)
        self.mainwindow.pushbutton_game.clicked.connect(self.mainwindow.close)
        self.mainwindow.pushbutton_group_game.clicked.connect(self.show_group_gamewindow)
        self.mainwindow.pushbutton_group_game.clicked.connect(self.mainwindow.close)
        self.mainwindow.pushButton.clicked.connect(self.show_multiplication_table)
        self.mainwindow.pushbutton_learning.clicked.connect(self.show_learningwindow)
        self.mainwindow.pushbutton_learning.clicked.connect(self.mainwindow.close)
        #self.mainwindow.pushButton_2.clicked.connect(self.mainwindow.close)
        #self.mainwindow.pushButton_3.clicked.connect(self.full_screen)
        self.mainwindow.show()
    
    #def full_screen(self):
        #if self.mainwindow.frameGeometry().width() == 1200 and self.mainwindow.frameGeometry().height() == 800:
            #self.mainwindow.showFullScreen()
        #else:
            #self.mainwindow.setGeometry(0, 0, 1200, 800)
            #self.mainwindow.frameGeometry().width() = 1200
            #self.mainwindow.frameGeometry().height() = 800
            #self.mainwindow.showMinimized()
            
            
    def show_multiplication_table(self):
        self.multiplication_table = Multiplication_table()
        self.multiplication_table.pushButton.clicked.connect(self.multiplication_table.close)
        self.multiplication_table.show()
    
    def show_learningwindow(self):
        self.learningwindow = LearningWindow()
        self.learningwindow.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.learningwindow.pushbutton_menu.clicked.connect(self.learningwindow.close)        
        self.learningwindow.show()
        
    def show_trainingwindow(self):
        self.trainingwindow = TrainingWindow()
        self.trainingwindow.set_ex()
        self.trainingwindow.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.trainingwindow.pushbutton_menu.clicked.connect(self.trainingwindow.close)
        self.trainingwindow.lineEdit.returnPressed.connect(self.enter)
        self.right_ans = 0
        self.trainingwindow.pushButton.clicked.connect(self.show_finewindow_training)
        self.trainingwindow.show()
    
    def enter(self):
        if self.trainingwindow.lineEdit.text().isdigit():
            if int(self.trainingwindow.lineEdit.text()) == self.trainingwindow.num1 * self.trainingwindow.num2:
                self.right_ans += 1
                self.trainingwindow.set_ex()
                self.trainingwindow.lineEdit.clear()
            else:
                self.show_explanationwindow_training()
        else:
            self.show_errors_window('Пожалуйста, введи численный ответ\nбез пробелов.')
            self.trainingwindow.lineEdit.clear()
                        
            
    def show_finewindow_training(self):
        self.finewindow_training = FineWindow_training()
        self.finewindow_training.pushButton.clicked.connect(self.finewindow_training.close)
        self.finewindow_training.pushButton.clicked.connect(self.show_mainwindow)
        self.finewindow_training.pushButton.clicked.connect(self.trainingwindow.close)
        self.finewindow_training.label.setText('Правильных ответов: {}'.format(self.right_ans))
        #print(self.right_ans)
        self.finewindow_training.show()     
            
    def show_explanationwindow_training(self):
        self.explanationwindow_training = ExplanationWindow_training()
        self.explanationwindow_training.pushButton.clicked.connect(self.explanationwindow_training.close)       
        self.explanationwindow_training.set_text(self.trainingwindow.num1, self.trainingwindow.num2, self.trainingwindow.answer, self.explanationwindow_training.label)
        #self.trainingwindow.set_ex()
        self.trainingwindow.lineEdit.clear()         
        self.explanationwindow_training.show()        

                
    def show_gamewindow(self):
        self.gamewindow = GameWindow()
        self.gamewindow.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.gamewindow.pushbutton_menu.clicked.connect(self.gamewindow.close) 
        self.gamewindow.pushButton.clicked.connect(self.button_clicked)
        self.gamewindow.show()
    
    def button_clicked(self):
        self.gamewindow.check()
        if self.gamewindow.check() == 5:
            if len(self.gamewindow.resolution_) == 5:
                self.show_finewindow()
        else:
            if len(self.gamewindow.resolution_) == 5:
                self.show_explanationwindow()
    
    def show_explanationwindow(self):
        self.explanationwindow = ExplanationWindow()
        self.explanationwindow.pushButton.clicked.connect(self.explanationwindow.close)
        self.explanationwindow.pushButton.clicked.connect(self.show_gamewindow)
        self.explanationwindow.set_text(self.gamewindow.errors, self.explanationwindow.labels)
        self.explanationwindow.label_6.setText('{} из 5'.format(self.gamewindow.check()))
        self.explanationwindow.show()
    
    def show_finewindow(self):
        self.finewindow = FineWindow()
        self.finewindow.pushButton.clicked.connect(self.finewindow.close)
        self.finewindow.pushButton.clicked.connect(self.show_gamewindow)
        self.finewindow.show() 
    
    def show_group_gamewindow(self):
        self.group_gamewindow = GroupGameWindow()
        self.group_gamewindow.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.group_gamewindow.pushbutton_menu.clicked.connect(self.group_gamewindow.close)  
        self.group_gamewindow.pushButton.clicked.connect(self.show_rules_group_game)
        self.group_gamewindow.pushButton_2.clicked.connect(self.check_group_gamewindow)
        self.group_gamewindow.show() 
    
    def check_group_gamewindow(self):
        if self.group_gamewindow.lineEdit.text() == '' and self.group_gamewindow.lineEdit_2.text() == '':
            self.show_errors_window('Пожалуйста, введите названия команд.')
        elif self.group_gamewindow.lineEdit.text() == '' or self.group_gamewindow.lineEdit_2.text() == '':
            self.show_errors_window('Пожалуйста, введите названия обеих команд.')
        elif self.group_gamewindow.lineEdit.text() == self.group_gamewindow.lineEdit_2.text():
            self.show_errors_window('Пожалуйста, введите различные \nназвания команд.')
        else:
            self.name1 = self.group_gamewindow.lineEdit.text()
            self.name2 = self.group_gamewindow.lineEdit_2.text()            
            self.group_gamewindow.close()
            self.show_group_gamewindow_RUN1()
            
    def show_group_gamewindow_RUN1(self):
        self.group_gamewindow_RUN1 = GroupGameWindow_RUN()
        self.group_gamewindow_RUN1.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.group_gamewindow_RUN1.pushbutton_menu.clicked.connect(self.group_gamewindow_RUN1.close) 
        self.group_gamewindow_RUN1.label.setText('Задания для команды {}:'.format(self.name1.capitalize()))
        self.group_gamewindow_RUN1.pushButton.clicked.connect(self.button_clicked_groupgame1)
        self.group_gamewindow_RUN1.show()  
    
    def button_clicked_groupgame1(self):   
        self.group_gamewindow_RUN1.check()
        if len(self.group_gamewindow_RUN1.resolution_) == 5:
            self.res1 = self.group_gamewindow_RUN1.check()
            self.show_next_window('{}, вы выполнили свои задания. \nТеперь очередь команды {}.'.format(self.name1.capitalize(), self.name2.capitalize()))
    
    def show_next(self):
        self.next_window.close()
        self.group_gamewindow_RUN1.close()
        self.show_group_gamewindow_RUN2()
        
        
    def show_next_window(self, text):
        self.next_window = Errors_window()
        self.next_window.pushButton.clicked.connect(self.show_next)
        self.next_window.label.setText(text)
        self.next_window.show()                
    
    def show_group_gamewindow_RUN2(self):
        self.group_gamewindow_RUN2 = GroupGameWindow_RUN()
        self.group_gamewindow_RUN2.pushbutton_menu.clicked.connect(self.show_mainwindow)
        self.group_gamewindow_RUN2.pushbutton_menu.clicked.connect(self.group_gamewindow_RUN2.close) 
        self.group_gamewindow_RUN2.label.setText('Задания для команды {}:'.format(self.name2.capitalize()))
        self.group_gamewindow_RUN2.pushButton.clicked.connect(self.button_clicked_groupgame2)
        self.group_gamewindow_RUN2.show()  
    
    def button_clicked_groupgame2(self):   
        self.group_gamewindow_RUN2.check()
        if len(self.group_gamewindow_RUN2.resolution_) == 5:
            self.res2 = self.group_gamewindow_RUN2.check()
            self.show_result_groupgame_window()
    
    def restart(self):
        self.result_groupgame_window.close()
        self.group_gamewindow_RUN2.close()
        self.show_mainwindow()
        
    def show_result_groupgame_window(self):
        self.result_groupgame_window = Result_groupgame_window()
        self.result_groupgame_window.pushButton.clicked.connect(self.restart)
        if self.res1 > self.res2:
            self.result_groupgame_window.label.setText('Поздравляем! \nПобедила команда {}!\n{}, не расстраивайтесь! \nЕщё немного тренировок и всё получится!'.format(self.name1, self.name2))
        elif self.res1 < self.res2:
            self.result_groupgame_window.label.setText('Поздравляем! \nПобедила команда {}!\n{}, не расстраивайтесь! \nЕщё немного тренировок и всё получится!'.format(self.name2, self.name1))
        elif self.res1 == self.res2:
            self.result_groupgame_window.label.setText('Ничья! Победила дружба!')
        
        self.result_groupgame_window.label_2.setText('Результат команды {}: {}'.format(self.name1, self.res1)) 
        self.result_groupgame_window.label_3.setText('Результат команды {}: {}'.format(self.name2, self.res2))

        self.result_groupgame_window.show()
        
    def show_errors_window(self, text):
        self.errors_window = Errors_window()
        self.errors_window.pushButton.clicked.connect(self.errors_window.close)
        self.errors_window.label.setText(text)
        self.errors_window.show()
        
    def show_rules_group_game(self):
        self.rules_group_game = Rules_group_game()
        self.rules_group_game.pushButton.clicked.connect(self.rules_group_game.close)
        self.rules_group_game.show()         
    
    
    
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InvisibleWindow()
    ex.show_mainwindow()
    sys.exit(app.exec())