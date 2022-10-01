import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Register(QDialog):
    def __init__(self):
        super(Register,self).__init__()
        loadUi("Register.ui",self)
app=QApplication(sys.argv)
mainwindow=Register()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.show()
app.exec_()