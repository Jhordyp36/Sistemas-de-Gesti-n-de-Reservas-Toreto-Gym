import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.utils.helpers import cargar_icono
from config.config import ICONS_DIR
    
def ventana_reservas_administrador(callback):
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    admin_window = tk.Tk()
    admin_window.title("Módulo de Reservas - Administrador")
    admin_window.state('zoomed')
    admin_window.configure(bg="#272643")
    cargar_icono(admin_window, os.path.join(ICONS_DIR, "Icono.ico"))

    frame_reservas = tk.Frame(admin_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_reservas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.85)

    label_reservas = tk.Label(frame_reservas, text="Gestión de Reservas", font=header_font, bg="#2c698d", fg="#ffffff")
    label_reservas.pack(pady=5)

    columns_reservas = ("ID", "Usuario", "Fecha", "Hora", "Estado")
    tree_reservas = ttk.Treeview(frame_reservas, columns=columns_reservas, show="headings")

    for col in columns_reservas:
        tree_reservas.heading(col, text=col)
        tree_reservas.column(col, anchor="center", width=150)

    tree_reservas.pack(fill="both", expand=True, pady=5)

    frame_buttons_reservas = tk.Frame(frame_reservas, bg="#2c698d")
    frame_buttons_reservas.pack(pady=10)

    btn_agendar = tk.Button(frame_buttons_reservas, text="Agendar Sesión", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_agendar.pack(side="left", padx=5, pady=5)

    btn_modificar = tk.Button(frame_buttons_reservas, text="Modificar Reservación", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_modificar.pack(side="left", padx=5, pady=5)

    btn_cancelar = tk.Button(frame_buttons_reservas, text="Cancelar Reservación", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_cancelar.pack(side="left", padx=5, pady=5)

    btn_historial = tk.Button(frame_buttons_reservas, text="Consultar Historial", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_historial.pack(side="left", padx=5, pady=5)

    btn_cerrar = tk.Button(admin_window, text="Cerrar", font=default_font, bg="#e3f6f5", command=lambda: regresar(callback, admin_window))
    btn_cerrar.place(relx=0.45, rely=0.92, relwidth=0.1, relheight=0.05)

    admin_window.mainloop()

def ventana_reservas_usuario(callback):
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    user_window = tk.Tk()
    user_window.title("Módulo de Reservas - Usuario")
    user_window.state('zoomed')
    user_window.configure(bg="#272643")
    cargar_icono(user_window, os.path.join(ICONS_DIR, "Icono.ico"))

    frame_reservas = tk.Frame(user_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_reservas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.85)

    label_reservas = tk.Label(frame_reservas, text="Reservas", font=header_font, bg="#2c698d", fg="#ffffff")
    label_reservas.pack(pady=5)

    columns_reservas = ("ID", "Fecha", "Hora", "Estado")
    tree_reservas = ttk.Treeview(frame_reservas, columns=columns_reservas, show="headings")

    for col in columns_reservas:
        tree_reservas.heading(col, text=col)
        tree_reservas.column(col, anchor="center", width=150)

    tree_reservas.pack(fill="both", expand=True, pady=5)

    frame_buttons_reservas = tk.Frame(frame_reservas, bg="#2c698d")
    frame_buttons_reservas.pack(pady=10)

    btn_agendar = tk.Button(frame_buttons_reservas, text="Agendar Sesión", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_agendar.pack(side="left", padx=5, pady=5)

    btn_modificar = tk.Button(frame_buttons_reservas, text="Modificar Reservación", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_modificar.pack(side="left", padx=5, pady=5)

    btn_cancelar = tk.Button(frame_buttons_reservas, text="Cancelar Reservación", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_cancelar.pack(side="left", padx=5, pady=5)

    btn_historial = tk.Button(frame_buttons_reservas, text="Consultar Historial", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Muy pronto", "Función en desarrollo"))
    btn_historial.pack(side="left", padx=5, pady=5)

    btn_cerrar = tk.Button(user_window, text="Cerrar", font=default_font, bg="#e3f6f5", command=lambda: regresar(callback, user_window))
    btn_cerrar.place(relx=0.45, rely=0.92, relwidth=0.1, relheight=0.05)

    user_window.mainloop()
    

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal