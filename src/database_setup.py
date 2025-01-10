import sqlite3
import os

# Crear la carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Conectar a la base de datos en la carpeta 'data'
conn = sqlite3.connect('data/usuarios.db')
cursor = conn.cursor()

# Crear la tabla de usuarios con la cédula como clave primaria
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        cedula TEXT PRIMARY KEY CHECK(length(cedula) = 10),
        apellidos TEXT NOT NULL,
        nombres TEXT NOT NULL,
        usuario TEXT NOT NULL,
        contrasena TEXT NOT NULL,
        rol TEXT NOT NULL CHECK(rol IN ('Usuario', 'Administrador'))
    )
''')

# Crear la tabla de logs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        fecha_hora TEXT NOT NULL
    )
''')

# Insertar un usuario de prueba con rol 'Administrador'
cursor.execute('''
    INSERT OR IGNORE INTO usuarios (cedula, apellidos, nombres, usuario, contrasena, rol)
    VALUES ('1234567890', 'Doe', 'John', 'admin', '1234', 'Administrador')
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
