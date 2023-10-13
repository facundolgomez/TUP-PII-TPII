from usuario import Usuario
from curso import Curso


lista_alum_registrado = []

class Estudante(Usuario):
    def __init__(self, legajo: int, anio_increcion_carrera: int, nombre: str, apellido: str, email: str, contrasena: str):
        super().__init__(nombre, apellido, email, contrasena)
        self.__legajo = legajo
        self.__anio_increcion_carrera = anio_increcion_carrera
        
def __str__(self):
    pass
    
def matricular_en_curso(self, curso : Curso):
    pass

def validar_credenciales(self, email: str, contrasena: str):
    for alumno in lista_alum_registrado:
        if alumno.email == email and alumno.contrasena == contrasena:
            print("Acceso concedido")
        return
    print("Correo electronico o contraseña incorrecta ")
        
        
    
        
estudante1 = Estudante(425323, 2022)
lista_alum_registrado.append(estudante1)



