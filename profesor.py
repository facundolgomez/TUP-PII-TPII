from usuario import Usuario
from curso import Curso

class Profesor(Usuario):
	def __init__(self, titulo: str, anio_egreso: int):
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def dictar_curso(self, curso: Curso)
        pass

    def __str__(self):
        pass       
        

