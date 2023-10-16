import profesor
import curso

def submenu(profesor_actual):
    while True:
        print("1 -> Dictar curso")
        print("2 -> Ver curso")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            # Opción 1: dictar curso
            nombre_curso = input("Ingrese el nombre del curso a dar de alta: ")
            nuevo_curso = curso.Curso(nombre_curso)
            profesor_actual.dictar_curso(nuevo_curso)
            print(f"Curso '{nuevo_curso.nombre}' dado de alta con éxito.")
            print(f"Nombre: {nuevo_curso.nombre}\nContraseña: {nuevo_curso.contrasenia_matriculación}")
        elif op == "2":
            # Opción 2: ver cursos
            for num, curso in enumerate(profesor_actual.mis_cursos):
                print(f"{num + 1} {curso.nombre}")
        elif op == "3":
            # Opción 3: volver al menú principal
            break
        else:
            print("Opción no válida")

        