"""How 2 use UI?"""
from scapy.all import *
from PyQt4 import QtGui, QtCore
from day2_basic_use import Ui_MainWindow
import sys

txt = ""

def handler_pck(pkt):
    global txt
    try:
        if pkt[TCP].payload:
            txt = pkt[TCP].payload         
    except:
        pass
def testfunc():
    print "Hello World"
    sniff(prn=handler_pck)

class Vsniff(Ui_MainWindow,QtGui.QMainWindow):
    def __init__(self):
        global txt
        QtGui.QMainWindow.__init__(self)
        
        #ui = Ui_MainWindow();
        self.setupUi(self)
        self.connect(self.Start, QtCore.SIGNAL('clicked()'), testfunc)



app = QtGui.QApplication(sys.argv)
mainwindow = Vsniff()
mainwindow.setWindowTitle("Hello I'm title")
txt_content = QtGui.QTextDocument(mainwindow)
txt_content.setPlainText(QtCore.QString("Hello TextBrowser"))
mainwindow.textBrowser.setDocument(txt_content)
mainwindow.show()
sys.exit(app.exec_())