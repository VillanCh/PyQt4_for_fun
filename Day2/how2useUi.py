"""How 2 use UI?"""
from PyQt4 import QtGui, QtCore
from day2_basic_use import Ui_MainWindow
import sys
def testfunc():
    print "Hello World"

class Vsniff(Ui_MainWindow,QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        #ui = Ui_MainWindow();
        self.setupUi(self)
        self.connect(self.Start, QtCore.SIGNAL('clicked()'), testfunc)


app = QtGui.QApplication(sys.argv)
mainwindow = Vsniff()
mainwindow.setWindowTitle("Hello I'm title")
mainwindow.show()
sys.exit(app.exec_())