# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtFormConfiguracion import Ui_FormConfiguracion
from Funciones import Funciones
from Interfaz.PyFormAltaEspacio import FormAltaEspacio
from Interfaz.PyMsgBox import MsgBox
from Interfaz.PyMsgBoxConfirm import MsgBoxConfirm

class FormConfiguracion(QtGui.QDialog, Ui_FormConfiguracion):
    def __init__(self, direccion, espacios, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setResult(0)
        self.lineEdit_Direccion.setEnabled(False)
        self.__direccion = direccion
        self.__espacios = espacios
        for espacio in self.__espacios:
            self.combo_Espacios.addItem(espacio, espacio)
        self.lineEdit_Direccion.setText(self.__direccion)
        self.pb_Add.clicked.connect(self.add_Espacio)
        self.pb_Remove.clicked.connect(self.remove_Espacio)
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        
    def add_Espacio(self):
        form = FormAltaEspacio()
        form.exec_()
        if (form.get_Espacio()!=None):
            self.__espacios.append(form.get_Espacio())
            self.combo_Espacios.addItem(form.get_Espacio(), form.get_Espacio())
            
    def remove_Espacio(self):
        msg = MsgBoxConfirm()
        msg.set_Text("¿Seguro elimina el Espacio?")
        msg.set_Title("Confirmar")
        if(msg.exec_()==1):        
            self.__espacios.remove(self.combo_Espacios.itemData(self.combo_Espacios.currentIndex()))   
            self.combo_Espacios.removeItem(self.combo_Espacios.currentIndex())
    
    def pb_Aceptar_Clicked(self):
        valid = Funciones.validar_configuracion(self.lineEdit_Direccion.text().strip(), self.combo_Espacios)
        msgbox = MsgBox()        
        if (valid[0]):
            self.__direccion = self.lineEdit_Direccion.text().strip().title()
            self.__espacios = Funciones.get_combo_items(self.combo_Espacios)
            msgbox.set_Text("Cambios Guardados")
            msgbox.set_Title("Informacion")
            msgbox.exec_()  
            self.close()
            self.setResult(1)
        else:
            msgbox.set_Title("Error")
            msgbox.set_Text(valid[1]) 
            msgbox.exec_()
            
    def get_Direccion(self):
        return self.__direccion
        
    def get_Espacios(self):
        return self.__espacios
        
    def get_Result(self):
        return self.result()
        
    
