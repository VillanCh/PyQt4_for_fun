import sys
from PyQt4 import QtCore, QtGui
"""
class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, flags=0):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("Hello, PyQt World")
        self.resize(300,200)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
"""

class window(QtGui.QMainWindow):
    def __init__(self, parent=None, flags=0):
        super(window,self).__init__()
        self.setWindowTitle("Hello PyQt4, what a great beginning!")
        #add a Qlable
        label = QtGui.QLabel(parent=self)
        label.setText("Hello ?? Do you remember me ?")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(label)
app = QtGui.QApplication(sys.argv)
demo = window()
demo.show()
app.exec_()