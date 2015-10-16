# -*- coding: utf-8 -*-

class Cliente():
    "Crear nuevo cliente"
    
    def __init__(self,Apellido,Nombre,DNI,Telefono,Direccion):
       
       self.__apellido = Apellido
       self.__nombre = Nombre
       self.__dni = DNI 
       self.__telefono = Telefono
       self.__direccion = Direccion
       
    def get_Apellido(self):
        "Retorna el Apellido del Cliente"
        return self.__apellido
        
    def get_Nombre(self):
        "Retorna el Nombre del Cliente"        
        return self.__nombre
    
    def get_Dni(self):
        "Retorna el DNI del Cliente"
        return self.__dni
    
    def get_Telefono(self):
        "Retorna el Telefono del Cliente"
        return self.__telefono
        
    def get_Direccion(self):
        "Retorna el Direccion del Cliente"
        return self.__direccion
        
    def set_Apellido(self,apellido):
        "Establecer el Apellido del Cliente"
        self.__apellido = apellido
        
    def set_Nombre(self,nombre):
        "Establecer el Nombre del Cliente"        
        self.__nombre = nombre
        
    def set_Dni(self,dni):
        "Establecer el DNI del Cliente"
        self.__dni = dni
        
    def set_Telefono(self,telefono):
        "Establecer el Telefono del Cliente"
        self.__telefono = telefono
    
    def set_Direccion(self,direccion):
        "Establecer el Direccion del Cliente"
        self.__direccion = direccion