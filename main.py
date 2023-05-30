from tools import *
from usuarios import class_usuario as usuario

"""
TODO: sector administrador
TODO: armar generador de remedios 
TODO: armar menu de usuario
"""

def menu_principal():
    while True:
        clear_screen()
        print("Pastillero Virtual")
        try:
            eleccion = int(input("""
            (1) - Login
            (2) - Crear cuenta
            (3) - Salir 
            """))
        except ValueError:
            print("Ingrese un numero valido")
            sleep_time(2)
            continue
        if eleccion == 1:
            login_data = usuario.Acciones_usuario.login(any)
            break
        elif eleccion == 2:
            usuario.Acciones_usuario.registro(any)
        elif eleccion == 3:
            clear_screen()
            print("Gracias por usar Pastillero Virtual")
            login_data = any
            break
        else:
            print("Ingrese un numero valido")
            sleep_time(2)
    return login_data

def main():
    login_data = menu_principal()

main()
 