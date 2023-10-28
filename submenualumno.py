import curso
from procesos import lista_cursos_campus
import archivo

def submenu(estudiante_actual):
    print(f"Bienvenido alumno {estudiante_actual.nombre} {estudiante_actual.apellido}")
    while True:
        print("1 -> Matricularse a un curso")
        print("2 -> Desmatricularse de un curso")
        print("3 -> Ver cursos matriculados")
        print("4 -> Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            if not lista_cursos_campus:
                print("Todavía no hay cursos disponibles.\n")
            else:
                for num, curso_actual in enumerate(
                    sorted(lista_cursos_campus, key=lambda curso: curso.nombre), start=1):
                    print(f"{num}- {curso_actual.nombre}")

                validación = True
                while validación:
                    materia = input("Ingrese el número del curso a matricularse: ")
                    if materia.isdigit():
                        materia_elegida = int(materia)
                        if 1 <= materia_elegida <= len(lista_cursos_campus):
                            curso_seleccionado = lista_cursos_campus[materia_elegida - 1]

                            if curso_seleccionado not in estudiante_actual.mis_cursos:
                                resultado = estudiante_actual.matricular_en_curso(curso_seleccionado)
                                if resultado:
                                    print(f"Te has matriculado correctamente en el curso '{curso_seleccionado.nombre}'.\n")
                                    validación = False
                                else:
                                    print("Has ingresado una contraseña incorrecta.\n")
                                    validación = False
                            else:
                                print("Ya estás matriculado en este curso.\n")
                                validación = False
                    else:
                        print("Opción no válida. Ingrese un número válido.")

        elif op == "2":
            if not lista_cursos_campus:
                print("Todavía no hay cursos disponibles.\n")
            elif not estudiante_actual.mis_cursos:
                print("Todavía no estás registrado en ningún curso.\n")
            else:
                validación = True
                while validación:
                    for num, curso_actual in enumerate(
                        sorted(estudiante_actual.mis_cursos, key=lambda curso: curso.nombre), start=1
                    ):
                        print(f"{num}- {curso_actual.nombre}")

                    materia = input("Ingrese el número del curso a desmatricularse: ")
                    if materia.isdigit():
                        materia_elegida = int(materia)
                        if 1 <= materia_elegida <= len(estudiante_actual.mis_cursos):
                            curso_seleccionado = estudiante_actual.mis_cursos[materia_elegida - 1]

                            if curso_seleccionado:
                                estudiante_actual.mis_cursos.remove(curso_seleccionado)
                                print(
                                    f"Te has desmatriculado correctamente del curso '{curso_seleccionado.nombre}'.\n"
                                )
                                validación = False
                        else:
                            desea_salir = input("Opción no válida. ¿Desea salir? V/F ")
                            desea_salir = desea_salir.lower()
                            if desea_salir == "v":
                                validación = False
                            elif desea_salir == "f":
                                validación = True
                            else:
                                print("Opción no válida. Intente nuevamente.\n")

        elif op == "3":
            if estudiante_actual.mis_cursos:
                print("Materias en las que estás matriculado:")
                for num, curso_actual in enumerate(estudiante_actual.mis_cursos, start=1):
                    print(f"{num}- {curso_actual.nombre}")
                print("")
                curso_seleccionado = input("Seleccione un curso para ver los archivos: ")
                if curso_seleccionado.isdigit():
                    curso_elegido = int(curso_seleccionado)
                    if 1 <= curso_elegido <= len(estudiante_actual.mis_cursos):
                        curso_estudiante = estudiante_actual.mis_cursos[curso_elegido - 1]
                        print(f"Nombre del curso: {curso_estudiante.nombre}")
                        print("Archivos adjuntos: ")
                        if not curso_estudiante.mis_archivos:
                            print("No hay archivos para mostrar")
                        else:
                            archivos_ordenados = sorted(curso_estudiante.mis_archivos, key=lambda archivo: archivo.fecha)
                            for archivo in archivos_ordenados:
                                print(f"{archivo.nombre}.{archivo.formato}")
                    else:
                        print("Opción incorrecta")
                else:
                    print("Opción incorrecta")
            else:
                print("No estás matriculado en ninguna materia.\n")

        elif op == "4":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción no válida.\n")
