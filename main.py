from tools import *
from menus import *
from usuarios import class_usuario as usuario

"""
TODO: sector administrador
TODO: armar generador de remedios 
TODO: armar menu de usuario
"""

def menu_usuario():
    CANTIDAD_DE_ELECCIONES = 3
    while True:
        clear_screen()
        try:
            menu_principal()
            eleccion = int(input())
        except ValueError:
            print("Ingrese un numero valido")
            sleep_time(2)
            continue
        else:
            if eleccion < 1 or eleccion > CANTIDAD_DE_ELECCIONES:
                print("Ingrese una opcion valida")
                sleep_time(2)
                continue
 
        match eleccion:
            case 1:
                login_data = usuario.Acciones_usuario.login(None)
                break
            case 2:
                usuario.Acciones_usuario.registro(None)
            case 3:
                clear_screen()
                print("Gracias por usar Pastillero Virtual")
                login_data = None
                break
            case _:
                print("Ingrese un numero valido")
                sleep_time(2)   
    return login_data

def main():
    login_data = menu_usuario()

main()
 