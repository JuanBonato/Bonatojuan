# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAltaCliente.ui'
#
# Created: Thu Oct 22 09:12:32 2015
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

class Ui_Form_Alta_Cliente(object):
    def setupUi(self, Form_Alta_Cliente):
        Form_Alta_Cliente.setObjectName(_fromUtf8("Form_Alta_Cliente"))
        Form_Alta_Cliente.setWindowModality(QtCore.Qt.NonModal)
        Form_Alta_Cliente.resize(300, 270)
        Form_Alta_Cliente.setMinimumSize(QtCore.QSize(300, 270))
        Form_Alta_Cliente.setMaximumSize(QtCore.QSize(300, 270))
        Form_Alta_Cliente.setModal(False)
        self.lineEdit_Apellido = QtGui.QLineEdit(Form_Alta_Cliente)
        self.lineEdit_Apellido.setGeometry(QtCore.QRect(105, 65, 150, 22))
        self.lineEdit_Apellido.setMaxLength(20)
        self.lineEdit_Apellido.setObjectName(_fromUtf8("lineEdit_Apellido"))
        self.lineEdit_DNI = QtGui.QLineEdit(Form_Alta_Cliente)
        self.lineEdit_DNI.setGeometry(QtCore.QRect(105, 95, 150, 22))
        self.lineEdit_DNI.setObjectName(_fromUtf8("lineEdit_DNI"))
        self.pb_Aceptar = QtGui.QPushButton(Form_Alta_Cliente)
        self.pb_Aceptar.setGeometry(QtCore.QRect(10, 235, 75, 24))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.label_Apellido = QtGui.QLabel(Form_Alta_Cliente)
        self.label_Apellido.setGeometry(QtCore.QRect(40, 68, 46, 15))
        self.label_Apellido.setObjectName(_fromUtf8("label_Apellido"))
        self.pb_Cancelar = QtGui.QPushButton(Form_Alta_Cliente)
        self.pb_Cancelar.setGeometry(QtCore.QRect(215, 235, 75, 24))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.label_Telefono = QtGui.QLabel(Form_Alta_Cliente)
        self.label_Telefono.setGeometry(QtCore.QRect(40, 129, 46, 15))
        self.label_Telefono.setObjectName(_fromUtf8("label_Telefono"))
        self.lineEdit_Direccion = QtGui.QLineEdit(Form_Alta_Cliente)
        self.lineEdit_Direccion.setGeometry(QtCore.QRect(105, 155, 150, 22))
        self.lineEdit_Direccion.setObjectName(_fromUtf8("lineEdit_Direccion"))
        self.lineEdit_Telefono = QtGui.QLineEdit(Form_Alta_Cliente)
        self.lineEdit_Telefono.setGeometry(QtCore.QRect(105, 125, 150, 22))
        self.lineEdit_Telefono.setObjectName(_fromUtf8("lineEdit_Telefono"))
        self.label_Nombre = QtGui.QLabel(Form_Alta_Cliente)
        self.label_Nombre.setGeometry(QtCore.QRect(40, 36, 46, 15))
        self.label_Nombre.setObjectName(_fromUtf8("label_Nombre"))
        self.label_DNI = QtGui.QLabel(Form_Alta_Cliente)
        self.label_DNI.setGeometry(QtCore.QRect(40, 98, 46, 15))
        self.label_DNI.setObjectName(_fromUtf8("label_DNI"))
        self.lineEdit_Nombre = QtGui.QLineEdit(Form_Alta_Cliente)
        self.lineEdit_Nombre.setGeometry(QtCore.QRect(105, 33, 150, 22))
        self.lineEdit_Nombre.setMaxLength(20)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.label_Direccion = QtGui.QLabel(Form_Alta_Cliente)
        self.label_Direccion.setGeometry(QtCore.QRect(40, 160, 46, 15))
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))
        self.label_Mascotas = QtGui.QLabel(Form_Alta_Cliente)
        self.label_Mascotas.setGeometry(QtCore.QRect(40, 190, 46, 15))
        self.label_Mascotas.setObjectName(_fromUtf8("label_Mascotas"))
        self.combo_Mascotas = QtGui.QComboBox(Form_Alta_Cliente)
        self.combo_Mascotas.setEnabled(False)
        self.combo_Mascotas.setGeometry(QtCore.QRect(105, 186, 110, 22))
        self.combo_Mascotas.setObjectName(_fromUtf8("combo_Mascotas"))
        self.pb_Add_Mascota = QtGui.QPushButton(Form_Alta_Cliente)
        self.pb_Add_Mascota.setEnabled(False)
        self.pb_Add_Mascota.setGeometry(QtCore.QRect(225, 186, 30, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pb_Add_Mascota.setFont(font)
        self.pb_Add_Mascota.setObjectName(_fromUtf8("pb_Add_Mascota"))

        self.retranslateUi(Form_Alta_Cliente)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_Alta_Cliente.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Alta_Cliente)
        Form_Alta_Cliente.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Apellido)
        Form_Alta_Cliente.setTabOrder(self.lineEdit_Apellido, self.lineEdit_DNI)
        Form_Alta_Cliente.setTabOrder(self.lineEdit_DNI, self.lineEdit_Telefono)
        Form_Alta_Cliente.setTabOrder(self.lineEdit_Telefono, self.lineEdit_Direccion)
        Form_Alta_Cliente.setTabOrder(self.lineEdit_Direccion, self.pb_Add_Mascota)
        Form_Alta_Cliente.setTabOrder(self.pb_Add_Mascota, self.pb_Aceptar)
        Form_Alta_Cliente.setTabOrder(self.pb_Aceptar, self.pb_Cancelar)
        Form_Alta_Cliente.setTabOrder(self.pb_Cancelar, self.combo_Mascotas)

    def retranslateUi(self, Form_Alta_Cliente):
        Form_Alta_Cliente.setWindowTitle(_translate("Form_Alta_Cliente", "Clientes - Alta", None))
        self.lineEdit_Apellido.setPlaceholderText(_translate("Form_Alta_Cliente", "Máximo 20 Caracteres", None))
        self.lineEdit_DNI.setPlaceholderText(_translate("Form_Alta_Cliente", "8 Dígitos", None))
        self.pb_Aceptar.setText(_translate("Form_Alta_Cliente", "Aceptar", None))
        self.label_Apellido.setText(_translate("Form_Alta_Cliente", "Apellido", None))
        self.pb_Cancelar.setText(_translate("Form_Alta_Cliente", "Cancelar", None))
        self.label_Telefono.setText(_translate("Form_Alta_Cliente", "Telefono", None))
        self.lineEdit_Direccion.setPlaceholderText(_translate("Form_Alta_Cliente", "Máximo 30 Caracteres", None))
        self.lineEdit_Telefono.setPlaceholderText(_translate("Form_Alta_Cliente", "15 Digitos Sin Guiones", None))
        self.label_Nombre.setText(_translate("Form_Alta_Cliente", "Nombre", None))
        self.label_DNI.setText(_translate("Form_Alta_Cliente", "DNI", None))
        self.lineEdit_Nombre.setPlaceholderText(_translate("Form_Alta_Cliente", "Máximo 20 Caracteres", None))
        self.label_Direccion.setText(_translate("Form_Alta_Cliente", "Direccion", None))
        self.label_Mascotas.setText(_translate("Form_Alta_Cliente", "Mascotas", None))
        self.pb_Add_Mascota.setText(_translate("Form_Alta_Cliente", "+", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_Alta_Cliente = QtGui.QDialog()
    ui = Ui_Form_Alta_Cliente()
    ui.setupUi(Form_Alta_Cliente)
    Form_Alta_Cliente.show()
    sys.exit(app.exec_())

