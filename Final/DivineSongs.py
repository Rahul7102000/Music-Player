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

class DS(QMainWindow):
    def __init__(self):
        super(DS, self).__init__()
        loadUi("Divine Songs.ui", self)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play27.clicked.connect(self.playfunction27)
        self.pause27.clicked.connect(self.pausefunction27)
        self.resume27.clicked.connect(self.resumefunction27)

        # song 2
        self.play28.clicked.connect(self.playfunction28)
        self.pause28.clicked.connect(self.pausefunction28)
        self.resume28.clicked.connect(self.resumefunction28)

        # song 3
        self.play29.clicked.connect(self.playfunction29)
        self.pause29.clicked.connect(self.pausefunction29)
        self.resume29.clicked.connect(self.resumefunction29)

        # song 1

    def playfunction27(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Divine/Sher Aaya Sher.mp3")
        pygame.mixer.music.play()

    def pausefunction27(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction27(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 2

    def playfunction28(self):

        pygame.mixer.init()
        pygame.mixer.music.load("../music/Divine/Azadi.mp3")
        pygame.mixer.music.play()

    def pausefunction28(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction28(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 3

    def playfunction29(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Divine/Mere Gully Mein.mp3")
        pygame.mixer.music.play()

    def pausefunction29(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction29(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    #BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/omepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = DS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()