from usuario import Usuario
from curso import Curso

alumnos_registrados = []

class Estudiante(Usuario):
	def __init__(self, legajo: int, anio_inscripcion_carrera: int):
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__():
        pass

    def matricular_en_curso(self, curso: Curso)       
        pass


estudiante1 = Estudiante(423423, 2020)

alumnos_registrados.append(estudiante1)

