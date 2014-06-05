# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Producto.ui'
#
# Created: Thu Jun  5 05:49:28 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(619, 438)
        self.gridLayout = QtGui.QGridLayout(Productos)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtGui.QPushButton(Productos)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(Productos)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(Productos)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Productos)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Productos)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.comboBox = QtGui.QComboBox(Productos)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 2)
        self.tabla = QtGui.QTableView(Productos)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setSortingEnabled(True)
        self.tabla.setObjectName("tabla")
        self.gridLayout.addWidget(self.tabla, 2, 0, 1, 5)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QtGui.QApplication.translate("Productos", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Productos", "Añadir Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Productos", "Editar ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Productos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Productos", "Ingrese el nombre de un producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Productos", "Seleccione una marca", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Productos", "NIKE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Productos", "REEBOK", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Productos", "SAMSUNG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Productos", "APPLE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Productos", "MICROSOFT", None, QtGui.QApplication.UnicodeUTF8))

