class Receta:
    
    #constructor
    def __init__(self, fecha, nombre, padecimiento, descripcion):
        self.fecha = fecha
        self.nombre = nombre
        self.padecimiento = padecimiento
        self.descripcion = descripcion

    #Métodos get y set
    
    def getFecha(self):
        return self.fecha

    def setfecha(self, fecha):
        self.fecha = fecha

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPadecimeinto(self):
        return self.padecimiento

    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
   