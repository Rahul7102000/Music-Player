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

class ARS(QMainWindow):
    def __init__(self):
        super(ARS, self).__init__()
        loadUi("main.ui", self)
        self.play_PB.clicked.connect(lambda: self.videoPlayer.play())
        self.pause_PB.clicked.connect(lambda: self.videoPlayer.pause())
        self.stop_PB.clicked.connect(lambda: self.videoPlayer.stop())
        self.actionOpen.triggered.connect(self.select_video)

    def select_video(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select Video')
        self.load_video(filepath)

    def load_video(self, filepath):
        media = phonon.Phonon.MediaSource(filepath)
        self.videoPlayer.load(media)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        self.videoPlayer.play()


app = QApplication(sys.argv)
mainwindow = ARS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.showMaximized()
app.exec_()