from abc import ABC, abstractmethod


class Usuario(ABC):
    conj_emails = set()
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

        if email in Usuario.conj_emails:
            raise ValueError("El email ya existe, debe proporcionar otro")
        else:
            self.email = email
            Usuario.conj_emails.add(email)

    
    def __str__(self):
        pass


    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass        