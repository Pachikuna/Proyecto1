import sqlite3

createDb = sqlite3.connect('Marcas.db')

p = createDb.cursor()

def crearBDTablas():
    p.execute('''CREATE TABLE marca
                        (id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        descripcion TEXT,
                        pais TEXT)''')
    p.execute('''CREATE TABLE products
                        (codigo TEXT PRIMARY KEY,
                        nombre TEXT,
                        descripcion TEXT,
                        color TEXT,
                        precio INTEGER,
                        id_marca INTEGER, FOREIGN KEY(id_marca) REFERENCES marcas(id_marca))''')


def agregarmarca(nombre, descripcion, pais):
    p.execute('''INSERT INTO marca (nombre, descripcion, pais)
    VALUES (?,?,?)''',(nombre, descripcion, pais))


def agregarproduct(codigo, nombre, descripcion, color, precio, id_marca):
    p.execute('''INSERT INTO products (codigo, nombre, descripcion, color, precio, id_marca)
    VALUES (?,?,?,?,?,?)''',(codigo, nombre, descripcion, color, precio, id_marca))


def main():
    crearBDTablas()

    agregarmarca("NIKE", "IMPLEMENTACION DEPORTIVA", "ESTADOS UNIDOS")
    agregarmarca("REBOOK", "IMPLEMENTACION DEPORTIVA", "INGLATERRA")
    agregarmarca("APPLE", "INDUSTRIA TECNOLOGICA", "ESTADOS UNIDOS")
    agregarmarca("MICROSOFT", "INDUSTRIA TECNOLOGICA", "ESTADOS UNIDOS")
    agregarmarca("SAMSUMG", "INDUSTRIA TECNOLOGICA", "COREA SUR")

    agregarproduct("NK01", "HYPERVENOM", "ZAPATILLA FUTBOL", "AMARILLO", 47000, 1)
    agregarproduct("NK02", "MERCURIAL", "ZAPATILLA FUTBOL", "AZUL", 35000, 1)
    agregarproduct("NK03", "CTR360", "ZAPATILLA FUTBOL", "AZUL", 45000, 1)
    agregarproduct("NK04", "TIEMPO", "ZAPATILLA FUTBOL", "NEGRO", 55000, 1)

    agregarproduct("RBK01", "TERRAIN SERIES SPORT", "ZAPATILLA CROSSFIT", "NEGRA", 44000, 2)
    agregarproduct("RBK02", "KAMIKAZE", "ZAPATILLA BASKETBOL", "NARANJO", 55000, 2)
    agregarproduct("RBK03", "CLASSIC LEATHER", "ZAPATILLA DE VESTIR", "CAFE", 24000, 2)
    agregarproduct("RBK04", "ZQUICK", "ZAPATILLA RUNNING", "AZUL", 59000, 2)

    agregarproduct("APP01", "IFONE", "TELEFONO", "BLANCO", 260000, 3)
    agregarproduct("APP02", "ITV", "SMART-TV", "GRIS", 43000, 3)
    agregarproduct("APP03", "IPOD", "REPRODUCTOR", "NEGRO", 200000, 3)
    agregarproduct("APP04", "IMAC", "COMPUTADOR", "GRIS", 1200000, 3)

    agregarproduct("MS01", "XBOX360", "CONSOLA", "NEGRO", 90000, 4)
    agregarproduct("MS02", "XBOXONE", "CONSOLA", "NEGRO", 250000, 4)
    agregarproduct("MS03", "HALO4", "JUEGO", "VERDE", 9000, 4)
    agregarproduct("MS04", "WINDDOWS8.1", "S.O.", "AZUL", 99000, 4)

    agregarproduct("SAM01", "SM7", "AUTOMOVIL", "PLATA", 5600000, 5)
    agregarproduct("SAM02", "HEADSET", "AUDIFONOS", "NEGRO", 4500, 5)
    agregarproduct("SAM03", "GALAXY CAMARAS", "CAMARA FOTOGRAFICA", "NEGRO", 250000, 5)
    agregarproduct("SAM04", "HOME-THEATER'", "SONIDO", "PLATA", 170000, 5)

    createDb.commit()

    #Obtener todos los campos de todos los productos
    p.execute('SELECT * FROM products')
    productsList = ['Codigo: ', 'Nombre: ', 'Descripcion: ', 'Color: ', 'Precio: ', 'ID Marca: ']
    count = 0
    for i in p:
        print '\n'
        for j in i:
            print str(productsList[count]) + str(j) #Se imprime un elemento de productsList junto con el elemento j en i
            if count<5: count+=1
            else: count = 0

    #Obtener el campo color de todos los productos
    p.execute('SELECT color FROM products')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'COLOR:'
    for i in p:
        print str(i)

    #Obtener todos los campos de los productos asociados a la marca NIKE
    p.execute('SELECT * FROM products WHERE id_marca = 1')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS NIKE'
    for i in p:
        print str(i)

    #Obtener todos los productos cuyo precio es menor a 10000
    p.execute('SELECT nombre FROM products WHERE precio < 10000')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS CON PRECIO MENOR A 10000'
    for i in p:
        print str(i)

    #Obtener todos los productos cuyo precio es mayor a 20000
    p.execute('SELECT nombre FROM products WHERE precio > 20000')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS CON PRECIO MAYOR A 20000'
    for i in p:
        print str(i)

    #Borrar el registro con primary key NK02 en la tabla de productos
    p.execute('DELETE FROM products WHERE codigo = "NK02"')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTO CON CODIGO NK02 BORRADO CON EXITO'
    createDb.commit()

    #Borra todos los registros cuya marca es REEBOK
    p.execute('DELETE FROM products WHERE id_marca = 2')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS REEBOK BORRADOS CON EXITO'
    createDb.commit()

    #Actualizar la columna color a verde del producto cuya primary key es SAM01
    p.execute('UPDATE products SET color = "VERDE" WHERE codigo = "SAM01"')
    createDb.commit()

    #Actualizar el precio de todos los productos cuya marca es SAMSUMG y dejarlos en 2000
    p.execute('UPDATE products SET precio = 2000 WHERE id_marca = 5')
    createDb.commit()

    #Obtener todos los productos cuya marca sea NIKE y el precio sea mayor a 5.000
    p.execute('SELECT nombre FROM products WHERE id_marca= 1 and precio > 5000')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS NIKE CON PRECIO MAYOR A 5000'
    for i in p:
        print str(i)

    #Obtener todos los productos cuya marca sea APPLE o MICROSOFT
    p.execute('SELECT nombre FROM products WHERE id_marca = 3 or id_marca = 4')
    print '\n'
    print '-__-__-__-__-__-__-__-__-__-__-__-__-__-__'
    print 'PRODUCTOS QUE SON APPLE O MICROSOFT'
    for i in p:
        print str(i)




if __name__ == '__main__': main()



