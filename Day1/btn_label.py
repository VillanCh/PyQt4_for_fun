# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'btn_label.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.btn_close = QtGui.QPushButton(Form)
        self.btn_close.setGeometry(QtCore.QRect(300, 280, 101, 21))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.btn_change = QtGui.QPushButton(Form)
        self.btn_change.setGeometry(QtCore.QRect(300, 210, 101, 31))
        self.btn_change.setObjectName(_fromUtf8("btn_change"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 90, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_close.setText(_translate("Form", "Close the Block", None))
        self.btn_change.setText(_translate("Form", "change label", None))
        self.label.setText(_translate("Form", "TextLabel", None))

def __main__():
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    Form = QtGui.QWidget()
    a = ui.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    __main__()