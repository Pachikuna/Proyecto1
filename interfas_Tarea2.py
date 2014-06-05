# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfas_Tarea2.ui'
#
# Created: Thu Jun  5 03:55:32 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tarea1(object):
    def setupUi(self, Tarea1):
        Tarea1.setObjectName("Tarea1")
        Tarea1.resize(619, 438)
        self.gridLayout = QtGui.QGridLayout(Tarea1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtGui.QPushButton(Tarea1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(Tarea1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(Tarea1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Tarea1)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Tarea1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.comboBox = QtGui.QComboBox(Tarea1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 2)
        self.widget = QtGui.QWidget(Tarea1)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 5)

        self.retranslateUi(Tarea1)
        QtCore.QMetaObject.connectSlotsByName(Tarea1)

    def retranslateUi(self, Tarea1):
        Tarea1.setWindowTitle(QtGui.QApplication.translate("Tarea1", "Tarea1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Tarea1", "Añadir Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Tarea1", "Editar ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Tarea1", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Tarea1", "Ingrese el nombre de un producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Tarea1", "Seleccione una marca", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Tarea1", "NIKE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Tarea1", "REEBOK", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Tarea1", "SAMSUNG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Tarea1", "APPLE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Tarea1", "MICROSOFT", None, QtGui.QApplication.UnicodeUTF8))

