# Modulo de carreras, se usará en la entrega final.


class Carrera:
    def __init__(self, nombre: str, cant_anios: int):
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    def __str__(self):
        pass

    def get_cantidad_materias(self) -> int:
        pass
