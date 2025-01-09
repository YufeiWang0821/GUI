# -*- coding: utf-8 -*-
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from draw import Draw
import re

class Ui_Compiler(object):
    def setupUi(self, Form):
        ui_width = 900
        ui_height = 1200
        a_width = 800
        a_height = 1100
        leftlayout_width = 350
        Form.setObjectName("Form")
        Form.resize(ui_width, ui_height)
        Form.setStyleSheet("background-color: #f5f5f5;")  # 设置背景色为浅灰色
        Form.setMinimumSize(QtCore.QSize(ui_width, ui_height))
        Form.setMaximumSize(QtCore.QSize(ui_width, ui_height))
        self.setGeometry(500, 500, a_width, a_height)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)  # 每秒刷新一次
        self.timer_started = False

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, a_width, a_height))
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

        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: #555555;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)

        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: #555555;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4, 0, QtCore.Qt.AlignHCenter)

        # 运行按钮布局
        self.horizontalLayout0 = QtWidgets.QHBoxLayout()
        self.horizontalLayout0.setObjectName("horizontalLayout")
        
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
        self.horizontalLayout0.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout0)

        # 运行结果标签
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #333333;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # 新增的左侧组件部分
        self.left_layout = QtWidgets.QVBoxLayout()
        # 图片显示框
        self.image_label = QtWidgets.QLabel(self.layoutWidget)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setMinimumHeight(100)
        self.left_layout.addWidget(self.image_label)
        # 信息框
        self.info_label = QtWidgets.QLabel(self.layoutWidget)
        self.left_layout.addWidget(self.info_label)
        # 输入框
        self.input_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_line.setPlaceholderText("请输入图片序号")
        font.setPointSize(10)
        self.input_line.setFont(font)
        self.input_line.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; padding: 10px;")
        self.input_line.textChanged.connect(self.update_image)  # 当输入框内容改变时更新图片
        self.left_layout.addWidget(self.input_line)
        #左侧组件设置
        self.image_label.setFixedWidth(leftlayout_width)
        self.info_label.setFixedWidth(leftlayout_width)
        self.input_line.setFixedWidth(leftlayout_width)
        self.horizontalLayout.addLayout(self.left_layout)

        # 热力图组件
        self.figure = plt.figure(facecolor="#f5f5f5")
        self.canvas = FigureCanvas(self.figure)
        # 将热力图组件放入一个QWidget容器中
        self.canvas_widget = QtWidgets.QWidget(self.layoutWidget)
        self.canvas_widget.setMinimumHeight(400)
        self.canvas_layout = QtWidgets.QVBoxLayout(self.canvas_widget)
        self.canvas_layout.addWidget(self.canvas)
        # 将canvas的QWidget容器加入到水平布局
        self.horizontalLayout.addWidget(self.canvas_widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # 输出区域
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; padding: 10px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setMaximumHeight(300)
        self.verticalLayout_2.addWidget(self.textBrowser)

        # 设置文本内容和按钮事件
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.run_selected_dataset)  # Connect button to method
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.executable = None  # To store the selected executable

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "板卡GUI"))
        self.label.setText(_translate("Form", "请选择功能"))
        self.radioButton.setText(_translate("Form", "LeNet-5 Inference on CIFAR10"))
        self.radioButton_2.setText(_translate("Form", "FC-3 Inference on MNIST"))
        self.radioButton_3.setText(_translate("Form", "SNN Inference"))
        self.radioButton_4.setText(_translate("Form", "FC-3 手写数字识别"))
        self.pushButton.setText(_translate("Form", "运行指定功能"))
        self.label_2.setText(_translate("Form", "运行结果"))

    def run_selected_dataset(self):
        # Determine which dataset is selected
        if self.radioButton.isChecked():
            self.executable = "../build/bin/lenet5-quan-run"  # Executable for Cifar-10
            self.hmsize = 10
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_2.isChecked():
            self.executable = "../build/bin/fc3-quan-run"  # Executable for MNIST
            self.hmsize = 10
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_3.isChecked():
            self.executable = "../build/bin/snn-quan-run"
            self.hmsize = 11
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_4.isChecked():
            self.subWindow = Draw()  # 创建子界面实例
            self.subWindow.show()  # 显示子界面
        else:
            self.textBrowser.append("请先选择一个功能")
            return

    def run_executable(self, executable):
        self.predictions = {}
        # 创建 QProcess
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.start("sudo", [executable])
        # if not self.timer_started:
        #     print("timer started")
        #     self.timer_started = True
        #     self.timer.start(1000)
        #     self.timer.timeout.connect(self.update_heatmap)

    def on_readyReadStandardOutput(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.textBrowser.append(output)  # 实时更新textBrowser
         # 使用正则表达式解析每行输出
        lines = output.splitlines()
        for line in lines:
            match = re.match(r"Image name: (\S+)\s+Label: (\d+)\s+Predicted: (\d+)", line)
            if match:
                image_name, label, predicted = match.groups()
                self.predictions[image_name] = {"label": int(label), "predicted": int(predicted)}
                if not self.timer_started:
                    print("timer started")
                    self.timer_started = True
                    self.timer.start(1000)
                    self.timer.timeout.connect(self.update_heatmap)

    def update_heatmap(self):
        print(f"update_heatmap & size of predictions now {len(self.predictions)}")
        # 假设 self.predictions 字典存储了每张图片的预测情况
        # 每项存储结构 {'label': true_label, 'predicted': predicted_label}
        
        # 初始化一个10x10的矩阵，表示10个类别的混淆矩阵
        confusion_matrix = np.zeros((self.hmsize, self.hmsize), dtype=int)

        # 遍历每一张图片的预测结果
        for image_name, data in self.predictions.items():
            true_label = data["label"]
            predicted_label = data["predicted"]
            
            # 更新混淆矩阵的对应位置
            confusion_matrix[true_label][predicted_label] += 1

        # 绘制热力图
        self.draw_heatmap(confusion_matrix)

    def draw_heatmap(self, heatmap):
        # 清空之前的画布
        self.figure.clear()
        # 绘制热力图
        ax = self.figure.add_subplot(111)
        cax = ax.matshow(heatmap, cmap='Oranges')
        # 添加颜色条
        plt.colorbar(cax)
        # 设置刻度
        ax.set_xticks(np.arange(self.hmsize))
        ax.set_yticks(np.arange(self.hmsize))
        ax.set_title("Heatmap")
        for (i, j), value in np.ndenumerate(heatmap):
            ax.text(j, i, f'{value}', ha='center', va='center', color='black', fontsize=7)
        # 设置边距以使图形水平居中
        plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)
        # 显示图形
        self.canvas.draw()
    
    def update_image(self):
        # 清空图片
        self.image_label.clear()

        # 检查 predictions 是否为空
        if not self.predictions:
            self.info_label.setText("错误：没有可用的预测数据！")
            return
        # 获取用户输入的图片序号
        try:
            image_index = int(self.input_line.text())  # 获取输入框中的序号，并尝试转换为整数
        except ValueError:
            self.info_label.setText("错误：请输入有效的数字序号！")
            return
        # 检查序号是否合法
        if self.radioButton.isChecked():
            dataset_name = "CIFAR10"
        elif self.radioButton_2.isChecked():
            dataset_name = "MNIST"
        else:
            self.info_label.setText("错误：当前选项没有可显示图片！")

        # 如果序号合法，显示对应的图片和预测数据
        image_path = f"data/{dataset_name}/test_{image_index}.png"
        try:
            # 尝试加载图片
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                self.info_label.setText(f"错误：无法加载图片 test_{image_index}.png")
                return
            self.image_label.setPixmap(pixmap)
        except Exception as e:
            self.info_label.setText(f"错误：加载图片时出现问题 ({str(e)})")
            return
        # 显示对应的预测数据
        try:
            prediction_data = self.predictions[f"test_{image_index}.txt"]
            self.info_label.setText(f"{prediction_data}")
        except:
            self.info_label.setText("Not yet inferred.")
            return