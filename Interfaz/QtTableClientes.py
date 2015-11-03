# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableClientes.ui'
#
# Created: Mon Oct 19 11:37:06 2015
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

class Ui_Listado_Clientes(object):
    def setupUi(self, Listado_Clientes):
        Listado_Clientes.setObjectName(_fromUtf8("Listado_Clientes"))
        Listado_Clientes.resize(840, 420)
        self.table_Clientes = QtGui.QTableWidget(Listado_Clientes)
        self.table_Clientes.setGeometry(QtCore.QRect(0, 0, 840, 380))
        self.table_Clientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_Clientes.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_Clientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_Clientes.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_Clientes.setObjectName(_fromUtf8("table_Clientes"))
        self.table_Clientes.setColumnCount(5)
        self.table_Clientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Clientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Clientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Clientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Clientes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Clientes.setHorizontalHeaderItem(4, item)
        self.table_Clientes.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Clientes.horizontalHeader().setDefaultSectionSize(150)
        self.table_Clientes.horizontalHeader().setMinimumSectionSize(120)
        self.table_Clientes.horizontalHeader().setStretchLastSection(True)
        self.table_Clientes.verticalHeader().setVisible(False)
        self.pb_Mascotas = QtGui.QPushButton(Listado_Clientes)
        self.pb_Mascotas.setGeometry(QtCore.QRect(10, 390, 75, 24))
        self.pb_Mascotas.setObjectName(_fromUtf8("pb_Mascotas"))
        self.pb_Salir = QtGui.QPushButton(Listado_Clientes)
        self.pb_Salir.setGeometry(QtCore.QRect(755, 390, 75, 23))
        self.pb_Salir.setObjectName(_fromUtf8("pb_Salir"))

        self.retranslateUi(Listado_Clientes)
        QtCore.QObject.connect(self.pb_Salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Listado_Clientes.close)
        QtCore.QMetaObject.connectSlotsByName(Listado_Clientes)

    def retranslateUi(self, Listado_Clientes):
        Listado_Clientes.setWindowTitle(_translate("Listado_Clientes", "Clientes - Listado", None))
        self.table_Clientes.setSortingEnabled(True)
        item = self.table_Clientes.horizontalHeaderItem(0)
        item.setText(_translate("Listado_Clientes", "Apellido", None))
        item = self.table_Clientes.horizontalHeaderItem(1)
        item.setText(_translate("Listado_Clientes", "Nombre", None))
        item = self.table_Clientes.horizontalHeaderItem(2)
        item.setText(_translate("Listado_Clientes", "DNI", None))
        item = self.table_Clientes.horizontalHeaderItem(3)
        item.setText(_translate("Listado_Clientes", "Telefono", None))
        item = self.table_Clientes.horizontalHeaderItem(4)
        item.setText(_translate("Listado_Clientes", "Direccion", None))
        self.pb_Mascotas.setText(_translate("Listado_Clientes", "Ver Mascotas", None))
        self.pb_Salir.setText(_translate("Listado_Clientes", "Salir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Listado_Clientes = QtGui.QDialog()
    ui = Ui_Listado_Clientes()
    ui.setupUi(Listado_Clientes)
    Listado_Clientes.show()
    sys.exit(app.exec_())

