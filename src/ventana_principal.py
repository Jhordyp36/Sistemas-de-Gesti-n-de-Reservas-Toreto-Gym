import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from config.config import ICONS_DIR, IMAGES_DIR, DB_PATH  # Importa ICONS_DIR desde config
from src.utils.helpers import centrar_ventana, cargar_icono
from src.navegacion import navegar_a_iniciar_sesion

def crear_ventana_principal(rol):
    # Configuración de la ventana principal
    ventana_principal = Tk()
    ventana_principal.title("Sistemas de Gestión de Reservas Toreto Gym")
    ventana_principal.config(bg="#5688a8")
    centrar_ventana(ventana_principal, 900, 500)
    cargar_icono(ventana_principal, os.path.join(ICONS_DIR, "Icono.ico"))
    
    imagen_logotipo = PhotoImage(file=os.path.join(IMAGES_DIR, "Logotipo.png"))
    label_imagen = Label(ventana_principal, image=imagen_logotipo, bg="#5688a8")
    label_imagen.place(x=0, y=0)

    # Etiqueta de bienvenida
    label = Label(
        ventana_principal,
        text=f"Bienvenido, {rol}",
        font=("Helvetica", 18, "bold"),
        bg="#5688a8",
        fg="white"
    )
    label.pack(pady=15)

    # Frame para organizar los botones
    frame_botones = Frame(ventana_principal, bg="#5688a8")
    frame_botones.pack(pady=20)

    # Funciones de los botones
    def abrir_reservas():
        messagebox.showinfo("Reservas abiertas", "¡Estamos en proceso!")

    def abrir_clases_y_entrenadores():
        messagebox.showinfo("Clases y Entrenadores abiertos", "¡Estamos en proceso!")

    def abrir_usuarios():
        # Crear ventana modal
        ventana_usuarios = Toplevel()
        ventana_usuarios.title("Gestión de Usuarios")
        ventana_usuarios.config(bg="lightgray")
        centrar_ventana(ventana_usuarios, 600, 400)
        ventana_usuarios.grab_set()  # Hace la ventana modal
        ventana_usuarios.resizable(False, False)

        # Encabezado
        Label(
            ventana_usuarios,
            text="Gestión de Usuarios",
            font=("Helvetica", 16, "bold"),
            bg="lightgray",
            fg="black"
        ).pack(pady=10)

        # Frame para el Treeview
        frame_tree = Frame(ventana_usuarios)
        frame_tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Configuración del Treeview
        tree_agenda = ttk.Treeview(
            frame_tree, columns=("Id", "Usuario", "Rol"), show="headings", height=10
        )
        tree_agenda.pack(fill=BOTH, expand=True)

        # Configuración de las columnas
        tree_agenda.heading("Id", text="ID")
        tree_agenda.heading("Usuario", text="Usuario")
        tree_agenda.heading("Rol", text="Rol")

        tree_agenda.column("Id", anchor=CENTER, width=100)
        tree_agenda.column("Usuario", anchor=W, width=200)
        tree_agenda.column("Rol", anchor=W, width=150)

        # Conexión a la base de datos para obtener usuarios
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id, usuario, rol FROM usuarios")  # Obtenemos ID, usuario y rol
            usuarios = cursor.fetchall()
            conn.close()

            # Insertar datos en el Treeview
            if usuarios:
                for id_usuario, usuario, rol in usuarios:
                    tree_agenda.insert("", END, values=(id_usuario, usuario, rol))
            else:
                messagebox.showinfo("Información", "No hay usuarios registrados.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")

        # Botón para regresar
        def regresar():
            ventana_usuarios.destroy()

        boton_regresar = Button(
            ventana_usuarios,
            text="Regresar",
            font=("Helvetica", 12),
            bg="blue",
            fg="white",
            command=regresar
        )
        boton_regresar.pack(pady=10)


    def abrir_membresias():
        messagebox.showinfo("Gestión de Membresías abierta", "¡Estamos en proceso!")

    def abrir_equipos():
        messagebox.showinfo("Gestión de Equipos abierta", "¡Estamos en proceso!")

    def abrir_reportes():
        messagebox.showinfo("Reportes abiertos", "¡Estamos en proceso!")

    def abrir_configuracion():
        messagebox.showinfo("Configuración abierta", "¡Estamos en proceso!")

    def abrir_soporte():
        messagebox.showinfo("Soporte abierto", "¡Estamos en proceso!")
        
    

    def cerrar_sesion():
        ventana_principal.destroy()
        navegar_a_iniciar_sesion()

    # Botones según el rol
    botones_administrador = [
        ("Reservas", abrir_reservas),
        ("Clases y Entrenadores", abrir_clases_y_entrenadores),
        ("Gestión de Usuarios", abrir_usuarios),
        ("Membresías y Pagos", abrir_membresias),
        ("Gestión de Equipos", abrir_equipos),
        ("Reportes y Estadísticas", abrir_reportes),
        ("Configuración", abrir_configuracion),
        ("Soporte y Ayuda", abrir_soporte),
    ]

    botones_usuario = [
        ("Clases y Entrenadores", abrir_clases_y_entrenadores),
        ("Membresías y Pagos", abrir_membresias),
        ("Configuración", abrir_configuracion),
        ("Soporte y Ayuda", abrir_soporte),
    ]

    # Determinar los botones a mostrar según el rol
    botones = botones_administrador if rol == "Administrador" else botones_usuario

    # Creación de botones en una cuadrícula
    for i, (nombre, comando) in enumerate(botones):
        boton = Button(
            frame_botones,
            text=nombre,
            font=("Helvetica", 12),
            width=20,
            height=2,
            bg="lightblue",
            fg="black",
            command=comando,
        )
        boton.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    # Botón de cerrar sesión
    boton_cerrar = Button(
        ventana_principal,
        text="Cerrar sesión",
        font=("Helvetica", 12),
        bg="blue",
        fg="white",
        command=cerrar_sesion,
    )
    boton_cerrar.pack(pady=20)

    ventana_principal.mainloop()
