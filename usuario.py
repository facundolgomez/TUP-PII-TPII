from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    
    def __str__(self):
        pass


    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass        