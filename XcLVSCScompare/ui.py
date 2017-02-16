# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XcLVSCScompare.ui'
#
# Created: Thu Oct 20 09:38:21 2016
#      by: PyQt4 UI code generator 4.9.6
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
        MainWindow.resize(668, 556)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.newsheetchoose = QtGui.QSpinBox(self.centralwidget)
        self.newsheetchoose.setGeometry(QtCore.QRect(510, 20, 121, 22))
        self.newsheetchoose.setObjectName(_fromUtf8("newsheetchoose"))
        self.newvscs = QtGui.QLabel(self.centralwidget)
        self.newvscs.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.newvscs.setObjectName(_fromUtf8("newvscs"))
        self.newvscsaddress = QtGui.QTextBrowser(self.centralwidget)
        self.newvscsaddress.setGeometry(QtCore.QRect(90, 10, 311, 41))
        self.newvscsaddress.setObjectName(_fromUtf8("newvscsaddress"))
        self.newvscschoose = QtGui.QPushButton(self.centralwidget)
        self.newvscschoose.setGeometry(QtCore.QRect(410, 20, 75, 21))
        self.newvscschoose.setAutoRepeatDelay(300)
        self.newvscschoose.setObjectName(_fromUtf8("newvscschoose"))
        self.oldsheetchoose = QtGui.QSpinBox(self.centralwidget)
        self.oldsheetchoose.setGeometry(QtCore.QRect(510, 80, 121, 22))
        self.oldsheetchoose.setObjectName(_fromUtf8("oldsheetchoose"))
        self.newvscsaddress_2 = QtGui.QTextBrowser(self.centralwidget)
        self.newvscsaddress_2.setGeometry(QtCore.QRect(90, 70, 311, 41))
        self.newvscsaddress_2.setObjectName(_fromUtf8("newvscsaddress_2"))
        self.oldvscschoose = QtGui.QPushButton(self.centralwidget)
        self.oldvscschoose.setGeometry(QtCore.QRect(410, 80, 75, 21))
        self.oldvscschoose.setAutoRepeatDelay(300)
        self.oldvscschoose.setObjectName(_fromUtf8("oldvscschoose"))
        self.oldvscs = QtGui.QLabel(self.centralwidget)
        self.oldvscs.setGeometry(QtCore.QRect(20, 80, 61, 21))
        self.oldvscs.setObjectName(_fromUtf8("oldvscs"))
        self.compareall = QtGui.QPushButton(self.centralwidget)
        self.compareall.setGeometry(QtCore.QRect(90, 200, 75, 21))
        self.compareall.setAutoRepeatDelay(300)
        self.compareall.setObjectName(_fromUtf8("compareall"))
        self.outputaddress = QtGui.QLabel(self.centralwidget)
        self.outputaddress.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.outputaddress.setObjectName(_fromUtf8("outputaddress"))
        self.outputaddressdisplay = QtGui.QTextBrowser(self.centralwidget)
        self.outputaddressdisplay.setGeometry(QtCore.QRect(90, 130, 311, 41))
        self.outputaddressdisplay.setObjectName(_fromUtf8("outputaddressdisplay"))
        self.outputaddresschoose = QtGui.QPushButton(self.centralwidget)
        self.outputaddresschoose.setGeometry(QtCore.QRect(410, 140, 75, 21))
        self.outputaddresschoose.setAutoRepeatDelay(300)
        self.outputaddresschoose.setObjectName(_fromUtf8("outputaddresschoose"))
        self.comparesheet = QtGui.QPushButton(self.centralwidget)
        self.comparesheet.setGeometry(QtCore.QRect(200, 200, 91, 21))
        self.comparesheet.setAutoRepeatDelay(300)
        self.comparesheet.setObjectName(_fromUtf8("comparesheet"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 290, 411, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XcLVSCScompare", None))
        self.newvscs.setText(_translate("MainWindow", "New VSCS", None))
        self.newvscschoose.setText(_translate("MainWindow", "Browse", None))
        self.oldvscschoose.setText(_translate("MainWindow", "Browse", None))
        self.oldvscs.setText(_translate("MainWindow", "Old VSCS", None))
        self.compareall.setText(_translate("MainWindow", "Compare All", None))
        self.outputaddress.setText(_translate("MainWindow", "Output Fold", None))
        self.outputaddresschoose.setText(_translate("MainWindow", "Browse", None))
        self.comparesheet.setText(_translate("MainWindow", "Compare Sheet", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

