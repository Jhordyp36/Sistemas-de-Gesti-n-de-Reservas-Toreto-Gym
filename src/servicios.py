import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from config.config import DB_PATH, ICONS_DIR
from src.utils.helpers import cargar_icono

def conexion_db():
    """Conectar a la base de datos SQLite y devolver la conexión."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def ventana_clases_entrenadores(callback):
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Gestión de Clases y Entrenadores")
    root.state("zoomed")  # Especifica el tamaño fijo de la ventana
    root.resizable(False, False)  # Desactiva el cambio de tamaño
    root.configure(bg="#272643")
    # root.attributes('-topmost', True)  # Mantiene la ventana en el frente
    cargar_icono(root, ICONS_DIR)

    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    # Frame principal
    main_frame = tk.Frame(root, bg="#272643")
    main_frame.pack(fill="both", expand=True)

    # Barra superior
    top_bar = tk.Frame(main_frame, bg="#2c698d", pady=5)
    top_bar.pack(side="top", fill="x")

    # Botones de "Clases" y "Entrenadores"
    btn_clases = tk.Button(top_bar, text="Clases", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(vista_clases_frame, frames))
    btn_clases.pack(side="left", padx=10)

    btn_entrenadores = tk.Button(top_bar, text="Entrenadores", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(vista_entrenadores_frame, frames))
    btn_entrenadores.pack(side="left", padx=10)

    # Botón de regresar
    btn_regresar = tk.Button(top_bar, text="Regresar", font=default_font, bg="#bae8e8", command=lambda: regresar(callback, root))
    btn_regresar.pack(side="right", padx=10)

    # Función para cambiar vistas
    def cambiar_vista(vista_frame, frames):
        for frame in frames:
            frame.pack_forget()
        vista_frame.pack(fill="both", expand=True)

    # Vista de Clases
    vista_clases_frame = tk.Frame(main_frame, bg="#272643")

    label_clases = tk.Label(vista_clases_frame, text="Clases Programadas", font=header_font, bg="#272643", fg="#ffffff")
    label_clases.pack(pady=10)

    # Tabla de clases
    columns_clases = ("Nombre", "Fecha", "Hora", "Entrenador", "Participantes")
    tree_clases = ttk.Treeview(vista_clases_frame, columns=columns_clases, show="headings", height=15)

    for col in columns_clases:
        tree_clases.heading(col, text=col)
        tree_clases.column(col, anchor="center", width=150)

    tree_clases.pack(pady=10, padx=10)

    # Botones de acciones sobre clases
    frame_buttons_clases = tk.Frame(vista_clases_frame, bg="#272643")
    frame_buttons_clases.pack(pady=10)

    btn_crear_clase = tk.Button(frame_buttons_clases, text="Crear Clase", font=default_font, bg="#bae8e8")
    btn_crear_clase.pack(side="left", padx=5)

    btn_editar_clase = tk.Button(frame_buttons_clases, text="Editar Clase", font=default_font, bg="#bae8e8")
    btn_editar_clase.pack(side="left", padx=5)

    btn_eliminar_clase = tk.Button(frame_buttons_clases, text="Eliminar Clase", font=default_font, bg="#bae8e8")
    btn_eliminar_clase.pack(side="left", padx=5)

    btn_generar_reporte_clases = tk.Button(frame_buttons_clases, text="Generar Reporte", font=default_font, bg="#bae8e8")
    btn_generar_reporte_clases.pack(side="left", padx=5)

    btn_estadisticas_clases = tk.Button(frame_buttons_clases, text="Estadísticas", font=default_font, bg="#bae8e8")
    btn_estadisticas_clases.pack(side="left", padx=5)

    btn_registrar_participacion = tk.Button(frame_buttons_clases, text="Registrar Participación", font=default_font, bg="#bae8e8")
    btn_registrar_participacion.pack(side="left", padx=5)

    # Vista de Entrenadores
    vista_entrenadores_frame = tk.Frame(main_frame, bg="#272643")

    label_entrenadores = tk.Label(vista_entrenadores_frame, text="Entrenadores Registrados", font=header_font, bg="#272643", fg="#ffffff")
    label_entrenadores.pack(pady=10)

    # Tabla de entrenadores
    columns_entrenadores = ("Nombres", "Cédula", "Teléfono", "Correo")
    tree_entrenadores = ttk.Treeview(vista_entrenadores_frame, columns=columns_entrenadores, show="headings", height=15)

    for col in columns_entrenadores:
        tree_entrenadores.heading(col, text=col)
        tree_entrenadores.column(col, anchor="center", width=150)

    tree_entrenadores.pack(pady=10, padx=10)

    # Botones de acciones sobre entrenadores
    frame_buttons_entrenadores = tk.Frame(vista_entrenadores_frame, bg="#272643")
    frame_buttons_entrenadores.pack(pady=10)

    btn_registrar_entrenador = tk.Button(frame_buttons_entrenadores, text="Registrar Entrenador", font=default_font, bg="#bae8e8")
    btn_registrar_entrenador.pack(side="left", padx=5)

    btn_editar_entrenador = tk.Button(frame_buttons_entrenadores, text="Editar Entrenador", font=default_font, bg="#bae8e8")
    btn_editar_entrenador.pack(side="left", padx=5)

    btn_eliminar_entrenador = tk.Button(frame_buttons_entrenadores, text="Eliminar Entrenador", font=default_font, bg="#bae8e8")
    btn_eliminar_entrenador.pack(side="left", padx=5)

    btn_generar_reporte_entrenadores = tk.Button(frame_buttons_entrenadores, text="Generar Reporte", font=default_font, bg="#bae8e8")
    btn_generar_reporte_entrenadores.pack(side="left", padx=5)

    btn_evaluacion_entrenador = tk.Button(frame_buttons_entrenadores, text="Evaluar Entrenador", font=default_font, bg="#bae8e8")
    btn_evaluacion_entrenador.pack(side="left", padx=5)

    # Configuración de vistas
    frames = [vista_clases_frame, vista_entrenadores_frame]
    vista_clases_frame.pack(fill="both", expand=True)

    root.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal
    
if __name__ == "__main__":
    ventana_clases_entrenadores()
