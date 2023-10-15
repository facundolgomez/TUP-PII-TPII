from usuario import Usuario
from curso import Curso

lista_profes_registrados = []

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def dictar_curso(self, curso: Curso):
        pass

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Email: {self.email}, Título: {self.__titulo}"

    
    #<----------------Hecho por salvi XD nose si estara bien :D espero que si-------------------------->
    
    def validar_credenciales(self, email, contrasena) -> bool:
        for profe in lista_profes_registrados:
            if profe.email == email and profe.contrasena == contrasena:
                print("Acceso concedido")
            return
        print("Correo electronico o contraseña incorrecta ")
        
