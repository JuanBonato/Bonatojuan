# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from QtFormAltaMascota import Ui_Form_Alta_Mascota

class FormAltaCliente(QtGui.QDialog, Ui_Form_Alta_Mascota):
    def __init__(self, mascota = None, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        if (mascota!=None):
            self.lineEdit_Nombre.setText(mascota.get_Nombre)
            self.lineEdit_Nombre.setText(mascota.get_Raza)
            self.spinBox_Peso.setValue(mascota.get_Peso)
