from tools import *
import usuarios.conexion_db_usuarios as modelo

class Acciones_usuario:

    def registro(self):
        clear_screen()
        print("CREAR CUENTA")
        """
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su password: ")
        """
        #check/ignore
        nombre = "test/check"
        apellido = "test/check"
        email = "test/check"
        password = "test/check"

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registro()

        if registro[0] >= 1:
            clear_screen()
            print(f"Bienvenido {registro[1].nombre} {registro[1].apellido}")
        else:
            print("No se pudo registrar el usuario")
            print(registro)

        
