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
        # Ordeno alfabeticamente la lista de cursos del profesor
        self.mis_cursos.sort(key=lambda curso: curso.nombre)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Título: {self.__titulo}, Año de Egreso: {self.__anio_egreso}"

    # Getters y Setters
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def anio_egreso(self):
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso):
        self.__anio_egreso = nuevo_anio_egreso