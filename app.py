import estudiante
import submenualumno
import profesor
import submenuprofesor

#funciones para busqueda
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



lista_profes_registrados = []

lista_alum_registrado = []

lista_cursos_campus = []

#profe de prueba
profe = profesor.Profesor("Carlos", "rodriguez", "mailprofe", "contra", "ingeniero", 1998)
lista_profes_registrados.append(profe)


#alumnos de prueba
estudiante1 = estudiante.Estudiante("franco", "gonzalez", "mail", "contra", 434312, 2022)
lista_alum_registrado.append(estudiante1)

estudiante2 = estudiante.Estudiante("lucas", "diaz", "otromail", "contra", 75632, 2022)
lista_alum_registrado.append(estudiante2)




ejecutar_programa = True 

while ejecutar_programa:
    print("Bienvenido al Campus Virtual")
    print("<--------------------------->")
    print("1 -> Ingresar como alumno")
    print("2 -> Ingresar como profesor")
    print("3 -> Ver cursos")
    print("4 -> Salir")

    op = input("Seleccione una opción: ")
    #ingresar como alumno
    if op == "1":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_estudiante = buscando_estudiante(gmail)

        if un_estudiante:
            if un_estudiante.validar_credenciales(gmail, password):
                print("ACCESO EXITOSO")
                submenualumno.submenu(un_estudiante)
            else:
                print("Correo electronico o contraseña incorrecta")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.")

    # Ingresar como profesor            
    elif op == "2":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_profesor = buscando_profesor(gmail)

        if un_profesor:
            if un_profesor.validar_credenciales(gmail, password):
                print("ACCESO EXITOSO")
                submenuprofesor.submenu(un_profesor)
            else:
                print("Correo electronico o contraseña incorrecta ")
        else:
            print("El profesor no existe. Debe darse de alta en alumnado.")

    # Lista de cursos del campus virtual    
    elif op == "3":
        if lista_cursos_campus:
            for curso in sorted(lista_cursos_campus, key=lambda curso: curso.nombre):
                print(f"Materia: {curso.nombre}, Carrera: Tecnicatura Universitaria en Programación")
        else:
            print("Todavia no hay cursos disponibles en el campus virtual")
        

    elif op == "4":
        ejecutar_programa = False






