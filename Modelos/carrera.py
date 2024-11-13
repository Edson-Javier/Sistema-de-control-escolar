import re
from base_datos.conexion import conectar_bd

class Carrera:
    def __init__(self, nombre_carrera):
        self.nombre_carrera = nombre_carrera
    
    def validar_nombre_carrera(self):
        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\.]+$"
        return re.match(patron, self.nombre_carrera) is not None
    
    # def validar_id(self):
    #     conexion = conectar_bd()
    #     cursor = conexion.cursor()
    #     cursor.execute("SELECT COUNT(*) FROM carrera WHERE id = %s", (self.id,))
    #     resultado = cursor.fetchone()
    #     cursor.close()
    #     conexion.close()

    #     return resultado[0] == 1
    
    def es_valido(self):
        nombre_valido = self.validar_nombre_carrera()
        # id_valido = self.validar_id()
        
        return nombre_valido #and id_valido