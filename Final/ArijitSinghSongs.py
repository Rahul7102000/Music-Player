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

class ASS(QMainWindow):
    def __init__(self):
        super(ASS, self).__init__()
        loadUi("Arijit Singh Songs.ui", self)

        self.ad24.clicked.connect(self.addtoplst24)
        self.ad25.clicked.connect(self.addtoplst25)
        self.ad26.clicked.connect(self.addtoplst26)
        self.ad27.clicked.connect(self.addtoplst27)
        self.ad23.clicked.connect(self.addtoplst23)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction1)

        # Song 1
        self.play18.clicked.connect(self.playfunction18)
        self.pause18.clicked.connect(self.pausefunction18)
        self.resume18.clicked.connect(self.resumefunction18)

        # song 2
        self.play19.clicked.connect(self.playfunction19)
        self.pause19.clicked.connect(self.pausefunction19)
        self.resume19.clicked.connect(self.resumefunction19)

        # song 3
        self.play20.clicked.connect(self.playfunction20)
        self.pause20.clicked.connect(self.pausefunction20)
        self.resume20.clicked.connect(self.resumefunction20)

        # song 4
        self.play21.clicked.connect(self.playfunction21)
        self.pause21.clicked.connect(self.pausefunction21)
        self.resume21.clicked.connect(self.resumefunction21)

        # song 5
        self.play22.clicked.connect(self.playfunction22)
        self.pause22.clicked.connect(self.pausefunction22)
        self.resume22.clicked.connect(self.resumefunction22)

        # song 1

    def playfunction18(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Ik Vaari Aa.mp3")
        pygame.mixer.music.play()

    def pausefunction18(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction18(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 2

    def playfunction19(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Ilahi.mp3")
        pygame.mixer.music.play()

    def pausefunction19(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction19(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 3

    def playfunction20(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Raabta.mp3")
        pygame.mixer.music.play()

    def pausefunction20(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction20(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 4

    def playfunction21(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Subah-Subah.mp3")
        pygame.mixer.music.play()

    def pausefunction21(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction21(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 5

    def playfunction22(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Haareya.mp3")
        pygame.mixer.music.play()

    def pausefunction22(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction22(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction1(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs

    def addtoplst23(self):
        newPath = shutil.copy('../music/Arijit Singh/Ik Vaari Aa.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst24(self):
        newPath = shutil.copy('../music/Arijit Singh/Ilahi.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst25(self):
        newPath = shutil.copy('../music/Arijit Singh/Raabta.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst26(self):
        newPath = shutil.copy('../music/Arijit Singh/Subah-Subah.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst27(self):
        newPath = shutil.copy('../music/Arijit Singh/Haareya.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)


app = QApplication(sys.argv)
mainwindow = ASS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()
