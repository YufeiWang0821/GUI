import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_wear_leveling import Ui_WearLeveling  #导入你写的界面类
#from UI import Ui_Form
 
class MyMainWindow(QMainWindow,Ui_WearLeveling): 
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("磨损均衡")  # 设置左上角标题

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())    
