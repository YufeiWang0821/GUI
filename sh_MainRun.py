import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from sh import Ui_Sh

class sh_MainRun(QMainWindow, Ui_Sh):
    def __init__(self, parameter=None, parent=None):
        super(sh_MainRun, self).__init__(parent)
        self.setupUi(self, parameter)  # 传递参数给 Ui_Sh

if __name__ == "__main__":
    app = QApplication(sys.argv)
    parameter = 0
    myWin = sh_MainRun(parameter)  # 创建 sh_MainRun 并传递参数
    myWin.show()
    sys.exit(app.exec_())