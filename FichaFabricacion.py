from FichaEmpleado import FichaEmpleado
class FichaFabricacion(FichaEmpleado):
    def __init__(self, articulos_mes):
        super().__init__()
        self.articulos_mes = articulos_mes

    def inc_articulos(self, suma):
        self.articulos_mes += suma

        