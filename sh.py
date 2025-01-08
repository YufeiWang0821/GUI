from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sh(object):
    def setupUi(self, Form, parameter=None):
        Form.setObjectName("Form")
        Form.resize(464, 449)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 401, 41))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 411, 371))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 根据传入的参数来执行逻辑
        if parameter:
            self.run_script(parameter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "脚本运行窗口"))
        self.label.setText(_translate("Form", "当前正在运行"))

    def run_script(self, parameter):
        # 根据传入的参数执行不同的脚本并显示结果
        output = self.execute_script_based_on_param(parameter)
        self.textBrowser.setText(output)
        
    def execute_script_based_on_param(self, parameter):
        # 模拟根据参数执行不同的操作
        if parameter == "script_1":
            return "Running script 1..."
        elif parameter == "script_2":
            return "Running script 2..."
        else:
            return "Unknown script"