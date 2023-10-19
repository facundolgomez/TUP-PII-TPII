import profesor
import estudiante
import curso

#funciones de busqueda
def buscando_profesor(email):
    for profe in lista_profes_registrados:
        if profe.email == email:
            return profe
    return None


def buscando_estudiante(email):
    for estudiante in lista_alum_registrado:
        if estudiante.email == email:
            return estudiante
    return None


######LISTAS#####

lista_profes_registrados = [] #lista para los profes registrados

lista_alum_registrado = [] #lista para alumnos registrados

lista_cursos_campus = [] #lista de cursos del campus




#profe de prueba
profe = profesor.Profesor("Carlos", "rodriguez", "mailprofe", "contra", "ingeniero", 1998)
lista_profes_registrados.append(profe)


#alumnos de prueba
estudiante1 = estudiante.Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022)
lista_alum_registrado.append(estudiante1)

estudiante2 = estudiante.Estudiante("lucas", "diaz", "otromail", "contra", 75632, 2022)
lista_alum_registrado.append(estudiante2)

