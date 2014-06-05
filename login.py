# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Wed Jun  4 23:17:46 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(296, 272)
        self.pushButton = QtGui.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtGui.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 191, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 110, 191, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtGui.QLabel(login)
        self.label.setGeometry(QtCore.QRect(120, 10, 111, 51))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 141, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Descargas/lock-512.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(QtGui.QApplication.translate("login", "login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("login", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("login", "                  Username", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("login", "                  Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("login", "<html><head/><body><p><span style=\" font-size:16pt;\">Login</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

