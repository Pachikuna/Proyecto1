import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtGui.QLabel("Seleccionado", self)
        self.combo = QtGui.QComboBox(self)
        brands = [
            {"id": "1", "name": "WRSI"},
            {"id": "2", "name": "Venture"},
            {"id": "3", "name": "Vango"}]
        for element in brands:
            self.combo.addItem(element["name"], element["id"])

        self.combo.move(50, 50)
        self.lbl.move(10, 150)
        self.combo.activated[int].connect(self.onActivated)
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()

    def onActivated(self, index):
        pk = self.combo.itemData(index)
        text = self.combo.itemText(index)
        self.lbl.setText("La marca seleccionada es " + text + " y su pk es " + pk)
        self.lbl.adjustSize()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()