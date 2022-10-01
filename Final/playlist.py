import sys

# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUi
from pygame import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# noinspection PyUnresolvedReferences
import PyQt5.uic
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.Qt import *
import webbrowser
from tkinter import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import pygame


def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class Mplayer(QMainWindow):
    def __init__(self):
        super(Mplayer, self).__init__()
        loadUi("playlist.ui", self)

        self.player = QMediaPlayer()
        self.backtohome1.clicked.connect(self.backtomain)
        self.player.error.connect(self.erroralert)
        self.player.play()

        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        # Add viewer for video playback, separate floating window.
        self.viewer = ViewerWindow(self)
        # noinspection PyTypeChecker
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        # Connect control buttons/slides for media player.
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.resumebutton.clicked.connect(self.player.play)

        # playlist

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.browse1.clicked.connect(self.open_file)

        self.setAcceptDrops(True)

        self.show()

    def backtomain(self):
        sys.path.append('../Final/homepage.py')
        import homepage

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")

        if path:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(path)
                )
            )

        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())

        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)


class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    # noinspection PyMethodOverriding
    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    # noinspection PyMethodOverriding
    def rowCount(self, index):
        return self.playlist.mediaCount()


app = QApplication(sys.argv)
mainwindow = Mplayer()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.setFixedWidth(521)
widget.setFixedHeight(381)
app.exec_()