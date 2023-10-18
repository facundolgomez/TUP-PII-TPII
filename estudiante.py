from usuario import Usuario
from curso import Curso


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mis_cursos = []  

    def __str__(self):
        pass


    
    def matricular_en_curso(self, curso_seleccionado: Curso):
        contrasenia_matriculacion = input(f"Ingrese la contraseña de matriculación para '{curso_seleccionado.nombre}': ")

    # Validar la contraseña
        if contrasenia_matriculacion == curso_seleccionado.contrasenia_matriculacion:
            if curso_seleccionado not in self.mis_cursos:
                self.mis_cursos.append(curso_seleccionado)
                #ordenando la lista de cursos para ese estudiante
                self.mis_cursos.sort(key=lambda curso: curso.nombre)
                print(f"Te has matriculado en el curso '{curso_seleccionado.nombre}'.")
        else:
            print("Contraseña de matriculacion incorrecta.")

    
    
    def validar_credenciales(self, email: str, contrasenia_ingresada: str) -> bool:
        acceso_concedido = False  
        for alumno in lista_alum_registrado:
            if alumno.email == email and alumno.contrasenia == contrasenia_ingresada:
                acceso_concedido = True
                return acceso_concedido  
        
    
    
   


<<<<<<< HEAD
<<<<<<< HEAD
    
=======

#Pasar a submenualum

while True:
    try:
    
        estudiante1 = Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022)
        lista_alum_registrado.append(estudiante1)
        break
    except:
        print("Usuario repetido")
    


    estudiante2 = Estudiante("lucas", "diaz", "otromail", "contra", 75632, 2022)
    lista_alum_registrado.append(estudiante2)

#funcion para buscar si el estudiante existe, no pertenece a la clase
def buscando_estudiante(email):
    for estudiante in lista_alum_registrado:
        if estudiante.email == email:
            return estudiante
    return None

>>>>>>> 16cf1dd57bc8bc71bb6d5d5c085be7c3c78fd64b
=======
    
>>>>>>> 80bef683aa130b0243ff9f40d9e757881167d43e
    
    

            

    
        
    



