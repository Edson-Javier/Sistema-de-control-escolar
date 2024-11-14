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
        
        # Verifica si la contraseña existe antes de validar
        contrasena_valida = self.validar_contrasena() if hasattr(self, 'contrasena') else True
        
        return (nombre_valido and direccion_valida and telefono_valido and 
                especialidad_valida and contrasena_valida)
    
    @classmethod
    def sin_contrasena(cls, nombre, direccion, telefono, especialidad):
        # Constructor alternativo que no define el atributo `contrasena`
        instancia = cls.__new__(cls)  # Crear instancia sin llamar a __init__
        instancia.nombre = nombre
        instancia.direccion = direccion
        instancia.telefono = telefono
        instancia.especialidad = especialidad
        return instancia