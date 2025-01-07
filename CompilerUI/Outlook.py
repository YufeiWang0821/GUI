# -*- coding: utf-8 -*-
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_Compiler(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 800)
        Form.setStyleSheet("background-color: #f5f5f5;")  # 设置背景色为浅灰色
        Form.setMinimumSize(QtCore.QSize(700, 800))
        Form.setMaximumSize(QtCore.QSize(700, 800))

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 600, 700))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(15)  # 增加控件之间的间距
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 标题
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)  # 增加标题字体大小
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #333333;")  # 标题颜色为深灰色
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        # 单选按钮
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: #555555;")  # 单选按钮颜色
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton, 0, QtCore.Qt.AlignHCenter)

        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: #555555;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)

        # 运行按钮布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
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
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # 运行结果标签
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #333333;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)

        # 热力图组件
        self.figure = plt.figure(facecolor="#f5f5f5")
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_2.addWidget(self.canvas)

        # 输出区域
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; padding: 10px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setMinimumHeight(200)
        self.verticalLayout_2.addWidget(self.textBrowser)

        # 设置文本内容和按钮事件
        self.retranslateUi(Form)
        #self.pushButton.clicked.connect(self.run_selected_dataset)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.executable = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "板卡GUI"))
        self.label.setText(_translate("Form", "请选择功能"))
        self.radioButton.setText(_translate("Form", "LeNet-5 Inference on CIFAR10"))
        self.radioButton_2.setText(_translate("Form", "FC-3 Inference on MNIST"))
        self.pushButton.setText(_translate("Form", "运行指定功能"))
        self.label_2.setText(_translate("Form", "运行结果"))