#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3


def conectar():
    con = sqlite3.connect('Marcas.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_marca():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca"
    resultado = c.execute(query)
    marca = resultado.fetchall()
    con.close()
    return marca


def filtrarProductos(texto):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products WHERE nombre LIKE \"%{0}%\"".format(texto)
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto


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
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto


def obtener_productos2(pk):
    con = conectar()
    c = con.cursor()
    try:
        query = "SELECT * FROM products WHERE id_marca = ?"
        resultado = c.execute(query, [pk])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    producto = resultado.fetchall()
    con.close()
    return producto


def buscarEditar(codigo):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products WHERE codigo = ?"
    resultado = c.execute(query, [codigo])
    producto = resultado.fetchall()
    con.commit()
    con.close()
    return producto


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


if __name__ == "__main__":

    marca = obtener_marca()
    for marcas in marca:
        print marcas

    producto = obtener_productos2(2)
    for produc in producto:
        print produc
