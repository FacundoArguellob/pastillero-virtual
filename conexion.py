import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pastillero_db",
        port=3306,
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]




#db check
"""
try:
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pastillero_db",
        port=3306,
    )
    
    # Verificar si la conexión se estableció correctamente
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
    
    # Cerrar la conexión
    conexion.close()

except mysql.connector.Error as error:
    print("Error al conectar a la base de datos:", error)
"""