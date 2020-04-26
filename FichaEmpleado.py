class FichaEmpleado():
    def __init__(self, nombre, edad, antiguedad, cualificacion):
        self.nombre = nombre
        self.edad = edad
        self.antiguedad = antiguedad
        self.cualificacion = cualificacion

    def __sueldo(self):
        return (1000 + self.antiguedad * 25 + self.cualificacion * 100)

    def set_cualificacion(self, cualificacion):
        if cualificacion in [1,2,3,4,5]:
            self.cualificacion = cualificacion
