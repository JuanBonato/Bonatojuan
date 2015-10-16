# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAltaMascota.ui'
#
# Created: Fri Oct 16 15:32:07 2015
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

class Ui_Form_Alta_Mascota(object):
    def setupUi(self, Form_Alta_Mascota):
        Form_Alta_Mascota.setObjectName(_fromUtf8("Form_Alta_Mascota"))
        Form_Alta_Mascota.setWindowModality(QtCore.Qt.WindowModal)
        Form_Alta_Mascota.resize(300, 270)
        Form_Alta_Mascota.setMinimumSize(QtCore.QSize(300, 270))
        Form_Alta_Mascota.setMaximumSize(QtCore.QSize(300, 270))
        Form_Alta_Mascota.setModal(True)
        self.lineEdit_Raza = QtGui.QLineEdit(Form_Alta_Mascota)
        self.lineEdit_Raza.setGeometry(QtCore.QRect(110, 82, 150, 22))
        self.lineEdit_Raza.setMaxLength(20)
        self.lineEdit_Raza.setObjectName(_fromUtf8("lineEdit_Raza"))
        self.pb_Aceptar = QtGui.QPushButton(Form_Alta_Mascota)
        self.pb_Aceptar.setGeometry(QtCore.QRect(10, 235, 75, 24))
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.label_Apellido = QtGui.QLabel(Form_Alta_Mascota)
        self.label_Apellido.setGeometry(QtCore.QRect(35, 85, 46, 15))
        self.label_Apellido.setObjectName(_fromUtf8("label_Apellido"))
        self.pb_Cancelar = QtGui.QPushButton(Form_Alta_Mascota)
        self.pb_Cancelar.setGeometry(QtCore.QRect(215, 235, 75, 24))
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))
        self.label_Telefono = QtGui.QLabel(Form_Alta_Mascota)
        self.label_Telefono.setGeometry(QtCore.QRect(35, 146, 46, 15))
        self.label_Telefono.setObjectName(_fromUtf8("label_Telefono"))
        self.label_Nombre = QtGui.QLabel(Form_Alta_Mascota)
        self.label_Nombre.setGeometry(QtCore.QRect(35, 53, 46, 15))
        self.label_Nombre.setObjectName(_fromUtf8("label_Nombre"))
        self.label_DNI = QtGui.QLabel(Form_Alta_Mascota)
        self.label_DNI.setGeometry(QtCore.QRect(35, 115, 46, 15))
        self.label_DNI.setObjectName(_fromUtf8("label_DNI"))
        self.lineEdit_Nombre = QtGui.QLineEdit(Form_Alta_Mascota)
        self.lineEdit_Nombre.setGeometry(QtCore.QRect(110, 50, 150, 22))
        self.lineEdit_Nombre.setMaxLength(20)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.combo_Duenio = QtGui.QComboBox(Form_Alta_Mascota)
        self.combo_Duenio.setGeometry(QtCore.QRect(110, 143, 151, 22))
        self.combo_Duenio.setMaxVisibleItems(5)
        self.combo_Duenio.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_Duenio.setObjectName(_fromUtf8("combo_Duenio"))
        self.spinBox_Peso = QtGui.QSpinBox(Form_Alta_Mascota)
        self.spinBox_Peso.setGeometry(QtCore.QRect(110, 112, 61, 22))
        self.spinBox_Peso.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_Peso.setMaximum(200)
        self.spinBox_Peso.setObjectName(_fromUtf8("spinBox_Peso"))
        self.label_Peso = QtGui.QLabel(Form_Alta_Mascota)
        self.label_Peso.setGeometry(QtCore.QRect(180, 115, 46, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Peso.setFont(font)
        self.label_Peso.setObjectName(_fromUtf8("label_Peso"))

        self.retranslateUi(Form_Alta_Mascota)
        QtCore.QObject.connect(self.pb_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_Alta_Mascota.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Alta_Mascota)
        Form_Alta_Mascota.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Raza)
        Form_Alta_Mascota.setTabOrder(self.lineEdit_Raza, self.pb_Aceptar)
        Form_Alta_Mascota.setTabOrder(self.pb_Aceptar, self.pb_Cancelar)

    def retranslateUi(self, Form_Alta_Mascota):
        Form_Alta_Mascota.setWindowTitle(_translate("Form_Alta_Mascota", "Mascotas - Alta", None))
        self.lineEdit_Raza.setPlaceholderText(_translate("Form_Alta_Mascota", "Máximo 20 Caracteres", None))
        self.pb_Aceptar.setText(_translate("Form_Alta_Mascota", "Aceptar", None))
        self.label_Apellido.setText(_translate("Form_Alta_Mascota", "Raza", None))
        self.pb_Cancelar.setText(_translate("Form_Alta_Mascota", "Cancelar", None))
        self.label_Telefono.setText(_translate("Form_Alta_Mascota", "Dueño", None))
        self.label_Nombre.setText(_translate("Form_Alta_Mascota", "Nombre", None))
        self.label_DNI.setText(_translate("Form_Alta_Mascota", "Peso", None))
        self.lineEdit_Nombre.setPlaceholderText(_translate("Form_Alta_Mascota", "Máximo 20 Caracteres", None))
        self.label_Peso.setText(_translate("Form_Alta_Mascota", "Kg", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_Alta_Mascota = QtGui.QDialog()
    ui = Ui_Form_Alta_Mascota()
    ui.setupUi(Form_Alta_Mascota)
    Form_Alta_Mascota.show()
    sys.exit(app.exec_())

