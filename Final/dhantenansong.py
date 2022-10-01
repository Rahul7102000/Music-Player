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

class dtns(QMainWindow):
    def __init__(self):
        super(dtns, self).__init__()
        loadUi("dhan te nan song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play64.clicked.connect(self.playfunction64)
        self.pause64.clicked.connect(self.pausefunction64)
        self.resume64.clicked.connect(self.resumefunction64)

    def playfunction64(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vishal Dadlani/dhan te nan.mp3")
        pygame.mixer.music.play()

    def pausefunction64(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction64(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = dtns()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()