import psycopg2
from psycopg2.extras import RealDictCursor

def conectar_bd():
    return psycopg2.connect(
        dbname="sistema_escolar", user="postgres", password="123456", host="localhost"
    )

def crear_registro(tabla, columnas, valores):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    columnas_str = ", ".join(columnas)
    valores_str = ", ".join(["%s"] * len(valores))
    query = f"INSERT INTO {tabla} ({columnas_str}) VALUES ({valores_str})"

    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def buscar_registro(tabla, columna, valor):
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    query = f"SELECT * FROM {tabla} WHERE {columna} = %s"
    cursor.execute(query, (valor,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado is None:
        raise Exception("Registro no encontrado")

    return resultado

def buscar_nombre_usuario(tabla, id_usuario):
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    query = f"SELECT nombre FROM {tabla} WHERE id = %s"
    cursor.execute(query, (id_usuario,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado

def buscar_registro_usuario(id_usuario, password):
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    query = "SELECT * FROM usuario WHERE id = %s AND contrasena = %s"
    cursor.execute(query, (id_usuario, password))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado

def modificar_registro(tabla, id_columna, id_valor, nuevos_valores):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    set_clause = ", ".join([f"{col} = %s" for col in nuevos_valores.keys()])
    query = f"UPDATE {tabla} SET {set_clause} WHERE {id_columna} = %s"
    valores = list(nuevos_valores.values()) + [id_valor]

    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_registro(tabla, columna, valor):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = f"DELETE FROM {tabla} WHERE {columna} = %s"
    cursor.execute(query, (valor,))

    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_siguiente_id(tabla, id_columna):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = f"SELECT MAX({id_columna}) FROM {tabla}"
    cursor.execute(query)
    resultado = cursor.fetchone()[0]

    siguiente_id = 1 if resultado is None else resultado + 1

    cursor.close()
    conexion.close()
    return siguiente_id

def obtener_todos_registros(tabla):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)
    resultado = cursor.fetchall()

    cursor.close()
    conexion.close()
    return resultado