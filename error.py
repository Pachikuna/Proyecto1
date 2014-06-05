# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created: Wed Jun  4 23:18:33 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(389, 76)
        self.horizontalLayout = QtGui.QHBoxLayout(Error)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Confirmacion = QtGui.QLabel(Error)
        self.Confirmacion.setObjectName("Confirmacion")
        self.horizontalLayout.addWidget(self.Confirmacion)
        self.pushButton = QtGui.QPushButton(Error)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        Error.setWindowTitle(QtGui.QApplication.translate("Error", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.Confirmacion.setText(QtGui.QApplication.translate("Error", "usuario o password incorrectos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Error", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

