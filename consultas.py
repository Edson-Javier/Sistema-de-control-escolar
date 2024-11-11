import mysql.connector

def conectar_bd():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = '',
        database = ''
    )
    return conexion

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
    cursor = conexion.cursor(dictionary=True)

    query = f"SELECT * FROM {tabla} WHERE {columna} = %s"
    cursor.execute(query, (valor,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado is None:
        raise Exception("Registro no encontrado")

    return resultado

def buscar_registro_usuario(id_usuario, password):
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)

    query = f"SELECT * FROM usuario WHERE ID_Usuario = %s and Password = %s"
    cursor.execute(query, (id_usuario, password,))

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

def eliminar_registro(tabla, columna, valores):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = f"DELETE FROM {tabla} WHERE {columna} = %s"
    cursor.execute(query, (valores,))

    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_siguiente_id(tabla, id_columna):
    conexion = conectar_bd()

    cursor = conexion.cursor()
    query = f"SELECT MAX({id_columna}) FROM {tabla}"
    cursor.execute(query)
    resultado = cursor.fetchone()[0]

    if resultado is None:
        siguiente_id = 1
    else:
        siguiente_id = resultado + 1

    return siguiente_id

def obtener_todos_registros(tabla):
    conexion = conectar_bd()

    cursor = conexion.cursor(dictionary=True)
    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)

    resultado = cursor.fetchall()

    return resultado
