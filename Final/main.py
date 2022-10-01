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

firebaseConfig = {
    'apiKey': "AIzaSyAiLz49Xn4LuOrze7U93Z9RW_wYYEFOVos",
    'authDomain': "authdemo-cafbe.firebaseapp.com",
    'databaseURL': "https://authdemo-cafbe-default-rtdb.firebaseio.com",
    'projectId': "authdemo-cafbe",
    'storageBucket': "authdemo-cafbe.appspot.com",
    'messagingSenderId': "840909774948",
    'appId': "1:840909774948:web:cacbfb0726d6a8d16c3f71",
    'measurementId': "G-S4DRHKZWWP"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signupbutton.clicked.connect(self.gotosignup)
        self.error.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        # noinspection PyStatementEffect
        try:
            auth.sign_in_with_email_and_password(email, password)
            sys.path.append('../Final/homepage.py')
            import homepage

        except:
            self.error.setVisible(True)

    def gotosignup(self):
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("signup.ui", self)

        widget.setFixedWidth(611)
        widget.setFixedHeight(476)
        self.signupbutton1.clicked.connect(self.signupfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backtologin.clicked.connect(self.gobacktologin)
        self.error.setVisible(False)

    def gobacktologin(self):
        login1 = Login()
        widget.addWidget(login1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpassword_2.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except:
                self.error.setVisible(True)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(664)
widget.setFixedHeight(520)
widget.show()
app.exec_()
