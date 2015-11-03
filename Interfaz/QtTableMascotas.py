# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableMascotas.ui'
#
# Created: Wed Oct 21 01:00:37 2015
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

class Ui_Listado_Mascotas(object):
    def setupUi(self, Listado_Mascotas):
        Listado_Mascotas.setObjectName(_fromUtf8("Listado_Mascotas"))
        Listado_Mascotas.resize(650, 420)
        self.table_Mascotas = QtGui.QTableWidget(Listado_Mascotas)
        self.table_Mascotas.setGeometry(QtCore.QRect(0, 0, 650, 380))
        self.table_Mascotas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_Mascotas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_Mascotas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_Mascotas.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_Mascotas.setObjectName(_fromUtf8("table_Mascotas"))
        self.table_Mascotas.setColumnCount(6)
        self.table_Mascotas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_Mascotas.setHorizontalHeaderItem(5, item)
        self.table_Mascotas.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Mascotas.horizontalHeader().setDefaultSectionSize(100)
        self.table_Mascotas.horizontalHeader().setMinimumSectionSize(100)
        self.table_Mascotas.horizontalHeader().setStretchLastSection(True)
        self.table_Mascotas.verticalHeader().setVisible(False)
        self.pb_Salir = QtGui.QPushButton(Listado_Mascotas)
        self.pb_Salir.setGeometry(QtCore.QRect(565, 390, 75, 23))
        self.pb_Salir.setObjectName(_fromUtf8("pb_Salir"))

        self.retranslateUi(Listado_Mascotas)
        QtCore.QObject.connect(self.pb_Salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Listado_Mascotas.close)
        QtCore.QMetaObject.connectSlotsByName(Listado_Mascotas)

    def retranslateUi(self, Listado_Mascotas):
        Listado_Mascotas.setWindowTitle(_translate("Listado_Mascotas", "Mascotas - Listado", None))
        self.table_Mascotas.setSortingEnabled(True)
        item = self.table_Mascotas.horizontalHeaderItem(0)
        item.setText(_translate("Listado_Mascotas", "Nombre", None))
        item = self.table_Mascotas.horizontalHeaderItem(1)
        item.setText(_translate("Listado_Mascotas", "Raza", None))
        item = self.table_Mascotas.horizontalHeaderItem(2)
        item.setText(_translate("Listado_Mascotas", "Peso", None))
        item = self.table_Mascotas.horizontalHeaderItem(3)
        item.setText(_translate("Listado_Mascotas", "Dueño", None))
        item = self.table_Mascotas.horizontalHeaderItem(4)
        item.setText(_translate("Listado_Mascotas", "Paseador", None))
        item = self.table_Mascotas.horizontalHeaderItem(5)
        item.setText(_translate("Listado_Mascotas", "Codigo", None))
        self.pb_Salir.setText(_translate("Listado_Mascotas", "Salir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Listado_Mascotas = QtGui.QDialog()
    ui = Ui_Listado_Mascotas()
    ui.setupUi(Listado_Mascotas)
    Listado_Mascotas.show()
    sys.exit(app.exec_())

