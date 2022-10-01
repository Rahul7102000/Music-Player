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

class vcs(QMainWindow):
    def __init__(self):
        super(vcs, self).__init__()
        loadUi("vaathi coming song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play68.clicked.connect(self.playfunction68)
        self.pause68.clicked.connect(self.pausefunction68)
        self.resume68.clicked.connect(self.resumefunction68)

    def playfunction68(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vaathi Coming.mp3")
        pygame.mixer.music.play()

    def pausefunction68(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction68(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = vcs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()