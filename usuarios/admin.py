from tools import *
from datetime import *
import conexion


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


def check_admin(email, password):
    email_admin = "admin@admin.com"
    password_admin = "admin"
    if email == email_admin and password == password_admin:
        clear_screen()
        print(f"Bienvenido Administrador. Ultima conexion: {datetime.now()}")
        menu_admin()
    else:
        return False
    
def menu_admin():
    while True:
        try:
            eleccion = int(input("""
            (1) - Ver tablas
            (2) - Modificar tablas
            (3) - Salir
            """))
        except ValueError:
            print("Opcion no valida")

        if eleccion == 1:
            clear_screen()
            Admin.ver_tablas(any)
        elif eleccion == 2:
            clear_screen()
            Admin.modificar_tablas(any)
        elif eleccion == 3:
            break
        else:
            print("Opcion no valida")
            sleep_time(2)
            


class Admin():
    
    def __init__(self):
        pass


    def ver_tablas(self):
        sql = "SHOW TABLES;"
        cursor.execute(sql)
        result = cursor.fetchall()
        while True:

            print("Seleccione una tabla para ver su contenido\n")
            for indice, tabla in enumerate(result, start=1):
                print(f"""({indice}) - {tabla[0]}""")

            try:
                eleccion = int(input(""))
            except ValueError:
                print("Opcion no valida")
                sleep_time(2)
            if eleccion > len(result):
                print("numero fuera de rango")
            tabla_eleccion = result[eleccion-1][0]
            print(f"Tabla seleccionada: {tabla_eleccion}")
            sleep_time(2)
            Admin.show_table(any, tabla_eleccion)

    def show_table(self, tabla_eleccion):
        clear_screen()
        sql = f"SELECT * FROM {tabla_eleccion};"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"""
            ID: {resultado[0]}
            Nombre: {resultado[1]}
            Apellido: {resultado[2]}
            Email: {resultado[3]}
            Password: {resultado[4]:.10}
            
            
            """)





    def modificar_tablas(self):
        print("Modificar tablas")
        sleep_time(1)

