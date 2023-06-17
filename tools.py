import os
import time
from faker import Faker

fake = Faker()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep_time(seconds):
    time.sleep(seconds)

def generar_usuario_fake():
    nombre = fake.name()
    apellido = fake.last_name()
    email = fake.email()
    password = fake.password()
    return nombre, apellido, email, password

def generar_remedio_fake():
    nombre = fake.word()
    descripcion = fake.sentence()
    return nombre, descripcion

def loader(flag):
    items = ["0", "o", "o", "o", "o", "o"]

    while True:
        print("".join(items), end="\r")
        time.sleep(0.5)
        items.insert(0, items.pop())
        if flag:
            break