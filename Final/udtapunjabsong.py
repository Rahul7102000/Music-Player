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

class ups(QMainWindow):
    def __init__(self):
        super(ups, self).__init__()
        loadUi("udta punjab song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play41.clicked.connect(self.playfunction41)
        self.pause41.clicked.connect(self.pausefunction41)
        self.resume41.clicked.connect(self.resumefunction41)

    def playfunction41(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Ud-Daa Punjab.mp3")
        pygame.mixer.music.play()

    def pausefunction41(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction41(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = ups()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()