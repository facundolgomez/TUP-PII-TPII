import random
import string
from archivo import Archivo


class Curso:
    __siguiente_codigo = 1

    def __init__(self, nombre: str):
        self.__codigo = self.__generar_prox_cod()
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generador_contrasenia()
        self.__mis_archivos = []

    @classmethod
    def __generar_prox_cod(cls):
        prox_cod = cls.__siguiente_codigo
        cls.__siguiente_codigo += 1
        return prox_cod

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def nuevo_archivo(self, archivo: Archivo):
        if isinstance(archivo, Archivo):
            self.mis_archivos.append(archivo)
        else:
            print("El objeto no es de tipo Archivo.")

    @property
    def mis_archivos(self):
        return self.__mis_archivos

    @mis_archivos.setter
    def mis_archivos(self, nuevo_mis_archivos):
        self.__mis_archivos = nuevo_mis_archivos

    def __str__(self):
        return (
            f"Nombre: {self.__nombre}\nContraseña: {self.__contrasenia_matriculacion}"
        )

    @staticmethod
    def __generador_contrasenia() -> str:
        longitud = 6
        caracteres = string.ascii_letters + string.digits
        contrasenia = ""
        for x in range(longitud):
            contrasenia += random.choice(caracteres)
        return contrasenia
