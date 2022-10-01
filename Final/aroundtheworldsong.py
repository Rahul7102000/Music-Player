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

class atws(QMainWindow):
    def __init__(self):
        super(atws, self).__init__()
        loadUi("around the world song.ui", self)

        self.ad28.clicked.connect(self.addtoplst28)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play58.clicked.connect(self.playfunction58)
        self.pause58.clicked.connect(self.pausefunction58)
        self.resume58.clicked.connect(self.resumefunction58)

    def playfunction58(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/KSHMR/Around The World.mp3")
        pygame.mixer.music.play()

    def pausefunction58(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction58(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs


    def addtoplst28(self):
        newPath = shutil.copy('../music/KSHMR/Around The World.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

app = QApplication(sys.argv)
mainwindow = atws()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()