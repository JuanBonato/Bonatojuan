# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtGui import QTableWidgetItem
from Entidad.Url import Url
from Interfaz.QtMainWindow import Ui_MainWindow
from Interfaz.PyFormAltaCliente import FormAltaCliente
from Interfaz.PyFormAltaPaseador import FormAltaPaseador
from Interfaz.PyFormAltaMascota import FormAltaMascota
from Interfaz.PyFormAltaPaseo import FormAltaPaseo
from Interfaz.PyTableClientes import TableClientes
from Interfaz.PyTablePaseadores import TablePaseadores
from Interfaz.PyTableMascotas import TableMascotas
from Interfaz.PyMsgBoxConfirm import MsgBoxConfirm
from Interfaz.PyWebView import WebView
from Interfaz.PyFormConfiguracion import FormConfiguracion
from Funciones import Funciones
import time

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.clientes = Funciones.crear_lista_cliente()
        self.paseadores = Funciones.crear_lista_paseadores()
        self.mascotas = Funciones.crear_lista_mascota()
        self.paseos_activos = {}
        self.paseos_historial = []
        self.espacios = []
        self.direccion = "9 de Julio 50 Concepcion del Uruguay"
        self.actionAltaCliente.triggered.connect(self.alta_Cliente)
        self.actionAltaMascota.triggered.connect(self.alta_Mascota)
        self.actionAltaPaseador.triggered.connect(self.alta_Paseador)
        self.actionListadoCliente.triggered.connect(self.listado_Clientes)
        self.actionListadoPaseador.triggered.connect(self.listado_Paseadores)        
        self.actionListadoMascota.triggered.connect(self.listado_Mascotas)        
        self.actionConfiguracion.triggered.connect(self.configuracion)        
        self.pb_Salida.clicked.connect(self.alta_Paseo)
        self.pb_Arribo.clicked.connect(self.registro_Arribo)
        self.tab_Paseos.currentChanged.connect(self.tab_Change)
        self.table_Activos.cellDoubleClicked.connect(self.show_Map)

    def configuracion(self):
        form = FormConfiguracion(self.direccion, self.espacios)
        if (form.exec_()==1):
            self.direccion = form.get_Direccion()
            self.espacios = form.get_Espacios()
    
    def alta_Cliente(self):
        form = FormAltaCliente(self.clientes, self.paseadores, self.mascotas)
        form.exec_()
        if (form.get_Cliente()!=None):
            self.clientes = Funciones.add_cliente(self.clientes, form.get_Cliente())
            self.mascotas.update(form.get_Mascotas())
        
    def alta_Mascota(self):
        form = FormAltaMascota(self.mascotas, self.paseadores, self.clientes)
        form.exec_()        
        if (form.get_Mascota()!=None):
            self.mascotas = Funciones.add_mascota(self.mascotas, form.get_Mascota())        
        
    def alta_Paseador(self):
        form = FormAltaPaseador(self.paseadores)
        form.exec_()
        if (form.get_Paseador()!=None):
            self.paseadores = Funciones.add_paseador(self.paseadores, form.get_Paseador())
        
    def alta_Paseo(self):
        form = FormAltaPaseo(self.paseos_activos, self.paseadores, self.mascotas, self.espacios)
        if (form.exec_()==1):
            self.paseos_activos[form.get_Paseo().get_Paseador()] = form.get_Paseo()
            self.update_Table_Activos(self.paseos_activos.values())
            
    def listado_Clientes(self):
        tabla = TableClientes(self.clientes, self.mascotas, self.paseadores)
        tabla.exec_()
        self.clientes.update(tabla.get_Clientes())
        
    def listado_Paseadores(self):
        tabla = TablePaseadores(self.paseadores, self.clientes, self.mascotas)
        tabla.exec_()
        self.clientes.update(tabla.get_Paseadores())
        
    def listado_Mascotas(self):
        tabla = TableMascotas(self.mascotas, self.clientes, self.paseadores)
        tabla.exec_()
        
    def registro_Arribo(self):
        self.table_Activos.setCurrentCell(self.table_Activos.currentRow(), 3)
        item = self.table_Activos.currentItem()
        if(item!=None):
            paseo = Funciones.get_paseo(self.paseos_activos, int(item.text().strip()))
            msg_confirm = MsgBoxConfirm()
            msg_confirm.set_Text("¿Registra el arribo del paseador?")
            msg_confirm.set_Title("Confirmar")
            msg_confirm.exec_()
            if (msg_confirm.get_Result()==1):
                self.paseos_activos[paseo.get_Paseador()].set_Arribo(time.strftime("%H:%M:%S"))
                self.paseos_historial.append(self.paseos_activos.pop(paseo.get_Paseador()))
                self.update_Table_Activos(self.paseos_activos.values())
                self.update_Table_Historial(self.paseos_historial)
        
    def update_Table_Activos(self,paseos):
        self.table_Activos.setColumnHidden(3,False)
        for i in range(0,self.table_Activos.rowCount()):
            self.table_Activos.removeRow(i)
        self.table_Activos.setRowCount(0)        
        for paseo in paseos:
            salida = str(paseo.get_Salida().hour) + ":" + str(paseo.get_Salida().minute) + ":" + str(paseo.get_Salida().second)
            tentativo = str(paseo.get_Tentativo().hour) + ":" + str(paseo.get_Tentativo().minute) + ":" + str(paseo.get_Tentativo().second)
            codigo = str(paseo.get_Paseador())
            paseador = Funciones.get_paseador(self.paseadores, paseo.get_Paseador())
            itemSalida = QTableWidgetItem(salida)
            itemTentativo = QTableWidgetItem(tentativo)
            itemCodigo = QTableWidgetItem(codigo)
            itemPaseador = QTableWidgetItem(paseador.get_Nombre())
            rowCount = self.table_Activos.rowCount()
            self.table_Activos.insertRow(rowCount)
            self.table_Activos.setItem(rowCount,0,itemSalida)
            self.table_Activos.setItem(rowCount,1,itemTentativo) 
            self.table_Activos.setItem(rowCount,2,itemPaseador)
            self.table_Activos.setItem(rowCount,3,itemCodigo)
        self.table_Activos.resizeColumnsToContents()
        self.table_Activos.setColumnHidden(3,True)
        self.table_Activos.horizontalHeader().setStretchLastSection(True) 

    def update_Table_Historial(self,paseos):
        self.table_Historial.setColumnHidden(4,False)
        for i in range(0,self.table_Historial.rowCount()):
            self.table_Historial.removeRow(i)
        self.table_Historial.setRowCount(0)        
        for paseo in paseos:
            salida = str(paseo.get_Salida().hour) + ":" + str(paseo.get_Salida().minute) + ":" + str(paseo.get_Salida().second)
            print(salida,type(salida))            
            arribo = paseo.get_Arribo()
            fecha = paseo.get_Fecha()
            codigo = str(paseo.get_Paseador())
            paseador = Funciones.get_paseador(self.paseadores, paseo.get_Paseador())
            itemSalida = QTableWidgetItem(salida)
            itemArribo = QTableWidgetItem(arribo)
            itemCodigo = QTableWidgetItem(codigo)
            itemPaseador = QTableWidgetItem(paseador.get_Nombre())
            itemFecha = QTableWidgetItem(fecha)
            rowCount = self.table_Historial.rowCount()
            self.table_Historial.insertRow(rowCount)
            self.table_Historial.setItem(rowCount,0,itemFecha)
            self.table_Historial.setItem(rowCount,1,itemSalida) 
            self.table_Historial.setItem(rowCount,2,itemArribo)
            self.table_Historial.setItem(rowCount,3,itemPaseador)
            self.table_Historial.setItem(rowCount,4,itemCodigo)
        self.table_Historial.resizeColumnsToContents()
        self.table_Historial.setColumnHidden(4,True)
        self.table_Historial.horizontalHeader().setStretchLastSection(True)           
            
    def show_Map(self):
        self.table_Activos.setCurrentCell(self.table_Activos.currentRow(), 3)
        item = self.table_Activos.currentItem()
        paseo = Funciones.get_paseo(self.paseos_activos, int(item.text().strip()))
        if(item!=None):
            mapa = WebView(Url(self.direccion, Funciones.get_recorrido(self.direccion, paseo.get_Espacio(), self.mascotas,self.clientes, int(item.text().strip())), "14"))
            mapa.exec_()
            
    def tab_Change(self):
        self.pb_Arribo.setEnabled(self.tab_Paseos.currentIndex()!=1) 
        self.pb_Salida.setEnabled(self.tab_Paseos.currentIndex()!=1)
