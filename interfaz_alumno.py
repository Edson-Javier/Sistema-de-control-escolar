import tkinter as tk
from tkinter import ttk, PhotoImage
import ttkbootstrap as ttkb

class AlumnoInterfaz:
    def __init__(self):
        self.window = ttkb.Window(themename="flatly")
        self.window.title("Alumnos")
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


        ttkb.Label(self.window, text="Gestión de Alumnos", font=("Georgia", 18, "bold"), foreground="white", background="#222b3a").place(x=100, y=25)
        button_style = {
            "width": 25,
            "padding": (10, 5) 
        }

        ttkb.Label(self.window, text="Buscar Alumno:", font=("Georgia", 12, "bold"), foreground="White", background="#222b3a").place(x=750, y=25)
        self.buscar_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.buscar_entry.place(x=900, y=25, width=300)

        self.btn_buscar = ttkb.Button(self.window, text="Buscar", style="primary.TButton", command=self.buscar)
        self.btn_buscar.place(x=1220, y=25)


# Tabla Treeview para mostrar profesores justo debajo de la barra de búsqueda
        columns = ("id", "nombre", "direccion", "telefono", "semestre", "estatus", "carrera")
        self.tree = ttkb.Treeview(self.window, columns=columns, show="headings", height=8, style="mystyle.Treeview")
        
        # Definir encabezados de columna
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("direccion", text="Dirección")
        self.tree.heading("telefono", text="Teléfono")
        self.tree.heading("semestre", text="Semestre")
        self.tree.heading("estatus", text="Estatus")
        self.tree.heading("carrera", text="Carrera")

        # Configurar tamaño de las columnas
        self.tree.column("id", width=25, anchor="center")
        self.tree.column("nombre", width=100, anchor="center")
        self.tree.column("direccion", width=100, anchor="center")
        self.tree.column("telefono", width=60, anchor="center")
        self.tree.column("semestre", width=25, anchor="center")
        self.tree.column("estatus", width=25, anchor="center")
        self.tree.column("carrera", width=25, anchor="center")

        # Aplicar estilo para fondo oscuro en el Treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", 
                        background="#e0e0e0", 
                        foreground="black", 
                        rowheight=25, 
                        fieldbackground="#e0e0e0")
        style.configure("mystyle.Treeview.Heading", font=("Georgia", 12, "bold"))

        # Agregar tabla a la ventana con scrollbar
        self.tree.place(x=725, y=200, width=600, height=280)
        scrollbar = ttkb.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=1325, y=200, height=280)


        #ID
        ttkb.Label(self.window, text="ID Alumno:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=150)
        self.id_entry = ttkb.Entry(self.window, font=("Georgia", 12), state="readonly")
        self.id_entry.place(x=400, y=150, width=300)

        #Nombre
        ttkb.Label(self.window, text="Nombre:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=200)
        self.nombre_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.nombre_entry.place(x=400, y=200, width=300)

        #Dirección
        ttkb.Label(self.window, text="Dirección:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=250)
        self.direccion_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.direccion_entry.place(x=400, y=250, width=300)

        #Telefono
        ttkb.Label(self.window, text="Teléfono:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=300)
        self.telefono_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.telefono_entry.place(x=400, y=300, width=300)

        #Semestre
        ttkb.Label(self.window, text="Semestre:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=350)
        self.semestre = ["Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto"]
        self.semestre_combobox = ttkb.Combobox(self.window, values=self.semestre, font=("Georgia", 12), state="readonly")
        self.semestre_combobox.place(x=400, y=350, width=300)

        #Estatus
        ttkb.Label(self.window, text="Estatus:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=400)
        self.estatus = ["Activo", "Inactivo"]
        self.estatus_combobox = ttkb.Combobox(self.window, values=self.estatus, font=("Georgia", 12), state="readonly")
        self.estatus_combobox.place(x=400, y=400, width=300)

        #Carrera
        ttkb.Label(self.window, text="Carrera:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=450)
        self.carrera = ["INCO", "INNI", "INFO"] ###############################################
        self.carrera_combobox = ttkb.Combobox(self.window, values=self.carrera, font=("Georgia", 12), state="readonly")
        self.carrera_combobox.place(x=400, y=450, width=300)

        #Contraseña
        ttkb.Label(self.window, text="Contraseña:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=500)
        self.contraseña_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.contraseña_entry.place(x=400, y=500, width=300)



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
        print("Creando nuevo profesor")

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
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.estatus_combobox.set("")
        self.semestre_combobox.set("")
        self.carrera_combobox.set("")
        self.buscar_entry.delete(0, tk.END)
        self.contraseña_entry.delete(0, tk.END)

    def on_tree_select(self, event):
        #obtener el seleccionado
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            data = item["values"]

            self.id_entry.config(state="normal")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, data[0])  
            self.id_entry.config(state="readonly")
            
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, data[1])  
            
            self.direccion_entry.delete(0, tk.END)
            self.direccion_entry.insert(0, data[2])  
            
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, data[3])  
            
            self.especialidad_combobox.set(data[4])   


#comentar o descomentar
AlumnoInterfaz()
