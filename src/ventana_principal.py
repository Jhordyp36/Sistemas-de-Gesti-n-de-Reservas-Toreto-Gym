import os
from tkinter import CENTER, Button, Frame, Label, PhotoImage, Tk
from config.config import ICONS_DIR, IMAGES_DIR
from src.utils.helpers import cargar_icono
from src.navegacion import navegar_a_iniciar_sesion
from src.membresias import ventana_membresias
from src.servicios import ventana_clases_entrenadores
from src.pagos_facturacion import ventana_pagos_facturacion
from src.administracion_sistema import ventana_administracion
from src.gestion_equipos import ventana_gestion_equipos

def crear_ventana_principal(rol, usuario):
    # Configuración de la ventana principal
    ventana_principal = Tk()
    ventana_principal.title("Sistemas de Gestión de Reservas Toreto Gym")
    ventana_principal.state('zoomed')  # Pantalla completa
    ventana_principal.configure(bg="#272643")  # Fondo oscuro

    # Cargar el ícono
    cargar_icono(ventana_principal, os.path.join(ICONS_DIR, "Icono.ico"))

    # Imagen de logotipo
    imagen_logotipo = PhotoImage(file=os.path.join(IMAGES_DIR, "Logotipo.png"))
    label_imagen = Label(ventana_principal, image=imagen_logotipo, bg="#272643")
    label_imagen.place(x=0, y=0, relwidth=1)

    # Etiqueta de bienvenida (se coloca debajo de la imagen)
    label = Label(ventana_principal, text=f"Bienvenido, {usuario}", font=("Segoe UI", 18, "bold"), bg="#272643", fg="white")
    label.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Frame para organizar los botones (centrado)
    frame_botones = Frame(ventana_principal, bg="#2c698d", padx=10, pady=10)
    frame_botones.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centrado en el medio de la ventana

    # Funciones de los botones
    def abrir_membresias():
        ventana_principal.destroy()
        ventana_membresias(usuario, lambda: crear_ventana_principal(rol, usuario))

    def abrir_servicios():
        ventana_principal.destroy()
        ventana_clases_entrenadores(lambda: crear_ventana_principal(rol, usuario))

    def abrir_pagos_facturacion():
        ventana_principal.destroy()
        ventana_pagos_facturacion(lambda: crear_ventana_principal(rol, usuario))

    def abrir_administracion():
        ventana_principal.destroy()
        ventana_administracion(usuario, lambda: crear_ventana_principal(rol, usuario))

    def abrir_gestion_equipos():
        ventana_principal.destroy()
        ventana_gestion_equipos(lambda: crear_ventana_principal(rol, usuario))

    # Creación de botones nuevos
    boton_membresias = Button(
        frame_botones,
        text="Membresías",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_membresias,
        relief="groove",
        bd=2
    )
    boton_membresias.grid(row=0, column=0, padx=10, pady=10)

    boton_servicios = Button(
        frame_botones,
        text="Servicios",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_servicios,
        relief="groove",
        bd=2
    )
    boton_servicios.grid(row=0, column=1, padx=10, pady=10)

    boton_pagos_facturacion = Button(
        frame_botones,
        text="Pagos y Facturación",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_pagos_facturacion,
        relief="groove",
        bd=2
    )
    boton_pagos_facturacion.grid(row=1, column=0, padx=10, pady=10)

    boton_administracion = Button(
        frame_botones,
        text="Administración del Sistema",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_administracion,
        relief="groove",
        bd=2
    )
    boton_administracion.grid(row=1, column=1, padx=10, pady=10)

    boton_gestion_equipos = Button(
        frame_botones,
        text="Gestión de Equipos",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_gestion_equipos,
        relief="groove",
        bd=2
    )
    boton_gestion_equipos.grid(row=2, column=0, padx=10, pady=10)

    # Botón de cerrar sesión dentro del frame_botones
    boton_cerrar = Button(
        frame_botones,
        text="Cerrar sesión",
        font=("Segoe UI", 12, "bold"),
        width=20,
        height=2,
        bg="#e3f6f5",
        fg="black",
        command=lambda: ventana_principal.destroy() or navegar_a_iniciar_sesion(),
        relief="groove",
        bd=2
    )
    boton_cerrar.grid(row=3, column=0, columnspan=2, pady=20)  # Se pone en una nueva fila

    ventana_principal.mainloop()
