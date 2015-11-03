# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtTableClientes import Ui_Listado_Clientes
from Interfaz.PyTableMascotas import TableMascotas
from Interfaz.PyFormAltaCliente import FormAltaCliente
from PyQt4.QtGui import QTableWidgetItem
from Funciones import Funciones

class TableClientes(QtGui.QDialog, Ui_Listado_Clientes):
    def __init__(self, clientes, mascotas, paseadores, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__clientes = clientes
        self.__mascotas = mascotas
        self.__paseadores = paseadores
        self.__clientes_objects = self.__clientes.values()
        self.update_Table()
        self.table_Clientes.cellDoubleClicked.connect(self.edit_Triggered)
        self.pb_Mascotas.clicked.connect(self.pb_Mascotas_Clicked)        
        
    def update_Table(self):
        self.table_Clientes.setRowCount(0)   
        for cliente in self.__clientes_objects:
            nombre = cliente.get_Nombre()
            apellido = cliente.get_Apellido()
            dni = str(cliente.get_Dni())
            telefono = str(cliente.get_Telefono())
            direccion = cliente.get_Direccion()            
            item_nombre = QTableWidgetItem(nombre)
            item_apellido = QTableWidgetItem(apellido)
            item_dni = QTableWidgetItem(dni)
            item_telefono = QTableWidgetItem(telefono)
            item_direccion = QTableWidgetItem(direccion)
            rowCount = self.table_Clientes.rowCount()
            self.table_Clientes.insertRow(rowCount)
            self.table_Clientes.setItem(rowCount,0,item_nombre)
            self.table_Clientes.setItem(rowCount,1,item_apellido) 
            self.table_Clientes.setItem(rowCount,2,item_dni)
            self.table_Clientes.setItem(rowCount,3,item_telefono)
            self.table_Clientes.setItem(rowCount,4,item_direccion)
        self.table_Clientes.resizeColumnsToContents()
        self.table_Clientes.horizontalHeader().setStretchLastSection(True)
        
    def pb_Mascotas_Clicked(self):
        self.table_Clientes.setCurrentCell(self.table_Clientes.currentRow(), 2)
        item = self.table_Clientes.currentItem()
        cliente = Funciones.get_cliente(self.__clientes, int(item.text().strip()))        
        mascotas_cliente = Funciones.get_mascotas_cliente(self.__mascotas, cliente)
        table_mascotas = TableMascotas(mascotas_cliente, self.__clientes, self.__paseadores)
        table_mascotas.exec_()
        
    def edit_Triggered(self):
        self.table_Clientes.setCurrentCell(self.table_Clientes.currentRow(), 2)
        item = self.table_Clientes.currentItem()
        cliente = Funciones.get_cliente(self.__clientes, int(item.text().strip()))
        form = FormAltaCliente(self.__clientes, self.__paseadores, self.__mascotas, cliente)
        form.exec_()
        if (form.get_Cliente()!=None):
            self.__clientes = Funciones.add_cliente(self.__clientes, form.get_Cliente())
            self.update_Table()
            
    def get_Clientes(self):
        return self.__clientes
        
        
        
        
        
        
        
        
        
        
        
        