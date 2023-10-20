import profesor
import estudiante
import curso


def buscando_profesor(email):
    """
    Funcion busqueda de profesor
    
    Esta función busca un profesor por su dirección de correo electrónico en una 
    lista de profesores registrados.
    """
    for profe in lista_profes_registrados:
        if profe.email == email:
            return profe
    return None


def buscando_estudiante(email):
    """
    Funcion busqueda de estudiante
    
    Esta función busca un estudiante por su dirección de correo electrónico en una 
    lista de estudiantes registrados.
    """
    for estudiante in lista_alum_registrado:
        if estudiante.email == email:
            return estudiante
    return None


# Lista para los profesores registrados
lista_profes_registrados = [] 

# Lista para alumnos registrados
lista_alum_registrado = [] 

# Lista de cursos del campus
lista_cursos_campus = ["Programación I", "Programación II", "Laboratorio I", "Ingles I", "Ingles II"]

# Instancia de profesor
profe = profesor.Profesor("Carlos", "Rodriguez", "mailprofe", "contra", "ingeniero", 1998) 
lista_profes_registrados.append(profe)

# Instancia de estudiante
estudiante1 = estudiante.Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022)
lista_alum_registrado.append(estudiante1)

# Instancia de estudiante
estudiante2 = estudiante.Estudiante("lucas", "diaz", "otromail", "contra", 75632, 2022) 
lista_alum_registrado.append(estudiante2)

