import sqlite3
from tkinter import Tk, Button, Frame, Label, Entry, ttk, messagebox, StringVar, OptionMenu
from config.config import DB_PATH  # Ruta de la base de datos

# Conexión a la base de datos
def conectar_base_datos():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Error de Base de Datos", f"Error al conectar con la base de datos: {e}")

# Crear ventana principal
def ventana_administracion(callback):
    ventana = Tk()
    ventana.title("Administración del Sistema")
    ventana.state("zoomed")  # Abrir ventana en pantalla completa
    ventana.configure(bg="#272643")
    
    # Botones principales
    frame_botones_principales = Frame(ventana, bg="#2c698d", height=100)  # Ajustar altura
    frame_botones_principales.pack(side="top", fill="x")  # Garantizar que esté en la parte superior
    
    # Contenedor principal dinámico
    frame_contenido = Frame(ventana, bg="#272643")
    frame_contenido.pack(fill="both", expand=True, padx=20, pady=20)  # Debajo del frame de botones

    # Función para limpiar el contenido dinámico
    def limpiar_contenido():
        for widget in frame_contenido.winfo_children():
            widget.destroy()

    # Función: Cargar vista de "Registro"
    def cargar_registro():
        limpiar_contenido()
        

        # Botones del módulo "Registro"
        frame_botones = Frame(frame_contenido, bg="#272643")
        frame_botones.pack(side="top", fill="x")

        Button(frame_botones, text="Crear Usuario", font=("Segoe UI", 12), bg="#bae8e8", command=crear_usuario_vista).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Modificar Contraseña", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: messagebox.showinfo("Modificar Contraseña", "Función en desarrollo")).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Resetear Contraseña", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: messagebox.showinfo("Resetear Contraseña", "Función en desarrollo")).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Eliminar Usuario", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: messagebox.showinfo("Eliminar Usuario", "Función en desarrollo")).pack(side="left", padx=10, pady=10)

        # Tabla de credenciales
        Label(frame_contenido, text="Consultar Credenciales", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)
        
        frame_tabla = Frame(frame_contenido, bg="#272643")
        frame_tabla.pack(fill="both", expand=True)

        # Barra de búsqueda
        Label(frame_tabla, text="Buscar:", font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        busqueda_var = StringVar()
        Entry(frame_tabla, textvariable=busqueda_var, width=30).grid(row=0, column=1, padx=10, pady=5, sticky="w")
        Button(frame_tabla, text="Buscar", command=lambda: cargar_datos(tabla, busqueda_var.get())).grid(row=0, column=2, padx=10, pady=5)

        # Tabla
        columnas = ("cedula", "apellidos", "nombres", "usuario", "rol")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        tabla.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        for col in columnas:
            tabla.heading(col, text=col.capitalize())

        frame_tabla.grid_rowconfigure(1, weight=1)
        frame_tabla.grid_columnconfigure(0, weight=1)

        cargar_datos(tabla)

    # Función: Cargar datos en la tabla
    def cargar_datos(tabla, filtro=""):
        conn = conectar_base_datos()
        if not conn:
            return

        cursor = conn.cursor()
        query = "SELECT cedula, apellidos, nombres, usuario, rol FROM usuarios"
        if filtro:
            query += " WHERE cedula LIKE ? OR apellidos LIKE ? OR nombres LIKE ?"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)

        datos = cursor.fetchall()
        conn.close()

        # Limpiar tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Insertar datos
        for fila in datos:
            tabla.insert("", "end", values=fila)

    # Función: Crear usuario (vista y funcionalidad)
    def crear_usuario_vista():
        limpiar_contenido()

        Label(frame_contenido, text="Crear Usuario", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Campos de entrada
        frame_formulario = Frame(frame_contenido, bg="#272643")
        frame_formulario.pack(pady=10)

        campos = ["Cédula", "Apellidos", "Nombres", "Usuario", "Contraseña", "Rol"]
        entradas = {}

        for i, campo in enumerate(campos):
            Label(frame_formulario, text=campo, font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if campo == "Rol":
                rol_var = StringVar()
                rol_var.set("Usuario")
                entrada = OptionMenu(frame_formulario, rol_var, "Administrador", "Usuario")
                entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
                entradas[campo] = rol_var
            else:
                entrada = Entry(frame_formulario, width=30, show="*" if campo == "Contraseña" else None)
                entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
                entradas[campo] = entrada

        # Botón para guardar usuario
        Button(frame_contenido, text="Guardar Usuario", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: guardar_usuario(entradas)).pack(pady=10)

    # Función: Guardar usuario en la base de datos
    def guardar_usuario(entradas):
        datos = {campo: entrada.get() if isinstance(entrada, Entry) else entrada.get() for campo, entrada in entradas.items()}

        # Validación de campos vacíos
        if any(not valor for valor in datos.values()):
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        conn = conectar_base_datos()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (cedula, apellidos, nombres, usuario, contrasena, rol) VALUES (?, ?, ?, ?, ?, ?)",
                (datos["Cédula"], datos["Apellidos"], datos["Nombres"], datos["Usuario"], datos["Contraseña"], datos["Rol"])
            )
            conn.commit()
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
            cargar_registro()
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al guardar el usuario: {e}")
        finally:
            conn.close()

    # Función: Cargar vista de "Auditoría"
    def cargar_auditoria():
        limpiar_contenido()
        Label(frame_contenido, text="Auditoría - Funcionalidad en desarrollo", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=20)

    # Función: Cargar vista de "Gestión de Logs"
    def cargar_logs():
        limpiar_contenido()
        Label(frame_contenido, text="Gestión de Logs - Funcionalidad en desarrollo", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=20)

    

    Button(frame_botones_principales, text="Registro", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_registro, padx=20, pady=10).pack(side="left", padx=10)
    Button(frame_botones_principales, text="Auditoría", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_auditoria, padx=20, pady=10).pack(side="left", padx=10)
    Button(frame_botones_principales, text="Gestión de Logs", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_logs, padx=20, pady=10).pack(side="left", padx=10)

    # Botón "Regresar al Menú Principal"
    Button(frame_botones_principales, text="Regresar al Menú Principal", font=("Segoe UI", 14), bg="#d9534f", fg="white", padx=20, pady=10, command=lambda: regresar(callback, ventana)).pack(side="right", padx=10)

    ventana.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal