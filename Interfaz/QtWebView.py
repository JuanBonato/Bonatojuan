# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebView.ui'
#
# Created: Mon Oct 26 19:41:30 2015
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

class Ui_FormRecorrido(object):
    def setupUi(self, FormRecorrido):
        FormRecorrido.setObjectName(_fromUtf8("FormRecorrido"))
        FormRecorrido.resize(640, 640)
        self.webViewMapa = QtWebKit.QWebView(FormRecorrido)
        self.webViewMapa.setGeometry(QtCore.QRect(0, 0, 640, 640))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        self.webViewMapa.setFont(font)
        self.webViewMapa.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webViewMapa.setObjectName(_fromUtf8("webViewMapa"))
        self.slider_Zoom = QtGui.QSlider(FormRecorrido)
        self.slider_Zoom.setGeometry(QtCore.QRect(590, 250, 22, 160))
        self.slider_Zoom.setMinimum(1)
        self.slider_Zoom.setMaximum(16)
        self.slider_Zoom.setPageStep(4)
        self.slider_Zoom.setProperty("value", 14)
        self.slider_Zoom.setOrientation(QtCore.Qt.Vertical)
        self.slider_Zoom.setObjectName(_fromUtf8("slider_Zoom"))
        self.label_Zoom = QtGui.QLabel(FormRecorrido)
        self.label_Zoom.setGeometry(QtCore.QRect(587, 230, 46, 13))
        self.label_Zoom.setObjectName(_fromUtf8("label_Zoom"))

        self.retranslateUi(FormRecorrido)
        QtCore.QMetaObject.connectSlotsByName(FormRecorrido)

    def retranslateUi(self, FormRecorrido):
        FormRecorrido.setWindowTitle(_translate("FormRecorrido", "Recorrido", None))
        self.label_Zoom.setText(_translate("FormRecorrido", "Zoom", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormRecorrido = QtGui.QDialog()
    ui = Ui_FormRecorrido()
    ui.setupUi(FormRecorrido)
    FormRecorrido.show()
    sys.exit(app.exec_())

