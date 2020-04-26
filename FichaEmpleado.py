class FichaEmpleado():
    def __init__(self, nombre, edad, antiguedad, cualificacion):
        self.nombre = nombre
        self.edad = edad
        self.antiguedad = antiguedad
        self.cualificacion = cualificacion

    def __sueldo(self):
        return (1000 + self.antiguedad * 25 + self.cualificacion * 100)