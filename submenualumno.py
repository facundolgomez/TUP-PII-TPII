import curso
from procesos import lista_cursos_campus
from estudiante import Estudiante


def submenu(estudiante_actual):
    while True:
        print("1 -> Matricularse a un curso")
        print("2 -> Ver cursos matriculados")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            for num, curso in enumerate(lista_cursos_campus, start=1):
                print(f"{num} {curso}")
            print("")

            validacion = True

            while validacion:
                materia = input("Ingrese el número del curso a matricularse: ")
                if materia.isdigit():  # Verificando si la entrada es un número
                    materia_elegida = int(materia)
                    if 1 <= materia_elegida <= len(lista_cursos_campus):
                        curso_seleccionado = lista_cursos_campus[materia_elegida - 1]

                        # Validar que el estudiante no esté ya matriculado en el curso
                        if curso_seleccionado not in estudiante_actual.mis_cursos:
                            resultado = estudiante_actual.matricular_en_curso(
                                curso_seleccionado
                            )
                            if resultado:
                                print(
                                    f"Te has matriculado correctamente en el curso '{curso_seleccionado.nombre}'."
                                )
                                validacion = False
                            else:
                                print("Ha ingresado una contraseña incorrecta ")
                        else:
                            print("Ya estás matriculado en este curso.")

                else:
                    print("Opción no válida. Ingrese un número válido.")

        elif op == "2":
            # lista de los cursos en los que el alumno se encuentra matriculado
            if estudiante_actual.mis_cursos:
                print("Materias en las que estás matriculado: ")
                for num, curso_actual in enumerate(
                    estudiante_actual.mis_cursos, start=1
                ):
                    print(f"{num}- {curso_actual.nombre}")
                print("")
            else:
                print("No estás matriculado en ninguna materia")
                print("")

        elif op == "3":
            print("")
            break

        else:
            print("Opción no válida")
            print("")
