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

class ATS(QMainWindow):
    def __init__(self):
        super(ATS, self).__init__()
        loadUi("Amit Trivedi Songs.ui", self)

        self.ad15.clicked.connect(self.addtoplst15)
        self.ad16.clicked.connect(self.addtoplst16)
        self.ad17.clicked.connect(self.addtoplst17)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play11.clicked.connect(self.playfunction11)
        self.pause11.clicked.connect(self.pausefunction11)
        self.resume11.clicked.connect(self.resumefunction11)

        # song 2
        self.play12.clicked.connect(self.playfunction12)
        self.pause12.clicked.connect(self.pausefunction12)
        self.resume12.clicked.connect(self.resumefunction12)

        # song 3
        self.play13.clicked.connect(self.playfunction13)
        self.pause13.clicked.connect(self.pausefunction13)
        self.resume13.clicked.connect(self.resumefunction13)

        # song 1

    def playfunction11(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Namo-Namo.mp3")
        pygame.mixer.music.play()

    def pausefunction11(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction11(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 2

    def playfunction12(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Ud-Daa Punjab.mp3")
        pygame.mixer.music.play()

    def pausefunction12(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction12(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 3

    def playfunction13(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Naina Da Kya Kasoor.mp3")
        pygame.mixer.music.play()

    def pausefunction13(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction13(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

    def addtoplst15(self):
        newPath = shutil.copy('../music/Amit Trivedi/Namo-Namo.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst16(self):
        newPath = shutil.copy('../music/Amit Trivedi/Ud-Daa Punjab.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst17(self):
        newPath = shutil.copy('../music/Amit Trivedi/Naina Da Kya Kasoor.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)


app = QApplication(sys.argv)
mainwindow = ATS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()
