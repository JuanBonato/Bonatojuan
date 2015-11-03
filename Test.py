# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from Interfaz import PyMainWindow

if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    interfaz = PyMainWindow.MainWindow()
    MainApp = interfaz
    MainApp.show()
    sys.exit(app.exec_())
    

interfaz.__init__
