from abc import ABC, abstractmethod


class Usuario(ABC):
    conj_emails = set()
    def init(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia


        if email in Usuario.conj_emails:
            raise ValueError("El email ya existe, debe proporcionar otro")
        else:
            self.email = email
            Usuario.conj_emails.add(email)


    
    def __str__(self):


    def str(self):

        pass


    def validar_credenciales(self, email: str, contrasenia: str) -> bool:

        pass        

