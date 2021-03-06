#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('alumnos.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_alumnos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM alumnos"
    resultado= c.execute(query)
    alumnos = resultado.fetchall()
    con.close()
    return alumnos

def delete(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM alumnos WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

if __name__ == "__main__":

    alumnos = obtener_alumnos()
    for alumno in alumnos:
        print alumno["nombres"]
