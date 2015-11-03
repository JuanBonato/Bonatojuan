# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtTablePaseadores import Ui_Listado_Paseadores
from PyQt4.QtGui import QTableWidgetItem
from Funciones import Funciones
from Interfaz.PyTableMascotas import TableMascotas
from Interfaz.PyFormAltaPaseador import FormAltaPaseador

class TablePaseadores(QtGui.QDialog, Ui_Listado_Paseadores):
    def __init__(self, paseadores, clientes, mascotas, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__paseadores = paseadores
        self.__clientes = clientes
        self.__mascotas = mascotas  
        self.__paseadores_objects = self.__paseadores.values()
        self.update_Table()
        self.pb_Mascotas.clicked.connect(self.pb_Mascotas_Clicked)
        self.table_Paseadores.cellDoubleClicked.connect(self.edit_Triggered)
        
    def update_Table(self):
        self.table_Paseadores.setRowCount(0)    
        for paseador in self.__paseadores_objects:
            nombre = paseador.get_Nombre()
            apellido = paseador.get_Apellido()
            dni = str(paseador.get_Dni())
            telefono = str(paseador.get_Telefono())
            item_nombre = QTableWidgetItem(nombre)
            item_apellido = QTableWidgetItem(apellido)
            item_dni = QTableWidgetItem(dni)
            item_telefono = QTableWidgetItem(telefono)
            rowCount = self.table_Paseadores.rowCount()
            self.table_Paseadores.insertRow(rowCount)
            self.table_Paseadores.setItem(rowCount,0,item_nombre)
            self.table_Paseadores.setItem(rowCount,1,item_apellido) 
            self.table_Paseadores.setItem(rowCount,2,item_dni)
            self.table_Paseadores.setItem(rowCount,3,item_telefono)
        self.table_Paseadores.resizeColumnsToContents()
        self.table_Paseadores.horizontalHeader().setStretchLastSection(True)
        
    def pb_Mascotas_Clicked(self):
        self.table_Paseadores.setCurrentCell(self.table_Paseadores.currentRow(), 2)
        item = self.table_Paseadores.currentItem()
        paseador = Funciones.get_paseador(self.__paseadores, int(item.text().strip()))        
        mascotas_paseador = Funciones.get_mascotas_paseador(self.__mascotas, paseador)
        table_mascotas = TableMascotas(mascotas_paseador, self.__clientes, self.__paseadores)
        table_mascotas.exec_()
        
    def edit_Triggered(self):
        self.table_Paseadores.setCurrentCell(self.table_Paseadores.currentRow(), 2)
        item = self.table_Paseadores.currentItem()
        paseador = Funciones.get_paseador(self.__paseadores, int(item.text().strip()))
        form = FormAltaPaseador(self.__paseadores, paseador)
        form.exec_()
        if (form.get_Paseador()!=None):
            self.__paseadores = Funciones.add_paseador(self.__paseadores, form.get_Paseador())
            self.update_Table()
            
    def get_Paseadores(self):
        return self.__paseadores
