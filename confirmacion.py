# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmacion.ui'
#
# Created: Wed Jun  4 20:49:21 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 121)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Confirmacion = QtGui.QLabel(Dialog)
        self.Confirmacion.setGeometry(QtCore.QRect(30, 30, 341, 31))
        self.Confirmacion.setObjectName("Confirmacion")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Confirmacion", None, QtGui.QApplication.UnicodeUTF8))
        self.Confirmacion.setText(QtGui.QApplication.translate("Dialog", "Realmente desea eliminar el producto seleccionado ?", None, QtGui.QApplication.UnicodeUTF8))

