# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAltaEspacio.ui'
#
# Created: Sat Oct 31 11:02:37 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormAltaEspacio(object):
    def setupUi(self, FormAltaEspacio):
        FormAltaEspacio.setObjectName(_fromUtf8("FormAltaEspacio"))
        FormAltaEspacio.resize(400, 100)
        self.pb_Aceptar = QtGui.QPushButton(FormAltaEspacio)
        self.pb_Aceptar.setGeometry(QtCore.QRect(5, 70, 75, 23))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.pb_Cancelar = QtGui.QPushButton(FormAltaEspacio)
        self.pb_Cancelar.setGeometry(QtCore.QRect(320, 70, 75, 23))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.lineEdit_Direccion = QtGui.QLineEdit(FormAltaEspacio)
        self.lineEdit_Direccion.setGeometry(QtCore.QRect(135, 30, 181, 20))
        self.lineEdit_Direccion.setObjectName(_fromUtf8("lineEdit_Direccion"))
        self.label_Direccion = QtGui.QLabel(FormAltaEspacio)
        self.label_Direccion.setGeometry(QtCore.QRect(83, 33, 51, 16))
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))

        self.retranslateUi(FormAltaEspacio)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), FormAltaEspacio.close)
        QtCore.QMetaObject.connectSlotsByName(FormAltaEspacio)

    def retranslateUi(self, FormAltaEspacio):
        FormAltaEspacio.setWindowTitle(_translate("FormAltaEspacio", "Espacios Verdes - Alta", None))
        self.pb_Aceptar.setText(_translate("FormAltaEspacio", "Aceptar", None))
        self.pb_Cancelar.setText(_translate("FormAltaEspacio", "Cancelar", None))
        self.label_Direccion.setText(_translate("FormAltaEspacio", "Direccion", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormAltaEspacio = QtGui.QDialog()
    ui = Ui_FormAltaEspacio()
    ui.setupUi(FormAltaEspacio)
    FormAltaEspacio.show()
    sys.exit(app.exec_())

