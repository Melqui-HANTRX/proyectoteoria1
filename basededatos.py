import sqlite3
import os


def crear_base_de_datos():
    # Obtener la ruta de la carpeta actual para evitar bases de datos "fantasma"
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(ruta_carpeta, "gestion_proyectos.db")

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # Tabla Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT,
            correo TEXT
        )
    ''')

    # Tabla Proyectos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyectos (
            id_proyecto INTEGER PRIMARY KEY,
            id_cliente INTEGER,
            nombre TEXT NOT NULL,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            estado TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
        )
    ''')

    # Tabla Pagos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id_pago INTEGER PRIMARY KEY,
            id_proyecto INTEGER,
            monto REAL,
            tipo_pago TEXT,
            fecha TEXT,
            FOREIGN KEY (id_proyecto) REFERENCES proyectos (id_proyecto)
        )
    ''')

    conexion.commit()
    conexion.close()
    print(f"Base de datos creada/verificada en: {ruta_db}")


if __name__ == "__main__":
    crear_base_de_datos()