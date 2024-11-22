import sqlite3
import os
from tkinter import *
from tkinter import messagebox

# Función para centrar la ventana
def centrar_ventana(ventana, ancho, alto):
    # Obtener las dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular la posición centrada
    x = (pantalla_ancho - ancho) // 2
    y = (pantalla_alto - alto) // 2

    # Colocar la ventana en el centro
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

# Función para verificar el login
def verificar_login(campo_usuario, campo_contrasena, DB_PATH):
    usuario = campo_usuario.get()
    contrasena = campo_contrasena.get()

    # Conectar a la base de datos
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

# Función para registrar un nuevo usuario
def registrar_usuario(ICONS_DIR, DB_PATH):
    # Crear una nueva ventana para el registro
    ventana_registro = Toplevel()
    ventana_registro.title("Registrar Usuario")
    ventana_registro.config(bg="lightblue")
    ventana_registro.iconbitmap(os.path.join(ICONS_DIR, "Icono.ico"))
    ventana_registro.resizable(False, False)

    # Centrar la ventana de registro
    centrar_ventana(ventana_registro, 400, 300)

    # Crear las etiquetas y campos de entrada para el registro
    Label(ventana_registro, text="Nuevo Usuario:", font=("Helvetica", 12), bg="lightblue").place(x=35, y=50)
    campo_usuario_registro = Entry(ventana_registro, font=("Helvetica", 12))
    campo_usuario_registro.place(x=150, y=50, width=200, height=25)
    Label(ventana_registro, text="Contraseña:", font=("Helvetica", 12), bg="lightblue").place(x=35, y=100)
    campo_contrasena_registro = Entry(ventana_registro, font=("Helvetica", 12), show="*")
    campo_contrasena_registro.place(x=150, y=100, width=200, height=25)

    def guardar_usuario():
        usuario = campo_usuario_registro.get()
        contrasena = campo_contrasena_registro.get()

        # Verificar si el usuario ya existe
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
            ventana_registro.destroy()  # Cerrar la ventana de registro

        conn.close()

    Button(ventana_registro, text="Registrar", font=("Helvetica", 12), command=guardar_usuario).place(x=150, y=150, width=100, height=30)
    Button(ventana_registro, text="Regresar", font=("Helvetica", 12), command=ventana_registro.destroy).place(x=150, y=200, width=100, height=30)

# Función para crear la ventana de login
def crear_ventana_iniciar_sesion(ICONS_DIR, IMAGES_DIR, DB_PATH):
    login = Tk()
    login.title("Sistemas de Gestión de Reservas Toreto Gym")
    login.config(bg="lightblue")
    login.iconbitmap(os.path.join(ICONS_DIR, "Icono.ico"))
    login.resizable(False, False)

    # Centrar la ventana de login
    centrar_ventana(login, 816, 500)

    # Cargar imagen en la ventana
    imagen_superior = PhotoImage(file=os.path.join(IMAGES_DIR, "Información.png"))
    label_imagen = Label(login, image=imagen_superior)
    label_imagen.place(x=0, y=0)

    # Título y mensaje
    label_titulo = Label(login, text="Bienvenido/a", font=("Helvetica", 18, "bold"), bg="lightblue")
    label_titulo.place(x=322, y=255)
    label_instruccion = Label(login, text="Ingresa tus datos para acceder", font=("Helvetica", 12), bg="lightblue")
    label_instruccion.place(x=290, y=290)

    # Campos de usuario y contraseña
    Label(login, text="Usuario:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=320)
    campo_usuario = Entry(login, font=("Helvetica", 12))
    campo_usuario.place(x=200 + 100, y=320, width=200, height=25)

    Label(login, text="Contraseña:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=370)
    campo_contrasena = Entry(login, font=("Helvetica", 12), show="*")
    campo_contrasena.place(x=200 + 100, y=370, width=200, height=25)

    # Función que se ejecuta al presionar Enter
    def presionar_enter(event):
        verificar_login(campo_usuario, campo_contrasena, DB_PATH)

    campo_contrasena.bind("<Return>", presionar_enter)

    # Botones de login y registro
    Button(login, text="Iniciar sesión", font=("Helvetica", 12), command=lambda: verificar_login(campo_usuario, campo_contrasena, DB_PATH)).place(x=250 + 100, y=420, width=100, height=30)
    Button(login, text="Registrarse", font=("Helvetica", 12), command=lambda: registrar_usuario(ICONS_DIR, DB_PATH)).place(x=600, y=350, width=100, height=30)

    # Enlace de "Olvidé mi contraseña"
    label_olvidada = Label(login, text="¿Olvidaste tu contraseña?", font=("Helvetica", 10, "italic"), bg="lightblue", fg="blue")
    label_olvidada.place(x=320, y=460)

    login.mainloop()
