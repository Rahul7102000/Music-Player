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

class AKS(QMainWindow):
    def __init__(self):
        super(AKS, self).__init__()
        loadUi("Ayushmann Khuranna Songs.ui", self)

        self.ad29.clicked.connect(self.addtoplst29)
        self.ad30.clicked.connect(self.addtoplst30)
        self.ad31.clicked.connect(self.addtoplst31)
        self.ad32.clicked.connect(self.addtoplst32)


        # BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play23.clicked.connect(self.playfunction23)
        self.pause23.clicked.connect(self.pausefunction23)
        self.resume23.clicked.connect(self.resumefunction23)

        # song 2
        self.play24.clicked.connect(self.playfunction24)
        self.pause24.clicked.connect(self.pausefunction24)
        self.resume24.clicked.connect(self.resumefunction24)

        # song 3
        self.play25.clicked.connect(self.playfunction25)
        self.pause25.clicked.connect(self.pausefunction25)
        self.resume25.clicked.connect(self.resumefunction25)

        # song 4
        self.play26.clicked.connect(self.playfunction26)
        self.pause26.clicked.connect(self.pausefunction26)
        self.resume26.clicked.connect(self.resumefunction26)

    # song 1

    def playfunction23(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Ayushmann Khuranna/Mitti Di Khushboo.mp3")
        pygame.mixer.music.play()

    def pausefunction23(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction23(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 2

    def playfunction24(self):

        pygame.mixer.init()
        pygame.mixer.music.load("../music/Ayushmann Khuranna/Yahin Hoon Main.mp3")
        pygame.mixer.music.play()

    def pausefunction24(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction24(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 3
    def playfunction25(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Ayushmann Khuranna/Saadi Galli Aaja.mp3")
        pygame.mixer.music.play()

    def pausefunction25(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction25(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 4

    def playfunction26(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Ayushmann Khuranna/Pani Da Rang.mp3")
        pygame.mixer.music.play()

    def pausefunction26(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction26(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    #BackButtonsFunction

    def backhomepagefunction(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('../Final/categoryofsongs.py')
        import categoryofsongs


    def addtoplst29(self):
        newPath = shutil.copy('../music/Ayushmann Khuranna/Mitti Di Khushboo.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst30(self):
        newPath = shutil.copy('../music/Ayushmann Khuranna/Yahin Hoon Main.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)


    def addtoplst31(self):
        newPath = shutil.copy('../music/Ayushmann Khuranna/Saadi Galli Aaja.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

    def addtoplst32(self):
        newPath = shutil.copy('../music/Ayushmann Khuranna/Pani Da Rang.mp3',
                              r'../Playlist')
        print("Path of copied file : ", newPath)

app = QApplication(sys.argv)
mainwindow = AKS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()