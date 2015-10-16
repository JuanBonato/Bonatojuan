# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtFormAltaCliente import Ui_Form_Alta_Cliente

class FormAltaCliente(QtGui.QDialog, Ui_Form_Alta_Cliente):
    def __init__(self, cliente = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.cliente = cliente
        if (self.cliente!=None):
            self.lineEdit_Nombre.setText(cliente.get_Nombre())
            self.lineEdit_Apellido.setText(cliente.get_Apellido())
            self.lineEdit_Direccion.setText(cliente.get_Direccion)
            self.lineEdit_DNI.setText(cliente.get_Dni)
            self.lineEdit_Telefono.setText(cliente.get_Telefono)
        
            
