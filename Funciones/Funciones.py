from Entidad.Cliente import Cliente
from Entidad.Mascota import Mascota
from Entidad.Paseador import Paseador
from PyQt4 import QtGui
import random

def crear_lista_cliente():
    lcnombre = ["Pedro","Walter Fabian","Alberto","Francisco","Juan Martín","Roberto","Gonzalo","Damian Emanuel","Brian Andrés","Justo José"]
    lcapellido = ["Castillo","Fernandez","Martinez","Palermo","Montillo","Carballo","Castelar","Rasello","Mendez","Días"]
    lctelefono = [3442523123,3445632661,34474392176,3442499888,3445657999,3447090998,3442439876,3445698000,3447512345,3442691929]
    lcdireccion = ["9 de Julio 1098","Galarza 967","Ameghino 459","Artigas 765","Juan Perón 209","San Martín 499","Moreno 1743","Rocamora 333","14 de julio 287","Combatiente de Malvinas 1044"]
    lcdni = [30987123,29345654,30987678,25616263,32234985,35458765,28675432,31009800,34010199,30011911]
    dic_clientes = {}    
    for i in range(0,10):
        cliente = Cliente(lcapellido[i],lcnombre[i],lcdni[i],lctelefono[i],lcdireccion[i]+" Concepcion del Uruguay")
        dic_clientes[cliente.get_Dni()] = cliente
    return dic_clientes

def crear_lista_paseadores():
    lpnombre = ["Mario","Nestor","Ricardo","Juan Manuel","Franco","Esteban","Federico","Nicolás","Eduardo","Ramón","Carlos"]
    lpapellido = ["Leto","Kloster","Postiga","Villanova","Taborda","Ambrosioni","Prin","Sito","Mercier","Pantera","Rodriguez"]
    lptelefono = [3442429486,34456981267,3447919592,3442901080,3445433747,3447999000,3442413233,34456910007,3447421900,3442612121]
    lpdni = [30777123,32657812,28789234,26413678,35879012,31212987,28796325,37512318,28791214,30912345]
    dic_paseadores = {}
    for i in range(0,10):
        paseador = Paseador(lpapellido[i],lpnombre[i],lpdni[i],lptelefono[i])
        dic_paseadores[paseador.get_Dni()] = paseador
    return dic_paseadores

def crear_lista_mascota():
    lmnombre = ["Platon","Budy","Roki","Terry","Pichi","Tacho","Luna","Laika","Toby","Miki"]
    lmraza = ["Golden","Labrador","Pastor Alemán","San Bernardo","Boxer","Rottweiler","Dálmata","Doberman","Rottweiler",""]
    lmpeso = [54,49,51,45,31,55,29,49,47,50]
    dic_mascotas = {}
    lpdni = [30777123,32657812,28789234,26413678,35879012,31212987,28796325,37512318,28791214,30912345]
    lcdni = [30987123,29345654,30987678,25616263,32234985,35458765,28675432,31009800,34010199,30011911]
    for i in range(0,10):
        mascota = Mascota(lmnombre[i],lmraza[i],lmpeso[i],random.choice(lcdni),random.choice(lpdni),i)
        dic_mascotas[mascota.get_Codigo()] = mascota
    return dic_mascotas

def select_paseador(paseadores):
    aux = paseadores.keys()    
    dni = []
    for key in aux:
        dni.append(key)
    return (random.choice(dni))

def get_paseador(paseadores, dni):
    return paseadores.get(dni)
    
def get_cliente(clientes, dni):
    return clientes.get(dni)
    
def get_mascota(mascotas, codigo):
    return mascotas.get(codigo)
    
def get_paseo(paseos, codigo):
    return paseos.get(codigo)
    
def format_cliente(cliente):
    cliente.set_Dni(int(cliente.get_Dni()))
    cliente.set_Telefono(int(cliente.get_Telefono()))
    return cliente
    
def format_paseador(paseador):
    paseador.set_Dni(int(paseador.get_Dni()))
    paseador.set_Telefono(int(paseador.get_Dni()))
    return paseador
    
def validar_telefono(telefono):
    valid = True    
    try :
        int(telefono)
    except(ValueError):
        valid = False
    return valid
    
def validar_dni_cliente(clientes, dni):
    valid = True  
    if (len(dni)==8):
        try:
            dni = int(dni)
            if (dni in clientes):
                valid = False
        except (ValueError):
            valid = False
    else:
        valid = False
    return valid

def validar_dni_paseador(paseadores, dni):
    valid = True    
    if (len(dni)==8):
        try:
            dni = int(dni)
            if (dni in paseadores):
                valid = False
        except (ValueError):
            valid = False
    else:
        valid = False
    return valid

def validar_cliente(clientes, cliente, mascotas, modif):
    valid = True
    error = None
    if (not(validar_dni_cliente(clientes, cliente.get_Dni())) and (not(modif))):
        valid = False
        error = "Cliente Existente"
    elif (not(validar_telefono(cliente.get_Telefono()))):
        valid = False
        error = "Telefono Incorrecto"
    elif (cliente.get_Nombre()=="") or (cliente.get_Apellido()=="") or (cliente.get_Direccion()==""):
        valid = False
        error = "Todos los campos son Obligatorios"
    elif (mascotas.itemData(mascotas.currentIndex()) == None):
        valid = False
        error = "Debe tener al menos 1 mascota"
    return valid,error

def validar_mascota(mascota, clientes):
    valid = True
    error = None
    if (mascota.get_Peso()==0) or (mascota.get_Nombre()=="") or (mascota.get_Raza()==""):
        valid = False
        error = "Todos los campos son obligatorios"
    elif (clientes.itemData(clientes.currentIndex()) == None):
        valid = False
        error = "La mascota debe tener duenio"
    return valid, error
    
def validar_paseador(paseadores, paseador, modif):
    valid = True
    error = None
    if (not(validar_dni_paseador(paseadores, paseador.get_Dni())) and (not(modif))):
        valid = False
        error = "Paseador Existente"
    elif (not(validar_telefono(paseador.get_Telefono()))):
        valid = False
        error = "Telefono Incorrecto"
    elif (paseador.get_Nombre()=="") or (paseador.get_Apellido()==""):
        valid = False
        error = "Todos los campos son Obligatorios"
    return valid,error

def validar_paseo(paseos, paseo):
    valid = True
    error = None
    paseador = paseos.get(paseo.get_Paseador())
    if (paseador!=None):
        valid = False
        error = "El paseador ya se encuentra Activo"
    elif (paseo.get_Tentativo() == paseo.get_Salida()):
        valid = False
        error = "Todos los campos son obligatorios"
    return valid, error

def get_mascotas_cliente(mascotas, cliente):
    dic = {}
    aux = mascotas.values()
    for mascota in aux:
        if (mascota.get_Dni_Duenio()==cliente.get_Dni()):
            dic[mascota.get_Codigo()] = mascota
    return dic
    
def get_mascotas_paseador(mascotas, paseador):
    dic = {}
    aux = mascotas.values()
    for mascota in aux:
        if (mascota.get_Dni_Paseador()==paseador.get_Dni()):
            dic[mascota.get_Codigo()] = mascota
    return dic
    
def set_cliente(mascotas, mascotas_alta, cliente):
    for mascota in mascotas_alta:
        mascotas[mascota].set_Dni_Duenio(cliente.get_Dni())
    return mascotas
    
def add_cliente(clientes, cliente):
    clientes[cliente.get_Dni()] = cliente  
    return clientes
    
def add_paseador(paseadores, paseador):
    paseadores[paseador.get_Dni()] = paseador 
    return paseadores
    
def add_mascota(mascotas, mascota):
    mascotas[mascota.get_Codigo()] = mascota 
    return mascotas    
    
def add_paseo(paseos, paseo):
    paseos[paseo.get_Paseador()] = paseo
    return paseos

def get_recorrido(agencia, espacio, dic_mascotas,dic_clientes,paseador):
    recorrido = [agencia]
    mascotas = dic_mascotas.values()
    for m in mascotas:
        if (m.get_Dni_Paseador()==paseador):
            recorrido.append(dic_clientes[m.get_Dni_Duenio()].get_Direccion())
    a = "|"
    recorrido.append(espacio)
    a = a.join(recorrido)
    return a
    
def validar_espacio(espacio):
    valid = True
    error = ""
    if (espacio == ""):
        valid = False
        error = "Debe completar el campo Direccion"
    return valid, error
    
def validar_configuracion(direccion, espacios):
    valid = True
    error = ""
    if (direccion == ""):
        valid = False
    elif (espacios.itemData(espacios.currentIndex()) == None):
        valid = False
        error = "Debe haber al menos 1 espacio verde"
    return valid, error
    
def get_combo_items(combo):
    i = 0
    items = []
    count = combo.count()
    for i in range(0,(count)):
        combo.setCurrentIndex(i)
        items.append(combo.itemData(combo.currentIndex()))
    return items
        
    
    
    
    
    
    
