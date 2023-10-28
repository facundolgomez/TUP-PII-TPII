import profesor
import curso
import procesos
from archivo import Archivo



def submenu(profesor_actual):
    print(f"Bienvenido profesor {profesor_actual.nombre} {profesor_actual.apellido}")
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
            print(f"El código es: {nuevo_curso.codigo}")
            print(f"Contraseña: {nuevo_curso.contrasenia_matriculacion}")

            
            # Agregando una materia a la lista de cursos del campus
            procesos.lista_cursos_campus.append(nuevo_curso)
            # Ordeno la lista definitivamente para que cuando el usuario elija un curso coincida con los indices de la lista
            procesos.lista_cursos_campus.sort(key=lambda curso: curso.nombre)

        elif op == "2":
            # Ver cursos
            if not profesor_actual.mis_cursos:
                print("El profesor no ha dictado cursos todavía.\n")
            else:
                for num, curso_actual in enumerate(
                    sorted(profesor_actual.mis_cursos, key=lambda curso: curso.nombre),
                    start=1,
                ):
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

                # Obtiene el curso seleccionado
                curso_seleccionado = profesor_actual.mis_cursos[op - 1]

                # Muestra el nombre del curso y la contraseña de matriculación
                print(f"Nombre: {curso_seleccionado.nombre}")
                print(f"Código: {curso_seleccionado.codigo}")
                print(
                    f"Contraseña de matriculación: {curso_seleccionado.contrasenia_matriculacion}"
                )
                print(f"Cantidad de archivos: {len(curso_seleccionado.mis_archivos)}")

                msj_adjunto = input("Desea agregar un archivo adjunto? V/F ")
                msj_adjunto = msj_adjunto.lower()
                if msj_adjunto == "v":
                    nombre_archivo = input("Ingrese nombre del archivo: ")
                    formato = input("Ingrese formato del archivo: ")
                    archivo_creado = Archivo(nombre_archivo, formato)
                    curso_seleccionado.mis_archivos.append(archivo_creado)
                    print("Archivo registrado correctamente\n")
                
                elif msj_adjunto == "f":
                    continue

                else:
                    print("Opción incorrecta\n")    
                   
        elif op == "3":
            print("Volviendo al menu principal...\n")
            break

        else:
            print("Opción no válida.\n")
