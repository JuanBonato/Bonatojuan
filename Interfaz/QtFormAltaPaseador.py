# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAltaPaseador.ui'
#
# Created: Fri Oct 16 11:57:49 2015
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

class Ui_Form_Alta_Paseador(object):
    def setupUi(self, Form_Alta_Paseador):
        Form_Alta_Paseador.setObjectName(_fromUtf8("Form_Alta_Paseador"))
        Form_Alta_Paseador.setWindowModality(QtCore.Qt.WindowModal)
        Form_Alta_Paseador.resize(300, 270)
        Form_Alta_Paseador.setMinimumSize(QtCore.QSize(300, 270))
        Form_Alta_Paseador.setMaximumSize(QtCore.QSize(300, 270))
        Form_Alta_Paseador.setModal(True)
        self.lineEdit_Apellido = QtGui.QLineEdit(Form_Alta_Paseador)
        self.lineEdit_Apellido.setGeometry(QtCore.QRect(110, 82, 150, 22))
        self.lineEdit_Apellido.setObjectName(_fromUtf8("lineEdit_Apellido"))
        self.lineEdit_DNI = QtGui.QLineEdit(Form_Alta_Paseador)
        self.lineEdit_DNI.setGeometry(QtCore.QRect(110, 112, 150, 22))
        self.lineEdit_DNI.setObjectName(_fromUtf8("lineEdit_DNI"))
        self.pb_Aceptar = QtGui.QPushButton(Form_Alta_Paseador)
        self.pb_Aceptar.setGeometry(QtCore.QRect(10, 235, 75, 24))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.label_Apellido = QtGui.QLabel(Form_Alta_Paseador)
        self.label_Apellido.setGeometry(QtCore.QRect(35, 85, 46, 15))
        self.label_Apellido.setObjectName(_fromUtf8("label_Apellido"))
        self.pb_Cancelar = QtGui.QPushButton(Form_Alta_Paseador)
        self.pb_Cancelar.setGeometry(QtCore.QRect(215, 235, 75, 24))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.label_Telefono = QtGui.QLabel(Form_Alta_Paseador)
        self.label_Telefono.setGeometry(QtCore.QRect(35, 146, 46, 15))
        self.label_Telefono.setObjectName(_fromUtf8("label_Telefono"))
        self.lineEdit_Telefono = QtGui.QLineEdit(Form_Alta_Paseador)
        self.lineEdit_Telefono.setGeometry(QtCore.QRect(110, 142, 150, 22))
        self.lineEdit_Telefono.setObjectName(_fromUtf8("lineEdit_Telefono"))
        self.label_Nombre = QtGui.QLabel(Form_Alta_Paseador)
        self.label_Nombre.setGeometry(QtCore.QRect(35, 53, 46, 15))
        self.label_Nombre.setObjectName(_fromUtf8("label_Nombre"))
        self.label_DNI = QtGui.QLabel(Form_Alta_Paseador)
        self.label_DNI.setGeometry(QtCore.QRect(35, 115, 46, 15))
        self.label_DNI.setObjectName(_fromUtf8("label_DNI"))
        self.lineEdit_Nombre = QtGui.QLineEdit(Form_Alta_Paseador)
        self.lineEdit_Nombre.setGeometry(QtCore.QRect(110, 50, 150, 22))
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))

        self.retranslateUi(Form_Alta_Paseador)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_Alta_Paseador.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Alta_Paseador)
        Form_Alta_Paseador.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Apellido)
        Form_Alta_Paseador.setTabOrder(self.lineEdit_Apellido, self.lineEdit_DNI)
        Form_Alta_Paseador.setTabOrder(self.lineEdit_DNI, self.lineEdit_Telefono)
        Form_Alta_Paseador.setTabOrder(self.lineEdit_Telefono, self.pb_Aceptar)
        Form_Alta_Paseador.setTabOrder(self.pb_Aceptar, self.pb_Cancelar)

    def retranslateUi(self, Form_Alta_Paseador):
        Form_Alta_Paseador.setWindowTitle(_translate("Form_Alta_Paseador", "Paseadores - Alta", None))
        self.lineEdit_Apellido.setPlaceholderText(_translate("Form_Alta_Paseador", "Máximo 20 Caracteres", None))
        self.lineEdit_DNI.setPlaceholderText(_translate("Form_Alta_Paseador", "8 Dígitos", None))
        self.pb_Aceptar.setText(_translate("Form_Alta_Paseador", "Aceptar", None))
        self.label_Apellido.setText(_translate("Form_Alta_Paseador", "Apellido", None))
        self.pb_Cancelar.setText(_translate("Form_Alta_Paseador", "Cancelar", None))
        self.label_Telefono.setText(_translate("Form_Alta_Paseador", "Telefono", None))
        self.lineEdit_Telefono.setPlaceholderText(_translate("Form_Alta_Paseador", "8 Dígitos Sin Guiones", None))
        self.label_Nombre.setText(_translate("Form_Alta_Paseador", "Nombre", None))
        self.label_DNI.setText(_translate("Form_Alta_Paseador", "DNI", None))
        self.lineEdit_Nombre.setPlaceholderText(_translate("Form_Alta_Paseador", "Máximo 20 Caracteres", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_Alta_Paseador = QtGui.QDialog()
    ui = Ui_Form_Alta_Paseador()
    ui.setupUi(Form_Alta_Paseador)
    Form_Alta_Paseador.show()
    sys.exit(app.exec_())

