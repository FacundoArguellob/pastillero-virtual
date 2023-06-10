from tools import *
import conexion
from admin import asistente_admin

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
  

class Admin():

    def mostrar_tabla(self):
        tabla_eleccion = asistente_admin.menu_tablas()
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
                clear_screen()
            case "remedios":
                for resultado in resultados:
                    print(f"""
                    ID: {resultado[0]}
                    Nombre: {resultado[1]}
                    Descrpcion: {resultado[2]}
                    """)
                input("Presione enter para continuar")
                clear_screen()
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
                

    def modificar_tablas(self):
        tabla_eleccion = asistente_admin.menu_tablas()
        
            

