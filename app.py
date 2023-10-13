#TP2-Programacion2



def main():
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
            gmail = input("Ingrese su correo electronico: ")
            password = input("Ingrese su contraseña: ")
            #Acompletar ingresando las claves del alumno
            print("Campus Virtual --> Alumno")
            print("1 -> Matricularse a un curso")
            print("2 -> Ver curso")
            print("3 -> Volver al menú principal")

            while True:
                x = input("Seleccione una opción: ")

                if x == "1":
                    print("<-- Materias a matricularse -->")
                    print("1 -> Programación I")
                    print("2 -> Programación II")
                    print("3 -> Laboratorio II")
                    print("4 -> Inglés I")
                    print("5 -> Ingles II")
                    print("0 -> para salir")
                    
                    while True:
                        y = input("Seleccione la materia a cursar: ")
                        #Haria algo, que lo que haria seria implementar la materia al estudiante.py PROGRAMAR
                        if y == "1":
                            print("Se agrego la mtareia Programación I")
                        elif y == "0":
                            break          
                        else:
                            print("Opción no válida. Seleccione 1, 2, 3 o 4...")
                    

                elif x == "2":
                    pass

                elif x == "3":
                    continue  
                else: 
                    print("Opción no válida. Seleccione 1, 2 o 3.")
            
                    
        elif op == "2":
            gmail = input("Ingrese su correo electronico: ")
            password = input("Ingrese su contraseña: ")
            #Acompletar ingresando las claves del alumno
            print("Campus Virtual --> Profesor")
            print("1 -> Dictar Curso")
            print("2 -> Ver curso")
            print("3 -> Volver al menú principal")

            x = input("Seleccione una opción: ")

        elif op == "3":
            print("Materias:")
            #Mostrar lista de todas las materias de campus 

        elif op == "4":
            ejecutar_programa = False  

main()