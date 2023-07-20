from entrada_db import get_db
from class_entrada import Entrada

#hago la funcion para insertar entradas faltantes
def insert_entrada(id, estadio, partido, precio, sector):
    db = get_db()
    cursor = db.cursor()
    statement = 'INSERT INTO entrada (id, estadio, partido, precio, sector) \
    VALUES ( ?, ?, ?, ?, ? )'
    cursor.execute(statement, [id, estadio, partido, precio, sector])
    db.commit()
    return True

#esta funcion no la pide, pero puede llegar a ser util, si se desean actualizar los precios de las entradas
def update_entrada(id, estadio, partido, precio, sector):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE entrada SET id = ?, estadio = ?, partido= ?, precio= ?, sector=? \
    WHERE id = ?"
    cursor.execute(statement, [estadio, partido, precio, sector, id])
    db.commit()
    return True

#esta funcion no la pide, pero sirve para borrar una entrada
def delete_entrada(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM copa WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

#sirve para obtener una entrada en específico de acuerdo a un id
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, estadio, partido, precio, sector FROM entrada WHERE id = ?"
    cursor.execute(statement, [id])
    single_entrada = cursor.fetchone()
    id = single_entrada[0]
    estadio = single_entrada[1]
    partido = single_entrada[2]
    precio = single_entrada[3]
    sector = single_entrada[4]
    entrada = Entrada(id,estadio, partido, precio, sector)
    return entrada.serialize()

#sirve para hacer una lisa de todas las entradas disponibles
def get_entradas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, estadio, partido, precio, sector FROM entrada"
    cursor.execute(query)
    entrada_list = cursor.fetchall()
    list_of_entradas=[]
    for entrada in entrada_list:
        id = entrada[0]
        estadio = entrada[1]
        partido = entrada[2]
        precio = entrada[3]
        sector = entrada[4]
        entrada_to_add = entrada(id,estadio, partido, precio, sector)
        list_of_entradas.append(entrada_to_add)
    return list_of_entradas
