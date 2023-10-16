#archivo para hacer los submenu del alumno y ahorrar codigo

def submenu(estudiante_actual):
    while True:
        print("1 -> Matricularse a un curso")
        print("2 -> Ver curso")
        print("3 -> Volver al menú principal")
        op = input("Seleccione una opción: ")
        if op == "1":
        #matricularse a un curso
            pass
        
        elif op == "2":
            #ver curso
            pass
        elif op == "3":
            break
            
        else:
            print("Opción no válida")




def materias():
    print("<-- Lista de cursos del Campus Virtual -->")
    print("1 -> Programación I")
    print("2 -> Programación II")
    print("3 -> Laboratorio II")
    print("4 -> Inglés I")
    print("5 -> Inglés II")
    op = int(input("Seleccione una opción: "))
    #forma rapida de validar de 1 a 5
    while op not in [1, 2, 3, 4, 5]:
        op = int(input("Seleccione una opción válida: "))
    return op    


