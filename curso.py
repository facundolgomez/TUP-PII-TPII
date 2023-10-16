import random
import string

class Curso:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generador_contrasenia()

    def __str__(self):
        pass


    def __generador_contrasenia(self):
        longitud = 6
        caracteres = string.ascii_letters + string.digits
        contrasenia = ''
        for x in range(longitud):
            contrasenia += random.choice(caracteres)
        return contrasenia

