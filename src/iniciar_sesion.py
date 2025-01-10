import os
import sqlite3
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
from config.config import ICONS_DIR, IMAGES_DIR, DB_PATH  # Importa desde config
from src.utils.helpers import centrar_ventana, cargar_icono
from src.navegacion import navegar_a_ventana_principal
import datetime  # Importa el módulo para manejar fechas y horas

intentos_restantes = 3  # Variable global para contar los intentos restantes

def verificar_login(campo_usuario, campo_contrasena, campo_rol, login):
    global intentos_restantes
    usuario = campo_usuario.get()
    contrasena = campo_contrasena.get()
    rol = campo_rol.get()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ? AND rol = ?", (usuario, contrasena, rol))
    resultado = cursor.fetchone()

    if resultado:
        # Registrar fecha y hora de inicio de sesión
        fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO logs (usuario, fecha_hora) VALUES (?, ?)", (usuario, fecha_hora_actual))
        conn.commit()

        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
        conn.close()
        login.destroy()
        navegar_a_ventana_principal(rol)
    else:
        intentos_restantes -= 1
        global label_intentos
        label_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
        if intentos_restantes > 0:
            messagebox.showerror(
                "Error de login",
                f"Usuario o contraseña incorrectos. Te quedan {intentos_restantes} intento(s)."
            )
        else:
            messagebox.showerror(
                "Error de login",
                "Has alcanzado el límite de intentos. El programa se cerrará."
            )
            conn.close()
            login.destroy()
            exit()

def recuperar_contrasena():
    messagebox.showinfo('Estamos en proceso', 'Estamos en proceso')

def crear_ventana_iniciar_sesion():
    
    default_font = ("Segoe UI", 12)
    
    login = tk.Tk()
    login.title("Sistemas de Gestión de Reservas Toreto Gym")
    login.config(bg="#272643")
    login.resizable(False, False)
    
    # Aumento de la altura de la ventana para evitar la superposición
    centrar_ventana(login, 816, 650)  # Aumento de la altura a 650 px
    cargar_icono(login, ICONS_DIR)
    
    imagen_superior = PhotoImage(file=os.path.join(IMAGES_DIR, "Informacion.png"))
    label_imagen = Label(login, image=imagen_superior)
    label_imagen.place(x=0, y=0)

    # Frame central de la ventana con los campos de login
    frame_login = tk.Frame(login, bg="#272643", padx=20, pady=20)
    frame_login.place(relx=0.25, rely=0.39, relwidth=0.5, relheight=0.5)  # Ajustar el `rely` a 0.39

    label_titulo = tk.Label(frame_login, text="Bienvenido/a", font=("Segoe UI", 18, "bold"), bg="#272643", fg="#ffffff")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))  # Agregar espacio solo en la parte inferior

    label_instruccion = tk.Label(frame_login, text="Ingresa tus datos para acceder", font=("Segoe UI", 12), bg="#272643", fg="#ffffff")
    label_instruccion.grid(row=1, column=0, columnspan=2, pady=(0, 15))  # Más espacio entre instrucciones y campos

    # Frame para los campos del formulario
    frame_campos = tk.Frame(frame_login, bg="#272643")
    frame_campos.grid(row=2, column=0, columnspan=2, pady=(0, 5))  # Agregar espacio debajo de los campos

    # Campo de Rol
    Label(frame_campos, text="Rol:", font=default_font, bg="#272643", fg="#ffffff").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    rol_seleccionado = tk.StringVar(value="Usuario")
    roles = ["Administrador", "Usuario"]
    campo_rol = tk.OptionMenu(frame_campos, rol_seleccionado, *roles)
    campo_rol.config(font=default_font)
    campo_rol.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Campo de Usuario
    Label(frame_campos, text="Usuario:", font=default_font, bg="#272643", fg="#ffffff").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    campo_usuario = tk.Entry(frame_campos, font=default_font)
    campo_usuario.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    # Campo de Contraseña
    Label(frame_campos, text="Contraseña:", font=default_font, bg="#272643", fg="#ffffff").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    campo_contrasena = tk.Entry(frame_campos, font=default_font, show="*")
    campo_contrasena.grid(row=2, column=1, padx=10, pady=(5, 1), sticky="ew")

    # Intentos restantes
    global label_intentos
    label_intentos = tk.Label(frame_login, text=f"Intentos restantes: {intentos_restantes}", font=("Segoe UI", 10), bg="#272643", fg="#ff0000")
    label_intentos.grid(row=3, column=0, columnspan=2, pady=5)  # Reducir el espacio debajo de "Intentos restantes"

    # Funcionalidad para presionar Enter
    def presionar_enter(event):
        verificar_login(campo_usuario, campo_contrasena, rol_seleccionado, login)
    
    campo_contrasena.bind("<Return>", presionar_enter)

    # Botón de Iniciar sesión
    btn_iniciar_sesion = tk.Button(frame_login, text="Iniciar sesión", font=default_font, bg="#bae8e8", command=lambda: verificar_login(campo_usuario, campo_contrasena, rol_seleccionado, login))
    btn_iniciar_sesion.grid(row=4, column=0, columnspan=2, pady=5)  # Espacio en la parte superior del botón

    # Label para recuperar contraseña
    label_olvidada = tk.Label(login, text="¿Olvidaste tu contraseña?", font=("Segoe UI", 10, "italic"), bg="#272643", fg="blue", cursor="hand2")
    label_olvidada.place(relx=0.38, rely=0.87)  # Posición fija para esta etiqueta

    label_olvidada.bind("<Button-1>", lambda e: recuperar_contrasena())

    # Iniciar la aplicación
    login.mainloop()
