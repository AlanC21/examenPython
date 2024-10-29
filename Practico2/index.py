# Importamos sqlite3 para poder utilizarla
import sqlite3

# Conexion a la base de datos llamada EESTN5, y despues se devuelve la conexion.
def conectarDB():
    return sqlite3.connect("EESTN5.db")

# Creamos la tabla de alumnos en el caso que no exista
def crearTablaAlumnos(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
    ''')
    conn.commit()

# Inserta datos en la tabla de alumnos y se elige a los alumnos mayores a 17 años
def insertarConsultarAlumnos(conn):
    cursor = conn.cursor()
    
    # Lista de alumnos para insertar en la tabla de alumnos
    alumnos = [
        ("Cordoba", 19), ("Cataldo", 19), ("Alsina", 19),
        ("Di Gialleonardo", 17), ("Stuffano", 17), ("Almiron", 17),
        ("Oromendia", 18), ("Barbe", 17)
    ]
    
    # Insertamos datos en la tabla
    cursor.executemany("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", alumnos)
    conn.commit()
    
    # Se hace la consulta de alumnos mayores a 17
    cursor.execute("SELECT * FROM alumnos WHERE edad > 17")
    alumnos_mayores = cursor.fetchall()
    
    # Se muestran los resultados
    for alumno in alumnos_mayores:
        print(alumno)

# Llamamos a la funciones
conn = conectarDB()
crearTablaAlumnos(conn)
insertarConsultarAlumnos(conn)
conn.close()
