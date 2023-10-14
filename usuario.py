from abc import ABC, abstractmethod

class Usuario(ABC):
    conj_emails = set()

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido

        if email in Usuario.conj_emails:
            raise ValueError("El email ya existe, debe proporcionar otro")
        else:
            self.email = email
            Usuario.conj_emails.add(email)

        self.contrasenia = contrasenia

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}, Email: {self.email}"

    @abstractmethod
    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass
