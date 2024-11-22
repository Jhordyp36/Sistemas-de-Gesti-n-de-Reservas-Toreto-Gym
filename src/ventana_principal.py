import os
from tkinter import *
from tkinter import messagebox
from config.config import ICONS_DIR, IMAGES_DIR # Importa ICONS_DIR desde config
from src.utils.helpers import centrar_ventana, cargar_icono
from src.navegacion import navegar_a_iniciar_sesion

def crear_ventana_principal():
    # Configuración de la ventana principal
    ventana_principal = Tk()
    ventana_principal.title("Sistemas de Gestión de Reservas Toreto Gym")
    ventana_principal.config(bg="#5688a8")
    centrar_ventana(ventana_principal, 900, 500)
    cargar_icono(ventana_principal, os.path.join(ICONS_DIR, "Icono.ico"))
    
    imagen_logotipo = PhotoImage(file=os.path.join(IMAGES_DIR, "Logotipo.png"))
    label_imagen = Label(ventana_principal, image=imagen_logotipo, bg= "#5688a8")
    label_imagen.place(x=0, y=0)

    # Etiqueta de bienvenida
    label = Label(ventana_principal, text="Bienvenido al Sistema de Gestión de Reservas", font=("Helvetica", 18, "bold"), bg="#5688a8", fg="white")
    label.pack(pady=15)

    # Frame para organizar los botones
    frame_botones = Frame(ventana_principal, bg="#5688a8")
    frame_botones.pack(pady=20)

    # Funciones de los botones
    def abrir_reservas():
        messagebox.showinfo("Reservas abiertas","¡Estamos en proceso!")

    def abrir_clases_y_entrenadores():
        messagebox.showinfo("Clases y Entrenadores abiertos","¡Estamos en proceso!")

    def abrir_usuarios():
        messagebox.showinfo("Gestión de Usuarios abierta","¡Estamos en proceso!")

    def abrir_membresias():
        messagebox.showinfo("Gestión de Membresías abierta","¡Estamos en proceso!")

    def abrir_equipos():
        messagebox.showinfo("Gestión de Equipos abierta","¡Estamos en proceso!")

    def abrir_reportes():
        messagebox.showinfo("Reportes abiertos","¡Estamos en proceso!")

    def abrir_configuracion():
        messagebox.showinfo("Configuración abierta","¡Estamos en proceso!")

    def abrir_soporte():
        messagebox.showinfo("Soporte abierto","¡Estamos en proceso!")
    def cerrar_sesion():
        ventana_principal.destroy()
        navegar_a_iniciar_sesion()

    # Lista de botones con sus nombres y funciones
    botones = [
        ("Reservas", abrir_reservas),
        ("Clases y Entrenadores", abrir_clases_y_entrenadores),
        ("Gestión de Usuarios", abrir_usuarios),
        ("Membresías y Pagos", abrir_membresias),
        ("Gestión de Equipos", abrir_equipos),
        ("Reportes y Estadísticas", abrir_reportes),
        ("Configuración", abrir_configuracion),
        ("Soporte y Ayuda", abrir_soporte)
    ]

    # Creación de botones en una cuadrícula
    for i, (nombre, comando) in enumerate(botones):
        boton = Button(frame_botones, text=nombre, font=("Helvetica", 12), width=20, height=2, 
                       bg="lightblue", fg="black", command=comando)
        boton.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    # Botón de cerrar sesión
    boton_cerrar = Button(ventana_principal, text="Cerrar sesión", font=("Helvetica", 12), 
                          bg="red", fg="white", command=cerrar_sesion)
    boton_cerrar.pack(pady=20)

    ventana_principal.mainloop()
