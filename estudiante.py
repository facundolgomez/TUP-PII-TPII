from usuario import Usuario
from curso import Curso
from app import main


lista_alum_registrado = []
lista_mi_cursos = []

class Estudante(Usuario):
    def __init__(self, legajo: int, anio_increcion_carrera: int, nombre: str, apellido: str, email: str, contrasena: str):
        super().__init__(nombre, apellido, email, contrasena)
        self.__legajo = legajo
        self.__anio_increcion_carrera = anio_increcion_carrera
        
    def matricularse(self, curso):
        self.mi_cursos.append(curso.nombre)
    
def __str__(self):
    pass

 #<----------------Hecho por salvi XD nose si estara bien :D espero que si-------------------------->
    
def matricular_en_curso(self,opcion_curso,nombre: str, contrasena: str, curso : Curso):
    print("Lista de cursos disponibles:")
    for i, curso in enumerate(lista_mi_cursos, start=1):
        print(f"{i}. {nombre}")
    
        select_curso = lista_mi_cursos[opcion_curso]
        # Validar que el alumno no esté ya matriculado
        if select_curso in lista_mi_cursos:
            print("Ya estas matriculado en este curso")
            return

        contrasenia_metriculacion = input(f"Ingrese la contraseña de matriculación para '{lista_mi_cursos}': ")
        
        # Validar la contraseña
        if contrasena == contrasenia_metriculacion:
            nombre.matricularse(select_curso)
            print(f"Te has matriculado en el curso '{select_curso}'")
        else:
            print("Contraseña de matriculación incorrecta.")
            

def validar_credenciales(self, email: str, contrasena: str):
    for alumno in lista_alum_registrado:
        if alumno.email == email and alumno.contrasena == contrasena:
            print("Acceso concedido")
        return
    print("Correo electronico o contraseña incorrecta ")
    
        
    
    

    
        
        
    
        
estudante1 = Estudante(425323, 2022)
lista_alum_registrado.append(estudante1)




