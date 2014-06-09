#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3


<<<<<<< HEAD
def conectar(): #crea el archivo de base de datos Marcas
=======
def conectar():
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    con = sqlite3.connect('Marcas.db')
    con.row_factory = sqlite3.Row
    return con


<<<<<<< HEAD
def obtener_marca():#Funcion para extrar todos las marcas de la base de datos
=======
def obtener_marca():
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca"
    resultado = c.execute(query)
    marca = resultado.fetchall()
    con.close()
    return marca


<<<<<<< HEAD
def filtrarProductos(texto): #Funcion que extrae de acuerdo al combobox los
    con = conectar()         #elementos de la tabla
=======
def filtrarProductos(texto):
    con = conectar()
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    c = con.cursor()
    query = "SELECT * FROM products WHERE nombre LIKE \"%{0}%\"".format(texto)
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto


<<<<<<< HEAD
def insertarproductos(datos):#Funcion que agrega un nuevo producto a la tabla
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO products (codigo,nombre,descripcion,color,
        preciobruto,precioneto,id_marca) VALUES (?,?,?,?,?,?,?)"""
    c.execute(query, datos)
    con.commit()


def obtener_productos(): #Funcion que extrae los datos de la base de datos
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products" #extrae todos los productos y los guarda
=======
def insertarproductos(datos):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO products (codigo,nombre,descripcion,color,
        preciobruto,precioneto,id_marca) VALUES (?,?,?,?,?,?,?)"""
    c.execute(query, datos)
    con.commit()


def obtener_productos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products"
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto


<<<<<<< HEAD
def obtener_productos2(pk): # Funcion para seleccionar los productos de acuerdo
    con = conectar()        # a la variable pk que se extrae del combobox
    c = con.cursor()
    try:
        query = "SELECT * FROM products WHERE id_marca = ?"
        resultado = c.execute(query, [pk]) #guarda productos con id_marca = pk
=======
def obtener_productos2(pk):
    con = conectar()
    c = con.cursor()
    try:
        query = "SELECT * FROM products WHERE id_marca = ?"
        resultado = c.execute(query, [pk])
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    producto = resultado.fetchall()
    con.close()
    return producto


<<<<<<< HEAD
def buscarEditar(codigo): # Funcion que selecciona un producto para su posterior edicion
=======
def buscarEditar(codigo):
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products WHERE codigo = ?"
    resultado = c.execute(query, [codigo])
    producto = resultado.fetchall()
    con.commit()
    con.close()
    return producto
<<<<<<< HEAD
=======


def reescribeProducto(datos, cod2):
    con = conectar()
    c = con.cursor()
    cod = datos[0]
    nom = datos[1]
    descrip = datos[2]
    color = datos[3]
    preB = datos[4]
    preN = datos[5]
    pk = datos[6]
    query = """UPDATE products SET codigo = ?
            ,nombre = ?
            ,color = ?
            ,descripcion = ?
            ,preciobruto = ?
            ,precioneto = ?
            ,id_marca = ?
            WHERE codigo = ?"""
    infonueva = (cod, nom, descrip, color, preB, preN, pk, cod2)
    c.execute(query, infonueva)
    con.commit()


def delete(codigo):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM products WHERE codigo = ?"
    try:
        resultado = c.execute(query, [codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a


def reescribeProducto(datos, cod2): #Funcion principal para la edicion
                                    #de un producto
    con = conectar()
    c = con.cursor()
    cod = datos[0]#1
    nom = datos[1]#2
    descrip = datos[2]#3
    color = datos[3]#4
    preB = datos[4]#5
    preN = datos[5]#6
    pk = datos[6]#7, Desde 1 hasta 7, extrae y asigna los datos que
                 #se estan actualizando
    query = """UPDATE products SET codigo = ?
            ,nombre = ?
            ,color = ?
            ,descripcion = ?
            ,preciobruto = ?
            ,precioneto = ?
            ,id_marca = ?
            WHERE codigo = ?""" #funcion que sirve para actualizar los datos
                                #ingresados por el usuario
    infonueva = (cod, nom, descrip, color, preB, preN, pk, cod2)
    c.execute(query, infonueva)
    con.commit()

<<<<<<< HEAD

def delete(codigo): #Funcion usada para borrar productos de la tabla
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM products WHERE codigo = ?"
    try:
        resultado = c.execute(query, [codigo]) #Elimina el producto selecionado
        con.commit()                           #y que tiene el id_marca = pk
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
=======
    producto = obtener_productos2(2)
    for produc in producto:
        print produc
>>>>>>> 08b40a24ec3eecaf11210edb5e627ea3ea64b00a
