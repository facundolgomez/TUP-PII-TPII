import profesor
import curso
import estudiante
import procesos

def submenu(profesor_actual):
    while True:
        print("1 -> Dictar curso")
        print("2 -> Ver curso")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            # Dictar curso
            nombre_curso = input("Ingrese el nombre del curso a dar de alta: ")
            nuevo_curso = curso.Curso(nombre_curso)
            profesor_actual.dictar_curso(nuevo_curso)
            print(f"Curso '{nuevo_curso.nombre}' dado de alta con éxito.")
            print(f"Nombre: {nuevo_curso.nombre}")
            print(f"Contraseña: {nuevo_curso.contrasenia_matriculacion}")
            #agregando una materia a la lista de cursos del campus
            procesos.lista_cursos_campus.append(nuevo_curso)
            #ordeno la lista definitivamente para que cuando el usuario elija un curso coincida con los indices de la lista
            procesos.lista_cursos_campus.sort(key=lambda curso: curso.nombre)


        elif op == "2":
            # Ver cursos
            if not profesor_actual.mis_cursos:
                print("El profesor no ha dictado cursos todavía.")
            else:
                for num, curso_actual in enumerate(sorted(profesor_actual.mis_cursos, key=lambda curso: curso.nombre), start=1):
                    print(f"{num}- {curso_actual.nombre}")


                validacion = True
                while validacion:
                    opcion = input("Ingrese el número del curso que desea ver: ")
                    if opcion.isdigit():
                        op = int(opcion)
                        if 1 <= op <= len(profesor_actual.mis_cursos):
                            validacion = False
                        else:
                            print("Opción no válida. Ingrese un número válido.")
                    
                # obtiene el curso seleccionado
                curso_seleccionado = profesor_actual.mis_cursos[op - 1]

                # muestra el nombre del curso y la contraseña de matriculación
                print(f"Nombre: {curso_seleccionado.nombre}")
                print(f"Contraseña de matriculación: {curso_seleccionado.contrasenia_matriculacion}")

        elif op == "3":
            # Volver al menú principal
            break
        else:
            print("Opción no válida")




