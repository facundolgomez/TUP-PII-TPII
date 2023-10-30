class Carrera:
    def __init__(self, nombre: str, cant_anios: int):
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def cant_anios(self):
        return self.__cant_anios

    @cant_anios.setter
    def cant_anios(self, nueva_cant_anios):
        self.__cant_anios = nueva_cant_anios    

    def __str__(self):
        return f"Nombre carrera: {self.nombre}. Cantidad de años: {self.cant_anios}"

    def get_cantidad_materias(self, lista_cursos) -> int:
        return len(lista_cursos)
        
