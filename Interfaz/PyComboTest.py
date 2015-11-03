# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtComboTest import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pb_agregar)
        self.pushButton_2.clicked.connect(self.pb_remove)
        
        
    def pb_agregar(self):
        #lista = ["juan","domi","el otro juan"]
        self.comboBox.addItem("juan",38991704)
        
    def pb_remove(self):
        self.comboBox.removeItem(self.comboBox.currentIndex())