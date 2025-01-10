import tkinter as tk
from tkinter import messagebox

def generar_reporte():
    messagebox.showinfo("Muy pronto", "Esta funcionalidad estará disponible próximamente.")

def ventana_ReportesEstadisticas_administrador():
    # Configuración del tipo de letra
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    # Configuración inicial de la ventana
    admin_window = tk.Tk()
    admin_window.title("Módulo de Reportes y Estadísticas - Administrador")
    admin_window.state('zoomed')  # Inicia en pantalla completa
    admin_window.configure(bg="#272643")  # Color de fondo de la ventana

    # Frame izquierdo - Opciones comunes
    frame_izquierdo = tk.Frame(admin_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_izquierdo.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.8)

    label_izquierdo = tk.Label(frame_izquierdo, text="Opciones Generales", font=header_font, bg="#2c698d", fg="#ffffff")
    label_izquierdo.pack(pady=5)

    botones_comunes = [
        "Visualizar gráficos de uso por horario",
        "Mostrar estadísticas de concurrencia diaria",
        "Mostrar tendencias de renovación de membresías",
        "Generar alertas de anomalías en uso de recursos",
        "Analizar ocupación de instalaciones",
    ]

    for boton in botones_comunes:
        tk.Button(frame_izquierdo, text=boton, font=default_font, bg="#bae8e8", command=generar_reporte).pack(pady=5, fill="x")

    # Frame derecho - Opciones avanzadas del Administrador
    frame_derecho = tk.Frame(admin_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_derecho.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.8)

    label_derecho = tk.Label(frame_derecho, text="Opciones Avanzadas (Administrador)", font=header_font, bg="#2c698d", fg="#ffffff")
    label_derecho.pack(pady=5)

    botones_avanzados = [
        "Categorizar clientes por intereses y frecuencia",
        "Analizar comportamiento de clientes",
        "Exportar reportes en PDF y Excel",
        "Generar análisis financiero",
        "Mostrar indicadores clave de rendimiento",
        "Generar reportes automatizados",
        "Generar informe personalizado",
        "Comparar estadísticas entre períodos",
        "Generar informe de ingresos mensuales",
    ]

    for boton in botones_avanzados:
        tk.Button(frame_derecho, text=boton, font=default_font, bg="#bae8e8", command=generar_reporte).pack(pady=5, fill="x")

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(admin_window, text="Regresar al Menú Principal", font=default_font, bg="#e3f6f5", command=admin_window.destroy)
    btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)

    # Iniciar la aplicación
    admin_window.mainloop()

def ventana_ReportesEstadisticas_usuario():
    # Configuración del tipo de letra
    default_font = ("Segoe UI", 12)
    header_font = ("Segoe UI", 14, "bold")

    # Configuración inicial de la ventana
    user_window = tk.Tk()
    user_window.title("Módulo de Reportes y Estadísticas - Usuario")
    user_window.state('zoomed')  # Inicia en pantalla completa
    user_window.configure(bg="#272643")  # Color de fondo de la ventana

    # Frame único - Opciones del Usuario
    frame_unico = tk.Frame(user_window, bg="#2c698d", padx=10, pady=10, relief="groove", bd=5)
    frame_unico.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.8)

    label_unico = tk.Label(frame_unico, text="Opciones del Usuario", font=header_font, bg="#2c698d", fg="#ffffff")
    label_unico.pack(pady=5)

    botones_usuario = [
        "Visualizar gráficos de uso por horario",
        "Mostrar estadísticas de concurrencia diaria",
        "Mostrar tendencias de renovación de membresías",
        "Generar alertas de anomalías en uso de recursos",
        "Analizar ocupación de instalaciones",
    ]

    for boton in botones_usuario:
        tk.Button(frame_unico, text=boton, font=default_font, bg="#bae8e8", command=generar_reporte).pack(pady=5, fill="x")

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(user_window, text="Regresar al Menú Principal", font=default_font, bg="#e3f6f5", command=user_window.destroy)
    btn_regresar.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)

    # Iniciar la aplicación
    user_window.mainloop()


