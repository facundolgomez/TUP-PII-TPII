from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = []

    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)
        #ordeno la lista alfabeticamente de los cursos de una instancia del profesor para que sea correcto con el orden de los cursos 
        self.mis_cursos.sort(key=lambda curso: curso.nombre)

    def __str__(self):
        pass

    
    def validar_credenciales(self, email, contrasenia_ingresada) -> bool:
        acceso_concedido = False
        for profe in lista_profes_registrados:
            if profe.email == email and profe.contrasenia == contrasenia_ingresada:
                acceso_concedido = True
                return acceso_concedido
        
        







  