from abc import ABC, abstractmethod
from datetime import date

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasena: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
def __str__(self):
    pass
def validar_credenciales(self, email: str, contrasena: str) -> bool:
    pass


