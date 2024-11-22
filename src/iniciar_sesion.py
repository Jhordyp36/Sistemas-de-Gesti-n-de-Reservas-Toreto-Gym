import os
import sqlite3
from tkinter import *
from tkinter import messagebox
from config.config import ICONS_DIR, IMAGES_DIR, DB_PATH  # Importa desde config
from src.utils.helpers import centrar_ventana, cargar_icono
from src.navegacion import navegar_a_ventana_principal

def verificar_login(campo_usuario, campo_contrasena, login):
    usuario = campo_usuario.get()
    contrasena = campo_contrasena.get()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
        login.destroy()
        navegar_a_ventana_principal()
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

def registrar_usuario():
    ventana_registro = Toplevel()
    ventana_registro.title("Registrar Usuario")
    ventana_registro.config(bg="lightblue")
    cargar_icono(ventana_registro, os.path.join(ICONS_DIR, "Icono.ico"))
    centrar_ventana(ventana_registro, 400, 300)
    ventana_registro.resizable(False, False)

    Label(ventana_registro, text="Nuevo Usuario:", font=("Helvetica", 12), bg="lightblue").place(x=35, y=50)
    campo_usuario_registro = Entry(ventana_registro, font=("Helvetica", 12))
    campo_usuario_registro.place(x=150, y=50, width=200, height=25)

    Label(ventana_registro, text="Contraseña:", font=("Helvetica", 12), bg="lightblue").place(x=35, y=100)
    campo_contrasena_registro = Entry(ventana_registro, font=("Helvetica", 12), show="*")
    campo_contrasena_registro.place(x=150, y=100, width=200, height=25)

    def guardar_usuario():
        usuario = campo_usuario_registro.get()
        contrasena = campo_contrasena_registro.get()

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showerror("Error", "El usuario ya existe.")
        else:
            cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
            conn.commit()
            messagebox.showinfo("Registro exitoso", "¡Usuario registrado exitosamente!")
            ventana_registro.destroy()

        conn.close()

    Button(ventana_registro, text="Registrar", font=("Helvetica", 12), command=guardar_usuario).place(x=150, y=150, width=100, height=30)
    Button(ventana_registro, text="Regresar", font=("Helvetica", 12), command=ventana_registro.destroy).place(x=150, y=200, width=100, height=30)

def crear_ventana_iniciar_sesion():
    login = Tk()
    login.title("Sistemas de Gestión de Reservas Toreto Gym")
    login.config(bg="lightblue")
    login.iconbitmap(os.path.join(ICONS_DIR, "Icono.ico"))
    login.resizable(False, False)

    centrar_ventana(login, 816, 500)

    imagen_superior = PhotoImage(file=os.path.join(IMAGES_DIR, "Información.png"))
    label_imagen = Label(login, image=imagen_superior)
    label_imagen.place(x=0, y=0)

    label_titulo = Label(login, text="Bienvenido/a", font=("Helvetica", 18, "bold"), bg="lightblue")
    label_titulo.place(x=322, y=255)
    label_instruccion = Label(login, text="Ingresa tus datos para acceder", font=("Helvetica", 12), bg="lightblue")
    label_instruccion.place(x=290, y=290)

    Label(login, text="Usuario:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=320)
    campo_usuario = Entry(login, font=("Helvetica", 12))
    campo_usuario.place(x=300, y=320, width=200, height=25)

    Label(login, text="Contraseña:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=370)
    campo_contrasena = Entry(login, font=("Helvetica", 12), show="*")
    campo_contrasena.place(x=300, y=370, width=200, height=25)

    def presionar_enter(event):
        verificar_login(campo_usuario, campo_contrasena, login)

    campo_contrasena.bind("<Return>", presionar_enter)

    Button(login, text="Iniciar sesión", font=("Helvetica", 12), command=lambda: verificar_login(campo_usuario, campo_contrasena, login)).place(x=350, y=420, width=100, height=30)
    Button(login, text="Registrarse", font=("Helvetica", 12), command=registrar_usuario).place(x=600, y=350, width=100, height=30)

    label_olvidada = Label(login, text="¿Olvidaste tu contraseña?", font=("Helvetica", 10, "italic"), bg="lightblue", fg="blue")
    label_olvidada.place(x=320, y=460)

    login.mainloop()
