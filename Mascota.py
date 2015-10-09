
class Mascota():
    def __init__(self,nom,raza,peso,cod):
        self.__nombre = nom
        self.__raza = raza
        self.__peso = peso
        self.__codigo = cod
        
    def getNombre(self):
        return self.__nombre

    def setNombre(self,nom):
        self.__nombre = nom
        
    def getRaza(self):
        return self.__raza

    def setRaza(self,raza):
        self.__raza = raza
        
    def getPeso(self):
        return self.__peso

    def setPeso(self,peso):
        self.__peso = peso
    
    def getCodigo(self):
        return self.__codigo

    def setCodigo(self,cod):
        self.__codigo = cod