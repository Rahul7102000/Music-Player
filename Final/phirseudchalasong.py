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

class psucs(QMainWindow):
    def __init__(self):
        super(psucs, self).__init__()
        loadUi("phir se ud chala song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play45.clicked.connect(self.playfunction45)
        self.pause45.clicked.connect(self.pausefunction45)
        self.resume45.clicked.connect(self.resumefunction45)

    def playfunction45(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\igthe\\Desktop\\Mp1\\music\\AR Rahman\\Phir-Se-Ud-Chala.mp3")
        pygame.mixer.music.play()

    def pausefunction45(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction45(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('../music/\homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../music/categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = psucs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()