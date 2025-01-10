import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_Elemento():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def eliminar_Elemento():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def editar_Elemento():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def filtrar_Elemento():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def ventana_GestionEquipos(callback):
    # Configuración del tipo de letra
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    # Configuración inicial de la ventana
    equipo_window = tk.Tk()
    equipo_window.title("Gestión de Equipos")
    equipo_window.state("zoomed")
    equipo_window.configure(bg="#272643")

    # Frame para "Añadir Elemento"
    frame_add = tk.Frame(equipo_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_add.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.8)

    label_add = tk.Label(frame_add, text="Añadir Elemento", font=header_font, bg="#2c698d", fg="#ffffff")
    label_add.pack(pady=5)

    tk.Label(frame_add, text="Nombre:", font=default_font, bg="#2c698d", fg="#ffffff").pack(anchor="w", pady=2)
    tk.Entry(frame_add, font=default_font).pack(fill="x", pady=2)

    tk.Label(frame_add, text="Categoría:", font=default_font, bg="#2c698d", fg="#ffffff").pack(anchor="w", pady=2)
    tk.Entry(frame_add, font=default_font).pack(fill="x", pady=2)

    tk.Button(frame_add, text="Agregar", font=default_font, bg="#bae8e8", command=add_Elemento).pack(pady=5)

    # Frame para "Control de Inventario"
    frame_inventory = tk.Frame(equipo_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_inventory.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.8)

    label_inventory = tk.Label(frame_inventory, text="Control de Inventario", font=header_font, bg="#2c698d", fg="#ffffff")
    label_inventory.pack(pady=5)

    entry_search = tk.Entry(frame_inventory, font=default_font)
    entry_search.pack(fill="x", pady=5)

    tk.Button(frame_inventory, text="Filtrar", font=default_font, bg="#bae8e8", command=filtrar_Elemento).pack(pady=5)

    # Tabla de inventario
    columns_inventory = ("ID", "Nombre", "Categoría", "Estado")
    tree_inventory = ttk.Treeview(frame_inventory, columns=columns_inventory, show="headings")

    for col in columns_inventory:
        tree_inventory.heading(col, text=col)
        tree_inventory.column(col, anchor="center", width=150)

    tree_inventory.pack(fill="both", expand=True, pady=5)

    # Botones de acciones para inventario
    frame_buttons_inventory = tk.Frame(frame_inventory, bg="#2c698d")
    frame_buttons_inventory.pack(pady=10)

    tk.Button(frame_buttons_inventory, text="Editar", font=default_font, bg="#bae8e8", command=editar_Elemento).pack(side="left", padx=5)
    tk.Button(frame_buttons_inventory, text="Eliminar", font=default_font, bg="#bae8e8", command=eliminar_Elemento).pack(side="left", padx=5)

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(equipo_window, text="Regresar al Menú Principal", font=default_font, bg="#bae8e8", command=lambda: regresar(callback, equipo_window))
    btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)

    # Iniciar la aplicación
    equipo_window.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal