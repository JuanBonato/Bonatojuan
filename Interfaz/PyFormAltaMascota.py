# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Entidad.Mascota import Mascota
from Interfaz.QtFormAltaMascota import Ui_Form_Alta_Mascota
from Funciones import Funciones
from Interfaz.PyMsgBox import MsgBox

class FormAltaMascota(QtGui.QDialog, Ui_Form_Alta_Mascota):
    def __init__(self, mascotas, paseadores, clientes, cliente = None, mascota = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__paseadores = paseadores
        self.__clientes = clientes
        self.__mascotas = mascotas
        self.__cliente = cliente
        self.__mascota = mascota
        self.__clientes_object = self.__clientes.values()
        self.__mascotas_object = self.__mascotas.values()
        if (self.__cliente==None):
            for cliente in self.__clientes_object:
                self.combo_Duenio.addItem(cliente.get_Nombre(), cliente.get_Dni())
        else:
            self.combo_Duenio.addItem(self.__cliente.get_Nombre(), self.__cliente.get_Dni())
            self.combo_Duenio.setEnabled(False)
        if (self.__mascota!=None):
            self.lineEdit_Nombre.setText(self.__mascota.get_Nombre())
            self.lineEdit_Raza.setText(self.__mascota.get_Raza())
            self.spinBox_Peso.setValue(self.__mascota.get_Peso())
            self.combo_Duenio.setCurrentIndex(self.combo_Duenio.findData(self.__mascota.get_Dni_Duenio()))
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        
    def pb_Aceptar_Clicked(self):
        if (self.__mascota!=None):
            codigo = self.__mascota.get_Codigo()
        else:
            codigo = len(self.__mascotas_object)
        mascota = Mascota(self.lineEdit_Nombre.text().strip().title(), self.lineEdit_Raza.text().strip().title(), self.spinBox_Peso.value(), self.combo_Duenio.itemData(self.combo_Duenio.currentIndex()), Funciones.select_paseador(self.__paseadores), codigo)
        msgbox = MsgBox()  
        valid = Funciones.validar_mascota(mascota)    
        if (valid[0]):
            msgbox.set_Text("Mascota Registrada")
            msgbox.setWindowTitle("Informacion")
            msgbox.exec_()
            self.__mascota = mascota
            self.close()
        else:
            msgbox.set_Title("Error")
            msgbox.set_Text(valid[1]) 
            msgbox.exec_()
    
    def get_Mascota(self):
        return self.__mascota
