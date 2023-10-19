import profesor
import estudiante
import curso


def buscando_profesor(email):
    """
    Funcion busqueda de profesor
    
    Esta función busca un profesor por su dirección de correo electrónico en una lista de profesores registrados.
    """
    for profe in lista_profes_registrados:
        if profe.email == email:
            return profe
    return None


def buscando_estudiante(email):
    """
    Funcion busqueda de estudiante
    
    Esta función busca un estudiante por su dirección de correo electrónico en una lista de estudiantes registrados.
    """
    for estudiante in lista_alum_registrado:
        if estudiante.email == email:
            return estudiante
    return None


lista_profes_registrados = [] #lista para los profes registrados

lista_alum_registrado = [] #lista para alumnos registrados

lista_cursos_campus = [] #lista de cursos del campus


profe = profesor.Profesor("Carlos", "rodriguez", "mailprofe", "contra", "ingeniero", 1998) #Instancia de profesor
lista_profes_registrados.append(profe)

estudiante1 = estudiante.Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022) #Instancia de estudiante
lista_alum_registrado.append(estudiante1)

estudiante2 = estudiante.Estudiante("lucas", "diaz", "otromail", "contra", 75632, 2022) #Instancia de estudiante
lista_alum_registrado.append(estudiante2)

