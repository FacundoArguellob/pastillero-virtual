from tools import *
import peticiones_db as modelo
from usuarios.sector_admin.asistente_admin import *

class Acciones_usuario:

    def registro(self):
        clear_screen()
        print("CREAR CUENTA")

        #test/check
        #nombre, apellido, email, password = generar_usuario_fake()
        
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su password: ")
        
        usuario = modelo.Peticiones_db(nombre, apellido, email, password)
        registro = usuario.registro()

        if registro[0] >= 1:
            clear_screen()
            print(f"Se registro el usuario correctamente")
            sleep_time(2)
        else:
            print("No se pudo registrar el usuario", registro)
            sleep_time(2)
        
    def login(self):
        clear_screen()
        print("LOGIN")

        #test/check
        #email, password = "admin@admin.com", "admin"

        while True:
            clear_screen()
            email = input("Ingrese su email: ")
            password = input("Ingrese su password: ")

            admin_check = check_admin(email, password) #check if admin

            usuario = modelo.Peticiones_db('', '', email, password)
            login = usuario.login()
            
            if admin_check == False:
                if login[0] >= 1:
                    clear_screen() 
                    print(f"Bienvenido {login[1][1]} {login[1][2]}")
                    sleep_time(2)
                    break
                else:
                    clear_screen()
                    print("No se pudo iniciar sesion, verifique los datos ingresados o crea una cuenta")
                    sleep_time(2)
        return login