import profesor
import curso

def submenu(profesor_actual):
    while True:
        print("1 -> Dictar curso")
        print("2 -> Ver curso")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            #dictar curso
            nombre_curso = input("Ingrese el nombre del curso a dar de alta: ")
            nuevo_curso = curso.Curso(nombre_curso)
            profesor_actual.dictar_curso(nuevo_curso)
            print(f"Curso '{nuevo_curso.get_nombre()}' dado de alta con éxito.")
            print(f"Nombre: {nuevo_curso.get_nombre()}")
            print(f"Contraseña: {nuevo_curso.get_contrasenia_matriculacion()}")



        
        elif op == "2":
        #ver cursos
            if not profesor_actual.mis_cursos:
                print("El profesor no ha dictado cursos todavía.")
            else:
                for num, curso_actual in enumerate(profesor_actual.mis_cursos):
                    print(f"{num + 1} {curso_actual.get_nombre()}")
        
                validacion = True
                while validacion:
                    op = input("Ingrese el número del curso que desea ver: ")
                    if op.isdigit():
                        op = int(op)
                        if 1 <= op <= len(profesor_actual.mis_cursos):
                            validacion = False
                        else:
                            print("Opción no válida. Ingrese un número válido.")
                    else:
                        print("Opción no válida. Ingrese un número válido.")

                # Obtiene el curso seleccionado
                curso_seleccionado = profesor_actual.mis_cursos[op - 1]

                # Muestra el nombre del curso y la contraseña de matriculación
                print(f"Nombre: {curso_seleccionado.get_nombre()}")
                print(f"Contraseña de matriculación: {curso_seleccionado.get_contrasenia_matriculacion()}")



        
        elif op == "3":
            #volver al menú principal
            break
        else:
            print("Opción no válida")

        