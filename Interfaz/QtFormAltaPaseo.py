# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAltaPaseo.ui'
#
# Created: Fri Oct 30 15:50:00 2015
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

class Ui_Form_Alta_Paseo(object):
    def setupUi(self, Form_Alta_Paseo):
        Form_Alta_Paseo.setObjectName(_fromUtf8("Form_Alta_Paseo"))
        Form_Alta_Paseo.setWindowModality(QtCore.Qt.NonModal)
        Form_Alta_Paseo.resize(300, 300)
        Form_Alta_Paseo.setMinimumSize(QtCore.QSize(300, 200))
        Form_Alta_Paseo.setMaximumSize(QtCore.QSize(300, 300))
        Form_Alta_Paseo.setModal(False)
        self.pb_Cancelar = QtGui.QPushButton(Form_Alta_Paseo)
        self.pb_Cancelar.setGeometry(QtCore.QRect(215, 270, 75, 24))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.pb_Aceptar = QtGui.QPushButton(Form_Alta_Paseo)
        self.pb_Aceptar.setGeometry(QtCore.QRect(10, 270, 75, 24))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.combo_Paseadores = QtGui.QComboBox(Form_Alta_Paseo)
        self.combo_Paseadores.setGeometry(QtCore.QRect(120, 30, 161, 22))
        self.combo_Paseadores.setMaxVisibleItems(5)
        self.combo_Paseadores.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_Paseadores.setObjectName(_fromUtf8("combo_Paseadores"))
        self.spinBox_Horas = QtGui.QSpinBox(Form_Alta_Paseo)
        self.spinBox_Horas.setGeometry(QtCore.QRect(120, 200, 42, 22))
        self.spinBox_Horas.setMaximum(99)
        self.spinBox_Horas.setObjectName(_fromUtf8("spinBox_Horas"))
        self.spinBox_Minutos = QtGui.QSpinBox(Form_Alta_Paseo)
        self.spinBox_Minutos.setGeometry(QtCore.QRect(200, 200, 42, 22))
        self.spinBox_Minutos.setObjectName(_fromUtf8("spinBox_Minutos"))
        self.label_Paseadores = QtGui.QLabel(Form_Alta_Paseo)
        self.label_Paseadores.setGeometry(QtCore.QRect(45, 35, 60, 15))
        self.label_Paseadores.setObjectName(_fromUtf8("label_Paseadores"))
        self.label_Duracion = QtGui.QLabel(Form_Alta_Paseo)
        self.label_Duracion.setGeometry(QtCore.QRect(55, 205, 60, 15))
        self.label_Duracion.setObjectName(_fromUtf8("label_Duracion"))
        self.label_Horas = QtGui.QLabel(Form_Alta_Paseo)
        self.label_Horas.setGeometry(QtCore.QRect(170, 205, 21, 16))
        self.label_Horas.setObjectName(_fromUtf8("label_Horas"))
        self.label_Minutos = QtGui.QLabel(Form_Alta_Paseo)
        self.label_Minutos.setGeometry(QtCore.QRect(250, 205, 21, 16))
        self.label_Minutos.setObjectName(_fromUtf8("label_Minutos"))
        self.label_Espacio = QtGui.QLabel(Form_Alta_Paseo)
        self.label_Espacio.setGeometry(QtCore.QRect(45, 122, 71, 16))
        self.label_Espacio.setObjectName(_fromUtf8("label_Espacio"))
        self.combo_Espacios = QtGui.QComboBox(Form_Alta_Paseo)
        self.combo_Espacios.setGeometry(QtCore.QRect(120, 115, 161, 22))
        self.combo_Espacios.setMaxVisibleItems(5)
        self.combo_Espacios.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_Espacios.setObjectName(_fromUtf8("combo_Espacios"))

        self.retranslateUi(Form_Alta_Paseo)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_Alta_Paseo.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Alta_Paseo)
        Form_Alta_Paseo.setTabOrder(self.combo_Paseadores, self.spinBox_Horas)
        Form_Alta_Paseo.setTabOrder(self.spinBox_Horas, self.spinBox_Minutos)
        Form_Alta_Paseo.setTabOrder(self.spinBox_Minutos, self.pb_Aceptar)
        Form_Alta_Paseo.setTabOrder(self.pb_Aceptar, self.pb_Cancelar)

    def retranslateUi(self, Form_Alta_Paseo):
        Form_Alta_Paseo.setWindowTitle(_translate("Form_Alta_Paseo", "Paseos - Alta", None))
        self.pb_Cancelar.setText(_translate("Form_Alta_Paseo", "Cancelar", None))
        self.pb_Aceptar.setText(_translate("Form_Alta_Paseo", "Aceptar", None))
        self.label_Paseadores.setText(_translate("Form_Alta_Paseo", "Paseador", None))
        self.label_Duracion.setText(_translate("Form_Alta_Paseo", "Duracion", None))
        self.label_Horas.setText(_translate("Form_Alta_Paseo", "Hs", None))
        self.label_Minutos.setText(_translate("Form_Alta_Paseo", "Min", None))
        self.label_Espacio.setText(_translate("Form_Alta_Paseo", "Espacio Verde", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_Alta_Paseo = QtGui.QDialog()
    ui = Ui_Form_Alta_Paseo()
    ui.setupUi(Form_Alta_Paseo)
    Form_Alta_Paseo.show()
    sys.exit(app.exec_())

