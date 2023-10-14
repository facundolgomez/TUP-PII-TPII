from usuario import Usuario
from curso import Curso

lista_profes_registrados = []

class Profesor(Usuario):
    def __init__(self, titulo: str, anio_egreso: int):
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def dictar_curso(self, curso: Curso):
        pass

    def __str__(self):
        pass
    
    #<----------------Hecho por salvi XD nose si estara bien :D espero que si-------------------------->
    
    def validar_credenciales(self, email, contrasena):
        for profe in lista_profes_registrados:
            if profe.email == email and profe.contrasena == contrasena:
                print("Acceso concedido")
            return
        print("Correo electronico o contraseña incorrecta ")
        