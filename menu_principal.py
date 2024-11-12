import tkinter as tk
from tkinter import PhotoImage
import ttkbootstrap as ttkb
from base_datos.conexion import buscar_nombre_usuario

class Menu_principal:
    def __init__(self, id_usuario, rol):
        self.id_usuario = id_usuario
        self.rol = rol
        self.nombre = self.obtener_nombre_usuario(self.rol, self.id_usuario)

        self.main_window = ttkb.Window(themename="flatly")  
        self.main_window.title("Menú Administracion")
        self.main_window.state('zoomed')


        button_style = {
            "width": 20,
            "height": 2,
            "font": ("Georgia", 20),
            "foreground": "white",
            "bg": "#222b3a",
            "relief": "flat"
        }

        try:
            self.logo = PhotoImage(file="recursos/logo.png")  
            self.main_window.iconphoto(False, self.logo)
        except Exception as e:
            print("Error al cargar el logo:", e)
        try:
            self.fondo = PhotoImage(file="recursos/menu_2.png")
            fondo_label = ttkb.Label(self.main_window, image=self.fondo)
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Error al cargar la imagen de fondo:", e)


        ttkb.Label(self.main_window, text=f"Usuario: {self.nombre}", font=("Georgia", 14, "bold"), foreground="white", background="#222b3a").place(x=1150, y=220)
        ttkb.Label(self.main_window, text=f"ID: {self.id_usuario}", font=("Georgia", 14, "bold"), foreground="white", background="#222b3a").place(x=1150, y=250)
        ttkb.Label(self.main_window, text=f"Rol: {self.rol}", font=("Georgia", 14, "bold"), foreground="white", background="#222b3a").place(x=1150, y=280)


        button_frame = ttkb.Frame(self.main_window, padding=20)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


        self.btn_usuarios = tk.Button(button_frame, text="Registrar Usuarios", **button_style, command=self.abrir_registrar_usuario)
        self.btn_usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_alumno = tk.Button(button_frame, text="Registrar Alumno", **button_style, command=self.abrir_registrar_alumno)
        self.btn_alumno.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.btn_profesor = tk.Button(button_frame, text="Registrar Profesor", **button_style, command=self.abrir_registrar_profesor)
        self.btn_profesor.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.btn_materia = tk.Button(button_frame, text="Registrar Materias", **button_style, command=self.abrir_registrar_materia)
        self.btn_materia.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.btn_carrera = tk.Button(button_frame, text="Registrar Carrera", **button_style, command=self.abrir_registrar_carrera)
        self.btn_carrera.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.btn_salon = tk.Button(button_frame, text="Registrar Salon", **button_style, command=self.abrir_registrar_carrera)
        self.btn_salon.grid(row=5, column=0, padx=10, pady=10, sticky="ew")


        self.btn_salir = tk.Button(self.main_window, text="Salir", width=20, height=1, command=self.salir, bg="#dc3545", font=("Georgia", 20))
        self.btn_salir.grid(row=1, column=0, padx=10, pady=10, sticky="s")

        self.main_window.mainloop()

    def salir(self):
        print("Cerrando el menú principal.")
        self.main_window.destroy()

    def abrir_registrar_usuario(self):
        print("Abriendo ventana para registrar usuarios.")

    def abrir_registrar_alumno(self):
        print("Abriendo ventana para registrar alumno.")

    def abrir_registrar_profesor(self):
        print("Abriendo ventana para registrar profesor.")

    def abrir_registrar_materia(self):
        print("Abriendo ventana para registrar materia.")

    def abrir_registrar_carrera(self):
        print("Abriendo ventana para registrar carrera.")

    def obtener_nombre_usuario(self, rol, id_usuario):
        if rol == "Coordinador":
            tabla = "coordinador"

        elif rol == "Maestro":
            tabla = "maestro"

        else:
            tabla = "alumno"

        registro = buscar_nombre_usuario(tabla, id_usuario)
        nombre = registro['nombre']

        return nombre

#si descomentan esta linea se puede visualizar el menu pricipal 1no
#menu = Menu_principal(self.id_usuario, self.rol)
