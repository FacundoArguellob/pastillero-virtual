from tools import *
from menus import *
from datetime import datetime
from usuarios.sector_admin.admin_class import *
from peticiones_db import *


def check_admin(email, password):
    email_admin = "admin@admin.com"
    password_admin = "admin"
    if email == email_admin and password == password_admin:
        clear_screen()
        print(f"Bienvenido Administrador. Ultima conexion: {datetime.today()}")
        menu_admin()
    else:
        return False
    

def menu_admin():
    while True:
        try:
            menu_admin_principal()
            eleccion = int(input())
        except ValueError:
            print("Opcion no valida")

        match eleccion:
            case 1:
                tabla_eleccion = menu_tablas()
                Admin.mostrar_tablas(any, tabla_eleccion)
            case 2:
                Admin.modificar_tablas(any)
            case 3:
                break
            case _:
                print("Numero fuera de rango")
                sleep_time(2)


def menu_tablas():
    tablas = Peticiones_db.mostrar_tablas()

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