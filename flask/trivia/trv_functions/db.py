import sqlite3


def consultar(sentencia = ""):
    bd = sqlite3.connect('data.db')
    cursor = bd.cursor()
    sentencia = 'SELECT nombre FROM categorias;'
    cursor.execute(sentencia)
    valores = cursor.fetchall()
    return valores
