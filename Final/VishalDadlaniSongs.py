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

class VDS(QMainWindow):
    def __init__(self):
        super(VDS, self).__init__()
        loadUi("Vishal Dadlani Songs.ui", self)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play35.clicked.connect(self.playfunction35)
        self.pause35.clicked.connect(self.pausefunction35)
        self.resume35.clicked.connect(self.resumefunction35)

        # song 2
        self.play36.clicked.connect(self.playfunction36)
        self.pause36.clicked.connect(self.pausefunction36)
        self.resume36.clicked.connect(self.resumefunction36)

        # song 3
        self.play37.clicked.connect(self.playfunction37)
        self.pause37.clicked.connect(self.pausefunction37)
        self.resume37.clicked.connect(self.resumefunction37)

        # song 4
        self.play38.clicked.connect(self.playfunction38)
        self.pause38.clicked.connect(self.pausefunction38)
        self.resume38.clicked.connect(self.resumefunction38)

# song 1

    def playfunction35(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vishal Dadlani/Balam Pichkari.mp3")
        pygame.mixer.music.play()

    def pausefunction35(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction35(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 2

    def playfunction36(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vishal Dadlani/Bappa.mp3")
        pygame.mixer.music.play()

    def pausefunction36(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction36(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 3

    def playfunction37(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vishal Dadlani/dhan te nan.mp3")
        pygame.mixer.music.play()

    def pausefunction37(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction37(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 4

    def playfunction38(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vishal Dadlani/Ud-Daa Punjab.mp3")
        pygame.mixer.music.play()

    def pausefunction38(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction38(self):
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
mainwindow = VDS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()