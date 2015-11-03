# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Entidad.Paseo import Paseo
from Interfaz.QtFormAltaPaseo import Ui_Form_Alta_Paseo
from Funciones import Funciones
from Interfaz.PyMsgBox import MsgBox

class FormAltaPaseo(QtGui.QDialog, Ui_Form_Alta_Paseo):
    def __init__(self, paseos, paseadores, mascotas, espacios, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setResult(0)
        self.__espacios = espacios
        self.__mascotas = mascotas
        self.__paseos = paseos
        self.__paseo = None
        self.__paseadores = paseadores
        self.__paseadores_object = self.__paseadores.values()
        for espacio in self.__espacios:
            self.combo_Espacios.addItem(espacio, espacio)
        for p in self.__paseadores_object:
            if ((len(Funciones.get_mascotas_paseador(self.__mascotas, p)))>0):
                self.combo_Paseadores.addItem(p.get_Nombre(), p.get_Dni())
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
   
    def pb_Aceptar_Clicked(self):
        paseador = Funciones.get_paseador(self.__paseadores, self.combo_Paseadores.itemData(self.combo_Paseadores.currentIndex()))
        paseo = Paseo(paseador.get_Dni(), self.spinBox_Horas.value(), self.spinBox_Minutos.value(), self.combo_Espacios.itemData(self.combo_Espacios.currentIndex()))  
        valid = Funciones.validar_paseo(self.__paseos, paseo) 
        msgbox = MsgBox()         
        if (valid[0]):
            msgbox.set_Text("Paseo Registrado")
            msgbox.set_Title("Informacion")
            msgbox.exec_()            
            self.__paseo = paseo
            self.close()
            self.setResult(1)
        else:
            msgbox.set_Title("Error")
            msgbox.set_Text(valid[1]) 
            msgbox.exec_()
            
    def get_Paseo(self):
        return self.__paseo