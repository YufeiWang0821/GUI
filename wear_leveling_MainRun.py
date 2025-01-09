import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from wear_leveling_function import Ui_WearLeveling  #导入你写的界面类
#from UI import Ui_Form

class wear_leveling_MainRun(QMainWindow,Ui_WearLeveling): 
    def __init__(self,parent =None):
        super(wear_leveling_MainRun,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("磨损均衡")  # 设置左上角标题

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = wear_leveling_MainRun()
    myWin.show()
    sys.exit(app.exec_())    
