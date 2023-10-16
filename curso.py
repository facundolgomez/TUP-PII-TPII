import random
import string

class Curso:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generador_contrasenia()

    def __str__(self):
        return f"Nombre: {self.__nombre}\nContraseña: {self.__contrasenia_matriculacion}"


    def get_nombre(self):
        return self.__nombre

    def get_contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion    


    def __generador_contrasenia(self):
        longitud = 6
        caracteres = string.ascii_letters + string.digits
        contrasenia = ''
        for x in range(longitud):
            contrasenia += random.choice(caracteres)
        return contrasenia



        