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
        self cargararchivos()
        self.show()
    def borrar(self):
        pass


    def cargararchivos():


def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
