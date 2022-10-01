import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUi
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.Qt import *
import webbrowser
import pygame
from pygame import *
import speech_recognition as sr
import pywhatkit as kit
import shutil


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("Main.ui", self)

        self.searchbutton.clicked.connect(self.searchfunction)

        # auto complete searchbar
        searchautocomplete = ["Amit Trivedi","Arijit Singh", "AR Rahman", "Ayushmann khuranna", "Divine", "KSHMR", "Mohit Chauhan", "Vishal Dadlani",
                              "Naina Da Kya Kasoor","Namo Namo", "Ud Daa Punjab", "Jai Ho", "Kun Faya Kun", "Nadaan Parindey", "Phir Se Ud Chala", "Haareya", "Ik Vaari Aa",
                              "Ilahi", "Raabta", "Subah Subah", "Mitti Di Khushboo", "Pani Da Rang", "Saadi Galli Aaja", "Yahin Hoon Main", "Azadi",
                              "Mere Gully Mein", "Sher Aaya Sher", "Around The World", "Bombay Dreams", "Matargashti", "Sadda Haq", "Balam Pichkari", "Bappa",
                              "Dhan Te Nan","Songs","Kabira", "Bekhayali", "Scam 1992 Theme Song", "Vaathi Coming", "Yalgaar", "Nazm Nazm"]
        completer = QCompleter(searchautocomplete)
        self.searchbar.setCompleter(completer)

        #####################################Add To Playlist########################################
        self.ad1.clicked.connect(self.addtoplst1)
        self.ad2.clicked.connect(self.addtoplst2)
        self.ad3.clicked.connect(self.addtoplst3)
        self.ad4.clicked.connect(self.addtoplst4)
        self.ad5.clicked.connect(self.addtoplst5)
        self.ad6.clicked.connect(self.addtoplst6)
        self.ad7.clicked.connect(self.addtoplst7)
        self.ad8.clicked.connect(self.addtoplst8)
        self.ad9.clicked.connect(self.addtoplst9)
        self.ad10.clicked.connect(self.addtoplst10)


        ############################################################################################
        ###voice button###
        self.micsearch.clicked.connect(self.speak)
        self.youspeak.setVisible(False)

        ########################################

        self.terms.clicked.connect(self.open_webbrowser)
        self.MPopen.clicked.connect(self.playermp)
        self.logout1.clicked.connect(self.logouthandler)
        self.openplaylist.clicked.connect(self.playlist12)
        self.openprofile.clicked.connect(self.profileopener)

        # Song 1
        self.play1.clicked.connect(self.playfunction1)
        self.pause1.clicked.connect(self.pausefunction1)
        self.resume1.clicked.connect(self.resumefunction1)

        # song 2
        self.play2.clicked.connect(self.playfunction2)
        self.pause2.clicked.connect(self.pausefunction2)
        self.resume2.clicked.connect(self.resumefunction2)

        # song 3
        self.play3.clicked.connect(self.playfunction3)
        self.pause3.clicked.connect(self.pausefunction3)
        self.resume3.clicked.connect(self.resumefunction3)

        # song 4
        self.play4.clicked.connect(self.playfunction4)
        self.pause4.clicked.connect(self.pausefunction4)
        self.resume4.clicked.connect(self.resumefunction4)

        # song 5
        self.play5.clicked.connect(self.playfunction5)
        self.pause5.clicked.connect(self.pausefunction5)
        self.resume5.clicked.connect(self.resumefunction5)

        # Song 6
        self.play6.clicked.connect(self.playfunction6)
        self.pause6.clicked.connect(self.pausefunction6)
        self.resume6.clicked.connect(self.resumefunction6)

        # song 7
        self.play7.clicked.connect(self.playfunction7)
        self.pause7.clicked.connect(self.pausefunction7)
        self.resume7.clicked.connect(self.resumefunction7)

        # song 8
        self.play8.clicked.connect(self.playfunction8)
        self.pause8.clicked.connect(self.pausefunction8)
        self.resume8.clicked.connect(self.resumefunction8)

        # song 9
        self.play9.clicked.connect(self.playfunction9)
        self.pause9.clicked.connect(self.pausefunction9)
        self.resume9.clicked.connect(self.resumefunction9)

        # song 10
        self.play10.clicked.connect(self.playfunction10)
        self.pause10.clicked.connect(self.pausefunction10)
        self.resume10.clicked.connect(self.resumefunction10)

    # song 1

    def playfunction1(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Kabira.mp3")
        pygame.mixer.music.play()

    def pausefunction1(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction1(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 2

    def playfunction2(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Bekhayali.mp3")
        pygame.mixer.music.play()

    def pausefunction2(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction2(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 3

    def playfunction3(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Mohit Chauhan/Sadda Haq.mp3")
        pygame.mixer.music.play()

    def pausefunction3(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction3(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 4

    def playfunction4(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Scam 1992.mp3")
        pygame.mixer.music.play()

    def pausefunction4(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction4(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 5

    def playfunction5(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Arijit Singh/Ik Vaari Aa.mp3")
        pygame.mixer.music.play()

    def pausefunction5(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction5(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 6

    def playfunction6(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Vaathi Coming.mp3")
        pygame.mixer.music.play()

    def pausefunction6(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction6(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 7

    def playfunction7(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Yalgaar.mp3")
        pygame.mixer.music.play()

    def pausefunction7(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction7(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 8

    def playfunction8(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Namo-Namo.mp3")
        pygame.mixer.music.play()

    def pausefunction8(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction8(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 9

    def playfunction9(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Amit Trivedi/Ud-Daa Punjab.mp3")
        pygame.mixer.music.play()

    def pausefunction9(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction9(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # song 10

    def playfunction10(self):
        pygame.mixer.init()
        pygame.mixer.music.load("../music/Nazm Nazm.mp3")
        pygame.mixer.music.play()

    def pausefunction10(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction10(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    # //////////////////////////////////////////////////////////////////////////

    def playlist12(self):
        sys.path.append('../Final/playlist.py')
        import playlist

    def logouthandler(self):

        sys.path.append('../Final/main.py')
        import main

    def open_webbrowser(self):
        webbrowser.open("../Final/Terms&Condition.html")

    # noinspection PyMethodMayBeStatic

    def playermp(self):
        sys.path.append('../Final/Mplayer.py')
        import Mplayer

    def profileopener(self):
        sys.path.append('../Final/profilehandle.py')
        import profilehandle

    ####################voice search function##############################
    def speak(self):
        self.youspeak.setVisible(True)

        sr.Microphone(device_index=1)
        r = sr.Recognizer()
        r.energy_threshold = 5000
        with sr.Microphone() as source:
            print("Speak!")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                search_url = text

                searchbar = QLineEdit(self)

                self.searchbar.setText(search_url)
            except:

                print("Can't recognize")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.searchfunction()

    def searchfunction(self):
        search = self.searchbar.text()

        #Category of Songs

        if search == 'Amit Trivedi':
            import AmitTrivediSongs

        elif search == 'Arijit Singh':
            import ArijitSinghSongs

        elif search == 'AR Rahman':
            import ARRahmanSongs

        elif search == 'Ayushmann khuranna':
            import AyushmannKhurannaSongs

        elif search == 'Divine':
            import DivineSongs

        elif search == 'KSHMR':
            import KSHMRSongs

        elif search == 'Mohit Chauhan':
            import MohitChauhanSongs

        elif search == 'Vishal Dadlani':
            import VishalDadlaniSongs

        #Separate Songs

        elif search == 'Naina Da Kya Kasoor':
            import nainadakyakasoorsong

        elif search == 'Namo Namo':
            import namonamosong

        elif search == 'Ud Daa Punjab':
            import udtapunjabsong

        elif search == 'Jai Ho':
            import jaihosong

        elif search == 'Kun Faya Kun':
            import kunfayakunsong

        elif search == 'Nadaan Parindey':
            import nadaanparindesong

        elif search == 'Phir Se Ud Chala':
            import phirseudchalasong

        elif search == 'Haareya':
            import haareyasong

        elif search == 'Ik Vaari Aa':
            import ikvaariaasong

        elif search == 'Ilahi':
            import illahisong

        elif search == 'Raabta':
            import raabtasong

        elif search == 'Subah Subah':
            import subahsubahsong

        elif search == 'Mitti Di Khushboo':
            import mittidikhushboosong

        elif search == 'Pani Da Rang':
            import panidarangsong

        elif search == 'Kun Faya Kun':
            import kunfayakunsong

        elif search == 'Saadi Galli Aaja':
            import saadigalliaajasong

        elif search == 'Yahin Hoon Main':
            import yahihoonmainsong

        elif search == 'Azadi':
            import azadisong

        elif search == 'Mere Gully Mein':
            import meregullymeinsong

        elif search == 'Sher Aaya Sher':
            import sheraayashersong

        elif search == 'Around The World':
            import aroundtheworldsong

        elif search == 'Bombay Dreams':
            import bombaydreamssong

        elif search == 'Matargashti':
            import matargashtisong

        elif search == 'Sadda Haq':
            import saddahaqsong

        elif search == 'Balam Pichkari':
            import balampichkarisong

        elif search == 'Bappa':
            import bappasong

        elif search == 'Dhan Te Nan':
            import dhantenansong

        elif search == 'Songs':
            import categoryofsongs

        elif search == 'Kabira':
            sys.path.append('../Final/kabirasong.py')
            import kabirasong

        elif search == 'Bekhayali':
            import bekhayalisong

        elif search == 'Scam 1992 Theme Song':
            import scamsong

        elif search == 'Vaathi Coming':
            import vaathicomingsong

        elif search == 'Yalgaar':
            import yalgaarsong

        elif search == 'Nazm Nazm':
            import nazmnazmsong

        else:
            kit.playonyt(search)


    #######################################################################
    def addtoplst1(self):

        newPath = shutil.copy(r'../music/Kabira.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst2(self):
        # Copy file to another directory
        newPath = shutil.copy(r'../music/Bekhayali.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst3(self):
        # Copy file to another directory
        newPath = shutil.copy(r'../music/\Mohit Chauhan/Sadda Haq.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst4(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Scam 1992.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst5(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Arijit Singh/Ik Vaari Aa.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst6(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Vaathi Coming.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst7(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Yalgaar.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst8(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Amit Trivedi/Namo-Namo.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst9(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Amit Trivedi/Ud-Daa Punjab.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)
    def addtoplst10(self):
        # Copy file to another directory
        newPath = shutil.copy('../music/Nazm Nazm.mp3', r'../Playlist')
        print("Path of copied file : ", newPath)


    #######################################################################
app = QApplication(sys.argv)
mainwindow = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.setFixedWidth(1371)
widget.setFixedHeight(850)
app.exec_()
