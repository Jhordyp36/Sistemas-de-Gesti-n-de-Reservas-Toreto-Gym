import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def regresar(callback, ventana):
    ventana.destroy()  # Cierra la ventana actual
    callback()  # Regresa al menú principal

def ventana_pagos_facturacion(callback):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Módulo de Pagos y Facturación")
    root.state('zoomed')
    root.configure(bg="#272643")
    root.resizable(False, False)  # Evita que la ventana sea redimensionable

    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    # Frame principal
    main_frame = tk.Frame(root, bg="#272643")
    main_frame.pack(fill="both", expand=True)

    # Barra superior
    top_bar = tk.Frame(main_frame, bg="#2c698d", pady=5)
    top_bar.pack(side="top", fill="x")

    # Botón Regresar
    btn_regresar = tk.Button(top_bar, text="Regresar", font=default_font, bg="#bae8e8", command=lambda: regresar(callback, root))
    btn_regresar.pack(side="right", padx=10)

    # Botones Pago y Facturación
    btn_pago = tk.Button(top_bar, text="Pago", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(pago_frame, [pago_frame, facturacion_frame]))
    btn_pago.pack(side="left", padx=10)

    btn_facturacion = tk.Button(top_bar, text="Facturación", font=default_font, bg="#bae8e8", command=lambda: cambiar_vista(facturacion_frame, [pago_frame, facturacion_frame]))
    btn_facturacion.pack(side="left", padx=10)

    # Función para cambiar vistas
    def cambiar_vista(vista_frame, frames):
        for frame in frames:
            frame.pack_forget()
        vista_frame.pack(fill="both", expand=True)

    # Vista de Pago
    pago_frame = tk.Frame(main_frame, bg="#272643")
    label_pago = tk.Label(pago_frame, text="Vista de Pagos", font=header_font, bg="#272643", fg="#ffffff")
    label_pago.pack(pady=10)

    # Botones en la vista de pago
    btn_agregar_pago = tk.Button(pago_frame, text="Añadir Método de Pago", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Estamos en proceso", "Función de añadir método de pago en desarrollo..."))
    btn_agregar_pago.pack(pady=5)

    btn_eliminar_pago = tk.Button(pago_frame, text="Eliminar Método de Pago", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Estamos en proceso", "Función de eliminar método de pago en desarrollo..."))
    btn_eliminar_pago.pack(pady=5)

    # Tabla de Pagos
    columns_pago = ("Cédula", "Apellidos", "Nombres", "Método de Pago", "Fecha y Hora de Pago", "Monto Total")
    tree_pago = ttk.Treeview(pago_frame, columns=columns_pago, show="headings", height=15)

    for col in columns_pago:
        tree_pago.heading(col, text=col)
        tree_pago.column(col, anchor="center", width=150)

    tree_pago.pack(pady=10, padx=10)

    # Vista de Facturación
    facturacion_frame = tk.Frame(main_frame, bg="#272643")
    label_facturacion = tk.Label(facturacion_frame, text="Vista de Facturación", font=header_font, bg="#272643", fg="#ffffff")
    label_facturacion.pack(pady=10)

    # Botón en la vista de facturación
    btn_historial_facturacion = tk.Button(facturacion_frame, text="Consultar Historial de Facturación", font=default_font, bg="#bae8e8", command=lambda: messagebox.showinfo("Estamos en proceso", "Función de historial de facturación en desarrollo..."))
    btn_historial_facturacion.pack(pady=10)

    # Tabla de Facturación
    columns_facturacion = ("Cédula", "Apellidos", "Nombres", "Método de Pago", "Fecha y Hora de Facturación", "Monto Total")
    tree_facturacion = ttk.Treeview(facturacion_frame, columns=columns_facturacion, show="headings", height=15)

    for col in columns_facturacion:
        tree_facturacion.heading(col, text=col)
        tree_facturacion.column(col, anchor="center", width=150)

    tree_facturacion.pack(pady=10, padx=10)

    # Iniciar con la vista de pago visible
    pago_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    ventana_pagos_facturacion(lambda: print("Regresando al menú principal"))
