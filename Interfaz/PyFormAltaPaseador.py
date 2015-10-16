# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from QtFormAltaPaseador import Ui_Form_Alta_Paseador

class FormAltaCliente(QtGui.QDialog, Ui_Form_Alta_Paseador):
    def __init__(self, paseador = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.paseador = paseador
        if (self.cliente!=None):
            self.lineEdit_Nombre.setText(paseador.get_Nombre())
            self.lineEdit_Apellido.setText(paseador.get_Apellido())
            self.lineEdit_DNI.setText(paseador.get_Dni)
            self.lineEdit_Telefono.setText(paseador.get_Telefono)