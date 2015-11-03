# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtFormAltaEspacio import Ui_FormAltaEspacio
from Funciones import Funciones
from Interfaz.PyMsgBox import MsgBox

class FormAltaEspacio(QtGui.QDialog, Ui_FormAltaEspacio):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        self.__espacio = None

    def pb_Aceptar_Clicked(self):
        valid = Funciones.validar_espacio(self.lineEdit_Direccion.text().strip())
        msg = MsgBox()
        if (valid[0]):
            self.__espacio = self.lineEdit_Direccion.text().strip().title()
            msg.set_Title("Informacion")
            msg.set_Text("Espacio Registrado")
            msg.exec_()
            self.close()
        else:
            msg.set_Title("Error")
            msg.set_Text(valid[1])      
            msg.exec_()
            
    def get_Espacio(self):
        return self.__espacio
    
                
    

