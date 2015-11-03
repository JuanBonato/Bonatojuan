# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormConfiguracion.ui'
#
# Created: Mon Nov  2 21:55:05 2015
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

class Ui_FormConfiguracion(object):
    def setupUi(self, FormConfiguracion):
        FormConfiguracion.setObjectName(_fromUtf8("FormConfiguracion"))
        FormConfiguracion.resize(330, 220)
        self.combo_Espacios = QtGui.QComboBox(FormConfiguracion)
        self.combo_Espacios.setGeometry(QtCore.QRect(130, 95, 160, 26))
        self.combo_Espacios.setObjectName(_fromUtf8("combo_Espacios"))
        self.label_Espacios = QtGui.QLabel(FormConfiguracion)
        self.label_Espacios.setGeometry(QtCore.QRect(5, 100, 91, 16))
        self.label_Espacios.setObjectName(_fromUtf8("label_Espacios"))
        self.label_Direccion = QtGui.QLabel(FormConfiguracion)
        self.label_Direccion.setGeometry(QtCore.QRect(5, 50, 121, 16))
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))
        self.lineEdit_Direccion = QtGui.QLineEdit(FormConfiguracion)
        self.lineEdit_Direccion.setGeometry(QtCore.QRect(130, 50, 194, 20))
        self.lineEdit_Direccion.setObjectName(_fromUtf8("lineEdit_Direccion"))
        self.pb_Add = QtGui.QPushButton(FormConfiguracion)
        self.pb_Add.setGeometry(QtCore.QRect(295, 93, 30, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pb_Add.setFont(font)
        self.pb_Add.setObjectName(_fromUtf8("pb_Add"))
        self.pb_Aceptar = QtGui.QPushButton(FormConfiguracion)
        self.pb_Aceptar.setGeometry(QtCore.QRect(5, 193, 75, 23))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.pb_Cancelar = QtGui.QPushButton(FormConfiguracion)
        self.pb_Cancelar.setGeometry(QtCore.QRect(250, 193, 75, 23))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.pb_Remove = QtGui.QPushButton(FormConfiguracion)
        self.pb_Remove.setGeometry(QtCore.QRect(295, 107, 30, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pb_Remove.setFont(font)
        self.pb_Remove.setObjectName(_fromUtf8("pb_Remove"))

        self.retranslateUi(FormConfiguracion)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), FormConfiguracion.close)
        QtCore.QMetaObject.connectSlotsByName(FormConfiguracion)
        FormConfiguracion.setTabOrder(self.lineEdit_Direccion, self.combo_Espacios)
        FormConfiguracion.setTabOrder(self.combo_Espacios, self.pb_Add)
        FormConfiguracion.setTabOrder(self.pb_Add, self.pb_Remove)
        FormConfiguracion.setTabOrder(self.pb_Remove, self.pb_Aceptar)
        FormConfiguracion.setTabOrder(self.pb_Aceptar, self.pb_Cancelar)
        
    def retranslateUi(self, FormConfiguracion):
        FormConfiguracion.setWindowTitle(_translate("FormConfiguracion", "Configuracion", None))
        self.label_Espacios.setText(_translate("FormConfiguracion", "Espacios Verdes", None))
        self.label_Direccion.setText(_translate("FormConfiguracion", "Direccion de la Agencia", None))
        self.pb_Add.setText(_translate("FormConfiguracion", "+", None))
        self.pb_Aceptar.setText(_translate("FormConfiguracion", "Aceptar", None))
        self.pb_Cancelar.setText(_translate("FormConfiguracion", "Cancelar", None))
        self.pb_Remove.setText(_translate("FormConfiguracion", "-", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormConfiguracion = QtGui.QDialog()
    ui = Ui_FormConfiguracion()
    ui.setupUi(FormConfiguracion)
    FormConfiguracion.show()
    sys.exit(app.exec_())

