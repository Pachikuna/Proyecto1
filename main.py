import sys
from PySide import QtGui, QtCore
import controller
from interfas_Tarea1 import Ui_Tarea1


class Form(QtGui.QTableView):
    def __init__(self, parent=None):
        QtGui.QTableView.__init__(self, parent)
        self.ventana =  Ui_Tarea1()
        self.ventana.setupUi(self)
        self.ventana.pushButton_3.clicked.connect(self.borrar)
#        self cargararchivos()
        self.render_table()
        self.show()
    def borrar(self):
        pass

    def render_table(self):
        self.table = QtGui.QTableView(self)
        self.table.setFixedWidth(790)
        self.table.setFixedHeight(450)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        #Se incorpora la tabla al layout
        self.ventana.addWidget(self.table)

#    def cargararchivos():
#    marca = controller.obtener_marca()


def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
