import os

#Centra las ventanas dependiendo de la computadora, es necesario pasar de parámetro la ventana que a centrar, el ancho y el alto que desea en la ventana.
def centrar_ventana(ventana, ancho, alto):
    # Obtener las dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular la posición centrada
    x = (pantalla_ancho - ancho) // 2
    y = (pantalla_alto - alto) // 2

    # Colocar la ventana en el centro
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

#Carga el icono para las ventanas, es necesario pasar de parámetro la ventana que utilizará el icono, y el path donde se ubica el icono.
def cargar_icono(ventana, icono_path):
    """Cargar un icono a la ventana."""
    if os.path.exists(icono_path):
        ventana.iconbitmap(icono_path)
    else:
        print(f"El icono {icono_path} no existe.")
