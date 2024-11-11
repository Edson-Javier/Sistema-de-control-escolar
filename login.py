import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox
from menu_principal import Menu_principal
from consultas import buscar_registro_usuario

class Menu_login:
    def __init__(self, master):
        self.master = master
        self.master.title("CONTROL ESCOLAR")
        pos_x = (self.master.winfo_screenwidth() - 800) // 2  
        pos_y = (self.master.winfo_screenheight() - 600) // 2
        self.master.geometry(f"800x600+{pos_x}+{pos_y}")


        try:
            self.logo = PhotoImage(file="recursos/logo.png")  
            self.master.iconphoto(False, self.logo)
        except Exception as e:
            print("Error al cargar el logo:", e)

        try:
            self.fondo = PhotoImage(file="recursos/login.png")
            fondo_label = ttkb.Label(self.master, image=self.fondo)
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Error al cargar la imagen de fondo:", e)


        style = ttkb.Style()
        style.configure("Custom.TButton", 
                        background="#222B3A", 
                        width=20, 
                        height=2, 
                        font=("Helvetica", 14, "bold"),
                        borderwidth=0,
                        relief=FLAT)

        style.configure("Custom.TLabel",
                        background="white",
                        foreground="#222B3A", 
                        font=("Helvetica", 13, "bold"))

        style.configure("Custom.TEntry",
                        fieldbackground="#d9d9d9",  
                        font=("Helvetica", 13),
                        foreground="black",
                        borderwidth=0,         
                        highlightthickness=0) 

        # Crear elementos de entrada para usuario y contraseña
        username_label = ttkb.Label(self.master, text="USERNAME", style="Custom.TLabel")
        username_label.place(x=125, y=160)

        self.txUser_id = ttkb.Entry(self.master, style="Custom.TEntry", font=20)
        self.txUser_id.place(x=125, y=180, width=200, height=30)

        password_label = ttkb.Label(self.master, text="PASSWORD", style="Custom.TLabel")
        password_label.place(x=125, y=260)

        self.txPassword = ttkb.Entry(self.master, style="Custom.TEntry", show="•", font=20)
        self.txPassword.place(x=125, y=280, width=200, height=30)

        login_btn = ttkb.Button(self.master, text="LOGIN", style="Custom.TButton", command=self.validar_login)
        login_btn.place(x=100, y=400)

        self.txUser_id.bind('<Return>', lambda event: self.txPassword.focus_set())
        self.txPassword.bind('<Return>', self.validar_login)

    def validar_login(self, event=None):

        id_usuario = self.txUser_id.get()
        password = self.txPassword.get()

        registro = buscar_registro_usuario(id_usuario, password)

        if registro:
            rol = registro['rol']
            nombre = registro['nombre']
            messagebox.showinfo("Inicio de sesion exitoso", "Bienvenido")
            self.master.destroy()
            Menu_principal(id_usuario, nombre, rol)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
