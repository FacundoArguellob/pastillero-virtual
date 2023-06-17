from tools import *
from datetime import *
from peticiones_db import *
from menus import *

class Admin():

    def mostrar_tablas(self, tabla_eleccion):
        clear_screen()
        resultados = Peticiones_db.mostrar_contentido_tablas(tabla_eleccion)

        mostrar_tabla_admin(tabla_eleccion, resultados)
                

    def modificar_tablas(self):
        tabla_eleccion = menu_tablas()