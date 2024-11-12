import tkinter as tk
from tkinter import ttk, PhotoImage
import ttkbootstrap as ttkb

class CarreraInterfaz:
    def __init__(self):
        self.window = ttkb.Window(themename="flatly")
        self.window.title("Carrera")
        self.window.state("zoomed")
        #self.window.configure(bg="#222b3a")

        try:
            self.logo = PhotoImage(file="recursos/logo.png")  
            self.window.iconphoto(False, self.logo)
        except Exception as e:
            print("Error al cargar el logo:", e)
        try:
            self.fondo = PhotoImage(file="recursos/reg_profesores.png")
            fondo_label = ttkb.Label(self.window, image=self.fondo)
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Error al cargar la imagen de fondo:", e)


        ttkb.Label(self.window, text="Registro de carrera", font=("Georgia", 18, "bold"), foreground="white", background="#222b3a").place(x=100, y=25)
        button_style = {
            "width": 25,
            "padding": (10, 5) 
        }

        ttkb.Label(self.window, text="Buscar Carrera:", font=("Georgia", 12, "bold"), foreground="White", background="#222b3a").place(x=750, y=25)
        self.buscar_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.buscar_entry.place(x=900, y=25, width=300)

        self.btn_buscar = ttkb.Button(self.window, text="Buscar", style="secondary.TButton", command=self.buscar)
        self.btn_buscar.place(x=1220, y=25)


        columns = ("id", "nombre")
        self.tree = ttkb.Treeview(self.window, columns=columns, show="headings", height=8, style="mystyle.Treeview")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.column("id", width=300, anchor="center")
        self.tree.column("nombre", width=300, anchor="center")
        style = ttk.Style()
        style.configure("mystyle.Treeview", 
                        background="#e0e0e0", 
                        foreground="black", 
                        rowheight=25, 
                        fieldbackground="#e0e0e0")
        style.configure("mystyle.Treeview.Heading", font=("Georgia", 12, "bold"))


        self.tree.place(x=200, y=250, width=600, height=300)
        scrollbar = ttkb.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=800, y=250, height=300)


        #ID
        ttkb.Label(self.window, text="ID Carrera:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=150)
        self.id_entry = ttkb.Entry(self.window, font=("Georgia", 12), state="readonly")
        self.id_entry.place(x=400, y=150, width=300)

        #Nombre
        ttkb.Label(self.window, text="Nombre:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=200)
        self.nombre_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.nombre_entry.place(x=400, y=200, width=300)



        self.btn_nuevo = ttkb.Button(self.window, text="Nuevo", style="info.TButton", command=self.nuevo, **button_style)
        self.btn_nuevo.place(x=200, y=600)

        self.btn_guardar = ttkb.Button(self.window, text="Guardar", style="success.TButton", command=self.guardar, **button_style)
        self.btn_guardar.place(x=400, y=600)

        self.btn_editar = ttkb.Button(self.window, text="Editar", style="warning.TButton", command=self.editar, **button_style)
        self.btn_editar.place(x=600, y=600)

        self.btn_eliminar = ttkb.Button(self.window, text="Eliminar", style="danger.TButton", command=self.eliminar, **button_style)
        self.btn_eliminar.place(x=800, y=600)

        # Botón de Salir
        self.btn_salir = ttkb.Button(self.window, text="Salir", style="secondary.TButton", command=self.window.quit, width=20)
        self.btn_salir.place(x=1000, y=600)

        self.window.mainloop()

    def buscar(self):
        print("Buscando profesor...")

    def nuevo(self):
        self.clear_fields()
        print("Creando nuevo profesor")
        self.clear_fields()

    def guardar(self):
        print("Guardando información del profesor")

    def editar(self):
        print("Editando información del profesor")

    def eliminar(self):
        print("Eliminando profesor")

    def clear_fields(self):
        """Limpia los campos de entrada."""
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, tk.END)
        self.id_entry.config(state="readonly")
        self.nombre_entry.delete(0, tk.END)


#comentar o descomentar
CarreraInterfaz()
