# -*- coding: utf-8 -*-
class Paseador():
    "Crear nuevo Paseador"
    
    def __init__(self,Apellido,Nombre,DNI,Telefono):
       self.__apellido = Apellido
       self.__nombre = Nombre
       self.__dni = DNI 
       self.__telefono = Telefono
       
    def GetApellido(self):
        "Retorna el Apellido del Paseador"
        return self.__apellido
        
    def GetNombre(self):
        "Retorna el Nombre del Paseador"        
        return self.__nombre
    
    def GetDni(self):
        "Retorna el DNI del Paseador"
        return self.__dni
    
    def GetTelefono(self):
        "Retorna el Telefono del Paseador"
        return self.__telefono
        
    def SetApellido(self,apellido):
        "Establecer el Apellido del Paseador"
        self.__apellido = apellido
        
    def SetNombre(self,nombre):
        "Establecer el Nombre del Paseador"        
        self.__nombre = nombre
        
    def SetDni(self,dni):
        "Establecer el DNI del Paseador"
        self.__dni = dni
        
    def SetTelefono(self,telefono):
        "Establecer el Telefono del Paseador"
        self.__telefono = telefono
