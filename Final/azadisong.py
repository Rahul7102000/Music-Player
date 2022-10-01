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
import shutil


class azs(QMainWindow):
    def __init__(self):
        super(azs, self).__init__()
        loadUi("azadi song.ui", self)

        self.ad33.clicked.connect(self.addtoplst33)
        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play55.clicked.connect(self.playfunction55)
        self.pause55.clicked.connect(self.pausefunction55)
        self.resume55.clicked.connect(self.resumefunction55)

    def addtoplst33(self):

        newPath = shutil.copy('../music/Divine/Azadi.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)

    def playfunction55(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Divine/Azadi.mp3")
        pygame.mixer.music.play()

    def pausefunction55(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction55(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('C../Final/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = azs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()