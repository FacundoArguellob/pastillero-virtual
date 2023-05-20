import hashlib
import conexion


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    

    def registro(self):
        #cifrado contrasenia
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest())
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]
        return result




    def login(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"