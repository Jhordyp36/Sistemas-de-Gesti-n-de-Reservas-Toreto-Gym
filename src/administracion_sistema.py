import datetime
import os
import sqlite3
import csv
from tkinter import Scrollbar, Tk, Button, Frame, Label, Entry, ttk, messagebox, StringVar, filedialog
from config.config import DB_PATH  # Usar la constante DB_PATH para la ruta de la base de datos

def conexion_db():
    """Conectar a la base de datos SQLite y devolver la conexión."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Crear ventana principal
def ventana_administracion(usuario, callback):
    ventana = Tk()
    ventana.title("Administración del Sistema")
    ventana.state("zoomed")  # Abrir ventana en pantalla completa
    ventana.resizable(False,False)
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

    # Función: Cargar vista de "Administración de Usuarios"
    def cargar_administracion_usuarios():
        limpiar_contenido()

        # Botones del módulo "Administración de Usuarios"
        frame_botones = Frame(frame_contenido, bg="#272643")
        frame_botones.pack(side="top", fill="x")

        Button(frame_botones, text="Crear Administrador", font=("Segoe UI", 12), bg="#bae8e8", command=crear_administrador_vista).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Modificar Contraseña", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: modificar_contrasena(tabla)).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Resetear Contraseña", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: resetear_contrasena(tabla)).pack(side="left", padx=10, pady=10)
        Button(frame_botones, text="Eliminar Usuario", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: eliminar_usuario(tabla)).pack(side="left", padx=10, pady=10)

        # Etiqueta de título
        Label(frame_contenido, text="Consultar Usuarios", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Frame contenedor de la tabla
        frame_tabla = Frame(frame_contenido, bg="#272643")
        frame_tabla.pack(fill="both", expand=True)

        # Barra de búsqueda
        Label(frame_tabla, text="Buscar:", font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        busqueda_var = StringVar()
        Entry(frame_tabla, textvariable=busqueda_var, width=30).grid(row=0, column=1, padx=10, pady=5, sticky="w")
        Button(frame_tabla, text="Buscar", command=lambda: cargar_datos(tabla, busqueda_var.get())).grid(row=0, column=2, padx=10, pady=5)

        # Scrollbars
        scroll_x = Scrollbar(frame_tabla, orient="horizontal")
        scroll_y = Scrollbar(frame_tabla, orient="vertical")

        # Tabla
        columnas = ("cedula", "apellidos", "nombres", "usuario", "telefono", "correo", "rol", "estado")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        tabla.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Configurar las barras de desplazamiento
        scroll_x.config(command=tabla.xview)
        scroll_y.config(command=tabla.yview)
        scroll_x.grid(row=2, column=0, columnspan=3, sticky="ew")
        scroll_y.grid(row=1, column=3, sticky="ns")

        # Encabezados y ajuste de anchos
        for col in columnas:
            tabla.heading(col, text=col.capitalize())
            tabla.column(col, width=100, anchor="center")  # Ajusta el ancho según tus necesidades

        # Ajustar tamaño del frame_tabla
        frame_tabla.grid_rowconfigure(1, weight=1)
        frame_tabla.grid_columnconfigure(0, weight=1)

        # Cargar datos
        cargar_datos(tabla)

    # Función: Cargar datos en la tabla
    def cargar_datos(tabla, filtro=""):
        conn = conexion_db()  # Cambio aquí
        if not conn:
            return

        cursor = conn.cursor()
        query = "SELECT cedula, apellidos, nombres, usuario, telefono, correo, rol, estado FROM usuarios WHERE estado = 'A'"
        if filtro:
            query += " AND (cedula LIKE ? OR apellidos LIKE ? OR nombres LIKE ? OR usuario LIKE ? OR telefono LIKE ? OR correo LIKE ?)"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%", f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)

        datos = cursor.fetchall()
        conn.close()

        # Limpiar tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Insertar datos
        for fila in datos:
            estado = "Eliminado" if fila[-1] == 'X' else "Activo"
            tabla.insert("", "end", values=fila[:-1] + (estado,))

    def modificar_contrasena(tabla):
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un usuario para modificar su contraseña")
            return

        usuario_id = tabla.item(seleccion)["values"][0]

        limpiar_contenido()

        # Elementos de la ventana de modificación
        Label(frame_contenido, text="Modificar Contraseña", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Etiquetas y entradas
        Label(frame_contenido, text="Contraseña Actual", font=("Segoe UI", 12), bg="#272643", fg="white").pack(pady=5)
        entry_actual = Entry(frame_contenido, show="*", font=("Segoe UI", 12))
        entry_actual.pack(pady=5)

        Label(frame_contenido, text="Nueva Contraseña", font=("Segoe UI", 12), bg="#272643", fg="white").pack(pady=5)
        entry_nueva = Entry(frame_contenido, show="*", font=("Segoe UI", 12))
        entry_nueva.pack(pady=5)

        Label(frame_contenido, text="Repetir Nueva Contraseña", font=("Segoe UI", 12), bg="#272643", fg="white").pack(pady=5)
        entry_repetir = Entry(frame_contenido, show="*", font=("Segoe UI", 12))
        entry_repetir.pack(pady=5)

        # Botones
        def actualizar_contrasena():
            actual = entry_actual.get()
            nueva = entry_nueva.get()
            repetir = entry_repetir.get()

            conn = conexion_db()
            if not conn:
                return

            try:
                cursor = conn.cursor()
                cursor.execute("SELECT contrasena FROM usuarios WHERE cedula = ?", (usuario_id,))
                resultado = cursor.fetchone()

                if not resultado or resultado[0] != actual:
                    messagebox.showerror("Error", "La contraseña actual no coincide")
                    return

                if nueva != repetir:
                    messagebox.showerror("Error", "Las nuevas contraseñas no coinciden")
                    return

                cursor.execute("UPDATE usuarios SET contrasena = ? WHERE cedula = ?", (nueva, usuario_id))
                conn.commit()
                messagebox.showinfo("Éxito", "Contraseña actualizada con éxito")
                cargar_administracion_usuarios()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al actualizar la contraseña: {e}")
            finally:
                conn.close()

        Button(frame_contenido, text="Actualizar", font=("Segoe UI", 12), bg="#bae8e8", command=actualizar_contrasena).pack(pady=10)
        Button(frame_contenido, text="Cancelar", font=("Segoe UI", 12), bg="#ff6f61", command=cargar_administracion_usuarios).pack(pady=10)
    # Función: Eliminar usuario (borrado lógico)
    def eliminar_usuario(tabla):
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un usuario para eliminar.")
            return
        
        usuario_id = tabla.item(seleccion)["values"][0]  # Cedula
        conn = conexion_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET estado = 'X' WHERE cedula = ?", (usuario_id,))
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Eliminacion: Administracion de Usuarios')", (usuario, fecha_hora_actual))
            conn.commit()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            cargar_administracion_usuarios()  # Recargar la tabla después de la eliminación
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al eliminar el usuario: {e}")
        finally:
            conn.close()

    # Función: Resetear contraseña
    def resetear_contrasena(tabla):
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un usuario para resetear la contraseña.")
            return

        usuario_id = tabla.item(seleccion)["values"][0]  # Cedula
        nueva_contrasena = None

        # Realizar la consulta para obtener el valor de la contraseña predeterminada
        conn = conexion_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            
            # Ejecutar la consulta para obtener la contraseña predeterminada
            cursor.execute("SELECT valor FROM parametros WHERE nombre = 'Contraseña Predeterminada'")
            resultado = cursor.fetchone()  # Obtiene el primer resultado de la consulta
            
            if resultado:
                nueva_contrasena = resultado[0]  # Almacena el valor de la contraseña predeterminada
            else:
                raise Exception("No se encontró la contraseña predeterminada en la base de datos.")
            
            # Actualizar la contraseña del usuario
            cursor.execute("UPDATE usuarios SET contrasena = ? WHERE cedula = ?", (nueva_contrasena, usuario_id))
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Reseteo: Administracion de Usuarios')", (usuario, fecha_hora_actual))
            
            # Confirmar cambios
            conn.commit()
            messagebox.showinfo("Éxito", f"Contraseña para el usuario {usuario_id} reseteada correctamente.")
            
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al resetear la contraseña: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    # Función: Crear administrador (en la misma ventana)
    def crear_administrador_vista():
        limpiar_contenido()

        Label(frame_contenido, text="Crear Administrador", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Campos de entrada
        frame_formulario = Frame(frame_contenido, bg="#272643")
        frame_formulario.pack(pady=10)

        campos = ["Cédula", "Apellidos", "Nombres", "Usuario", "Contraseña", "Rol"]
        entradas = {}

        for i, campo in enumerate(campos):
            Label(frame_formulario, text=campo, font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            # El rol será fijo como "Administrador" para todos los casos
            if campo == "Rol":
                rol_label = Label(frame_formulario, text="Administrador", font=("Segoe UI", 12), bg="#272643", fg="white")
                rol_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")
                entradas[campo] = "Administrador"  # Solo se asigna "Administrador"
            else:
                entrada = Entry(frame_formulario, width=30, show="*" if campo == "Contraseña" else None)
                entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
                entradas[campo] = entrada

        # Botón para guardar administrador
        Button(frame_contenido, text="Guardar Administrador", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: guardar_administrador(entradas)).pack(pady=10)
        
        # Botón de cancelar
        Button(frame_contenido, text="Cancelar", font=("Segoe UI", 12), bg="#f8d7da", command=cargar_administracion_usuarios).pack(pady=10)

    # Función: Guardar administrador en la base de datos
    def guardar_administrador(entradas):
        datos = {campo: entrada.get() if isinstance(entrada, Entry) else entrada for campo, entrada in entradas.items()}

        # Validación de campos vacíos
        if any(not valor for valor in datos.values()):
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        conn = conexion_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (cedula, apellidos, nombres, usuario, contrasena, rol) VALUES (?, ?, ?, ?, ?, ?)",
                (datos["Cédula"], datos["Apellidos"], datos["Nombres"], datos["Usuario"], datos["Contraseña"], datos["Rol"])
            )
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Creacion: Administracion de Usuarios')", (usuario, fecha_hora_actual))
            conn.commit()
            messagebox.showinfo("Éxito", "Administrador creado correctamente.")
            cargar_administracion_usuarios()  # Recargar la lista de usuarios
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al guardar el administrador: {e}")
        finally:
            conn.close()

    # Función: Cargar vista de "Administración de Parámetros"
    def cargar_administracion_parametros():
        limpiar_contenido()

        Label(frame_contenido, text="Administración de Parámetros", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Frame para los parámetros
        frame_formulario = Frame(frame_contenido, bg="#272643")
        frame_formulario.pack(pady=10)

        # Parámetros iniciales
        campos = ["Contraseña Predeterminada", "Porcentaje IVA"]
        entradas = {}
        labels = {}
        botones = {}

        # Obtener valores de la base de datos
        conn = conexion_db()
        if not conn:
            messagebox.showerror("Error de Conexión", "No se pudo conectar a la base de datos.")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT nombre, valor FROM parametros WHERE nombre IN ('Contraseña Predeterminada', 'Porcentaje IVA')")
        parametros = cursor.fetchall()
        conn.close()

        if not parametros:
            messagebox.showerror("Error", "No se pudieron cargar los parámetros desde la base de datos.")
            return

        valores_parametros = {nombre: valor for nombre, valor in parametros}

        # Mostrar los valores iniciales como Labels
        for i, campo in enumerate(campos):
            Label(frame_formulario, text=campo, font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="e")

            valor = valores_parametros.get(campo, "")

            label = Label(frame_formulario, text=valor, font=("Segoe UI", 12), bg="#272643", fg="white", anchor="w")
            label.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            labels[campo] = label

            # Crear los Entry (inicialmente ocultos)
            entrada = Entry(frame_formulario, width=30)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entrada.insert(0, valor)
            entrada.grid_remove()
            entradas[campo] = entrada

        # Botones para acciones
        frame_botones = Frame(frame_contenido, bg="#272643")
        frame_botones.pack(pady=10)

        boton_editar = Button(frame_botones, text="Editar Parámetros", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: habilitar_edicion(entradas, labels, botones))
        boton_editar.pack(side="left", padx=10)
        botones["editar"] = boton_editar

        boton_guardar = Button(frame_botones, text="Guardar", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: guardar_cambios(entradas, valores_parametros, labels, botones))
        boton_guardar.pack(side="left", padx=10)
        boton_guardar.pack_forget()
        botones["guardar"] = boton_guardar

        boton_cancelar = Button(frame_botones, text="Cancelar", font=("Segoe UI", 12), bg="#bae8e8", command=lambda: cancelar_edicion(entradas, labels, botones))
        boton_cancelar.pack(side="left", padx=10)
        boton_cancelar.pack_forget()
        botones["cancelar"] = boton_cancelar

    def habilitar_edicion(entradas, labels, botones):  
        for campo, label in labels.items():
            label.grid_remove()
            entradas[campo].grid()

        botones["editar"].pack_forget()
        botones["guardar"].pack(side="left", padx=10)
        botones["cancelar"].pack(side="left", padx=10)

    def cancelar_edicion(entradas, labels, botones):
        for campo, entrada in entradas.items():
            entrada.grid_remove()
            labels[campo].grid()

        botones["guardar"].pack_forget()
        botones["cancelar"].pack_forget()
        botones["editar"].pack(side="left", padx=10)

    def guardar_cambios(entradas, valores_parametros, labels, botones):
        respuesta = messagebox.askyesno("Confirmación", "¿Desea actualizar los valores?")
        if not respuesta:
            cancelar_edicion(entradas, labels, botones)
            return

        cambios_realizados = False
        for campo, entrada in entradas.items():
            nuevo_valor = entrada.get()
            if nuevo_valor != valores_parametros.get(campo, ""):
                cambios_realizados = True

        if not cambios_realizados:
            messagebox.showinfo("Sin Cambios", "No se realizaron cambios en los parámetros.")
            cancelar_edicion(entradas, labels, botones)
            return

        conn = conexion_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            for campo, entrada in entradas.items():
                nuevo_valor = entrada.get()
                cursor.execute("UPDATE parametros SET valor = ? WHERE nombre = ?", (nuevo_valor, campo))
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Modificacion: Administracion de Parametros')", (usuario, fecha_hora_actual))
            conn.commit()
            messagebox.showinfo("Éxito", "Los parámetros se han actualizado correctamente.")

            # Actualizar las etiquetas con los nuevos valores
            for campo, entrada in entradas.items():
                nuevo_valor = entrada.get()
                labels[campo].config(text=nuevo_valor)
                valores_parametros[campo] = nuevo_valor

        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error al guardar los parámetros: {e}")
        finally:
            conn.close()

        cancelar_edicion(entradas, labels, botones)

    def cargar_auditoria():
        limpiar_contenido()

        Label(frame_contenido, text="Auditoría", font=("Segoe UI", 16), bg="#272643", fg="white").pack(pady=10)

        # Crear tabla para mostrar los logs
        frame_tabla = Frame(frame_contenido, bg="#272643")
        frame_tabla.pack(pady=10, fill="both", expand=True)

        tabla_logs = ttk.Treeview(frame_tabla, columns=("ID", "Usuario", "Fecha y Hora", "Acción"), show="headings", height=15)
        tabla_logs.heading("ID", text="ID")
        tabla_logs.heading("Usuario", text="Usuario")
        tabla_logs.heading("Fecha y Hora", text="Fecha y Hora")
        tabla_logs.heading("Acción", text="Acción")

        tabla_logs.column("ID", width=50, anchor="center")
        tabla_logs.column("Usuario", width=150, anchor="center")
        tabla_logs.column("Fecha y Hora", width=150, anchor="center")
        tabla_logs.column("Acción", width=300, anchor="w")
        tabla_logs.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(frame_tabla, orient="vertical", command=tabla_logs.yview)
        scrollbar.pack(side="right", fill="y")
        tabla_logs.configure(yscrollcommand=scrollbar.set)

        # Barra de búsqueda
        frame_busqueda = Frame(frame_contenido, bg="#272643")
        frame_busqueda.pack(pady=10)

        Label(frame_busqueda, text="Buscar:", font=("Segoe UI", 12), bg="#272643", fg="white").grid(row=0, column=0, padx=5)
        entrada_busqueda = Entry(frame_busqueda, width=30)
        entrada_busqueda.grid(row=0, column=1, padx=5)
        Button(frame_busqueda, text="Buscar", bg="#bae8e8", font=("Segoe UI", 12),
            command=lambda: filtrar_logs(entrada_busqueda.get(), tabla_logs)).grid(row=0, column=2, padx=5)

        # Botones de exportación
        frame_botones = Frame(frame_contenido, bg="#272643")
        frame_botones.pack(pady=10)

        Button(frame_botones, text="Exportar Logs", bg="#bae8e8", font=("Segoe UI", 12),
            command=lambda: exportar_logs(tabla_logs)).grid(row=0, column=0, padx=10)

        cargar_logs(tabla_logs)
    
    def cargar_logs(tabla):
        conn = conexion_db()
        if not conn:
            return
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM logs")
            registros = cursor.fetchall()
            for registro in tabla.get_children():
                tabla.delete(registro)
            for registro in registros:
                tabla.insert("", "end", values=registro)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar logs: {e}")
        finally:
            conn.close()
            
    def filtrar_logs(termino, tabla):
        conn = conexion_db()
        if not conn:
            return
        try:
            cursor = conn.cursor()
            consulta = "SELECT * FROM logs WHERE usuario LIKE ? OR fecha_hora LIKE ? OR accion LIKE ?"
            cursor.execute(consulta, (f"%{termino}%", f"%{termino}%", f"%{termino}%"))
            registros = cursor.fetchall()
            for registro in tabla.get_children():
                tabla.delete(registro)
            for registro in registros:
                tabla.insert("", "end", values=registro)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al filtrar logs: {e}")
        finally:
            conn.close()
    
    def exportar_logs(tabla):
        # Obtener los registros de la tabla
        conn = conexion_db()
        registros = [tabla.item(fila)["values"] for fila in tabla.get_children()]
        
        if not registros:
            messagebox.showwarning("Sin datos", "No hay datos para exportar.")
            return

        # Seleccionar la carpeta donde guardar el archivo y permitir elegir nombre de archivo
        ruta = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        
        if not ruta:
            messagebox.showwarning("No se seleccionó archivo", "No se ha seleccionado un archivo para guardar.")
            return

        try:
            # Crear el archivo CSV y escribir los datos
            with open(ruta, mode='w', newline='', encoding='utf-8') as archivo_csv:
                writer = csv.writer(archivo_csv, delimiter=',')  # Usa coma como delimitador

                # Escribir los encabezados de las columnas
                writer.writerow(["ID", "Usuario", "Fecha y Hora", "Acción"])

                # Escribir los registros de la tabla
                for registro in registros:
                    writer.writerow(registro)

            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO logs (usuario, fecha_hora, accion) VALUES (?, ?, 'Exportacion: Auditoria')", (usuario, fecha_hora_actual))
            conn.commit()
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Logs exportados correctamente a: {ruta}")
        except Exception as e:
            # Mostrar mensaje de error si algo falla
            messagebox.showerror("Error", f"Error al exportar los logs: {e}")
    
    # Botones de navegación
    Button(frame_botones_principales, text="Administración de Usuarios", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_administracion_usuarios, padx=20, pady=10).pack(side="left", padx=10)
    Button(frame_botones_principales, text="Administración de Parámetros", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_administracion_parametros, padx=20, pady=10).pack(side="left", padx=10)
    Button(frame_botones_principales, text="Auditoría", font=("Segoe UI", 14), bg="#bae8e8", command=cargar_auditoria, padx=20, pady=10).pack(side="left", padx=10)
    Button(frame_botones_principales, text="Regresar", font=("Segoe UI", 14), bg="#bae8e8", command=lambda: regresar(callback, ventana), padx=20, pady=10).pack(side="left", padx=10)

    ventana.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal

if __name__ == "__main__":
    ventana_administracion()
