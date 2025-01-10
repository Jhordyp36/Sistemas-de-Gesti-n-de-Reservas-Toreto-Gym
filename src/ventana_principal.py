import os
from tkinter import CENTER, Button, Frame, Label, Menu, PhotoImage, Tk, messagebox
from config.config import ICONS_DIR, IMAGES_DIR
from src.utils.helpers import cargar_icono
from src.navegacion import navegar_a_iniciar_sesion
from src.clases_Entrenadores import ventana_ClasesEntrenadores
from src.membresias_pagos import ventana_membresiaspagos_administrador, ventana_membresiaspagos_usuario
from src.gestion_equipos import ventana_GestionEquipos
from src.reportes_estadisticas import ventana_ReportesEstadisticas_usuario, ventana_ReportesEstadisticas_administrador
from src.reservas import ventana_reservas_administrador, ventana_reservas_usuario
from src.administracion_sistema import ventana_administracion

def crear_ventana_principal(rol):
    # Configuración de la ventana principal
    ventana_principal = Tk()
    ventana_principal.title("Sistemas de Gestión de Reservas Toreto Gym")
    ventana_principal.state('zoomed')  # Pantalla completa
    ventana_principal.configure(bg="#272643")  # Fondo oscuro similar al segundo ejemplo

    # Cargar el ícono
    cargar_icono(ventana_principal, os.path.join(ICONS_DIR, "Icono.ico"))

    # Imagen de logotipo
    imagen_logotipo = PhotoImage(file=os.path.join(IMAGES_DIR, "Logotipo.png"))
    label_imagen = Label(ventana_principal, image=imagen_logotipo, bg="#272643")
    label_imagen.place(x=0, y=0, relwidth=1)

    # Etiqueta de bienvenida (se coloca debajo de la imagen)
    label = Label(ventana_principal, text=f"Bienvenido, {rol}", font=("Segoe UI", 18, "bold"), bg="#272643", fg="white")
    label.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Crear barra de menú
    barra_menu = Menu(ventana_principal, bg="#2c698d", fg="white")
    ventana_principal.config(menu=barra_menu)

    # Frame para organizar los botones (centrado)
    frame_botones = Frame(ventana_principal, bg="#2c698d", padx=10, pady=10)
    frame_botones.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centrado en el medio de la ventana

    # Funciones de los botones
    def abrir_administracion():
        ventana_principal.destroy()  # Cierra la ventana principal
        ventana_administracion(lambda: crear_ventana_principal(rol))

    def abrir_reservas():
        ventana_principal.destroy()  # Cierra la ventana principal
        if rol == "Administrador":
            ventana_reservas_administrador(lambda: crear_ventana_principal(rol))
        else:
            ventana_reservas_usuario(lambda: crear_ventana_principal(rol))

    def abrir_clases_y_entrenadores():
        ventana_principal.destroy()  # Cierra la ventana principal
        ventana_ClasesEntrenadores(lambda: crear_ventana_principal(rol))

    def abrir_membresias():
        ventana_principal.destroy()  # Cierra la ventana principal
        if rol == "Administrador":
            ventana_membresiaspagos_administrador(lambda: crear_ventana_principal(rol))
        else:
            ventana_membresiaspagos_usuario(lambda: crear_ventana_principal(rol))

    def abrir_equipos():
        ventana_principal.destroy()  # Cierra la ventana principal
        ventana_GestionEquipos(lambda: crear_ventana_principal(rol))

    def abrir_reportes():
        ventana_principal.destroy()  # Cierra la ventana principal
        if rol == "Administrador":
            ventana_ReportesEstadisticas_administrador(lambda: crear_ventana_principal(rol))
        else:
            ventana_ReportesEstadisticas_usuario(lambda: crear_ventana_principal(rol))


    # Menú de soporte (siempre visible)
    menu_soporte = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Soporte", menu=menu_soporte)
    menu_soporte.add_command(label="Ayuda", command=lambda: messagebox.showinfo("Soporte", "¡Estamos en proceso!"))

    # Menú de Administración del Sistema (solo para administrador)
    if rol == "Administrador":
        menu_configuracion = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Administración del Sistema", menu=menu_configuracion)
        menu_configuracion.add_command(label="Opciones", command=abrir_administracion)

    # Creación de botones comunes
    boton_reservas = Button(
        frame_botones,
        text="Reservas",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_reservas,
        relief="groove",
        bd=2
    )
    boton_reservas.grid(row=0, column=0, padx=10, pady=10)

    boton_membresias = Button(
        frame_botones,
        text="Membresías y Pagos",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_membresias,
        relief="groove",
        bd=2
    )
    boton_membresias.grid(row=1, column=0, padx=10, pady=10)

    boton_reportes = Button(
        frame_botones,
        text="Reportes y Estadísticas",
        font=("Segoe UI", 12),
        width=20,
        height=2,
        bg="#bae8e8",
        fg="black",
        command=abrir_reportes,
        relief="groove",
        bd=2
    )
    boton_reportes.grid(row=2, column=0, padx=10, pady=10)

    # Botones exclusivos para administrador
    if rol == "Administrador":
        boton_clases = Button(
            frame_botones,
            text="Clases y Entrenadores",
            font=("Segoe UI", 12),
            width=20,
            height=2,
            bg="#bae8e8",
            fg="black",
            command=abrir_clases_y_entrenadores,
            relief="groove",
            bd=2
        )
        boton_clases.grid(row=0, column=1, padx=10, pady=10)

        boton_equipos = Button(
            frame_botones,
            text="Gestión de Equipos",
            font=("Segoe UI", 12),
            width=20,
            height=2,
            bg="#bae8e8",
            fg="black",
            command=abrir_equipos,
            relief="groove",
            bd=2
        )
        boton_equipos.grid(row=1, column=1, padx=10, pady=10)

    # Botón de cerrar sesión dentro del frame_botones
    boton_cerrar = Button(frame_botones, text="Cerrar sesión", font=("Segoe UI", 12, "bold"), width=20, height=2, bg="#e3f6f5", fg="black",
                          command=lambda: ventana_principal.destroy() or navegar_a_iniciar_sesion(), relief="groove", bd=2)
    boton_cerrar.grid(row=3, column=0, columnspan=2, pady=20)  # Se pone en una nueva fila

    ventana_principal.mainloop()
