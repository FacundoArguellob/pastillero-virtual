from tools import *
from datetime import *
import conexion


database, cursor = conexion.conectar()

sql = "SHOW TABLES;"
cursor.execute(sql)
tablas = cursor.fetchall()


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
    CANTIDAD_DE_ELECCIONES = 3
    while True:
        try:
            eleccion = int(input("""
            (1) - Ver tablas
            (2) - Modificar tablas
            (3) - Salir
            """))
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
                Admin.mostrar_tabla(any)
            case 2:
                Admin.modificar_tablas(any)
            case 3:
                break
            case _:
                pass


def menu_tablas():
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

class Admin():


    def mostrar_tabla(self):
        tabla_eleccion = menu_tablas()
        clear_screen()
        sql = f"SELECT * FROM {tabla_eleccion};"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        match tabla_eleccion:
            case "usuarios":
                for resultado in resultados:
                    print(f"""
                    ID: {resultado[0]}
                    Nombre: {resultado[1]}
                    Apellido: {resultado[2]}
                    Email: {resultado[3]}
                    Password: {resultado[4]:.10}
                    """)
                input("Presione enter para continuar")
            case "remedios":
                for resultado in resultados:
                    print(f"""
                    ID: {resultado[0]}
                    Nombre: {resultado[1]}
                    Descrpcion: {resultado[2]}
                    """)
                input("Presione enter para continuar")
            case "recordatorios":
                for resultado in resultados:
                    print(f"""
                    ID: {resultado[0]}
                    Usuario_id: {resultado[1]}
                    remedio_id: {resultado[2]}
                    Dia: {resultado[3]}
                    Hora: {resultado[4]}
                    """)
                input("Presione enter para continuar")
                

    def modificar_tablas(self):
        tabla_eleccion = menu_tablas()
        
            

