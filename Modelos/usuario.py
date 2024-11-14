import re
from base_datos.conexion import conectar_bd

class Usuario:
    def __init__(self, contrasena, perfil_usuario, correo):
        self.contrasena = contrasena
        self.perfil_usuario = perfil_usuario
        self.correo = correo

    def validar_contrasena(self):        
        patron = r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ\s\#\.\-\!]+$"
        return re.match(patron, self.contrasena) is not None

    def validar_correo(self):
        patron = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, self.correo) is not None
    
    def validar_correo_unico(self):
        conexion = conectar_bd()
        cursor = conexion.cursor()

        query = 'SELECT COUNT(*) from usuario WHERE correo = %s'
        cursor.execute(query, (self.correo,))

        resultado = cursor.fetchone()

        return resultado[0] == 0

    
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
        correo_valido = self.validar_correo()
        correo_unico = self.validar_correo_unico()
        
        return contrasena_valida and correo_valido and correo_unico #and id_valido