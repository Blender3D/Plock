#!/usr/bin/env python2

import sys, os
import getpass

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, cast, pointer, sizeof
from ctypes import c_void_p, c_uint, c_char_p, c_char, c_int
from ctypes.util import find_library

LIBPAM = CDLL(find_library('pam'))
LIBC = CDLL(find_library('c'))

CALLOC = LIBC.calloc
CALLOC.restype = c_void_p
CALLOC.argtypes = [c_uint, c_uint]

STRDUP = LIBC.strdup
STRDUP.argstypes = [c_char_p]
STRDUP.restype = POINTER(c_char)

class PamHandle(Structure):
  _fields_ = [('handle', c_void_p)]
  
  def __init__(self):
    Structure.__init__(self)
    self.handle = 0

class PamMessage(Structure):  _fields_ = [('msg_style', c_int), ('msg', c_char_p)]
class PamResponse(Structure):  _fields_ = [('resp', c_char_p), ('resp_retcode', c_int)]

CONV_FUNC = CFUNCTYPE(c_int, c_int, POINTER(POINTER(PamMessage)), POINTER(POINTER(PamResponse)), c_void_p)

class PamConv(Structure):  _fields_ = [('conv', CONV_FUNC), ('appdata_ptr', c_void_p)]

PAM_START = LIBPAM.pam_start
PAM_START.restype = c_int
PAM_START.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]

PAM_AUTHENTICATE = LIBPAM.pam_authenticate
PAM_AUTHENTICATE.restype = c_int
PAM_AUTHENTICATE.argtypes = [PamHandle, c_int]


class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    self.centralwidget = QWidget(MainWindow)
    
    self.gridLayout1 = QGridLayout(self.centralwidget)
    self.gridLayout1.addItem(QSpacerItem(629, 239, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 1, 1)
    self.gridLayout1.addItem(QSpacerItem(94, 66, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 1)

    self.unlockFrame = QFrame(self.centralwidget)
    self.unlockFrame.setFrameShape(QFrame.StyledPanel)
    self.unlockFrame.setFrameShadow(QFrame.Raised)

    self.headerLabel = QLabel(self.unlockFrame)
    self.headerLabel.setAlignment(Qt.AlignCenter)

    self.gridLayout2 = QGridLayout(self.unlockFrame)
    self.gridLayout2.addWidget(self.headerLabel, 0, 0, 1, 1)
    
    self.horizontalLayout1 = QHBoxLayout()
    self.horizontalLayout2 = QHBoxLayout()
    
    self.gridLayout2.addLayout(self.horizontalLayout1, 1, 0, 1, 1)
    
    self.passwordLabel = QLabel(self.unlockFrame)
    self.passwordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

    self.horizontalLayout1.addWidget(self.passwordLabel)
    self.passwordTextbox = QLineEdit(self.unlockFrame)
    self.passwordTextbox.setEchoMode(QLineEdit.Password)
    self.unlockButton = QPushButton(self.unlockFrame)
    self.shutdownButton = QPushButton(self.unlockFrame)
    self.rebootButton = QPushButton(self.unlockFrame)
    
    self.horizontalLayout1.addWidget(self.passwordTextbox)

    self.horizontalLayout2.addWidget(self.unlockButton)
    self.horizontalLayout2.addWidget(self.shutdownButton)
    self.horizontalLayout2.addWidget(self.rebootButton)
    
    self.gridLayout2.addLayout(self.horizontalLayout2, 2, 0, 1, 1)
    self.gridLayout1.addWidget(self.unlockFrame, 1, 1, 1, 1)
    self.gridLayout1.addItem(QSpacerItem(86, 66, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 2, 1, 1)
    self.gridLayout1.addItem(QSpacerItem(629, 203, QSizePolicy.Minimum, QSizePolicy.Expanding), 2, 1, 1, 1)

    MainWindow.setCentralWidget(self.centralwidget)

    MainWindow.setWindowTitle('Lock Screen')
    self.headerLabel.setText('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /></head><body><span style="font-size:20pt; font-weight: bold;">The screen has been locked by %username%.</span></body></html>')
    self.passwordLabel.setText('Enter your password:')
    self.unlockButton.setText('Unlock')
    self.shutdownButton.setText('Shutdown')
    self.rebootButton.setText('Reboot')

    QObject.connect(self.passwordTextbox, SIGNAL('returnPressed()'), self.unlockButton.click)
    QMetaObject.connectSlotsByName(MainWindow)



class StartQT4(QMainWindow):
  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.showFullScreen()
    
    self.ui.passwordTextbox.grabKeyboard()
    self.ui.passwordTextbox.grabMouse()
    
    self.ui.headerLabel.setText(self.ui.headerLabel.text().replace('%username%', getpass.getuser()))
    self.connect(self.ui.unlockButton, SIGNAL('clicked()'), self.unlock)
  
  def closeEvent(self, event):
    event.ignore()
  
  def unlock(self):
    @CONV_FUNC
    def my_conv(n_messages, messages, p_response, app_data):
      addr = CALLOC(n_messages, sizeof(PamResponse))
      p_response[0] = cast(addr, POINTER(PamResponse))

      for i in range(n_messages):
        if messages[i].contents.msg_style == 1:
          pw_copy = STRDUP(str(self.ui.passwordTextbox.text()))
          p_response.contents[i].resp = cast(pw_copy, c_char_p)
          p_response.contents[i].resp_retcode = 0
      
      return 0
    
    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    
    if PAM_START('login', getpass.getuser(), pointer(conv), pointer(handle)) != 0 or PAM_AUTHENTICATE(handle, 0) != 0:
      self.ui.passwordTextbox.clear()
    else:
      sys.exit(0)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  lockscreen = StartQT4()
  lockscreen.show()
  
  sys.exit(app.exec_())