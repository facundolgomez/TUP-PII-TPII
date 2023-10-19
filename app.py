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
    #ingresar como alumno
    if op == "1":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_estudiante = procesos.buscando_estudiante(gmail)

        if un_estudiante:
            for un_estudiante in procesos.lista_alum_registrado:
                if un_estudiante.validar_credenciales(gmail, password):
                    print("ACCESO EXITOSO")
                    submenualumno.submenu(un_estudiante)
                    break
            else:
                print("Correo electronico o contraseña incorrecta")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.")

    # Ingresar como profesor            
    elif op == "2":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_profesor = procesos.buscando_profesor(gmail)

        if un_profesor:
            for un_profesor in procesos.lista_profes_registrados:
                if un_profesor.validar_credenciales(gmail, password):
                    print("ACCESO EXITOSO")
                    submenuprofesor.submenu(un_profesor)
                    break
            else:
                print("Correo electronico o contraseña incorrecta ")
        else:
            print("El profesor no existe. Debe darse de alta en alumnado.")

    # Lista de cursos del campus virtual    
    elif op == "3":
        if procesos.lista_cursos_campus:
            for curso in sorted(procesos.lista_cursos_campus, key=lambda curso: curso.nombre):
                print(f"Materia: {curso.nombre}, Carrera: Tecnicatura Universitaria en Programación")
        else:
            print("Todavia no hay cursos disponibles en el campus virtual")
        

    elif op == "4":
        ejecutar_programa = False









