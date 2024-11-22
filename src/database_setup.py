import sqlite3
import os

# Crear la carpeta 'data' si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Conectar a la base de datos en la carpeta 'data'
conn = sqlite3.connect('data/usuarios.db')
cursor = conn.cursor()

# Crear la tabla de usuarios, agregando la columna 'rol' para diferenciar entre 'administrador' y 'usuario'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        contrasena TEXT NOT NULL,
        rol TEXT NOT NULL DEFAULT 'usuario'  -- 'usuario' por defecto
    )
''')

# Insertar un usuario de prueba con rol 'administrador'
cursor.execute('''
    INSERT INTO usuarios (usuario, contrasena, rol)
    VALUES ('admin', '1234', 'administrador')  -- El primer usuario será un administrador
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
