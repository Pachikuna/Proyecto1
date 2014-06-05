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
    resultado= c.execute(query)
    marca = resultado.fetchall()
    con.close()
    return marca

def obtener_productos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM products"
    resultado= c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto



if __name__ == "__main__":

    marca = obtener_marca()
    for marcas in marca:
        print marcas


    producto = obtener_productos()
    for produc in producto:
        print produc