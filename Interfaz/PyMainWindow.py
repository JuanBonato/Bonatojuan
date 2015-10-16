# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from Interfaz.QtMainWindow import Ui_MainWindow
#from QtMainWindow import Ui_MainWindow
from Interfaz.PyFormAltaCliente import FormAltaCliente

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.actionAltaCliente.triggered.connect(self.alta_Cliente)
        self.actionAltaMascota.triggered.connect(self.alta_Mascota)
        self.actionAltaPaseador.triggered.connect(self.alta_Paseador)

    def alta_Cliente(self):
        form = FormAltaCliente()
        form.exec_()
        
    def alta_Mascota(self):
        form = FormAltaCliente()
        form.exec_()
        
    def alta_Paseador(self):
        form = FormAltaCliente()
        form.exec_()