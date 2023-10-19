from abc import ABC, abstractmethod

class Usuario(ABC):
    conj_emails = set()

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre  
        self._apellido = apellido  

        while email in Usuario.conj_emails:
            print("El email ya existe en el sistema. Ingrese otro por favor.")
            email = input("Nuevo correo electrónico: ")

        self._email = email  
        Usuario.conj_emails.add(email)

        self._contrasenia = contrasenia



    #getters y setters    

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre    

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def nombre(self, nuevo_apellido):
        self._apellido = nuevo_apellido   

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email   

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self._contrasenia = nueva_contrasenia   

    
    def validar_credenciales(self, email, contrasenia_ingresada) -> bool:
        return self.email == email and self.contrasenia == contrasenia_ingresada


