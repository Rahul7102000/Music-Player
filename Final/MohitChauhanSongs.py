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

class MCS(QMainWindow):
    def __init__(self):
        super(MCS, self).__init__()
        loadUi("Mohit Chauhan Songs.ui", self)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play32.clicked.connect(self.playfunction32)
        self.pause32.clicked.connect(self.pausefunction32)
        self.resume32.clicked.connect(self.resumefunction32)

        # song 2
        self.play33.clicked.connect(self.playfunction33)
        self.pause33.clicked.connect(self.pausefunction33)
        self.resume33.clicked.connect(self.resumefunction33)

        # song 3
        self.play34.clicked.connect(self.playfunction34)
        self.pause34.clicked.connect(self.pausefunction34)
        self.resume34.clicked.connect(self.resumefunction34)

    # song 1

    def playfunction32(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../Final/Mohit Chauhan/Matargashti.mp3")
        pygame.mixer.music.play()

    def pausefunction32(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction32(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 2

    def playfunction33(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../Final/Mohit Chauhan/Saadda Haq.mp3")
        pygame.mixer.music.play()

    def pausefunction33(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction33(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 3

    def playfunction34(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../Final/Mohit Chauhan/Phir-Se-Ud-Chala.mp3")
        pygame.mixer.music.play()

    def pausefunction34(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction34(self):
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
mainwindow = MCS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()