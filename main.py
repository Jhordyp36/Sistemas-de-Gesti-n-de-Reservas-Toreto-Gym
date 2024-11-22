import os
from tkinter import *
from src.iniciar_sesion import crear_ventana_iniciar_sesion

# Definir rutas de las carpetas
BASE_DIR = os.path.dirname('Proyecto')  # Carpeta principal donde está todo el proyecto
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
ICONS_DIR = os.path.join(ASSETS_DIR, 'icons')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
DB_PATH = os.path.join(BASE_DIR, "data/usuarios.db")

# Crear la ventana de Iniciar Sesión
crear_ventana_iniciar_sesion(ICONS_DIR, IMAGES_DIR, DB_PATH)

