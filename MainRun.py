import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
# from Functions import Ui_Form
from FunctionsTest import Ui_Form
#from HeatmapTest import Ui_Form
#from Outlook import Ui_Form

class MyMainWindow(QMainWindow,Ui_Form):
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())