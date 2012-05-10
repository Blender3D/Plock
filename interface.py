# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Thu May 10 02:55:11 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(707, 604)
    MainWindow.setMouseTracking(True)
    MainWindow.setAutoFillBackground(True)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    spacerItem = QtGui.QSpacerItem(20, 214, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
    spacerItem1 = QtGui.QSpacerItem(117, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
    self.frame = QtGui.QFrame(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
    self.frame.setSizePolicy(sizePolicy)
    self.frame.setMinimumSize(QtCore.QSize(400, 0))
    self.frame.setAutoFillBackground(False)
    self.frame.setStyleSheet(_fromUtf8("#frame {\n"
"  border: 8px solid palette(highlight);\n"
"  background: palette(window);\n"
"}\n"
"\n"
"QToolButton {\n"
"  padding: 7px;\n"
"  padding-top: 0px;\n"
"}"))
    self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
    self.frame.setObjectName(_fromUtf8("frame"))
    self.gridLayout = QtGui.QGridLayout(self.frame)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.headerLabel = QtGui.QLabel(self.frame)
    self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
    self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
    self.gridLayout.addWidget(self.headerLabel, 0, 0, 1, 1)
    self.formLayout = QtGui.QFormLayout()
    self.formLayout.setObjectName(_fromUtf8("formLayout"))
    self.label = QtGui.QLabel(self.frame)
    self.label.setObjectName(_fromUtf8("label"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
    self.statusMessage = QtGui.QLabel(self.frame)
    self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
    self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.statusMessage)
    self.passwordTextbox = QtGui.QLineEdit(self.frame)
    self.passwordTextbox.setEchoMode(QtGui.QLineEdit.Password)
    self.passwordTextbox.setObjectName(_fromUtf8("passwordTextbox"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.passwordTextbox)
    self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.unlockButton = QtGui.QToolButton(self.frame)
    self.unlockButton.setMinimumSize(QtCore.QSize(80, 0))
    self.unlockButton.setStyleSheet(_fromUtf8(""))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.unlockButton.setIcon(icon)
    self.unlockButton.setIconSize(QtCore.QSize(32, 32))
    self.unlockButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    self.unlockButton.setObjectName(_fromUtf8("unlockButton"))
    self.horizontalLayout.addWidget(self.unlockButton)
    self.switchButton = QtGui.QToolButton(self.frame)
    self.switchButton.setMinimumSize(QtCore.QSize(80, 0))
    self.switchButton.setIcon(icon)
    self.switchButton.setIconSize(QtCore.QSize(32, 32))
    self.switchButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    self.switchButton.setObjectName(_fromUtf8("switchButton"))
    self.horizontalLayout.addWidget(self.switchButton)
    self.shutdownButton = QtGui.QToolButton(self.frame)
    self.shutdownButton.setMinimumSize(QtCore.QSize(80, 0))
    self.shutdownButton.setIcon(icon)
    self.shutdownButton.setIconSize(QtCore.QSize(32, 32))
    self.shutdownButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    self.shutdownButton.setObjectName(_fromUtf8("shutdownButton"))
    self.horizontalLayout.addWidget(self.shutdownButton)
    self.rebootButton = QtGui.QToolButton(self.frame)
    self.rebootButton.setMinimumSize(QtCore.QSize(80, 0))
    self.rebootButton.setIcon(icon)
    self.rebootButton.setIconSize(QtCore.QSize(32, 32))
    self.rebootButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    self.rebootButton.setObjectName(_fromUtf8("rebootButton"))
    self.horizontalLayout.addWidget(self.rebootButton)
    self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
    self.line = QtGui.QFrame(self.frame)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
    self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)
    spacerItem2 = QtGui.QSpacerItem(117, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
    spacerItem3 = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)
    QtCore.QObject.connect(self.passwordTextbox, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.unlockButton.click)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
    self.headerLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">The screen has been locked by {}</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter your password:", None, QtGui.QApplication.UnicodeUTF8))
    self.statusMessage.setText(QtGui.QApplication.translate("MainWindow", "<span style=\" color:red;\">You have entered an invalid password</span>", None, QtGui.QApplication.UnicodeUTF8))
    self.unlockButton.setText(QtGui.QApplication.translate("MainWindow", "&Unlock", None, QtGui.QApplication.UnicodeUTF8))
    self.switchButton.setText(QtGui.QApplication.translate("MainWindow", "S&witch User", None, QtGui.QApplication.UnicodeUTF8))
    self.shutdownButton.setText(QtGui.QApplication.translate("MainWindow", "Shut &Down", None, QtGui.QApplication.UnicodeUTF8))
    self.rebootButton.setText(QtGui.QApplication.translate("MainWindow", "&Restart", None, QtGui.QApplication.UnicodeUTF8))

