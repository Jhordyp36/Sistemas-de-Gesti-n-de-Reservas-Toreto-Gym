import tkinter as tk
from tkinter import ttk, messagebox

def show_soon_message():
    messagebox.showinfo("Muy pronto", "¡Estamos en proceso!")

def ventana_membresiaspagos_administrador(callback):
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")
    
    admin_window = tk.Tk()
    admin_window.title("Membresías y Pagos - Administrador")
    admin_window.state("zoomed")
    admin_window.configure(bg="#272643")

    # Configuración general para los botones
    button_style = { 
        "wraplength": 150, 
        "justify": "center", 
        "anchor": "center"
    }

    # Frame de Métodos de Pago
    frame_metodo_pago = tk.LabelFrame(admin_window, text="Métodos de Pago", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_metodo_pago.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.48)

    # Configuración de filas y columnas
    frame_metodo_pago.grid_rowconfigure(0, weight=1)  # Botones
    frame_metodo_pago.grid_rowconfigure(1, weight=4)  # Tabla
    frame_metodo_pago.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Botones en Métodos de Pago
    botones_metodo_pago = [
        "Habilitar Método de Pago",
        "Deshabilitar Método de Pago",
        "Añadir Método de Pago",
        "Eliminar Método de Pago"
    ]

    for idx, text in enumerate(botones_metodo_pago):
        btn = tk.Button(frame_metodo_pago, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Métodos de Pago
    scrollbar_x = tk.Scrollbar(frame_metodo_pago, orient="horizontal")
    scrollbar_y = tk.Scrollbar(frame_metodo_pago, orient="vertical")

    table_metodo_pago = ttk.Treeview(
        frame_metodo_pago,
        columns=("cedula", "apellidos", "nombres", "metodo_pago"),
        xscrollcommand=scrollbar_x.set,
        yscrollcommand=scrollbar_y.set
    )
    table_metodo_pago.heading("cedula", text="Cédula")
    table_metodo_pago.heading("apellidos", text="Apellidos")
    table_metodo_pago.heading("nombres", text="Nombres")
    table_metodo_pago.heading("metodo_pago", text="Método de Pago")
    table_metodo_pago['show'] = 'headings'

    scrollbar_x.config(command=table_metodo_pago.xview)
    scrollbar_y.config(command=table_metodo_pago.yview)

    table_metodo_pago.grid(row=1, column=0, columnspan=4, sticky="nsew")
    scrollbar_x.grid(row=2, column=0, columnspan=4, sticky="ew")
    scrollbar_y.grid(row=1, column=4, sticky="ns")

    # Frame de Membresías
    frame_membresias = tk.LabelFrame(admin_window, text="Membresías", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_membresias.place(relx=0.5, rely=0.01, relwidth=0.48, relheight=0.48)

    # Configuración de filas y columnas
    frame_membresias.grid_rowconfigure(0, weight=1)  # Botones
    frame_membresias.grid_rowconfigure(1, weight=4)  # Tabla
    frame_membresias.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Botones en Membresías
    botones_membresias = [
        "Agregar Membresía",
        "Eliminar Membresía",
        "Comprar Membresía",
        "Renovar Membresía"
    ]

    for idx, text in enumerate(botones_membresias):
        btn = tk.Button(frame_membresias, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Membresías
    scrollbar_x_mem = tk.Scrollbar(frame_membresias, orient="horizontal")
    scrollbar_y_mem = tk.Scrollbar(frame_membresias, orient="vertical")

    table_membresias = ttk.Treeview(
        frame_membresias,
        columns=("cedula", "apellidos", "nombres", "estado_membresia"),
        xscrollcommand=scrollbar_x_mem.set,
        yscrollcommand=scrollbar_y_mem.set
    )
    table_membresias.heading("cedula", text="Cédula")
    table_membresias.heading("apellidos", text="Apellidos")
    table_membresias.heading("nombres", text="Nombres")
    table_membresias.heading("estado_membresia", text="Estado Membresía")
    table_membresias['show'] = 'headings'

    scrollbar_x_mem.config(command=table_membresias.xview)
    scrollbar_y_mem.config(command=table_membresias.yview)

    table_membresias.grid(row=1, column=0, columnspan=4, sticky="nsew")
    scrollbar_x_mem.grid(row=2, column=0, columnspan=4, sticky="ew")
    scrollbar_y_mem.grid(row=1, column=4, sticky="ns")

    # Frame de Pagos
    frame_pagos = tk.LabelFrame(admin_window, text="Pagos", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_pagos.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.48)

    # Configuración de filas y columnas
    frame_pagos.grid_rowconfigure(0, weight=1)  # Botones
    frame_pagos.grid_rowconfigure(1, weight=4)  # Tabla
    frame_pagos.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Botones en Pagos
    botones_pagos = [
        "Registrar Pago Manual",
        "Generar Reporte de Pagos",
        "Generar Factura",
        "Aplicar Descuento"
    ]

    for idx, text in enumerate(botones_pagos):
        btn = tk.Button(frame_pagos, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Pagos
    scrollbar_x_pagos = tk.Scrollbar(frame_pagos, orient="horizontal")
    scrollbar_y_pagos = tk.Scrollbar(frame_pagos, orient="vertical")

    table_pagos = ttk.Treeview(
        frame_pagos,
        columns=("cedula", "apellidos", "nombres", "metodo_pago", "reembolso", "aplica_descuento", "pago_total"),
        xscrollcommand=scrollbar_x_pagos.set,
        yscrollcommand=scrollbar_y_pagos.set
    )
    table_pagos.heading("cedula", text="Cédula")
    table_pagos.heading("apellidos", text="Apellidos")
    table_pagos.heading("nombres", text="Nombres")
    table_pagos.heading("metodo_pago", text="Método de Pago")
    table_pagos.heading("reembolso", text="Reembolso")
    table_pagos.heading("aplica_descuento", text="Aplica Descuento")
    table_pagos.heading("pago_total", text="Pago Total")
    table_pagos['show'] = 'headings'

    scrollbar_x_pagos.config(command=table_pagos.xview)
    scrollbar_y_pagos.config(command=table_pagos.yview)

    table_pagos.grid(row=1, column=0, columnspan=4, sticky="nsew")
    scrollbar_x_pagos.grid(row=2, column=0, columnspan=4, sticky="ew")
    scrollbar_y_pagos.grid(row=1, column=4, sticky="ns")
    
    # Botón para regresar al menú principal
    btn_regresar = tk.Button(admin_window, text="Regresar al Menú Principal", font=default_font, bg="#e3f6f5", command=lambda: regresar(callback, admin_window))
    btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)


    admin_window.mainloop()


def ventana_membresiaspagos_usuario(callback):
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")
    user_window = tk.Tk()
    user_window.title("Membresías y Pagos - Usuario")
    user_window.state("zoomed")
    user_window.configure(bg="#272643")

    # Configuración general para los botones
    button_style = {
        "wraplength": 150,
        "justify": "center",
        "anchor": "center"
    }

    # Frame de Métodos de Pago
    frame_metodo_pago = tk.LabelFrame(user_window, text="Métodos de Pago", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_metodo_pago.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.48)

    frame_metodo_pago.grid_rowconfigure(0, weight=1)  # Botones
    frame_metodo_pago.grid_rowconfigure(1, weight=4)  # Tabla
    frame_metodo_pago.grid_columnconfigure((0, 1), weight=1)

    # Botones en Métodos de Pago
    botones_metodo_pago = [
        "Añadir Método de Pago",
        "Eliminar Método de Pago"
    ]

    for idx, text in enumerate(botones_metodo_pago):
        btn = tk.Button(frame_metodo_pago, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Métodos de Pago
    scrollbar_x_user_metodo = tk.Scrollbar(frame_metodo_pago, orient="horizontal")
    scrollbar_y_user_metodo = tk.Scrollbar(frame_metodo_pago, orient="vertical")

    table_user_metodo_pago = ttk.Treeview(
        frame_metodo_pago,
        columns=("titulo1", "titulo2"),
        xscrollcommand=scrollbar_x_user_metodo.set,
        yscrollcommand=scrollbar_y_user_metodo.set
    )
    table_user_metodo_pago.heading("titulo1", text="Título 1")
    table_user_metodo_pago.heading("titulo2", text="Título 2")
    table_user_metodo_pago['show'] = 'headings'

    scrollbar_x_user_metodo.config(command=table_user_metodo_pago.xview)
    scrollbar_y_user_metodo.config(command=table_user_metodo_pago.yview)

    table_user_metodo_pago.grid(row=1, column=0, columnspan=2, sticky="nsew")
    scrollbar_x_user_metodo.grid(row=2, column=0, columnspan=2, sticky="ew")
    scrollbar_y_user_metodo.grid(row=1, column=2, sticky="ns")

    # Frame de Membresías
    frame_membresias = tk.LabelFrame(user_window, text="Membresías", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_membresias.place(relx=0.5, rely=0.01, relwidth=0.48, relheight=0.48)

    frame_membresias.grid_rowconfigure(0, weight=1)  # Botones
    frame_membresias.grid_rowconfigure(1, weight=4)  # Tabla
    frame_membresias.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Botones en Membresías
    botones_membresias = [
        "Comprar Membresía",
        "Renovar Membresía",
        "Cancelar Membresía",
        "Consultar Estado de Membresía"
    ]

    for idx, text in enumerate(botones_membresias):
        btn = tk.Button(frame_membresias, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Membresías
    scrollbar_x_mem_user = tk.Scrollbar(frame_membresias, orient="horizontal")
    scrollbar_y_mem_user = tk.Scrollbar(frame_membresias, orient="vertical")

    table_membresias_user = ttk.Treeview(
        frame_membresias,
        columns=("cedula", "apellidos", "nombres", "estado_membresia"),
        xscrollcommand=scrollbar_x_mem_user.set,
        yscrollcommand=scrollbar_y_mem_user.set
    )
    table_membresias_user.heading("cedula", text="Cédula")
    table_membresias_user.heading("apellidos", text="Apellidos")
    table_membresias_user.heading("nombres", text="Nombres")
    table_membresias_user.heading("estado_membresia", text="Estado Membresía")
    table_membresias_user['show'] = 'headings'

    scrollbar_x_mem_user.config(command=table_membresias_user.xview)
    scrollbar_y_mem_user.config(command=table_membresias_user.yview)

    table_membresias_user.grid(row=1, column=0, columnspan=4, sticky="nsew")
    scrollbar_x_mem_user.grid(row=2, column=0, columnspan=4, sticky="ew")
    scrollbar_y_mem_user.grid(row=1, column=4, sticky="ns")

    # Frame de Pagos
    frame_pagos = tk.LabelFrame(user_window, text="Pagos", padx=10, pady=10, font = header_font, bg="#2c698d", relief="groove", fg="#ffffff")
    frame_pagos.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.48)

    frame_pagos.grid_rowconfigure(0, weight=1)  # Botones
    frame_pagos.grid_rowconfigure(1, weight=4)  # Tabla
    frame_pagos.grid_columnconfigure((0, 1), weight=1)

    # Botones en Pagos
    botones_pagos = [
        "Configurar Pago Automático",
        "Generar Factura"
    ]

    for idx, text in enumerate(botones_pagos):
        btn = tk.Button(frame_pagos, text=text, **button_style, command=show_soon_message, font = default_font, bg="#bae8e8")
        btn.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

    # Scroll y Tabla Pagos
    scrollbar_x_pagos_user = tk.Scrollbar(frame_pagos, orient="horizontal")
    scrollbar_y_pagos_user = tk.Scrollbar(frame_pagos, orient="vertical")

    table_pagos_user = ttk.Treeview(
        frame_pagos,
        columns=("pagado", "fecha_pago", "proximo_pago"),
        xscrollcommand=scrollbar_x_pagos_user.set,
        yscrollcommand=scrollbar_y_pagos_user.set
    )
    table_pagos_user.heading("pagado", text="¿Pagado?")
    table_pagos_user.heading("fecha_pago", text="Fecha de Pago")
    table_pagos_user.heading("proximo_pago", text="Próximo Pago")
    table_pagos_user['show'] = 'headings'

    scrollbar_x_pagos_user.config(command=table_pagos_user.xview)
    scrollbar_y_pagos_user.config(command=table_pagos_user.yview)

    table_pagos_user.grid(row=1, column=0, columnspan=2, sticky="nsew")
    scrollbar_x_pagos_user.grid(row=2, column=0, columnspan=2, sticky="ew")
    scrollbar_y_pagos_user.grid(row=1, column=2, sticky="ns")
    
    # Botón para regresar al menú principal
    btn_regresar = tk.Button(user_window, text="Regresar al Menú Principal", font=default_font, bg="#e3f6f5", command=lambda: regresar(callback, user_window))
    btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)


    user_window.mainloop()

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal