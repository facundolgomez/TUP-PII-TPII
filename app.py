import submenualumno
import submenuprofesor
import procesos
import profesor
from carrera import Carrera

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
            print("El profesor no existe. Debe darse de alta en alumnado.")
            posee_codigo = input("¿Posee código de alta? Ingrese V/F: ")
            posee_codigo = posee_codigo.lower()
            if posee_codigo == "v":
                codigo_alta = input("\nIngrese el código de alta: ")
                if codigo_alta == "admin":
                    print("Por favor complete los siguientes campos para darse de alta: ")
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    mail = input("Ingrese su email: ")
                    contrasenia = input("Ingrese una contraseña: ")
                    titulo = input("Ingrese su titulo: ")
                    anio_egreso = input("Ingrese su año de egreso (AAAA): ")

                    profe_nuevo = profesor.Profesor(nombre, apellido, mail, contrasenia, titulo, anio_egreso)
                    procesos.lista_profes_registrados.append(profe_nuevo)
                    print("Profesor registrado\n")
                else:
                    print("Código de alta erroneo.\n")
            elif posee_codigo == "f":
                print("Para darse de alta solicite el código en alumnado.\n")
            else:
                print("Opción incorrecta.\n")

    # Lista de cursos del campus virtual
    elif op == "3":
        if procesos.lista_cursos_campus:
            longitud = max(len(curso.nombre) for curso in procesos.lista_cursos_campus)
            for curso in sorted(
                procesos.lista_cursos_campus, key=lambda curso: curso.nombre):
                # Justificado de texto
                nombre_curso = curso.nombre.ljust(longitud)
                print(f"Materia: {nombre_curso} Carrera: {procesos.carrera1.nombre}")
            print(f"Cantidad de cursos en la carrera: {procesos.carrera1.get_cantidad_materias(procesos.lista_cursos_campus)}\n")

        else:
            print("Todavia no hay cursos disponibles en el campus virtual.\n")

    elif op == "4":
        print("¡Hasta luego!")
        ejecutar_programa = False

    else:
        print("Por favor ingrese un número válido.\n")


