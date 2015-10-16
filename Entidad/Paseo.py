# Clase Paseo

class Paseo():
    def __init__(self,ti,tf,num):
        self.__tiempoInicio = ti
        self.__tiempoFin = tf
        
    def getNombre(self):
        return self.__tiempoInicio

    def setNombre(self,ti):
        self.__tiempoInicio = ti
        
    def getRaza(self):
        return self.__tiempoFin

    def setRaza(self,tf):
        self.__tiempoFin = tf
