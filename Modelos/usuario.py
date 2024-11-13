import re
from base_datos.conexion import conectar_bd

class Usuario:
    def __init__(self, contrasena, perfil_usuario, correo):
        self.contrasena = contrasena
        self.perfil_usuario = perfil_usuario
        self.correo = correo

    def validar_contrasena(self):        
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-\!]+$"
        return re.match(patron, self.especialidad) is not None

    def validar_correo(self):
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-]+$"
        return re.match(patron, self.direccion) is not None
    
    # def validar_id(self):
    #     conexion = conectar_bd()
    #     cursor = conexion.cursor()
    #     cursor.execute("SELECT COUNT(*) FROM carrera WHERE id = %s", (self.id,))
    #     resultado = cursor.fetchone()
    #     cursor.close()
    #     conexion.close()

    #     return resultado[0] == 1
    
    def es_valido(self):
        contrasena_valida = self.validar_contrasena()
        #correo_valido = self.validar_correo()
        
        return contrasena_valida #and correo_valido #and id_valido