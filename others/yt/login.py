import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.p_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gotosignup.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email = self.u_name.text()
        password = self.p_password.text()
        print("Successfully logged in with email: ", email, "and password:", password)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("Register.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.p_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.show()
app.exec_()
