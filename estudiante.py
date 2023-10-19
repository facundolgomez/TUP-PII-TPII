from usuario import Usuario
from curso import Curso
import procesos


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mis_cursos = []  

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Legajo: {self.__legajo}, Año de Inscripcion: {self.__anio_inscripcion_carreera}"


    
    def matricular_en_curso(self, curso_seleccionado: Curso):
        contrasenia_matriculacion = input(f"Ingrese la contraseña de matriculación para '{curso_seleccionado.nombre}': ")
        # Validar la contraseña
        if contrasenia_matriculacion == curso_seleccionado.contrasenia_matriculacion:
            if curso_seleccionado not in self.mis_cursos:
                self.mis_cursos.append(curso_seleccionado)
                # Ordenando la lista de cursos para ese estudiante
                self.mis_cursos.sort(key=lambda curso: curso.nombre)
                return True  # matriculacion exitosa
            
        return False  



        
    
    
   

   

            

    
        
    



