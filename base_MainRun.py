import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
#from base import Ui_base
from Ui_base_old import Ui_base

class base_MainRun(QMainWindow,Ui_base):
    def __init__(self,parent =None):
        super(base_MainRun,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = base_MainRun()
    myWin.show()
    sys.exit(app.exec_())