# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\24532\Desktop\GUI\base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#, QMessageBox, QDialog
#调用各个子界面
from sh_MainRun import sh_MainRun
from complier_MainRun import compiler_MainRun
#from WearLevelingUI.main import myWin


class Ui_base(object):
    def setupUi(self, Form):
        ui_width = 800
        ui_height = 1200
        a_width = 400
        a_height = 800
        Form.setObjectName("Form")
        Form.resize(ui_width, ui_height)
        Form.setMinimumSize(QtCore.QSize(ui_width, ui_height))
        Form.setMaximumSize(QtCore.QSize(ui_width, ui_height))


        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        Form.setFont(font)

        # 设置背景色为浅灰色
        Form.setStyleSheet("background-color: #f5f5f5;")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 50, a_width, a_height))
        self.layoutWidget.setObjectName("layoutWidget")

        # 总的layout
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)  # 控件之间增加间距
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        #
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)  # 设置标签水平居中
        self.label.setStyleSheet("color: #333333;")  # 设置文字颜色为深灰色
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        #
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_4)
        #
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_5)
        #
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_6)
        #
        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_7)
        #
        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_8)
        #
        self.radioButton_9 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_9.setStyleSheet("color: #333333;")
        self.verticalLayout.addWidget(self.radioButton_9)
        #
        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter)  # 设置标签水平居中
        self.label_2.setStyleSheet("color: #333333;")  # 设置文字颜色为深灰色
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        #
        self.radioButton_12 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_12.setStyleSheet("color: #333333;")
        self.verticalLayout_2.addWidget(self.radioButton_12)
        #
        self.radioButton_11 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_11.setStyleSheet("color: #333333;")
        self.verticalLayout_2.addWidget(self.radioButton_11)
        #
        self.radioButton_10 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_10.setStyleSheet("color: #333333;")
        self.verticalLayout_2.addWidget(self.radioButton_10)
        #
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("color: #333333;")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        #
        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)  # 设置标签水平居中
        self.label_3.setStyleSheet("color: #333333;")  # 设置文字颜色为深灰色
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        #
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("color: #333333;")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        #
        self.radioButton_13 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_13.setStyleSheet("color: #333333;")
        self.verticalLayout_3.addWidget(self.radioButton_13)
        #
        self.radioButton_14 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_14.setStyleSheet("color: #333333;")
        self.verticalLayout_3.addWidget(self.radioButton_14)
        #
        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter)  # 设置标签水平居中
        self.label_5.setStyleSheet("color: #333333;")  # 设置文字颜色为深灰色
        self.verticalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        #
        self.radioButton_15 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_15.setStyleSheet("color: #333333;")
        self.verticalLayout_4.addWidget(self.radioButton_15)
        #
        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter)  # 设置标签水平居中
        self.label_4.setStyleSheet("color: #333333;")  # 设置文字颜色为深灰色
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        #
        self.radioButton_16 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_16.setStyleSheet("color: #333333;")
        self.verticalLayout_5.addWidget(self.radioButton_16)
        #
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )
        self.verticalLayout_6.addWidget(self.pushButton)

        self.label.setFont(font)
        self.radioButton_4.setFont(font)
        self.radioButton_5.setFont(font)
        self.radioButton_6.setFont(font)
        self.radioButton_7.setFont(font)
        self.radioButton_8.setFont(font)
        self.radioButton_9.setFont(font)
        self.label_2.setFont(font)
        self.radioButton_12.setFont(font)
        self.radioButton_11.setFont(font)
        self.radioButton_10.setFont(font)
        self.radioButton_3.setFont(font)
        self.label_3.setFont(font)
        self.radioButton_2.setFont(font)
        self.radioButton_13.setFont(font)
        self.radioButton_14.setFont(font)
        self.label_5.setFont(font)
        self.radioButton_15.setFont(font)
        self.label_4.setFont(font)
        self.radioButton_16.setFont(font)
        self.pushButton.setFont(font)

        # button集合
        self.button_group = QtWidgets.QButtonGroup(Form)
        self.button_group.addButton(self.radioButton_2, 2)
        self.button_group.addButton(self.radioButton_3, 3)
        self.button_group.addButton(self.radioButton_4, 4)
        self.button_group.addButton(self.radioButton_5, 5)
        self.button_group.addButton(self.radioButton_6, 6)
        self.button_group.addButton(self.radioButton_7, 7)
        self.button_group.addButton(self.radioButton_8, 8)
        self.button_group.addButton(self.radioButton_9, 9)
        self.button_group.addButton(self.radioButton_10, 10)
        self.button_group.addButton(self.radioButton_11, 11)
        self.button_group.addButton(self.radioButton_12, 12)
        self.button_group.addButton(self.radioButton_13, 13)
        self.button_group.addButton(self.radioButton_14, 14)
        self.button_group.addButton(self.radioButton_15, 15)
        self.button_group.addButton(self.radioButton_16, 16)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.on_push_button_click)
        self.button_group.buttonClicked.connect(self.on_radio_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "测试项选择"))
        self.label.setText(_translate("Form", "MRAM芯片"))
        self.radioButton_4.setText(_translate("Form", "容量"))
        self.radioButton_5.setText(_translate("Form", "1-8bit位宽乘加计算"))
        self.radioButton_6.setText(_translate("Form", "算力"))
        self.radioButton_7.setText(_translate("Form", "单阵列核心计算能效"))
        self.radioButton_8.setText(_translate("Form", "全芯片处理能效"))
        self.radioButton_9.setText(_translate("Form", "与GPU的能效对比"))
        self.label_2.setText(_translate("Form", "RRAM芯片"))
        self.radioButton_12.setText(_translate("Form", "容量"))
        self.radioButton_11.setText(_translate("Form", "1、8、16bit位宽乘加计算"))
        self.radioButton_10.setText(_translate("Form", "算力"))
        self.radioButton_3.setText(_translate("Form", "能效"))
        self.label_3.setText(_translate("Form", "IR-Drop"))
        self.radioButton_2.setText(_translate("Form", "Binary FC-3算法识别准确率"))
        self.radioButton_13.setText(_translate("Form", "Binary LeNet-5算法识别准确率"))
        self.radioButton_14.setText(_translate("Form", "Naive Bayes算法识别准确率"))
        self.label_5.setText(_translate("Form", "系统寿命与通信开销"))
        self.radioButton_15.setText(_translate("Form", "测试"))
        self.label_4.setText(_translate("Form", "编译器"))
        self.radioButton_16.setText(_translate("Form", "负载测试"))
        self.pushButton.setText(_translate("Form", "开始测试"))

    # 判断应该调用哪个子窗口
    def on_radio_button_clicked(self, button):
        chosen_id = self.button_group.id(button)
        if chosen_id == 15:
            self.chosen_Ui = 1
        elif chosen_id == 16:
            self.chosen_Ui = 2
        elif chosen_id in range(2,15):
            self.chosen_Ui = 0
            self.shpara = chosen_id
        else:
            self.chosen_Ui = -1
        
    def on_push_button_click(self):
        print(self.chosen_Ui)
        # 根据选中的 RadioButton 创建对应的窗口实例
        if self.chosen_Ui == 0:# 调用脚本窗口
            window_class = sh_MainRun(parameter=self.shpara)
        elif self.chosen_Ui == 1:# 调用磨损均衡窗口
            window_class = compiler_MainRun()
        elif self.chosen_Ui == 2:# 调用编译器窗口
            window_class = compiler_MainRun()
        # else:
        #     QMessageBox.warning(None, "选择提示", "请先选择一个选项！")
        #     return
        # 调用一个通用的显示窗口方法
        if(self.chosen_Ui != -1):
            self.show_window(window_class)

    def show_window(self, window_class):
        # 创建窗口实例
        # window = QtWidgets.QDialog()
        # ui = window_class()  # 创建对应的窗口 UI 实例
        # ui.setupUi(window)  # 设置窗口的 UI
        # window.exec_()  # 弹出窗口，阻塞当前窗口，直到关闭
        self.subWindow = window_class
        self.subWindow.show()