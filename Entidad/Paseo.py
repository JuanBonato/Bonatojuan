# Clase Paseo
import time
from datetime import datetime, timedelta

class Paseo():
    def __init__(self, dni_paseador, horas, minutos, espacio):
        self.__fecha = time.strftime("%d/%m/%y")        
        self.__salida = datetime.now()
        self.__tentativo = self.__salida + timedelta(hours=horas, minutes=minutos)
        self.__arribo = None
        self.__espacio = espacio
        self.__dni_paseador = dni_paseador
        
    def get_Fecha(self):
        return self.__fecha
    
    def get_Salida(self):
        return self.__salida
    
    def get_Tentativo(self):
        return self.__tentativo
        
    def get_Arribo(self):
        return self.__arribo
        
    def get_Paseador(self):
        return self.__dni_paseador
        
    def get_Espacio(self):
        return self.__espacio
    
    def set_Fecha(self, fecha):
        self.__fecha = fecha
    
    def set_Salida(self, salida):
        self.__salida = salida
    
    def set_Tentativo(self, tentativo):
        self.__tentativo = tentativo
        
    def set_Arribo(self, arribo):
        self.__arribo = arribo
        
    def set_Espacio(self, espacio):        
        self.__espacio = espacio
        
    def set_Paseador(self, dni_paseador):
        self.__dni_paseador = dni_paseador