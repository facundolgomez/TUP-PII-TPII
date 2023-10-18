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

<<<<<<< HEAD
<<<<<<< HEAD
    #getters y setters    
=======
    #agregar setters
>>>>>>> 16cf1dd57bc8bc71bb6d5d5c085be7c3c78fd64b
=======
    #getters y setters    
>>>>>>> 80bef683aa130b0243ff9f40d9e757881167d43e
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self):
        self._nombre = nombre    

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def nombre(self):
        self._nombre = nombre    

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self):
        return self._email    

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self):
        return self._contrasenia    

    @abstractmethod
    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        pass


