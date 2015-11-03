# -*- coding: utf-8 -*-
class Paseador():
    "Crear nuevo Paseador"
    
    def __init__(self,Apellido,Nombre,DNI,Telefono):
       self.__apellido = Apellido
       self.__nombre = Nombre
       self.__dni = DNI 
       self.__telefono = Telefono
       
    def get_Apellido(self):
        "Retorna el Apellido del Paseador"
        return self.__apellido
        
    def get_Nombre(self):
        "Retorna el Nombre del Paseador"        
        return self.__nombre
    
    def get_Dni(self):
        "Retorna el DNI del Paseador"
        return self.__dni
    
    def get_Telefono(self):
        "Retorna el Telefono del Paseador"
        return self.__telefono
        
    def set_Apellido(self,apellido):
        "Establecer el Apellido del Paseador"
        self.__apellido = apellido
        
    def set_Nombre(self,nombre):
        "Establecer el Nombre del Paseador"        
        self.__nombre = nombre
        
    def set_Dni(self,dni):
        "Establecer el DNI del Paseador"
        self.__dni = dni
        
    def set_Telefono(self,telefono):
        "Establecer el Telefono del Paseador"
        self.__telefono = telefono
