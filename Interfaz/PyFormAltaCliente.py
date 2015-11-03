# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Entidad.Cliente import Cliente
from Interfaz.QtFormAltaCliente import Ui_Form_Alta_Cliente
from Funciones import Funciones
from Interfaz.PyMsgBox import MsgBox
from Interfaz.PyFormAltaMascota import FormAltaMascota

class FormAltaCliente(QtGui.QDialog, Ui_Form_Alta_Cliente):
    def __init__(self, clientes, paseadores, mascotas, cliente = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__cliente = cliente
        self.__clientes = clientes
        self.__paseadores = paseadores
        self.__mascotas = mascotas
        self.__mascotas_alta = []
        if (self.__cliente!=None):
            self.lineEdit_Nombre.setText(cliente.get_Nombre())
            self.lineEdit_Apellido.setText(cliente.get_Apellido())
            self.lineEdit_Direccion.setText(cliente.get_Direccion())
            self.lineEdit_DNI.setText(str(cliente.get_Dni()))
            self.lineEdit_Telefono.setText(str(cliente.get_Telefono()))
            self.lineEdit_DNI.setEnabled(False)
            dic_mascotas_cliente = Funciones.get_mascotas_cliente(self.__mascotas, self.__cliente)
            list_mascotas_cliente = dic_mascotas_cliente.values()            
            for value in list_mascotas_cliente:            
                self.combo_Mascotas.addItem(value.get_Nombre(), value.get_Codigo())
            self.combo_Mascotas.setEnabled(True)
            self.pb_Add_Mascota.setEnabled(True)
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        self.pb_Add_Mascota.clicked.connect(self.pb_Add_Mascota_Clicked)
        self.lineEdit_DNI.editingFinished.connect(self.enable_Combo)
        
    def enable_Combo(self):
        self.combo_Mascotas.setEnabled(self.lineEdit_DNI.text().strip()!="")
        self.pb_Add_Mascota.setEnabled(self.lineEdit_DNI.text().strip()!="")
        
    def pb_Add_Mascota_Clicked(self):
        c = Cliente( self.lineEdit_Apellido.text().strip().title(), self.lineEdit_Nombre.text().strip().title(), self.lineEdit_DNI.text().strip(), self.lineEdit_Telefono.text().strip(), self.lineEdit_Direccion.text().strip().title()+" Concepcion del Uruguay")        
        form = FormAltaMascota(self.__mascotas, self.__paseadores, self.__clientes, c)
        form.exec_()
        if (form.get_Mascota!=None):
            m = form.get_Mascota()
            self.__mascotas_alta.append(m.get_Codigo())
            self.__mascotas[m.get_Codigo()] = m
            self.combo_Mascotas.addItem(m.get_Nombre(), m.get_Codigo())  
            
    def pb_Aceptar_Clicked(self):
        c = Cliente( self.lineEdit_Apellido.text().strip().title(), self.lineEdit_Nombre.text().strip().title(), self.lineEdit_DNI.text().strip(), self.lineEdit_Telefono.text().strip(), self.lineEdit_Direccion.text().strip().title())
        msgbox = MsgBox()   
        valid = Funciones.validar_cliente(self.__clientes, c, self.combo_Mascotas, self.__cliente!=None)
        if (valid[0]):
            msgbox.set_Text("Cliente Registrado")
            msgbox.setWindowTitle("Informacion")
            msgbox.exec_()
            self.__cliente = Funciones.format_cliente(c)
            self.__mascotas = Funciones.set_cliente(self.__mascotas, self.__mascotas_alta, self.__cliente)
            self.close()
            
        else:
            msgbox.set_Title("Error")
            msgbox.set_Text(valid[1]) 
            msgbox.exec_()
            
    def get_Cliente(self):
        return self.__cliente

    def get_Mascotas(self):
        return self.__mascotas
