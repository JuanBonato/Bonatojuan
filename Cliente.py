# -*- coding: utf-8 -*-

class Cliente():
    "Crear nuevo cliente"
    
    def __init__(self,Apellido,Nombre,DNI,Telefono,Direccion):
       
       self.__apellido = Apellido
       self.__nombre = Nombre
       self.__dni = DNI 
       self.__telefono = Telefono
       self.__direccion = Direccion
       
    def GetApellido(self):
        "Retorna el Apellido del Cliente"
        return self.__apellido
        
    def GetNombre(self):
        "Retorna el Nombre del Cliente"        
        return self.__nombre
    
    def GetDni(self):
        "Retorna el DNI del Cliente"
        return self.__dni
    
    def GetTelefono(self):
        "Retorna el Telefono del Cliente"
        return self.__telefono
        
    def GetDireccion(self):
        "Retorna el Direccion del Cliente"
        return self.__direccion
        
    def SetApellido(self,apellido):
        "Establecer el Apellido del Cliente"
        self.__apellido = apellido
        
    def SetNombre(self,nombre):
        "Establecer el Nombre del Cliente"        
        self.__nombre = nombre
        
    def SetDni(self,dni):
        "Establecer el DNI del Cliente"
        self.__dni = dni
        
    def SetTelefono(self,telefono):
        "Establecer el Telefono del Cliente"
        self.__telefono = telefono
    
    def SetDireccion(self,direccion):
        "Establecer el Direccion del Cliente"
        self.__direccion = direccion