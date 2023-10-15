from usuario import Usuario
from curso import Curso



lista_alum_registrado = []
lista_mi_cursos = []


class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscrpcion_carrera: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscrpcion_carrera
        
    def __str__(self):
        pass

    def matricular_en_curso(self, curso: Curso):
        pass

    def validar_credenciales(self, email: str, contrasenia_ingresada: str):
        acceso_concedido = False  

        for alumno in lista_alum_registrado:
            if alumno.email == email and alumno.contrasenia == contrasenia_ingresada:
                acceso_concedido = True
                print("ACCESO CONCEDIDO")
                return acceso_concedido  
            
        else:
            print("Correo electrónico o contraseña incorrecta")
    
    
   




estudiante1 = Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022)
lista_alum_registrado.append(estudiante1)

#funcion para buscar si el estudiante existe
def buscando_estudiante(email):
    for estudiante in lista_alum_registrado:
        if estudiante.email == email:
            return estudiante
    return None

    
    

 #<----------------Hecho por salvi XD nose si estara bien :D espero que si-------------------------->
  
"""    
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
            """
            

    
        
    



