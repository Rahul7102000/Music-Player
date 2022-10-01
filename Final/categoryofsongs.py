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

class COS(QMainWindow):
    def __init__(self):
        super(COS, self).__init__()
        loadUi("categoryofsongs.ui", self)
        self.backhomepage.clicked.connect(self.backtohome)
        self.click1.clicked.connect(self.click1function)
        self.click2.clicked.connect(self.click2function)
        self.click3.clicked.connect(self.click3function)
        self.click4.clicked.connect(self.click4function)
        self.click5.clicked.connect(self.click5function)
        self.click6.clicked.connect(self.click6function)
        self.click7.clicked.connect(self.click7function)
        self.click8.clicked.connect(self.click8function)

    def backtohome(self):
        import homepage

    def click1function(self):
        import AmitTrivediSongs

    def click2function(self):
        import ARRahmanSongs

    def click3function(self):
        import ArijitSinghSongs

    def click4function(self):
        import AyushmannKhurannaSongs

    def click5function(self):
        import DivineSongs

    def click6function(self):
        import KSHMRSongs

    def click7function(self):
        import MohitChauhanSongs

    def click8function(self):
        import VishalDadlaniSongs


app = QApplication(sys.argv)
mainwindow = COS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1370)
widget.setFixedHeight(896)
widget.showMaximized()
app.exec_()