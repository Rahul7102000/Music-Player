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

class KSHMRS(QMainWindow):
    def __init__(self):
        super(KSHMRS, self).__init__()
        loadUi("KSHMR Songs.ui", self)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play30.clicked.connect(self.playfunction30)
        self.pause30.clicked.connect(self.pausefunction30)
        self.resume30.clicked.connect(self.resumefunction30)

        # song 2
        self.play31.clicked.connect(self.playfunction31)
        self.pause31.clicked.connect(self.pausefunction31)
        self.resume31.clicked.connect(self.resumefunction31)

        #song 1

    def playfunction30(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/KSHMR/Bombay Dreams.mp3")
        pygame.mixer.music.play()

    def pausefunction30(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction30(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 2

    def playfunction31(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/KSHMR/Around The World.mp3")
        pygame.mixer.music.play()

    def pausefunction31(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction31(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    #BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = KSHMRS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()