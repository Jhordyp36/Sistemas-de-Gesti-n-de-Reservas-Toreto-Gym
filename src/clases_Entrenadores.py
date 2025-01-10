import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.utils.helpers import cargar_icono
from config.config import ICONS_DIR
def add_Clase():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def eliminar_Clase():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def editar_Clase():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def filtar_Clase():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def add_Entrenador():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def eliminar_Entrenador():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def editar_Entrenador():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def filtar_Entrenador():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def ventana_ClasesEntrenadores(callback):
        # Configuración del tipo de letra
        default_font = ("Segoe UI", 12)
        header_font = ("Segoe UI", 14, "bold")

        # Configuración inicial de la ventana
        ce_window = tk.Tk()
        ce_window.title("Módulo de Clases y Entrenadores")
        ce_window.state('zoomed')  # Inicia en pantalla completa
        ce_window.configure(bg="#272643")  # Color de fondo de la ventana
        cargar_icono(ce_window, os.path.join(ICONS_DIR, "Icono.ico"))

        # Frame para Clases
        frame_clases = tk.Frame(ce_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
        frame_clases.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.8)

        label_clases = tk.Label(frame_clases, text="Clases", font=header_font, bg="#2c698d", fg="#ffffff")
        label_clases.pack(pady=5)

        entry_buscar_clases = tk.Entry(frame_clases, font=default_font)
        entry_buscar_clases.pack(pady=5, fill="x")

        btn_filtrar_clases = tk.Button(frame_clases, text="Filtrar", font=default_font, bg="#bae8e8", command=filtar_Clase)
        btn_filtrar_clases.pack(pady=5)

        # Tabla de clases
        columns_clases = ("Clase", "Entrenador", "Fecha", "Hora")
        tree_clases = ttk.Treeview(frame_clases, columns=columns_clases, show="headings")

        # Configurar las columnas y encabezados de la tabla
        for col in columns_clases:
                tree_clases.heading(col, text=col)
                tree_clases.column(col, anchor="center", width=150)  # Ajustamos el ancho de las columnas

        # Empacar la tabla
        tree_clases.pack(fill="both", expand=True, pady=5)

        # Botones de acciones para las clases
        frame_buttons_clases = tk.Frame(frame_clases, bg="#2c698d")
        frame_buttons_clases.pack(pady=10)

        btn_agregar_clase = tk.Button(frame_buttons_clases, text="Agregar", font=default_font, bg="#bae8e8", command=add_Clase)
        btn_agregar_clase.pack(side="left", padx=5, pady=5)
        btn_editar_clase = tk.Button(frame_buttons_clases, text="Editar", font=default_font, bg="#bae8e8", command=editar_Clase)
        btn_editar_clase.pack(side="left", padx=5, pady=5)
        btn_eliminar_clase = tk.Button(frame_buttons_clases, text="Eliminar", font=default_font, bg="#bae8e8", command=eliminar_Clase)
        btn_eliminar_clase.pack(side="left", padx=5, pady=5)

        # Frame para Entrenadores
        frame_entrenadores = tk.Frame(ce_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
        frame_entrenadores.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.8)

        label_entrenadores = tk.Label(frame_entrenadores, text="Entrenadores", font=header_font, bg="#2c698d", fg="#ffffff")
        label_entrenadores.pack(pady=5)

        entry_buscar_entrenadores = tk.Entry(frame_entrenadores, font=default_font)
        entry_buscar_entrenadores.pack(pady=5, fill="x")

        btn_filtrar_entrenadores = tk.Button(frame_entrenadores, text="Filtrar", font=default_font, bg="#bae8e8", command=filtar_Entrenador)
        btn_filtrar_entrenadores.pack(pady=5)

        # Tabla de entrenadores
        columns_entrenadores = ("Cédula", "Apellidos", "Nombres", "Clase")
        tree_entrenadores = ttk.Treeview(frame_entrenadores, columns=columns_entrenadores, show="headings")

        # Configurar las columnas y encabezados de la tabla
        for col in columns_entrenadores:
                tree_entrenadores.heading(col, text=col)
                tree_entrenadores.column(col, anchor="center", width=150)  # Ajustamos el ancho de las columnas

        # Empacar la tabla
        tree_entrenadores.pack(fill="both", expand=True, pady=5)

        # Botones de acciones para los entrenadores
        frame_buttons_entrenadores = tk.Frame(frame_entrenadores, bg="#2c698d")
        frame_buttons_entrenadores.pack(pady=10)

        btn_agregar_entrenador = tk.Button(frame_buttons_entrenadores, text="Agregar", font=default_font, bg="#bae8e8", command=add_Entrenador)
        btn_agregar_entrenador.pack(side="left", padx=5, pady=5)
        btn_editar_entrenador = tk.Button(frame_buttons_entrenadores, text="Editar", font=default_font, bg="#bae8e8", command=editar_Entrenador)
        btn_editar_entrenador.pack(side="left", padx=5, pady=5)
        btn_eliminar_entrenador = tk.Button(frame_buttons_entrenadores, text="Eliminar", font=default_font, bg="#bae8e8", command=eliminar_Entrenador)
        btn_eliminar_entrenador.pack(side="left", padx=5, pady=5)

        # Botón para regresar al menú principal
        btn_regresar = tk.Button(ce_window, text="Regresar al Menú Principal", font=default_font, bg="#e3f6f5", command=lambda: regresar(callback, ce_window))
        btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)

        # Iniciar la aplicación
        ce_window.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal