#! /usr/bin/env python
__author__ = 'RBH'

import sys
from PyQt4 import QtCore, QtGui, uic


class ImageDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = uic.loadUi("./mainWindow.ui")
        self.ui.show()

        # Make some local modifications.
        self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.connect(self.ui.okButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("accept()"))
        self.connect(self.ui.cancelButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

app = QtGui.QApplication(sys.argv)
window = ImageDialog()
sys.exit(app.exec_())