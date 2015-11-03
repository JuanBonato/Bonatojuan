# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtTableMascotas import Ui_Listado_Mascotas
from PyQt4.QtGui import QTableWidgetItem
from Funciones import Funciones
from Interfaz.PyFormAltaMascota import FormAltaMascota

class TableMascotas(QtGui.QDialog, Ui_Listado_Mascotas):
    def __init__(self, mascotas, clientes, paseadores, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__mascotas = mascotas
        self.__clientes = clientes
        self.__paseadores = paseadores
        self.__mascotas_objects = self.__mascotas.values()
        self.update_Table()
        self.table_Mascotas.cellDoubleClicked.connect(self.edit_Triggered)
        
    def update_Table(self):
        self.table_Mascotas.setRowCount(0) 
        self.table_Mascotas.setColumnHidden(5,False)
        for mascota in self.__mascotas_objects:
            nombre = mascota.get_Nombre()
            raza = mascota.get_Raza()
            peso = str(mascota.get_Peso())
            duenio = Funciones.get_cliente(self.__clientes, mascota.get_Dni_Duenio())
            nombre_duenio = duenio.get_Nombre()
            paseador = Funciones.get_paseador(self.__paseadores, mascota.get_Dni_Paseador())         
            nombre_paseador = paseador.get_Nombre()  
            codigo = str(mascota.get_Codigo())
            item_nombre = QTableWidgetItem(nombre)
            item_raza = QTableWidgetItem(raza)
            item_peso = QTableWidgetItem(peso)
            item_duenio = QTableWidgetItem(nombre_duenio)
            item_paseador = QTableWidgetItem(nombre_paseador)
            item_codigo = QTableWidgetItem(codigo)
            rowCount = self.table_Mascotas.rowCount()
            self.table_Mascotas.insertRow(rowCount)
            self.table_Mascotas.setItem(rowCount,0,item_nombre)
            self.table_Mascotas.setItem(rowCount,1,item_raza) 
            self.table_Mascotas.setItem(rowCount,2,item_peso)
            self.table_Mascotas.setItem(rowCount,3,item_duenio)
            self.table_Mascotas.setItem(rowCount,4,item_paseador)
            self.table_Mascotas.setItem(rowCount,5,item_codigo)
        self.table_Mascotas.resizeColumnsToContents()
        self.table_Mascotas.setColumnHidden(5,True)
        self.table_Mascotas.horizontalHeader().setStretchLastSection(True)
        
    def edit_Triggered(self):
        self.table_Mascotas.setCurrentCell(self.table_Mascotas.currentRow(), 5)
        item = self.table_Mascotas.currentItem()
        mascota = Funciones.get_mascota(self.__mascotas, int(item.text().strip()))
        form = FormAltaMascota(self.__mascotas, self.__paseadores, self.__clientes, None, mascota)
        form.exec_()
        if (form.get_Mascota()!=None):
            self.__mascotas = Funciones.add_mascota(self.__mascotas, form.get_Mascota())
            self.update_Table()
            
    def get_Mascotas(self):
        return self.__mascotas
