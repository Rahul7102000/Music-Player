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


class nns(QMainWindow):
    def __init__(self):
        super(nns, self).__init__()
        loadUi("namo namo song.ui", self)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play40.clicked.connect(self.playfunction40)
        self.pause40.clicked.connect(self.pausefunction40)
        self.resume40.clicked.connect(self.resumefunction40)

    def playfunction40(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Namo-Namo.mp3")
        pygame.mixer.music.play()

    def pausefunction40(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction40(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs


app = QApplication(sys.argv)
mainwindow = nns()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()