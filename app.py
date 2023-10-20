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
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_estudiante = procesos.buscando_estudiante(gmail)

        if un_estudiante:
            for un_estudiante in procesos.lista_alum_registrado:
                if un_estudiante.validar_credenciales(gmail, password):
                    print("ACCESO EXITOSO")
                    print("")
                    submenualumno.submenu(un_estudiante)
                    break
            else:
                print("Correo electronico o contraseña incorrecta")
                print("")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.")
            print("")

    # Ingresar como profesor            
    elif op == "2":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_profesor = procesos.buscando_profesor(gmail)

        if un_profesor:
            for un_profesor in procesos.lista_profes_registrados:
                if un_profesor.validar_credenciales(gmail, password):
                    print("ACCESO EXITOSO")
                    print("")
                    submenuprofesor.submenu(un_profesor)
                    break
            else:
                print("Correo electronico o contraseña incorrecta.")
                print("")
        else:
            print("El profesor no existe. Debe darse de alta en alumnado.")
            print("")

    # Lista de cursos del campus virtual    
    elif op == "3":
        # Ordena la lista alfabéticamente
        lista_cursos_ordenados = sorted(procesos.lista_cursos_campus)

        longitud_maxima_materia = max(len(f"Materia: {curso}") for curso in procesos.lista_cursos_campus)

        for curso in lista_cursos_ordenados:
            # Establece el espacio sobrante hacia la derecha del nombre de la materia
            espacio_derecha = " " * (longitud_maxima_materia - len(f"Materia: {curso}"))
            print(f"Materia: {curso}{espacio_derecha} Carrera: Tecnicatura Universitaria en Programación")

        print("")

    elif op == "4":
        print("¡Hasta luego!")
        ejecutar_programa = False

    else:
        print("Ingrese un número válido.")
        print("")








