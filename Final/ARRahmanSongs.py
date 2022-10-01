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


class ARS(QMainWindow):
    def __init__(self):
        super(ARS, self).__init__()
        loadUi("AR Rahman Songs.ui", self)

        self.ad19.clicked.connect(self.addtoplst19)
        self.ad20.clicked.connect(self.addtoplst20)
        self.ad21.clicked.connect(self.addtoplst21)
        self.ad22.clicked.connect(self.addtoplst22)

        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play14.clicked.connect(self.playfunction14)
        self.pause14.clicked.connect(self.pausefunction14)
        self.resume14.clicked.connect(self.resumefunction14)

        # song 2
        self.play15.clicked.connect(self.playfunction15)
        self.pause15.clicked.connect(self.pausefunction15)
        self.resume15.clicked.connect(self.resumefunction15)

        # song 3
        self.play16.clicked.connect(self.playfunction16)
        self.pause16.clicked.connect(self.pausefunction16)
        self.resume16.clicked.connect(self.resumefunction16)

        # song 4
        self.play17.clicked.connect(self.playfunction17)
        self.pause17.clicked.connect(self.pausefunction17)
        self.resume17.clicked.connect(self.resumefunction17)

        # song 1

    def playfunction14(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/AR Rahman/Kun Faya Kun.mp3")
        pygame.mixer.music.play()

    def pausefunction14(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction14(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 2

    def playfunction15(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/AR Rahman/Phir-Se-Ud-Chala.mp3")
        pygame.mixer.music.play()

    def pausefunction15(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction15(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 3

    def playfunction16(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/AR Rahman/Nadaan Parindey.mp3")
        pygame.mixer.music.play()

    def pausefunction16(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction16(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

        # song 4

    def playfunction17(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/AR Rahman/\Jai Ho.mp3")
        pygame.mixer.music.play()

    def pausefunction17(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction17(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    #BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs




    def addtoplst19(self):
        newPath = shutil.copy('../music/AR Rahman/Kun Faya Kun.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst20(self):
        newPath = shutil.copy('../music/AR Rahman/Phir-Se-Ud-Chala.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)


    def addtoplst21(self):
        newPath = shutil.copy('../music/AR Rahman/Nadaan Parindey.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst22(self):
        newPath = shutil.copy('../music/AR Rahman/Nadaan Parindey.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)


app = QApplication(sys.argv)
mainwindow = ARS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()