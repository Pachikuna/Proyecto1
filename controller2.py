# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from formularioad import*
import controller


class Form_2(QtGui.QWidget):
    def __init__(self, parent=None):#Funcion para crear la ventana Formulario
        super(Form_2, self).__init__()
        self.ventana = Ui_Formulario()
        self.ventana.setupUi(self)
        self.ventana.pushButton.clicked.connect(self.aceptar) #conecta el boton
        #aceptar para que cuando se haga click se ejecute la funcion aceptar
        self.ventana.pushButton_2.clicked.connect(self.cancelar)#Conecta el
        #boton cancelar para cerrar la ventana Formulario
        self.var = 0
        self.codigo = ""
        self.show()

    def carga(self, producto, codigo): #Funcion para extraer datos que se
                                       #quieren editar de la ventana Editar
        self.codigo = codigo
        self.ventana.lineEdit.setText(producto[0][0])#1
        self.ventana.lineEdit_2.setText(producto[0][1])#2
        self.ventana.lineEdit_3.setText(producto[0][2])#3
        self.ventana.lineEdit_4.setText(producto[0][3])#4
        self.ventana.lineEdit_5.setText(str(producto[0][4]))#5
        self.ventana.lineEdit_6.setText(str(producto[0][5]))#6
        #Del 1 hasta el 6 extrae los datos para editarlos
        self.var = 1
        self.ventana.comboBox.setCurrentIndex(producto[0][6])
        #durante la ejecucion si se quiere editar un producto
        #hay que asignarle si o si la marca para que funcione

    def aceptar(self): #funcion para agregar un producto a la tabla
        codi = self.ventana.lineEdit.text()#1
        nombre = self.ventana.lineEdit_2.text()#2
        descrip = self.ventana.lineEdit_3.text()#3
        color = self.ventana.lineEdit_4.text()#4
        preciobruto = self.ventana.lineEdit_5.text()#5
        precioneto = self.ventana.lineEdit_6.text()#6
        pk = self.ventana.comboBox.currentIndex()#7, desde el 1 al 7 extrae datos
        datos = (codi, nombre, descrip, color, preciobruto, precioneto, pk)
        cod2 = self.codigo
        if(self.var == 1):
            controller.reescribeProducto(datos, cod2) # Agrega el producto descrito desde
        else:                                           # el 1 al 7
            controller.insertarproductos(datos) # Agrega el producto descrito desde
        self.close()                               # el 1 al 7

    def cancelar(self):# funcion que al apretar el boton cancelar cierra esta
        self.close()    #ventana
