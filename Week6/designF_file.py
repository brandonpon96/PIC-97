# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designF.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(257, 186)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(30, 50, 191, 21))
        self.input.setObjectName(_fromUtf8("input"))
        self.enter = QtGui.QLabel(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.enter.setObjectName(_fromUtf8("enter"))
        self.result_label = QtGui.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.result_label.setObjectName(_fromUtf8("result_label"))
        self.result = QtGui.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(30, 120, 191, 16))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 257, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.enter.setText(_translate("MainWindow", "Enter math command: ", None))
        self.result_label.setText(_translate("MainWindow", "Result:", None))

