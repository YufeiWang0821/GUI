import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_wear_leveling import Ui_Form  #导入你写的界面类
 
 
class MyMainWindow(QMainWindow,Ui_Form): 
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())    
