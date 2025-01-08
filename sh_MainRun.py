import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from sh import Ui_Sh

class sh_MainRun(QMainWindow,Ui_Sh):
    def __init__(self,parent =None):
        super(sh_MainRun,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = sh_MainRun()
    myWin.show()
    sys.exit(app.exec_())