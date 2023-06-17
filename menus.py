# Toda la parte grafica de la app se despliega aca
from tools import clear_screen
def menu_principal():
    menu = """
    Bienvenido al Pastillero Virtual
    
        (1) - Login
        (2) - Crear cuenta
        (3) - Salir 
    """
    print(menu)

def menu_admin_principal():
    menu = """
        (1) - Ver tablas
        (2) - Modificar tablas
        (3) - Salir
    """
    print(menu)

def mostrar_tabla_admin(tabla_eleccion, resultados):
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
                clear_screen()