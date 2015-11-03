
class Mascota():
    def __init__(self, nom, raza, peso, dni_duenio, dni_paseador, cod):
        self.__nombre = nom
        self.__raza = raza
        self.__peso = peso
        self.__dni_duenio = dni_duenio
        self.__dni_paseador = dni_paseador
        self.__codigo = cod
        
    def get_Nombre(self):
        return self.__nombre

    def set_Nombre(self,nom):
        self.__nombre = nom
        
    def get_Raza(self):
        return self.__raza

    def set_Raza(self,raza):
        self.__raza = raza
        
    def get_Peso(self):
        return self.__peso

    def set_Peso(self,peso):
        self.__peso = peso
    
    def get_Codigo(self):
        return self.__codigo

    def set_Codigo(self,cod):
        self.__codigo = cod
        
    def get_Dni_Duenio(self):
        return self.__dni_duenio
        
    def set_Dni_Duenio(self,dni):
        self.__dni_duenio = dni
    
    def get_Dni_Paseador(self):
        return self.__dni_paseador
        
    def set_Dni_Paseador(self, dni):
        self.__dni_paseador = dni