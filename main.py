import os
from tkinter import *
from tkinter import messagebox

# Definir rutas de las carpetas
BASE_DIR = os.path.dirname('Login')  # Carpeta donde está este script
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
ICONS_DIR = os.path.join(ASSETS_DIR, 'icons')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')

# Función: Verificación del Login
def verificar_login():
    usuario = campo_usuario.get()
    contrasena = campo_contrasena.get()
    
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

# Creación de la Ventana Principal
login = Tk()
login.title("Sistemas de Gestión de Reservas Toreto Gym") #Nombre de la ventana: Sistemas de Gestión de Reservas Toreto Gym
login.geometry('816x500')  # Tamaño de la Ventana Principal
login.config(bg="lightblue")  # Color de Fondo

# Cargar el ícono de la ventana desde la carpeta icons
login.iconbitmap(os.path.join(ICONS_DIR, "Icono.ico"))  # Ruta del ícono

# No permite aumentar o reducir la Ventana
login.resizable(False, False)

# Cargar y mostrar la imagen desde la carpeta images
imagen_superior = PhotoImage(file=os.path.join(IMAGES_DIR, "Información.png"))  # Ruta de la imagen
label_imagen = Label(login, image=imagen_superior)
label_imagen.place(x=0, y=0)  # Posición de la imagen

# Título de la ventana
label_titulo = Label(login, text="Bienvenido/a", font=("Helvetica", 18, "bold"), bg="lightblue")
label_titulo.place(x=322, y=255)

# Mensaje de bienvenida/instrucción
label_instruccion = Label(login, text="Ingresa tus datos para acceder", font=("Helvetica", 12), bg="lightblue")
label_instruccion.place(x=290, y=290)

# Etiqueta de Usuario
Label(login, text="Usuario:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=320)

# Campo de entrada para el usuario
campo_usuario = Entry(login, font=("Helvetica", 12))
campo_usuario.place(x=200 + 100, y=320, width=200, height=25)

# Etiqueta de Contraseña
Label(login, text="Contraseña:", font=("Helvetica", 12), bg="lightblue").place(x=200, y=370)

# Campo de entrada para la contraseña
campo_contrasena = Entry(login, font=("Helvetica", 12), show="*")
campo_contrasena.place(x=200 + 100, y=370, width=200, height=25)

# Función que se ejecuta cuando se presiona Enter en el campo de contraseña
def presionar_enter(event):
    verificar_login()

# Vincular el evento Enter en el campo de contraseña
campo_contrasena.bind("<Return>", presionar_enter)

# Botón para iniciar sesión
Button(login, text="Iniciar sesión", font=("Helvetica", 12), command=verificar_login).place(x=250 + 100, y=420, width=100, height=30)

# Enlace para "Olvidé mi contraseña"
label_olvidada = Label(login, text="¿Olvidaste tu contraseña?", font=("Helvetica", 10, "italic"), bg="lightblue", fg="blue")
label_olvidada.place(x=320, y=460)

# Ejecutar la ventana
login.mainloop()
