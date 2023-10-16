from usuario import Usuario
from curso import Curso


lista_profes_registrados = []

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = []

    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)

    def __str__(self):
        pass

    
    #<----------------Hecho por salvi XD nose si estara bien :D espero que si-------------------------->
    
    def validar_credenciales(self, email, contrasenia_ingresada) -> bool:
        acceso_concedido = False
        for profe in lista_profes_registrados:
            if profe.email == email and profe.contrasenia == contrasenia_ingresada:
                acceso_concedido = True
                print("ACCESO EXITOSO")
                return acceso_concedido
        print("Correo electronico o contraseña incorrecta ")
        

profe = Profesor("Carlos", "rodriguez", "mailprofe", "contra", "ingeniero", 1998)
lista_profes_registrados.append(profe)

#tener en cuenta que esta funcion es para buscar si existe el profesor, no pertenece a la clase
def buscando_profesor(email):
    for profe in lista_profes_registrados:
        if profe.email == email:
            return profe
    return None