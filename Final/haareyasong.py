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

class hs(QMainWindow):
    def __init__(self):
        super(hs, self).__init__()
        loadUi("haareya song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play46.clicked.connect(self.playfunction46)
        self.pause46.clicked.connect(self.pausefunction46)
        self.resume46.clicked.connect(self.resumefunction46)

    def playfunction46(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Haareya.mp3")
        pygame.mixer.music.play()

    def pausefunction46(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction46(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../music/Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = hs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()