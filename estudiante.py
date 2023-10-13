from usuario import Usuario
from curso import Curso


class Estudiante(Usuario):
	def __init__(self, legajo: int, anio_inscripcion_carrera: int):
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__():
        pass

    def matricular_en_curso(self, curso: Curso)       
        pass


        