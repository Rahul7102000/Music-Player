import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import pyrebase
from pygame import *
from PyQt5.QtWidgets import *
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.Qt import *
import webbrowser
from tkinter import *
import pygame

class rs(QMainWindow):
    def __init__(self):
        super(rs, self).__init__()
        loadUi("raabta song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play49.clicked.connect(self.playfunction49)
        self.pause49.clicked.connect(self.pausefunction49)
        self.resume49.clicked.connect(self.resumefunction49)

    def playfunction49(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Raabta.mp3")
        pygame.mixer.music.play()

    def pausefunction49(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction49(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = rs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()