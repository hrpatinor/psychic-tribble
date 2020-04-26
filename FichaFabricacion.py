class FichaFabricacion():
    def __init__(self, articulos_mes):
        self.articulos_mes = articulos_mes

    def inc_articulos(self, suma):
        self.articulos_mes += suma
        
        