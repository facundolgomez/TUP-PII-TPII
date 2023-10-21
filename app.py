import submenualumno
import submenuprofesor
import procesos

ejecutar_programa = True

while ejecutar_programa:
    print("Bienvenido al Campus Virtual")
    print("<--------------------------->")
    print("1 -> Ingresar como alumno")
    print("2 -> Ingresar como profesor")
    print("3 -> Ver cursos")
    print("4 -> Salir")

    op = input("Seleccione una opción: ")

    # Ingresar como alumno
    if op == "1":
        mail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_estudiante = procesos.buscando_estudiante(mail)

        if un_estudiante:
            for un_estudiante in procesos.lista_alum_registrado:
                if un_estudiante.validar_credenciales(mail, password):
                    print("ACCESO EXITOSO\n")
                    submenualumno.submenu(un_estudiante)
                    break
            else:
                print("Correo electronico o contraseña incorrecta\n")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.\n")
    # Ingresar como profesor
    elif op == "2":
        mail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_profesor = procesos.buscando_profesor(mail)

        if un_profesor:
            for un_profesor in procesos.lista_profes_registrados:
                if un_profesor.validar_credenciales(mail, password):
                    print("ACCESO EXITOSO\n")
                    submenuprofesor.submenu(un_profesor)
                    break
            else:
                print("Correo electronico o contraseña incorrecta.\n")
        else:
            print("El profesor no existe. Debe darse de alta en alumnado.\n")
    # Lista de cursos del campus virtual
    elif op == "3":
        if procesos.lista_cursos_campus:
            longitud = max(len(curso.nombre) for curso in procesos.lista_cursos_campus)
            for curso in sorted(
                procesos.lista_cursos_campus, key=lambda curso: curso.nombre):
                # Justificado de texto
                nombre_curso = curso.nombre.ljust(longitud)
                print(
                    f"Materia: {nombre_curso} Carrera: Tecnicatura Universitaria en Programación")
            print("")

        else:
            print("Todavia no hay cursos disponibles en el campus virtual.\n")

    elif op == "4":
        print("¡Hasta luego!")
        ejecutar_programa = False

    else:
        print("Por favor ingrese un número válido.\n")


