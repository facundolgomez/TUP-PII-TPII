import estudiante
import submenualumno


ejecutar_programa = True 

while ejecutar_programa:
    print("Bienvenido al Campus Virtual")
    print("<--------------------------->")
    print("1 -> Ingresar como alumno")
    print("2 -> Ingresar como profesor")
    print("3 -> Ver cursos")
    print("4 -> Salir")

    op = input("Seleccione una opción: ")

    if op == "1":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        un_estudiante = estudiante.buscando_estudiante(gmail)

        if un_estudiante:
            if un_estudiante.validar_credenciales(gmail, password):
                sub_opcion = submenualumno.submenu()
                if sub_opcion == "1":
                    submenualumno.materias()
                elif sub_opcion == "2":
                    # Hacer lo de ver curso
                    pass
                elif sub_opcion == "3":
                    pass
                else:
                    print("Opción no válida")
            else:
                print("Error de ingreso")
        else:
            print("El estudiante no existe. Debe darse de alta en alumnado.")

    # Ingresar como profesor            
    elif op == "2":
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        print("Campus Virtual --> Profesor")
        print("1 -> Dictar Curso")
        print("2 -> Ver curso")
        print("3 -> Volver al menú principal")
        x = input("Seleccione una opción: ")

    # Lista de cursos del campus virtual    
    elif op == "3":
        cursos = [
            {"nombre": "Inglés I", "carrera": "Tecnicatura Universitaria en Programación"},
            {"nombre": "Inglés II", "carrera": "Tecnicatura Universitaria en Programación"},
            {"nombre": "Laboratorio I", "carrera": "Tecnicatura Universitaria en Programación"},
            {"nombre": "Laboratorio II", "carrera": "Tecnicatura Universitaria en Programación"},
            {"nombre": "Programación I", "carrera": "Tecnicatura Universitaria en Programación"},
            {"nombre": "Programación II", "carrera": "Tecnicatura Universitaria en Programación"}
        ]
        print("Materias")
        # Mostrar lista de todas las materias del campus 

    elif op == "4":
        ejecutar_programa = False



