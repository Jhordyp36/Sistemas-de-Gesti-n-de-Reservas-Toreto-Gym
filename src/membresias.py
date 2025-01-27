import csv
import datetime
from datetime import datetime
import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from src.utils.helpers import cargar_icono, centrar_ventana, verifica_identificacion, verifica_correo, verifica_telefono, verifica_nombres_apellidos, verifica_fecha_nacimiento, verifica_usuario
from config.config import DB_PATH, ICONS_DIR

def conexion_db():
    """Conectar a la base de datos SQLite y devolver la conexión."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
    
def cargar_datos_asistencias(tabla, filtro=""):
    conn = conexion_db()  # Establecer conexión con la base de datos
    if not conn:
        return

    cursor = conn.cursor()

    # Usar LEFT JOIN para incluir todos los usuarios, incluso si no tienen registro de asistencia
    query = '''
        SELECT usuarios.cedula, usuarios.apellidos, usuarios.nombres, 
               COALESCE(historial_asistencias.asistencia, 'No') AS asistencia
        FROM usuarios
        LEFT JOIN historial_asistencias ON usuarios.cedula = historial_asistencias.cedula
        WHERE usuarios.rol = 'Cliente'  -- Filtramos por rol 'Cliente'
    '''

    if filtro:
        query += " AND (usuarios.cedula LIKE ? OR usuarios.apellidos LIKE ? OR usuarios.nombres LIKE ?)"
        cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
    else:
        cursor.execute(query)

    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de insertar los nuevos datos
    for item in tabla.get_children():
        tabla.delete(item)

    # Insertar los datos obtenidos en la tabla
    for fila in datos:
        tabla.insert("", "end", values=fila)
        

def cargar_datos_edicion(tabla, filtro=""):
    conn = conexion_db()  # Establecer conexión con la base de datos
    if not conn:
        return

    cursor = conn.cursor()

    # Usar LEFT JOIN para incluir todos los usuarios, incluso si no tienen registro de asistencia
    query = '''
        SELECT usuarios.cedula, usuarios.apellidos, usuarios.nombres, 
               usuarios.correo, usuarios.telefono, usuarios.fecha_nacimiento
        FROM usuarios
        WHERE usuarios.rol = 'Cliente'  -- Filtramos por rol 'Cliente'
    '''

    if filtro:
        query += " AND (usuarios.cedula LIKE ? OR usuarios.apellidos LIKE ? OR usuarios.nombres LIKE ?)"
        cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
    else:
        cursor.execute(query)

    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de insertar los nuevos datos
    for item in tabla.get_children():
        tabla.delete(item)

    # Insertar los datos obtenidos en la tabla
    for fila in datos:
        tabla.insert("", "end", values=fila)

def registrar_cliente(actual, tree_clientes):
    def guardar_cliente():
        # Obtener los valores del formulario
        cedula = entry_cedula.get().strip()  # Obtener la cédula
        cedula = str(cedula).zfill(10)  # Asegurarse de que la cédula tenga 10 dígitos con ceros a la izquierda
        nombres = entry_nombres.get().strip()
        apellidos = entry_apellidos.get().strip()
        usuario = entry_usuario.get().strip()
        contrasena = None
        correo = entry_correo.get().strip()
        telefono = entry_telefono.get().strip()
        fecha_nacimiento = entry_fecha_nacimiento.get().strip()

        # Validaciones
        if not verifica_identificacion(cedula):
            messagebox.showerror("Error", "La cédula ingresada no es válida.")
            return

        if not verifica_nombres_apellidos(nombres) or not verifica_nombres_apellidos(apellidos):
            messagebox.showerror("Error", "Los nombres y apellidos deben ser válidos.")
            return
        
        if not verifica_usuario(usuario):
            messagebox.showerror("Error", "El usuario debe ser válido.")
            return

        if not verifica_correo(correo):
            messagebox.showerror("Error", "El correo electrónico no es válido.")
            return

        if not verifica_telefono(telefono):
            messagebox.showerror("Error", "El número de teléfono no es válido.")
            return

        if not verifica_fecha_nacimiento(fecha_nacimiento):
            messagebox.showerror("Error", "La fecha de nacimiento no es válida o la persona es menor de edad.")
            return

        # Guardar en la base de datos
        try:
            conn = conexion_db()
            cursor = conn.cursor()
            # Ejecutar la consulta para obtener la contraseña predeterminada
            cursor.execute("SELECT valor FROM parametros WHERE nombre = 'Contraseña Predeterminada'")
            resultado = cursor.fetchone()  # Obtiene el primer resultado de la consulta
            
            if resultado:
                contrasena = resultado[0]  # Almacena el valor de la contraseña predeterminada
            else:
                raise Exception("No se encontró la contraseña predeterminada en la base de datos.")
            
            cursor.execute(
                """
                INSERT INTO usuarios (cedula, apellidos, nombres, usuario, contrasena, telefono, correo, rol, fecha_nacimiento)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'Cliente', ?)
                """,
                (cedula, apellidos, nombres, usuario, contrasena, telefono, correo, fecha_nacimiento),
            )
            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Creacion: Membresias')", (actual, fecha_hora_actual))

            conn.commit()
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            ventana_registro.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el cliente: {e}")
        finally:
            conn.close()


    # Crear la ventana de registro
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrar Cliente")
    centrar_ventana(ventana_registro, 600, 600)
    ventana_registro.configure(bg="#272643")

    default_font = ("Segoe UI", 12)

    # Etiquetas y campos de entrada
    tk.Label(ventana_registro, text="Cédula:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_cedula = tk.Entry(ventana_registro, font=default_font)
    entry_cedula.pack(pady=5, padx=20, fill="x")

    tk.Label(ventana_registro, text="Nombres:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_nombres = tk.Entry(ventana_registro, font=default_font)
    entry_nombres.pack(pady=5, padx=20, fill="x")

    tk.Label(ventana_registro, text="Apellidos:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_apellidos = tk.Entry(ventana_registro, font=default_font)
    entry_apellidos.pack(pady=5, padx=20, fill="x")
    
    tk.Label(ventana_registro, text="Usuario:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_usuario = tk.Entry(ventana_registro, font=default_font)
    entry_usuario.pack(pady=5, padx=20, fill="x")

    tk.Label(ventana_registro, text="Correo Electrónico:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_correo = tk.Entry(ventana_registro, font=default_font)
    entry_correo.pack(pady=5, padx=20, fill="x")

    tk.Label(ventana_registro, text="Teléfono:", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_telefono = tk.Entry(ventana_registro, font=default_font)
    entry_telefono.pack(pady=5, padx=20, fill="x")

    tk.Label(ventana_registro, text="Fecha de Nacimiento (DD/MM/AAAA):", font=default_font, bg="#272643", fg="#ffffff").pack(pady=5, anchor="w", padx=20)
    entry_fecha_nacimiento = tk.Entry(ventana_registro, font=default_font)
    entry_fecha_nacimiento.pack(pady=5, padx=20, fill="x")

    # Botón para guardar
    btn_guardar = tk.Button(ventana_registro, text="Registrar", font=default_font, bg="#bae8e8", command=guardar_cliente)
    btn_guardar.pack(pady=20)

    ventana_registro.mainloop()
    
def consultar_cliente(entry_buscar, tree_clientes):
    filtro = entry_buscar.get().strip()  # Obtén el texto de la barra de búsqueda

    # Llamar a la función cargar_datos_asistencias con el filtro
    cargar_datos_asistencias(tree_clientes, filtro)

# Editar Cliente - Ahora recibe los parámetros necesarios
def editar_cliente(entries, tree_editar):
    # Obtenemos la cédula almacenada
    cedula = cédula_seleccionada.get()
    apellidos_ingresados = entries["Apellidos"].get()
    nombres_ingresados = entries["Nombres"].get()
    correo_ingresado = entries["Correo"].get()
    telefono_ingresado = entries["Teléfono"].get().strip()  # Asegurarnos de quitar espacios

    # Obtener la cédula del usuario seleccionado
    selected_item = tree_editar.selection()
    if not selected_item:
        messagebox.showwarning("Advertencia", "Debe seleccionar un cliente para editar.")
        return
    
    cedula = tree_editar.item(selected_item[0])['values'][0]

    # Verificar si los datos realmente cambiaron
    cliente_actual = tree_editar.item(selected_item[0])['values']
    apellidos_actual = cliente_actual[1]
    nombres_actual = cliente_actual[2]
    correo_actual = cliente_actual[3]
    telefono_actual = cliente_actual[4]

    # Verificar si hay algún cambio
    if (apellidos_ingresados == apellidos_actual and 
        nombres_ingresados == nombres_actual and 
        correo_ingresado == correo_actual and 
        telefono_ingresado == telefono_actual):
        messagebox.showinfo("Sin cambios", "No se han realizado cambios en la información.")
        return
    
    # Validar que el teléfono tenga 10 dígitos numéricos
    if not verifica_telefono(telefono_ingresado):
        messagebox.showerror("Error", "El teléfono debe tener 10 dígitos numéricos.")
        return

    # Verificar que el correo sea válido
    if not verifica_correo(correo_ingresado):
        messagebox.showerror("Error", "El correo es inválido.")
        return

    # Verificar que los nombres y apellidos no estén vacíos
    if not verifica_nombres_apellidos(nombres_ingresados) or not verifica_nombres_apellidos(apellidos_ingresados):
        messagebox.showerror("Error", "El nombre o apellido son inválidos.")
        return
    
    # Actualizamos los datos en la base de datos
    actualizar_cliente_en_base_de_datos(cedula, apellidos_ingresados, nombres_ingresados, correo_ingresado, telefono_ingresado)
    
    # Actualizar la tabla
    actualizar_tabla(tree_editar)
    
    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Los datos del cliente han sido actualizados con éxito.")

# Función para actualizar la tabla
def actualizar_tabla(tree_editar):
    # Limpiar la tabla actual
    for item in tree_editar.get_children():
        tree_editar.delete(item)
    
    # Aquí debes cargar nuevamente los datos de la base de datos
    cargar_datos_edicion(tree_editar)

def actualizar_cliente_en_base_de_datos(cedula, apellidos, nombres, correo, telefono):
    
    conn = conexion_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE usuarios SET apellidos = ?, nombres = ?, correo = ?, telefono = ? WHERE cedula = ?''', (apellidos, nombres, correo, telefono, cedula))
    conn.commit()
    conn.close()
def mostrar_mensaje(mensaje):
    # Esta función muestra los mensajes en un cuadro de diálogo o ventana emergente
    messagebox.showinfo("Información", mensaje)

def registrar_asistencia(cedula, tabla):
    fecha_actual = datetime.now().strftime('%Y-%m-%d')  # Fecha actual
    asistencia = "Si"  # Asistencia marcada como "Si"

    conn = conexion_db()
    cursor = conn.cursor()

    # Verificar si ya existe un registro para esa cédula y fecha con asistencia marcada como "Si"
    cursor.execute('''SELECT id FROM historial_asistencias WHERE cedula = ? AND fecha = ? AND asistencia = 'Si' ''', (cedula, fecha_actual))
    resultado = cursor.fetchone()

    if resultado:
        # Si ya está registrada la asistencia, mostramos un mensaje
        messagebox.showinfo("Asistencia ya registrada", "La asistencia ya ha sido registrada para este usuario hoy.")
    else:
        # Verificar si ya existe un registro para esa cédula y fecha
        cursor.execute('''SELECT id FROM historial_asistencias WHERE cedula = ? AND fecha = ? ''', (cedula, fecha_actual))
        resultado = cursor.fetchone()

        if resultado:
            # Si existe, actualiza la asistencia
            cursor.execute('''UPDATE historial_asistencias SET asistencia = ? WHERE cedula = ? AND fecha = ? ''', (asistencia, cedula, fecha_actual))
        else:
            # Si no existe, inserta un nuevo registro
            cursor.execute('''INSERT INTO historial_asistencias (cedula, fecha, asistencia) VALUES (?, ?, ?)''', (cedula, fecha_actual, asistencia))

        conn.commit()  # Asegúrate de hacer commit para guardar los cambios
        conn.close()

        # Recargar los datos en la tabla de la interfaz
        cargar_datos_asistencias(tabla)  # Esto debería actualizar la tabla con la nueva información

def consultar_historial_asistencias(tree_clientes, root):
    # Obtener la cédula del usuario seleccionado en la tabla inicial
    selected_item = tree_clientes.selection()
    if not selected_item:
        messagebox.showwarning("Advertencia", "Debe seleccionar un usuario para consultar su historial.")
        return

    cedula_usuario = tree_clientes.item(selected_item[0])['values'][0]

    conn = conexion_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM historial_asistencias WHERE cedula = ?", (cedula_usuario,))
        historial = cursor.fetchall()

        if not historial:
            messagebox.showinfo("Sin historial", "No existe historial de asistencias para este usuario.")
            return

        # Crear ventana modal (siempre por encima)
        historial_ventana = tk.Toplevel(root)
        historial_ventana.title("Historial de Asistencias")
        centrar_ventana(historial_ventana, 500, 300)
        historial_ventana.configure(bg="#272643")
        historial_ventana.resizable(False, False)

        # Configuración de la ventana para que siempre esté encima y no se pueda maximizar
        historial_ventana.attributes("-topmost", True)  # Ventana siempre encima
        historial_ventana.protocol("WM_DELETE_WINDOW", historial_ventana.destroy)  # Cerrar con X

        # Título de la ventana
        label_historial = tk.Label(historial_ventana, text="Historial de Asistencias", font=("Segoe UI", 14, "bold"), bg="#272643", fg="#ffffff")
        label_historial.pack(pady=10)

        # Crear la tabla para mostrar el historial de asistencias
        columns_historial = ("Fecha", "Asistencia")
        tree_historial = ttk.Treeview(historial_ventana, columns=columns_historial, show="headings", height=10)

        for col in columns_historial:
            tree_historial.heading(col, text=col)
            tree_historial.column(col, anchor="center", width=150)

        tree_historial.pack(pady=10, padx=10)

        # Llenamos la tabla con los datos del historial de asistencias
        for record in historial:
            tree_historial.insert("", "end", values=(record[1], record[2]))  # Ajusta el índice según la estructura de tu tabla

    except sqlite3.Error as e:
        messagebox.showerror("Error de base de datos", f"Hubo un error al consultar el historial: {e}")
    finally:
        # Asegúrate de cerrar la conexión después de la consulta
        conn.close()

def consultar_clientes_inactivos(root):
    # Conectar a la base de datos
    conn = conexion_db()
    cursor = conn.cursor()

    try:
        # Consultar todos los clientes con estado 'X' (inactivos)
        cursor.execute("SELECT cedula, apellidos, nombres, usuario, telefono, correo, fecha_nacimiento FROM usuarios WHERE estado = 'X'")
        clientes_inactivos = cursor.fetchall()

        if not clientes_inactivos:
            messagebox.showinfo("No hay clientes inactivos", "No existen clientes inactivos en la base de datos.")
            return

        # Crear ventana modal (siempre por encima)
        ventana_inactivos = tk.Toplevel(root)
        ventana_inactivos.title("Clientes Inactivos")
        centrar_ventana(ventana_inactivos, 700, 400)
        ventana_inactivos.configure(bg="#272643")
        ventana_inactivos.resizable(False, False)

        # Configuración de la ventana para que siempre esté encima y no se pueda maximizar
        ventana_inactivos.attributes("-topmost", True)  # Ventana siempre encima
        ventana_inactivos.protocol("WM_DELETE_WINDOW", ventana_inactivos.destroy)  # Cerrar con X

        # Título de la ventana
        label_inactivos = tk.Label(ventana_inactivos, text="Clientes Inactivos", font=("Segoe UI", 14, "bold"), bg="#272643", fg="#ffffff")
        label_inactivos.pack(pady=10)

        # Crear la tabla para mostrar los clientes inactivos
        columns_inactivos = ("Cédula", "Apellidos", "Nombres", "Usuario", "Teléfono", "Correo", "Fecha de Nacimiento")
        tree_inactivos = ttk.Treeview(ventana_inactivos, columns=columns_inactivos, show="headings", height=10)

        for col in columns_inactivos:
            tree_inactivos.heading(col, text=col)
            tree_inactivos.column(col, anchor="center", width=120)

        tree_inactivos.pack(pady=10, padx=10)

        # Llenamos la tabla con los datos de los clientes inactivos
        for cliente in clientes_inactivos:
            tree_inactivos.insert("", "end", values=cliente)

    except sqlite3.Error as e:
        messagebox.showerror("Error de base de datos", f"Hubo un error al consultar los clientes inactivos: {e}")
    finally:
        # Asegúrate de cerrar la conexión después de la consulta
        conn.close()

def generar_reportes_clientes_activos(root):
    # Abrir un cuadro de diálogo para seleccionar la carpeta y el nombre del archivo
    archivo_guardar = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
    
    if not archivo_guardar:
        return  # Si el usuario cancela la selección, no hacemos nada
    
    try:
        # Conectar a la base de datos
        conn = conexion_db()
        cursor = conn.cursor()

        # Consultar todos los clientes activos (estado 'A')
        cursor.execute("SELECT cedula, apellidos, nombres, telefono, correo, fecha_nacimiento FROM usuarios WHERE estado = 'A'")
        clientes_activos = cursor.fetchall()

        if not clientes_activos:
            messagebox.showinfo("No hay clientes activos", "No existen clientes activos en la base de datos.")
            return

        # Abrir el archivo CSV para escribir los datos
        with open(archivo_guardar, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            
            # Escribir la cabecera
            escritor_csv.writerow(["Cédula", "Apellidos", "Nombres", "Teléfono", "Correo", "Fecha de Nacimiento"])

            # Escribir los datos de los clientes activos
            escritor_csv.writerows(clientes_activos)

        messagebox.showinfo("Reporte generado", f"El reporte de clientes activos se ha generado exitosamente en: {archivo_guardar}")

    except sqlite3.Error as e:
        messagebox.showerror("Error de base de datos", f"Hubo un error al generar el reporte: {e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Hubo un error inesperado: {e}")
    finally:
        conn.close()

def exportar_clientes(root):
    # Abrir un cuadro de diálogo para seleccionar la carpeta y el nombre del archivo
    archivo_guardar = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
    
    if not archivo_guardar:
        return  # Si el usuario cancela la selección, no hacemos nada
    
    try:
        # Conectar a la base de datos
        conn = conexion_db()
        cursor = conn.cursor()

        # Consultar solo los clientes con rol 'Cliente' (excluyendo administradores y entrenadores)
        cursor.execute("SELECT cedula, apellidos, nombres, telefono, correo, estado, fecha_nacimiento FROM usuarios WHERE rol = 'Cliente'")
        clientes = cursor.fetchall()

        if not clientes:
            messagebox.showinfo("No hay clientes", "No existen clientes en la base de datos.")
            return

        # Abrir el archivo CSV para escribir los datos
        with open(archivo_guardar, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            
            # Escribir la cabecera
            escritor_csv.writerow(["Cédula", "Apellidos", "Nombres", "Teléfono", "Correo", "Estado", "Fecha de Nacimiento"])

            # Escribir los datos de los clientes
            escritor_csv.writerows(clientes)

        messagebox.showinfo("Exportación exitosa", f"Los datos de los clientes se han exportado exitosamente en: {archivo_guardar}")

    except sqlite3.Error as e:
        messagebox.showerror("Error de base de datos", f"Hubo un error al exportar los clientes: {e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Hubo un error inesperado: {e}")
    finally:
        conn.close()

def cambiar_vista(vista_frame, frames):
    for frame in frames:
        frame.pack_forget()
    vista_frame.pack(fill="both", expand=True)

def ventana_membresias(usuario, callback):
    global cédula_seleccionada  # Declaramos que vamos a usar esta variable globalmente

    # Configuración inicial
    root = tk.Tk()
    root.title("Módulo de Clientes")
    root.state('zoomed')
    root.resizable(False, False)
    root.configure(bg="#272643")
    cargar_icono(root, os.path.join(ICONS_DIR, "Icono.ico"))

    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")
    cédula_seleccionada = tk.StringVar()  # Ahora puedes acceder a esta variable globalmente dentro de las funciones

    # Frame principal
    main_frame = tk.Frame(root, bg="#272643")
    main_frame.pack(fill="both", expand=True)

    # Barra superior
    top_bar = tk.Frame(main_frame, bg="#2c698d", pady=5)
    top_bar.pack(side="top", fill="x")

    # Botón Regresar
    btn_regresar = tk.Button(top_bar, text="Regresar", font=default_font, bg="#bae8e8", command=lambda: regresar(callback, root))
    btn_regresar.pack(side="right", padx=10)

    btn_vista_general = tk.Button(top_bar, text="Vista General", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(vista_general_frame, frames))
    btn_vista_general.pack(side="left", padx=10)

    btn_editar_clientes = tk.Button(top_bar, text="Editar Clientes", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(editar_clientes_frame, frames))
    btn_editar_clientes.pack(side="left", padx=10)

    # Vista General
    vista_general_frame = tk.Frame(main_frame, bg="#272643")

    label_vista_general = tk.Label(vista_general_frame, text="Lista de Clientes", font=header_font, bg="#272643", fg="#ffffff")
    label_vista_general.pack(pady=10)

    # Barra de búsqueda en la vista general (centrado)
    frame_busqueda = tk.Frame(vista_general_frame, bg="#272643")
    frame_busqueda.pack(pady=5, padx=10)

    # Centramos los elementos
    label_buscar = tk.Label(frame_busqueda, text="Buscar:", font=default_font, bg="#272643", fg="#ffffff")
    label_buscar.pack(side="left", padx=5)

    entry_buscar = tk.Entry(frame_busqueda, font=default_font, width=30)  # Reducido el tamaño
    entry_buscar.pack(side="left", padx=5)

    btn_buscar = tk.Button(frame_busqueda, text="Buscar", font=default_font, bg="#bae8e8", command=lambda: consultar_cliente(entry_buscar, tree_clientes))
    btn_buscar.pack(side="left", padx=5)

    # Tabla de clientes
    columns_general = ("Cédula", "Apellidos", "Nombres", "Asistencia")
    tree_clientes = ttk.Treeview(vista_general_frame, columns=columns_general, show="headings", height=15)

    for col in columns_general:
        tree_clientes.heading(col, text=col)
        tree_clientes.column(col, anchor="center", width=150)

    tree_clientes.pack(pady=10, padx=10)

    # Llamar a cargar_datos_asistencias después de que la interfaz esté configurada
    cargar_datos_asistencias(tree_clientes)

    # Botones principales
    frame_buttons = tk.Frame(vista_general_frame, bg="#272643")
    frame_buttons.pack(pady=10)

    btn_registrar = tk.Button(frame_buttons, text="Registrar Cliente", font=default_font, bg="#bae8e8", command=lambda: registrar_cliente(usuario, tree_clientes))
    btn_registrar.pack(side="left", padx=5)

    btn_registrar_asistencia = tk.Button(
        frame_buttons, 
        text="Registrar Asistencia", 
        font=default_font, 
        bg="#bae8e8", 
        command=lambda: registrar_asistencia(tree_clientes.item(tree_clientes.selection()[0])['values'][0], tree_clientes)
    )
    btn_registrar_asistencia.pack(side="left", padx=5)



    btn_historial = tk.Button(frame_buttons, text="Consultar Historial", font=default_font, bg="#bae8e8", command=lambda: consultar_historial_asistencias(tree_clientes, root))
    btn_historial.pack(side="left", padx=5)

    btn_inactivos = tk.Button(frame_buttons, text="Clientes Inactivos", font=default_font, bg="#bae8e8", command=lambda: consultar_clientes_inactivos(root))
    btn_inactivos.pack(side="left", padx=5)

    btn_reportes = tk.Button(frame_buttons, text="Generar Reportes", font=default_font, bg="#bae8e8", command=lambda: generar_reportes_clientes_activos(root))
    btn_reportes.pack(side="left", padx=5)

    btn_exportar = tk.Button(frame_buttons, text="Exportar Clientes", font=default_font, bg="#bae8e8", command=lambda: exportar_clientes(root))
    btn_exportar.pack(side="left", padx=5)

    # Editar Clientes
    editar_clientes_frame = tk.Frame(main_frame, bg="#272643")

    label_editar_clientes = tk.Label(editar_clientes_frame, text="Editar Cliente", font=header_font, bg="#272643", fg="#ffffff")
    label_editar_clientes.pack(pady=10)

    # Barra de búsqueda
    frame_busqueda_editar = tk.Frame(editar_clientes_frame, bg="#272643")
    frame_busqueda_editar.pack(pady=5, padx=10)

    label_buscar_editar = tk.Label(frame_busqueda_editar, text="Buscar:", font=default_font, bg="#272643", fg="#ffffff")
    label_buscar_editar.pack(side="left", padx=5)

    entry_buscar_editar = tk.Entry(frame_busqueda_editar, font=default_font, width=30)  # Reducido el tamaño
    entry_buscar_editar.pack(side="left", padx=5)

    btn_buscar_editar = tk.Button(frame_busqueda_editar, text="Buscar", font=default_font, bg="#bae8e8", command=lambda: consultar_cliente(entry_buscar_editar, tree_editar))
    btn_buscar_editar.pack(side="left", padx=5)

    # Tabla de resultados
    columns_editar = ("Cédula", "Apellidos", "Nombres", "Correo", "Teléfono", "Fecha Nacimiento")
    tree_editar = ttk.Treeview(editar_clientes_frame, columns=columns_editar, show="headings", height=10)  # Altura reducida
    for col in columns_editar:
        tree_editar.heading(col, text=col)
        tree_editar.column(col, anchor="center", width=150)

    tree_editar.pack(padx=10, pady=10)  # Añadí bordes como en la vista general
    cargar_datos_edicion(tree_editar)


    def cargar_datos_editar(event):
        selected_item = tree_editar.selection()
        if selected_item:
            cliente = tree_editar.item(selected_item[0])['values']
            
            # Guardamos la cédula de forma oculta, puede ser un atributo del treeview o una variable global
            cédula_seleccionada.set(cliente[0])  # Asumimos que cliente[0] es la cédula
            
            # Ahora llenamos los campos de edición con los demás datos (sin cargar la cédula)
            entries["Apellidos"].delete(0, tk.END)
            entries["Apellidos"].insert(0, cliente[1])
            
            entries["Nombres"].delete(0, tk.END)
            entries["Nombres"].insert(0, cliente[2])
            
            entries["Correo"].delete(0, tk.END)
            entries["Correo"].insert(0, cliente[3])
            
            telefono = str(cliente[4])  # Convertir a string con str()
            print(f"Teléfono cargado: {telefono}")  # Esto te ayudará a ver qué valor se está insertando
            
            entries["Teléfono"].delete(0, tk.END)
            entries["Teléfono"].insert(0, telefono)



    # Asociamos la función de selección con el evento
    tree_editar.bind('<<TreeviewSelect>>', cargar_datos_editar)

    # Formulario de edición (eliminamos "Fecha de Nacimiento")
    frame_form = tk.Frame(editar_clientes_frame, bg="#272643")
    frame_form.pack(pady=10)

    labels = ["Apellidos", "Nombres", "Correo", "Teléfono"]  # Eliminamos "Fecha de Nacimiento"
    entries = {}

    # Dividimos los campos en dos columnas
    frame_left = tk.Frame(frame_form, bg="#272643")
    frame_left.pack(side="left", padx=10)

    frame_right = tk.Frame(frame_form, bg="#272643")
    frame_right.pack(side="left", padx=10)

    for i, label in enumerate(labels):
        tk.Label(frame_left if i < 2 else frame_right, text=label, font=default_font, bg="#272643", fg="#ffffff").pack(anchor="w")
        entry = tk.Entry(frame_left if i < 2 else frame_right, font=default_font)
        entry.pack(fill="x", pady=5)
        entries[label] = entry
        
    # Función para deseleccionar usuario
    def deseleccionar_usuario():
        # Limpiar la selección en la tabla
        tree_editar.selection_remove(tree_editar.selection())
        
        # Limpiar las entradas de edición
        for entry in entries.values():
            entry.delete(0, tk.END)

    # Botón para deseleccionar
    btn_deseleccionar = tk.Button(frame_form, text="Deseleccionar", font=default_font, bg="#bae8e8", command=deseleccionar_usuario)
    btn_deseleccionar.pack(side="right", padx=10, pady=10)

    # Botón Guardar
    btn_guardar = tk.Button(frame_form, text="Guardar Cambios", font=default_font, bg="#bae8e8", command=lambda: editar_cliente(entries, tree_editar))
    btn_guardar.pack(side="right", padx=10, pady=10)

    # Configuración de vistas
    frames = [vista_general_frame, editar_clientes_frame]
    vista_general_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    ventana_membresias()


def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal

