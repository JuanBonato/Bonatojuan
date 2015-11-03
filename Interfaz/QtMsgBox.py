# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MsgBox.ui'
#
# Created: Sat Oct 17 11:57:29 2015
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
        msg_Dialog.resize(400, 80)
        msg_Dialog.setWindowTitle(_fromUtf8(""))
        self.aceptar_pushButton = QtGui.QPushButton(msg_Dialog)
        self.aceptar_pushButton.setGeometry(QtCore.QRect(160, 52, 80, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.aceptar_pushButton.setFont(font)
        self.aceptar_pushButton.setObjectName(_fromUtf8("aceptar_pushButton"))
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

        self.retranslateUi(msg_Dialog)
        QtCore.QObject.connect(self.aceptar_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), msg_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(msg_Dialog)

    def retranslateUi(self, msg_Dialog):
        self.aceptar_pushButton.setText(_translate("msg_Dialog", "Aceptar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    msg_Dialog = QtGui.QDialog()
    ui = Ui_msg_Dialog()
    ui.setupUi(msg_Dialog)
    msg_Dialog.show()
    sys.exit(app.exec_())

