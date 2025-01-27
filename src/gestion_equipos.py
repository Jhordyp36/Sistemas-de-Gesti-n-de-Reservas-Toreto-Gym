import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.utils.helpers import cargar_icono, centrar_ventana
from config.config import ICONS_DIR

def ventana_gestion_equipos(callback):
    def mostrar_mensaje_proceso():
        messagebox.showinfo("¡Estamos en Proceso!", "Esta funcionalidad está en desarrollo.")

    # Crear ventana principal
    ventana_equipos = tk.Tk()  # Cambié Toplevel por Tk
    ventana_equipos.title("Gestión de Equipos")
    ventana_equipos.state("zoomed")
    ventana_equipos.resizable(False, False)
    ventana_equipos.configure(bg="#272643")
    cargar_icono(ventana_equipos, ICONS_DIR + "/Icono.ico")
    
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")
    
    # Frame principal
    main_frame = tk.Frame(ventana_equipos, bg="#272643")
    main_frame.pack(fill="both", expand=True)
    
    # Barra superior
    top_bar = tk.Frame(main_frame, bg="#2c698d", pady=5)
    top_bar.pack(side="top", fill="x")
    
    # Botón Regresar
    btn_regresar = tk.Button(top_bar, text="Regresar", font=default_font, bg="#bae8e8", command=lambda: regresar (callback, ventana_equipos))
    btn_regresar.pack(side="right", padx=10)
    
    # Vista de consulta de equipos
    vista_consulta_frame = tk.Frame(main_frame, bg="#272643")
    vista_consulta_frame.pack(fill="both", expand=True)
    
    label_vista_consulta = tk.Label(vista_consulta_frame, text="Consultar Equipos", font=header_font, bg="#272643", fg="#ffffff")
    label_vista_consulta.pack(pady=10)
    
    # Barra de búsqueda
    frame_busqueda = tk.Frame(vista_consulta_frame, bg="#272643")
    frame_busqueda.pack(pady=5, padx=10)
    
    label_buscar = tk.Label(frame_busqueda, text="Buscar:", font=default_font, bg="#272643", fg="#ffffff")
    label_buscar.pack(side="left", padx=5)
    
    entry_buscar = tk.Entry(frame_busqueda, font=default_font, width=30)  # Reducido el tamaño
    entry_buscar.pack(side="left", padx=5)
    
    btn_buscar = tk.Button(frame_busqueda, text="Buscar", font=default_font, bg="#bae8e8", command=mostrar_mensaje_proceso)
    btn_buscar.pack(side="left", padx=5)
    
    # Tabla de equipos
    columns_consulta = ("Categoría", "Equipo", "Estado")
    tree_equipos = ttk.Treeview(vista_consulta_frame, columns=columns_consulta, show="headings", height=10)
    
    for col in columns_consulta:
        tree_equipos.heading(col, text=col)
        tree_equipos.column(col, anchor="center", width=150)
    
    tree_equipos.pack(pady=10, padx=10)
    
    # Botones principales para gestionar equipos (debajo de la tabla)
    frame_buttons = tk.Frame(vista_consulta_frame, bg="#272643")
    frame_buttons.pack(pady=10)
    
    btn_guardar = tk.Button(frame_buttons, text="Registrar Equipo", font=default_font, bg="#bae8e8", command=mostrar_mensaje_proceso)
    btn_guardar.pack(side="left", padx=5)
    
    btn_actualizar = tk.Button(frame_buttons, text="Actualizar Estado", font=default_font, bg="#bae8e8", command=mostrar_mensaje_proceso)
    btn_actualizar.pack(side="left", padx=5)
    
    btn_generar_reporte = tk.Button(frame_buttons, text="Generar Reporte", font=default_font, bg="#bae8e8", command=mostrar_mensaje_proceso)
    btn_generar_reporte.pack(side="left", padx=5)
    
    ventana_equipos.mainloop()

if __name__ == "__main__":
    ventana_gestion_equipos()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal
