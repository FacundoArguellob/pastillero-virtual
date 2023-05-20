from tools import *
from usuarios import class_usuario as usuario

def check_eleccion(eleccion):

    try:
        if eleccion == 1 or eleccion == 2:
            if eleccion == 1:
                usuario.Acciones_usuario.login(any)
            elif eleccion == 2:
                usuario.Acciones_usuario.registro(any)
        else:
            print("Ingrese un numero valido")
            menu_principal()
    except ValueError:
        print("Ingrese un numero valido")
        menu_principal()


def menu_principal():
    clear_screen()
    print("Pastillero Virtual")
    eleccion = int(input("""
    (1) - Login
    (2) - Crear cuenta
    (3) - Salir 
    """))
    if eleccion == 3:
        clear_screen()
        print("Gracias por usar Pastillero Virtual")
    else:
        check_eleccion(eleccion)


def main():
    menu_principal()


main()
