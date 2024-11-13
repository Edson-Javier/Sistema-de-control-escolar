import re
from base_datos.conexion import conectar_bd

class Profesor:
    def __init__(self, nombre, direccion, telefono, especialidad, contrasena):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.especialidad = especialidad
        self.contrasena = contrasena
    
    def validar_nombre(self):
        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
        return re.match(patron, self.nombre) is not None

    def validar_direccion(self):
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-]+$"
        return re.match(patron, self.direccion) is not None
    
    def validar_telefono(self):
        patron = r"^[0-9]+$"
        return re.match(patron, self.telefono) is not None
    
    def validar_especialidad(self):
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-]+$"
        return re.match(patron, self.especialidad) is not None
    
    def validar_contrasena(self):        
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-\!]+$"
        return re.match(patron, self.especialidad) is not None
    
    
    # def validar_id(self):
    #     conexion = conectar_bd()
    #     cursor = conexion.cursor()
    #     cursor.execute("SELECT COUNT(*) FROM carrera WHERE id = %s", (self.id,))
    #     resultado = cursor.fetchone()
    #     cursor.close()
    #     conexion.close()

    #     return resultado[0] == 1
    
    def es_valido(self):
        nombre_valido = self.validar_nombre()
        direccion_valida = self.validar_direccion()
        telefono_valido = self.validar_telefono()
        especialidad_valida = self.validar_especialidad()  
        contrasena_valida = self.validar_contrasena()
        
        return (nombre_valido and direccion_valida and telefono_valido and 
            especialidad_valida and contrasena_valida)  #and id_valido