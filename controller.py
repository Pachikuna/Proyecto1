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



if __name__ == "__main__":

    marca = obtener_marca()
    for marcas in marca:
        print marcas["nombre"]