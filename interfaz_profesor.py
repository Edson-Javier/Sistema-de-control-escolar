import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import ttkbootstrap as ttkb
from Modelos.profesor import Profesor
from Modelos.usuario import Usuario
from base_datos.conexion import conectar_bd, buscar_registro, crear_registro, obtener_siguiente_id, modificar_registro, eliminar_registro

class ProfesorInterfaz:
    def __init__(self):
        self.window = ttkb.Window(themename="flatly")
        self.window.title("Profesores")
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


        ttkb.Label(self.window, text="Gestión de Profesores", font=("Georgia", 18, "bold"), foreground="white", background="#222b3a").place(x=100, y=25)
        button_style = {
            "width": 25,
            "padding": (10, 5) 
        }

        ttkb.Label(self.window, text="Buscar Profesor:", font=("Georgia", 12, "bold"), foreground="White", background="#222b3a").place(x=750, y=25)
        self.buscar_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.buscar_entry.place(x=900, y=25, width=300)

        self.btn_buscar = ttkb.Button(self.window, text="Buscar", style="secondary.TButton", command=self.buscar)
        self.btn_buscar.place(x=1220, y=27)



        columns = ("id", "nombre", "direccion", "telefono", "especialidad", "correo")
        self.tree = ttkb.Treeview(self.window, columns=columns, show="headings", height=8, style="mystyle.Treeview")
        

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("direccion", text="Dirección")
        self.tree.heading("telefono", text="Teléfono")
        self.tree.heading("especialidad", text="Especialidad")
        self.tree.heading("correo", text="Correo")


        self.tree.column("id", width=25, anchor="center")
        self.tree.column("nombre", width=100, anchor="center")
        self.tree.column("direccion", width=100, anchor="center")
        self.tree.column("telefono", width=100, anchor="center")
        self.tree.column("especialidad", width=100, anchor="center")
        self.tree.column("correo", width=100, anchor="center")


        style = ttk.Style()
        style.configure("mystyle.Treeview", 
                        background="#e0e0e0", 
                        foreground="black", 
                        rowheight=25, 
                        fieldbackground="#e0e0e0")
        style.configure("mystyle.Treeview.Heading", font=("Georgia", 12, "bold"))


        self.tree.place(x=725, y=150, width=600, height=400)
        scrollbar = ttkb.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=1325, y=150, height=400)

        self.tree.bind("<Double-1>", self.seleccionar_fila)

        self.mostrar_todos_registros()


        #ID
        ttkb.Label(self.window, text="ID Profesor:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=150)
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

        #Especialidad
        ttkb.Label(self.window, text="Especialidad:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=350)
        self.especialidades = ["Matemáticas", "Ciencias", "Lengua", "Historia", "Educación Física", "Arte"]
        self.especialidad_combobox = ttkb.Combobox(self.window, values=self.especialidades, font=("Georgia", 12), state="readonly")
        self.especialidad_combobox.place(x=400, y=350, width=300)

        ttkb.Label(self.window, text="Contraseña:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=400)
        self.contraseña_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.contraseña_entry.place(x=400, y=400, width=300)

        ttkb.Label(self.window, text="Correo:", font=("Georgia", 12, "bold"), foreground="black").place(x=200, y=450)
        self.correo_entry = ttkb.Entry(self.window, font=("Georgia", 12))
        self.correo_entry.place(x=400, y=450, width=300)



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
        id_profesor = self.buscar_entry.get()

        try:
            id_profesor_int = int(id_profesor)
        except:
            messagebox.showerror("Error", "El ID de Profesor debe ser numerico")
            return

        try:
            profesor_encontrado = buscar_registro("maestro", "id", id_profesor_int)
            usuario_encontrado = buscar_registro("usuario", "id", id_profesor_int)
            self.mostrar(profesor_encontrado, usuario_encontrado)
        except Exception as e:
            messagebox.showwarning("No encontrado", f"No se ha encontrado el cliente, error: {e}")
            return

    def mostrar(self, profesor, usuario):
        self.limpiar_tabla()

        id_profesor = profesor['id']
        nombre = profesor['nombre']
        direccion = profesor['direccion']
        telefono = profesor['telefono']
        especialidad = profesor['especialidad']
        correo = usuario['correo']

        self.tree.insert("", 0, values=(id_profesor, nombre, direccion, telefono, especialidad, correo))

    def nuevo(self):
        self.clear_fields()
        print()

    def guardar(self):
        nombre = self.nombre_entry.get().strip()
        direccion = self.direccion_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        especialidad = self.especialidad_combobox.get().strip()
        contrasena = self.contraseña_entry.get().strip()
        correo = self.correo_entry.get().strip()
        rol = "Profesor"

        self.clear_fields()

        profesor = Profesor(nombre, direccion, telefono, especialidad,contrasena)
        usuario = Usuario(contrasena, rol, correo) #Falta Correo

        try:
            telefono_int = int(telefono)
        except:
            messagebox.showerror("Error", "El telefono debe poseer solo valores numericos")
            return

        if profesor.es_valido() and usuario.es_valido():
            columnas_usuario = ("contrasena", "perfil_usuario", "correo")
            valores_usuario = (contrasena, rol, correo)

            id_profesor = obtener_siguiente_id("usuario", "id")

            columnas_profesor = ("id", "nombre", "direccion", "telefono", "especialidad")
            valores_profesor = (id_profesor, nombre, direccion, telefono_int, especialidad)

            try:
                crear_registro("usuario", columnas_usuario, valores_usuario)
                crear_registro("maestro", columnas_profesor, valores_profesor)
                messagebox.showinfo(message="Profesor creado satisfactoriamente.")
                self.mostrar_todos_registros()
            except Exception as e:
                messagebox.showerror(message=f"No se pudo registrar al Profesor. Intente nuevamente. Error: {e}")
                return
        else:
            messagebox.showerror(message="Datos del profesor invalidos o repetidos. Intente nuevamente.")
            return
    
    def editar(self):
        id_profesor = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        direccion = self.direccion_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        especialidad = self.especialidad_combobox.get().strip()
        contrasena = self.contraseña_entry.get().strip()
        correo = self.correo_entry.get().strip()

        try:
            id_profesor_int = int(id_profesor)
        except:
            messagebox.showerror("Error", "El id del profesor debe ser numerico")
            return

        try:
            telefono_int = int(telefono)
        except:
            messagebox.showerror("Error", "El telefono debe ser numerico")
            return


        if contrasena:
            profesor = Profesor(nombre, direccion, telefono, especialidad, contrasena)

            if profesor.es_valido():
                nuevos_datos_profesor = {"nombre": nombre,
                                "direccion": direccion,
                                "telefono": telefono_int,
                                "especialidad": especialidad}
                
                nuevos_datos_usuario = {"contrasena": contrasena,
                                        "correo": correo}
            else:
                messagebox.showerror("Error", "Los datos del Profesor no son validos")
                return
                
                
        else:
            profesor = Profesor.sin_contrasena(nombre, direccion, telefono, especialidad)

            if profesor.es_valido():
                nuevos_datos_profesor = {"nombre": nombre,
                                "direccion": direccion,
                                "telefono": telefono_int,
                                "especialidad": especialidad}
                
                nuevos_datos_usuario = {"correo": correo}

        try:
            modificar_registro("usuario", "id", id_profesor_int, nuevos_datos_usuario)
            modificar_registro("maestro", "id", id_profesor_int, nuevos_datos_profesor)

            registro_profesor = buscar_registro("maestro", "id", id_profesor_int)
            registro_usuario = buscar_registro("usuario", "id", id_profesor_int)

            self.mostrar(registro_profesor, registro_usuario)
            self.clear_fields()
            messagebox.showinfo("Modificacion realizada", "Los datos del Profesor han sido modificados adecuadamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se ha podido modificar los datos del Profesor. Error {e}")
            return


    def eliminar(self):
        id_profesor = self.id_entry.get()

        try:
            id_profesor_int = int(id_profesor)
        except:
            messagebox.showerror("Error", "El ID de Profesor debe ser solo numerico")
            return

        try:
            eliminar_registro("maestro", "id", id_profesor_int)
            eliminar_registro("usuario", "id", id_profesor_int)
            
            self.mostrar_todos_registros()
            self.clear_fields()
            messagebox.showinfo("Profesor eliminado", "Se ha eliminado al Profesor de la base de datos")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar los datos del Profesor. Error: {e}")
            return

    def clear_fields(self):
        """Limpia los campos de entrada."""
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, tk.END)
        self.id_entry.config(state="readonly")

        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)

        self.especialidad_combobox.config(state="normal")
        self.especialidad_combobox.delete(0, tk.END)
        self.especialidad_combobox.config(state="readonly")

        self.contraseña_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
    
    def limpiar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def seleccionar_fila(self, evento):
        fila_seleccionada = self.tree.selection()

        if fila_seleccionada:
            valores = self.tree.item(fila_seleccionada, "values")

            self.id_entry.config(state="normal")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, valores[0])
            self.id_entry.config(state="readonly")

            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, valores[1])

            self.direccion_entry.delete(0, tk.END)
            self.direccion_entry.insert(0, valores[2])

            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, valores[3])

            self.especialidad_combobox.config(state="normal")
            self.especialidad_combobox.delete(0, tk.END)
            self.especialidad_combobox.insert(0, valores[4])
            self.especialidad_combobox.config(state="readonly")

            self.correo_entry.delete(0, tk.END)
            self.correo_entry.insert(0, valores[5])

    
    def mostrar_todos_registros(self):
        # Limpiar el Treeview antes de insertar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        conexion = conectar_bd()
        cursor = conexion.cursor()
        
        # Consulta que une las dos tablas basándose en el id de maestro
        cursor.execute("""
            SELECT m.id, m.nombre, m.direccion, m.telefono, m.especialidad, u.correo
            FROM maestro AS m
            JOIN usuario AS u ON m.id = u.id
        """)
        
        registros = cursor.fetchall()

        # Imprimir registros para depurar
        print("Registros obtenidos:", registros)
        
        # Insertar cada registro en el Treeview
        for registro in registros:
            self.tree.insert("", "end", values=registro)
    
        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()
    
    def entry_buscar_vacio(self, evento):
        texto = self.nombre_entry.get().strip()
        if not texto:  # Si el campo está vacío
            self.mostrar_todos_registros()
            

ProfesorInterfaz()


