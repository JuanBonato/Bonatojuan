# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtMsgBoxConfirm import Ui_msg_Dialog

class MsgBoxConfirm(QtGui.QDialog, Ui_msg_Dialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setResult(0)
        self.pb_Aceptar.clicked.connect(self.pb_Aceptar_Clicked)
        
    def set_Text(self,text):
        self.msg_Label.setText(text)
        
    def set_Title(self,text):
        self.msg_Label.setWindowTitle(text)
        
    def pb_Aceptar_Clicked(self):
        self.setResult(1)
        
    def get_Result(self):
        return self.result()
        