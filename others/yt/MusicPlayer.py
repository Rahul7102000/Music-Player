import pygame
from pygame import mixer
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel , QToolButton,QListWidget ,QFileDialog
from PyQt5.uic import loadUi

from playsound import playsound

class MusicPlayer(QMainWindow):
    def __init__(self):
        super(MusicPlayer, self).__init__()
        loadUi("MusicPlayer.ui", self)

    def createMenubar(self):
        self.createMenubar()
        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        filemenu.addAction(self.fileOpen())

def playsong():
    loadUi("login.py", self)

def pausesong():
    playsound('C:\\Users\\igthe\\Desktop\\Mp\\music\\pl1.mp3')


def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()


def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()


def ListBox():
    mixer.init()
    songstatus = StringVar()
    songstatus.set("choosing")
    playlist = Listbox(root, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=('arial', 15), width=40)
    playlist.grid(columnspan=5)
    os.chdir(r'C:\Users\igthe\Desktop\Mp\music')
    songs = os.listdir()
    for s in songs:
        assert isinstance(playlist, object)
        playlist.insert(END, s)
def Button():
    mp_play = Button.playsong()
    mp_pause = Button.pausesong()
    mp_stop = Button.stopsong()
    mp_Resume = Button.resumesong()

def fileOpen():
    fileAc = QAction('Open File', self)
    fileAc.setShortcut('Ctrl+O')
    fileAc.setStatusTip('Open File')
    fileAc.triggered.connect(self.openFile)
    return fileAc


app = QApplication(sys.argv)
mainwindow2 = MusicPlayer()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow2)
widget.showMaximized()
widget.show()
app.exec_()
