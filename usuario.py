from abc import ABC, abstractmethod

#Esta es la clase abstracta, clase padre de Profesor y Estudiante
class Usuario(ABC):
    conj_emails = set()

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido

        #Aca cuando se crea una instancia se valida que el mail sea unico en base a un conjunto ya que no se puede repetir elementos
        if email in Usuario.conj_emails:
            raise ValueError("El email ya existe, debe proporcionar otro")
        else:
            self.email = email
            Usuario.conj_emails.add(email)

        self.contrasenia = contrasenia

    def __str__(self):
        pass


    @abstractmethod
    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass
