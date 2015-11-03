# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from Entidad.Paseador import Paseador
from Interfaz.QtFormAltaPaseador import Ui_Form_Alta_Paseador
from Funciones import Funciones
from Interfaz.PyMsgBox import MsgBox

class FormAltaPaseador(QtGui.QDialog, Ui_Form_Alta_Paseador):
    def __init__(self, paseadores, paseador = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__paseadores = paseadores
        self.__paseador = paseador
        if (paseador!=None):
            self.lineEdit_Nombre.setText(paseador.get_Nombre())
            self.lineEdit_Apellido.setText(paseador.get_Apellido())
            self.lineEdit_DNI.setText(str(paseador.get_Dni()))
            self.lineEdit_Telefono.setText(str(paseador.get_Telefono()))
            self.lineEdit_DNI.setEnabled(False)
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        
    def pb_Aceptar_Clicked(self):
        p = Paseador(self.lineEdit_Apellido.text().strip().title(), self.lineEdit_Nombre.text().strip().title(), self.lineEdit_DNI.text().strip(), self.lineEdit_Telefono.text().strip())
        msgbox = MsgBox() 
        valid = Funciones.validar_paseador(self.__paseadores, p, (self.__paseador!=None))
        if (valid[0]):
            msgbox.set_Text("Paseador Registrado")
            msgbox.setWindowTitle("Informacion")
            msgbox.exec_()
            self.__paseador = Funciones.format_paseador(p)
            self.close()
        else:
            msgbox.set_Title("Error")
            msgbox.set_Text(valid[1]) 
            msgbox.exec_()
            
    def get_Paseador(self):
        return self.__paseador