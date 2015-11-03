# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Interfaz.QtMsgBox import Ui_msg_Dialog

class MsgBox(QtGui.QDialog, Ui_msg_Dialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        
    def set_Text(self,text):
        self.msg_Label.setText(text)
        
    def set_Title(self,text):
        self.msg_Label.setWindowTitle(text)
        