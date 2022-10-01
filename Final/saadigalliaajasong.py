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

class sgas(QMainWindow):
    def __init__(self):
        super(sgas, self).__init__()
        loadUi("saadi galli aaja song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play53.clicked.connect(self.playfunction53)
        self.pause53.clicked.connect(self.pausefunction53)
        self.resume53.clicked.connect(self.resumefunction53)

    def playfunction53(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Ayushmann Khuranna/Saadi Galli Aaja.mp3")
        pygame.mixer.music.play()

    def pausefunction53(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction53(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = sgas()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()