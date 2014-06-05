import sys
from PySide import QtGui, QtCore
import controller
from interfas_Tarea1 import *

class Form(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__()
        self.ventana =  Ui_Tarea1()
        self.ventana.setupUi(self)
        self.render_table()
        self.ventana.pushButton_3.clicked.connect(self.borrar)
        self.cargararchivos()
        self.show()


    def borrar(self):
        pass

    def render_table(self):
        self.table = QtGui.QTableView(self)
        self.table.setFixedWidth(700)
        self.table.setFixedHeight(400)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        #Se incorpora la tabla al layout
        self.ventana.addWidget(self.table)


    def cargararchivos(self):
        producto = controller.obtener_productos()


        self.model = QtGui.QStandardItemModel(len(producto), 7)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"codigo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio Bruto"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Precio Neto"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"id marca"))


        r = 0
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

            r = r+1
        self.table.setModel(self.model)

        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 210)
        self.table.setColumnWidth(2, 210)
        self.table.setColumnWidth(3, 230)
        self.table.setColumnWidth(4, 240)
        self.table.setColumnWidth(5, 250)
        self.table.setColumnWidth(6, 260)



def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
