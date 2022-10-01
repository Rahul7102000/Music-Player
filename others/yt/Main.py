import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel
from PyQt5.uic import loadUi


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("Main.ui", self)

app = QApplication(sys.argv)
mainwindow = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.show()
app.exec_()
