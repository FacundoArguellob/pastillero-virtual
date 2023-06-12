import hashlib
import conexion


database, cursor = conexion.conectar()

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    

    def registro(self):        #cifrado contrasenia
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest())
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except Exception as error:
            result = [0, self, error]
        return result


    def login(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "SELECT * FROM usuarios WHERE email = %s AND passwd = %s"
        try:
            cursor.execute(sql, (self.email, cifrado.hexdigest()))
            result = [cursor.rowcount, cursor.fetchone()]
        except Exception as error:
            result = [0, self]
        return result