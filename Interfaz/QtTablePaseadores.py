# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TablePaseadores.ui'
#
# Created: Fri Oct 30 14:57:35 2015
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

class Ui_Listado_Paseadores(object):
    def setupUi(self, Listado_Paseadores):
        Listado_Paseadores.setObjectName(_fromUtf8("Listado_Paseadores"))
        Listado_Paseadores.resize(650, 420)
        self.table_Paseadores = QtGui.QTableWidget(Listado_Paseadores)
        self.table_Paseadores.setGeometry(QtCore.QRect(0, 0, 650, 380))
        self.table_Paseadores.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_Paseadores.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_Paseadores.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_Paseadores.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_Paseadores.setObjectName(_fromUtf8("table_Paseadores"))
        self.table_Paseadores.setColumnCount(4)
        self.table_Paseadores.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Paseadores.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Paseadores.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Paseadores.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Paseadores.setHorizontalHeaderItem(3, item)
        self.table_Paseadores.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Paseadores.horizontalHeader().setDefaultSectionSize(150)
        self.table_Paseadores.horizontalHeader().setMinimumSectionSize(120)
        self.table_Paseadores.horizontalHeader().setStretchLastSection(True)
        self.table_Paseadores.verticalHeader().setVisible(False)
        self.pb_Mascotas = QtGui.QPushButton(Listado_Paseadores)
        self.pb_Mascotas.setGeometry(QtCore.QRect(10, 390, 75, 24))
        self.pb_Mascotas.setObjectName(_fromUtf8("pb_Mascotas"))
        self.pb_Salir = QtGui.QPushButton(Listado_Paseadores)
        self.pb_Salir.setGeometry(QtCore.QRect(565, 390, 75, 23))
        self.pb_Salir.setObjectName(_fromUtf8("pb_Salir"))

        self.retranslateUi(Listado_Paseadores)
        QtCore.QObject.connect(self.pb_Salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Listado_Paseadores.close)
        QtCore.QMetaObject.connectSlotsByName(Listado_Paseadores)

    def retranslateUi(self, Listado_Paseadores):
        Listado_Paseadores.setWindowTitle(_translate("Listado_Paseadores", "Paseadores - Listado", None))
        self.table_Paseadores.setSortingEnabled(True)
        item = self.table_Paseadores.horizontalHeaderItem(0)
        item.setText(_translate("Listado_Paseadores", "Apellido", None))
        item = self.table_Paseadores.horizontalHeaderItem(1)
        item.setText(_translate("Listado_Paseadores", "Nombre", None))
        item = self.table_Paseadores.horizontalHeaderItem(2)
        item.setText(_translate("Listado_Paseadores", "DNI", None))
        item = self.table_Paseadores.horizontalHeaderItem(3)
        item.setText(_translate("Listado_Paseadores", "Telefono", None))
        self.pb_Mascotas.setText(_translate("Listado_Paseadores", "Ver Mascotas", None))
        self.pb_Salir.setText(_translate("Listado_Paseadores", "Salir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Listado_Paseadores = QtGui.QDialog()
    ui = Ui_Listado_Paseadores()
    ui.setupUi(Listado_Paseadores)
    Listado_Paseadores.show()
    sys.exit(app.exec_())

