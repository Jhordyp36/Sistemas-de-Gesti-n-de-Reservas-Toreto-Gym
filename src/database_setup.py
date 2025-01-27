import sqlite3
import os
from datetime import datetime, timedelta

# Crear la carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Conectar a la base de datos en la carpeta 'data'
conn = sqlite3.connect('data/usuarios.db')
cursor = conn.cursor()

# Crear la tabla de usuarios con la columna de asistencia diaria
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        cedula TEXT PRIMARY KEY CHECK(length(cedula) = 10),
        apellidos TEXT NOT NULL,
        nombres TEXT NOT NULL,
        usuario TEXT NOT NULL UNIQUE,
        contrasena TEXT NOT NULL,
        telefono TEXT NOT NULL CHECK(length(telefono) = 10),
        correo TEXT NOT NULL,
        rol TEXT NOT NULL CHECK(rol IN ('Cliente', 'Administrador', 'Entrenador')),
        estado TEXT NOT NULL DEFAULT 'A' CHECK(estado IN ('A', 'X')),
        fecha_nacimiento TEXT NOT NULL,
        asiste TEXT NOT NULL DEFAULT 'No'
    )
''')

# Crear la tabla de historial de asistencias
cursor.execute('''
    CREATE TABLE IF NOT EXISTS historial_asistencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cedula TEXT NOT NULL,
        fecha TEXT NOT NULL,
        asistencia TEXT NOT NULL CHECK(asistencia IN ('Si', 'No')),
        FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
    )
''')

# Crear la tabla de logs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        fecha_hora TEXT NOT NULL,
        accion TEXT NOT NULL
    )
''')

# Crear la tabla de parámetros
cursor.execute('''
    CREATE TABLE IF NOT EXISTS parametros (
        nombre TEXT PRIMARY KEY,
        valor TEXT NOT NULL
    )
''')

# Insertar valores predeterminados en la tabla de parámetros
cursor.execute('''
    INSERT OR IGNORE INTO parametros (nombre, valor)
    VALUES
    ('Contraseña Predeterminada', 'toretoGym'),
    ('Porcentaje IVA', '15%')
''')

# Insertar un usuario de prueba con rol 'Administrador'
cursor.execute('''
    INSERT OR IGNORE INTO usuarios (cedula, apellidos, nombres, usuario, contrasena, telefono, correo, rol, estado, fecha_nacimiento)
    VALUES ('1234567890', 'Doe', 'John', 'admin', '1234', '0912345678', 'johndoe@email.com', 'Administrador', 'A', '1980-01-01')
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
