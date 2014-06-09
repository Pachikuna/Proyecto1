# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
import controller2
from Producto import *


class Form(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__()
        self.ventana = Ui_Productos()
        self.ventana.setupUi(self)
        self.render_table()
        self.cargararchivos()
        self.ventana.comboBox.activated[int].connect(self.cargararchivos)
        self.ventana.lineEdit.textChanged[str].connect(self.filtro)
        self.ventana.pushButton.clicked.connect(self.editar)
        self.ventana.pushButton_2.clicked.connect(self.abreventana)
        self.ventana.pushButton_3.clicked.connect(self.borrar)
        self.show()

<<<<<<< HEAD
    def filtro(self, txt): #Funcion que llama a la funcion cargararchivoFiltro
                           #con el parametro products para volver imprimir
        texto = txt.encode('utf8')
        products = controller.filtrarProductos(txt)
        self.cargararchivoFiltro(products)

    def abreventana(self): #Funcion que abre la ventana Formulario
        formulario = controller2.Form_2(self)
        formulario.exec_()

    def editar(self): #Funcion que se activa al presionar el boton editar
        model = self.ventana.tabla.model()
        index = self.ventana.tabla.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            producto = controller.buscarEditar(cod)
            self.formulario = controller2.Form_2(self) #Abre la ventana Formulario
            self.formulario.carga(producto, cod)

    def borrar(self): #Funcion que se activa al presionar el boton Eliminar
        model = self.ventana.tabla.model()
        index = self.ventana.tabla.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(cod)):  #Llama a la funcion delete con la
                                          #fila que se quiere eliminar
                self.cargararchivos()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False

    def render_table(self):
        self.ventana.tabla.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)

    def cargararchivos(self): #Funcion que carga los archivos a la tabla
=======
    def filtro(self, txt):
        texto = txt.encode('utf8')
        products = controller.filtrarProductos(txt)
        self.cargararchivoFiltro(products)

    def abreventana(self):
        formulario = controller2.Form_2(self)
        formulario.exec_()
#        self.cargararchivos()

    def editar(self):
        model = self.ventana.tabla.model()
        index = self.ventana.tabla.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            producto = controller.buscarEditar(cod)
            self.formulario = controller2.Form_2(self)
            self.formulario.carga(producto, cod)

    def borrar(self):
        model = self.ventana.tabla.model()
        index = self.ventana.tabla.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(cod)):
                self.cargararchivos()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False

    def render_table(self):
        self.ventana.tabla.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ventana.tabla.adjustSize()
        #self.ventana.tabla.setStretch()

    def cargararchivos(self):
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
        if (self.ventana.comboBox.currentIndex() == 0):
            producto = controller.obtener_productos()
        else: producto = controller.obtener_productos2(self.ventana.comboBox.currentIndex())
        self.model = QtGui.QStandardItemModel(len(producto), 7)
        #Se asigna nombre y orden a las columnas
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"código"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio Bruto"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Precio Neto"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"id marca"))

        r = 0
        #Se llena la tabla con los productos extraidos de la base de dato
        for row in producto:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['preciobruto'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['precioneto'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['id_marca'])
            r = r + 1
<<<<<<< HEAD
        #Se asigna el ancho de las columnas
=======
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
        self.ventana.tabla.setModel(self.model)
        self.ventana.tabla.setColumnWidth(0, 100)
        self.ventana.tabla.setColumnWidth(1, 100)
        self.ventana.tabla.setColumnWidth(2, 150)
        self.ventana.tabla.setColumnWidth(3, 100)
        self.ventana.tabla.setColumnWidth(4, 100)
        self.ventana.tabla.setColumnWidth(5, 100)
        self.ventana.tabla.setColumnWidth(6, 100)

<<<<<<< HEAD
    def cargararchivoFiltro(self, productos): #Funcion que imprime la tabla filtrada
        self.model = QtGui.QStandardItemModel(len(productos), 7)
        #Se asigna nombre y orden a las columnas
=======
    def cargararchivoFiltro(self, productos):
        self.model = QtGui.QStandardItemModel(len(productos), 7)
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"código"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio Bruto"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Precio Neto"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"id marca"))
        r = 0
<<<<<<< HEAD
        #Se llena la tabla con los productos extraidos de la base de dato
=======
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['preciobruto'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['precioneto'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['id_marca'])
            r = r + 1
<<<<<<< HEAD
        #Se asigna el ancho de las columnas
=======
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
        self.ventana.tabla.setModel(self.model)
        self.ventana.tabla.setColumnWidth(0, 100)
        self.ventana.tabla.setColumnWidth(1, 100)
        self.ventana.tabla.setColumnWidth(2, 150)
        self.ventana.tabla.setColumnWidth(3, 100)
        self.ventana.tabla.setColumnWidth(4, 100)
        self.ventana.tabla.setColumnWidth(5, 100)
        self.ventana.tabla.setColumnWidth(6, 100)


def run(): #Funcion principal que ejecuta el programa completo
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
