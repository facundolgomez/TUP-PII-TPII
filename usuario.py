from abc import ABC, abstractmethod

class Usuario(ABC):
    conj_emails = set()

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre  
        self._apellido = apellido  

        if email in Usuario.conj_emails:
            raise ValueError("El email ya existe, debe proporcionar otro")
        else:
            self._email = email  
            Usuario.conj_emails.add(email)

        self._contrasenia = contrasenia 

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    @property
    def contrasenia(self):
        return self._contrasenia

    @abstractmethod
    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass

