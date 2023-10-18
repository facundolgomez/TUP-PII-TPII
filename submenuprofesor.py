import curso


def submenu(estudiante_actual):
    while True:
        print("1 -> Matricularse a un curso")
        print("2 -> Ver cursos matriculados")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")
        
        if op == "1":
            if not estudiante_actual.lista_cursos_campus:
                print("No hay cursos disponibles")
            else:
                for num, curso_actual in enumerate(sorted(estudiante_actual.lista_cursos_campus, key=lambda curso: curso.nombre), start=1):
                    print(f"{num}- {curso_actual.nombre}")

                validacion = True
                while validacion:
                    materia = int(input("Ingrese el numero del curso a matricularse: "))
                    if 1 <= materia <= len(estudiante_actual.lista_cursos_campus):
                        curso_seleccionado = estudiante_actual.lista_cursos_campus[materia - 1]
                        
                        # Validar que el estudiante no esté ya matriculado en el curso
                        if curso_seleccionado not in estudiante_actual.mis_cursos:
                            estudiante_actual.matricular_en_curso(curso_seleccionado)
                            validacion = False
                            print("Se ha matriculado correctamente en el curso.")
                        else:
                            print("Ya estás matriculado en este curso.")
                    else:
                        print("Opción no válida. Ingrese un número válido.")
                    
        elif op == "2":
            # lista de los cursos en los que el alumno se encuentra matriculado
            if estudiante_actual.mis_cursos:
                print("Materias en las que estás matriculado: ") 
                for num, curso_actual in enumerate(estudiante_actual.mis_cursos, start=1):
                    print(f"{num}- {curso_actual.nombre}")
            else:
                print("No estás matriculado en ninguna materia")        
            
        elif op == "3":
            break
            
        else:
            print("Opción no válida")



