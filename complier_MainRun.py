import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
#from compiler import Ui_Compiler
from compiler_functions_new import Ui_Compiler
#from HeatmapTest import Ui_Compiler

class compiler_MainRun(QMainWindow,Ui_Compiler):
    def __init__(self,parent =None):
        super(compiler_MainRun,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = compiler_MainRun()
    myWin.show()
    sys.exit(app.exec_())