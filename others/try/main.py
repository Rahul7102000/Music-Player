import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase
import mysql.connector

firebaseConfig = { 'apiKey': "AIzaSyCisR8CerEzsZbG0AXRWl2RSJFmi0wvAaI",
    'authDomain': "authdemo-a00db.firebaseapp.com",
    'databaseURL': "https://authdemo-a00db-default-rtdb.firebaseio.com",
    'projectId': "authdemo-a00db",
    'storageBucket': "authdemo-a00db.appspot.com",
    'messagingSenderId': "681646935568",
    'appId': "1:681646935568:web:20fa2602e2d3f6fa8b8495",
    'measurementId': "G-DT8XZETJN1"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.p_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email = self.u_name.text()
        password = self.p_password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
        except:
            self.invalid.setVisible(True)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.backtologin.clicked.connect(self.gobacktologin)
        self.invalid.setVisible(False)

    def gobacktologin(self):
        login1 = Login()
        widget.addWidget(login1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except:
                self.invalid.setVisible(True)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.show()
app.exec_()
