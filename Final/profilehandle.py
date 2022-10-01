import sys
import pygame
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.Qt import *
import webbrowser
from tkinter import *
from PyQt5.QtCore import *
import pyrebase





class profile(QMainWindow):
    def __init__(self):
        super(profile, self).__init__()
        loadUi("profile.ui", self)
        self.p1_playlist.clicked.connect(self.p_playlist)

        self.mp2.clicked.connect(self.m2player)
        self.terms.clicked.connect(self.openterms)
        self.backtomain4.clicked.connect(self.backtomainp4)
        self.logout2.clicked.connect(self.plogout)
        self.browseimg.clicked.connect(self.photohandler)

        self.profilepic = QLabel(self)
        self.profilepic.move(10, 50)



    # noinspection PyArgumentList
    @pyqtSlot()
    def photohandler(self):
        print('PyQt5 button click')
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        self.ppic.setPixmap(pixmap)

        self.ppic.adjustSize()  # <---

        # print(ocr.resimden_yaziya(imagePath))
        print(imagePath)

    def p_playlist(self):
        sys.path.append('../Final/playlist.py')
        import playlist

    def setpic(self):
        print("pic uploaded")

    def m2player(self):
        sys.path.append('../Final/Mplayer.py')
        import Mplayer

    def backtomainp4(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def openterms(self):
        webbrowser.open("../Final//Terms&Condition.html")

    def plogout(self):
        sys.path.append('../Final/main.py')
        import main


app = QApplication(sys.argv)
playlistwindow = profile()
widget = QtWidgets.QStackedWidget()
widget.addWidget(playlistwindow)
widget.setFixedWidth(631)
widget.setFixedHeight(501)
widget.show()
app.exec_()
