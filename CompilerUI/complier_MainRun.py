import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
# from Functions import Ui_Compiler
# from FunctionsTest import Ui_Compiler
#from CompilerUI.HeatmapTest import Ui_Compiler
from Outlook import Ui_Compiler

class compiler_MainRun(QMainWindow,Ui_Compiler):
    def __init__(self,parent =None):
        super(compiler_MainRun,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = compiler_MainRun()
    myWin.show()
    sys.exit(app.exec_())