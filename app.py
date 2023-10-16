import estudiante
import submenualumno
import profesor
import submenuprofesor


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
        un_estudiante = estudiante.buscando_estudiante(gmail)

        if un_estudiante:
            if un_estudiante.validar_credenciales(gmail, password):
                submenualumno.submenu(un_estudiante)
            else:
                print("Error de ingreso")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.")

    # Ingresar como profesor            
    elif op == "2":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_profesor = profesor.buscando_profesor(gmail)

        if un_profesor:
            if un_profesor.validar_credenciales(gmail, password):
                submenuprofesor.submenu(un_profesor)
            else:
                print("Error de ingreso")
        else:
            print("El profesor no existe. Debe darse de alta en alumnado.")

    # Lista de cursos del campus virtual    
    elif op == "3":
        # Aca lo que hay que hacer es mostrar mostrar una lista de todos los cursos del Campus Virtual ordenados alfabéticamente,
        # osea que los cursos van a ser los objetos que esten creados en el modulo correspondiente
        #y hay que mostrarlos de la forma Materia: Ingles 1 Carrera: Tecnicatura Univ en Programacion y asi en base a la cantidad de objetos que existan
        pass

    elif op == "4":
        ejecutar_programa = False



