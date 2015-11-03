# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MsgBoxConfirm.ui'
#
# Created: Thu Oct 22 09:13:48 2015
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

class Ui_msg_Dialog(object):
    def setupUi(self, msg_Dialog):
        msg_Dialog.setObjectName(_fromUtf8("msg_Dialog"))
        msg_Dialog.resize(400, 100)
        msg_Dialog.setWindowTitle(_fromUtf8(""))
        self.pb_Aceptar = QtGui.QPushButton(msg_Dialog)
        self.pb_Aceptar.setGeometry(QtCore.QRect(50, 68, 80, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_Aceptar.setFont(font)
        self.pb_Aceptar.setObjectName(_fromUtf8("pb_Aceptar"))
        self.msg_Label = QtGui.QLabel(msg_Dialog)
        self.msg_Label.setGeometry(QtCore.QRect(-1, 10, 401, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.msg_Label.setFont(font)
        self.msg_Label.setText(_fromUtf8(""))
        self.msg_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_Label.setObjectName(_fromUtf8("msg_Label"))
        self.pb_Cancelar = QtGui.QPushButton(msg_Dialog)
        self.pb_Cancelar.setGeometry(QtCore.QRect(265, 68, 80, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_Cancelar.setFont(font)
        self.pb_Cancelar.setObjectName(_fromUtf8("pb_Cancelar"))

        self.retranslateUi(msg_Dialog)
        QtCore.QObject.connect(self.pb_Aceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), msg_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(msg_Dialog)

    def retranslateUi(self, msg_Dialog):
        self.pb_Aceptar.setText(_translate("msg_Dialog", "Aceptar", None))
        self.pb_Cancelar.setText(_translate("msg_Dialog", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    msg_Dialog = QtGui.QDialog()
    ui = Ui_msg_Dialog()
    ui.setupUi(msg_Dialog)
    msg_Dialog.show()
    sys.exit(app.exec_())

