# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import QUrl
from Interfaz.QtWebView import Ui_FormRecorrido
from Entidad.Url import Url

class WebView(QtGui.QDialog, Ui_FormRecorrido):
    def __init__(self, url, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.__url = url
        self.webViewMapa.setUrl(QUrl(url.get_Url()))
        self.slider_Zoom.valueChanged.connect(self.set_Zoom)        
        
    def set_Zoom(self):
        self.__url.set_Zoom(str(self.slider_Zoom.value()))
        self.webViewMapa.load(QUrl(self.__url.get_Url()))

    
