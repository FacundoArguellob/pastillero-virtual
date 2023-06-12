from tools import *
from datetime import *
import admin_class as Admin
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

        match eleccion:
            case 1:
                Admin.mostrar_tabla(any)
            case 2:
                Admin.modificar_tablas(any)
            case 3:
                break
            case _:
                print("Numero fuera de rango")
                sleep_time(2)


def menu_tablas():
    sql = "SHOW TABLES;"
    cursor.execute(sql)
    tablas = cursor.fetchall()

    while True:
        clear_screen()
        print("Seleccione una tabla para ver / modificar su contenido\n")
        for indice, tabla in enumerate(tablas, start=1):
            print(f"""\t    ({indice}) - {tabla[0]}""")
        print("""\t    (0) - Salir""")

        try:
            eleccion = int(input(""))
            tabla_eleccion = tablas[eleccion-1][0]
        except ValueError:
            print("Opcion no valida")
            sleep_time(2)
        except IndexError:
            print("numero fuera de rango")
            sleep_time(2)
        if eleccion == 0:
            clear_screen()
            break
        print(f"Tabla seleccionada: {tabla_eleccion}")
        sleep_time(2)
        return tabla_eleccion