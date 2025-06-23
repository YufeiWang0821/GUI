# -*- coding: utf-8 -*-
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from draw import Draw
from datetime import datetime
import re
import os
import json

class Ui_Compiler(object):
    def setupUi(self, Form, parameter=None):
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

        self.parameter = parameter
        self.chip = "MRAM" if self.parameter==16 else "RRAM"

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
        #
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setStyleSheet(
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
        self.horizontalLayout0.addWidget(self.pushButton2)
        #
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
        self.input_line.returnPressed.connect(self.update_image)  # 按下回车时更新图片
        self.left_layout.addWidget(self.input_line)
        #左侧组件设置
        self.image_label.setFixedWidth(leftlayout_width)
        self.info_label.setFixedWidth(leftlayout_width)
        self.input_line.setFixedWidth(leftlayout_width)
        self.horizontalLayout.addLayout(self.left_layout)

        # 热力图组件
        self.figure = plt.figure(0, facecolor="#f5f5f5")
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
        self.pushButton2.clicked.connect(self.show_saved_data) # Show saved data
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.executable = None  # To store the selected executable
        self.predictions = {}
        self.process = QtCore.QProcess(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", f"{self.chip}芯片应用负载运行测试"))
        if self.parameter == 16:
            self.label.setText(_translate("Form", "<center>当前使用<font color='orange'>MRAM</font>芯片运行应用<br>请选择功能</center>"))
        elif self.parameter == 17:
            self.label.setText(_translate("Form", "<center>当前使用<font color='blue'>RRAM</font>芯片运行应用<br>请选择功能</center>"))
        self.radioButton.setText(_translate("Form", "LeNet-5 Inference on CIFAR10"))
        self.radioButton_2.setText(_translate("Form", "FC-3 Inference on MNIST"))
        self.radioButton_3.setText(_translate("Form", "SNN Inference on DVSGesture"))
        self.radioButton_4.setText(_translate("Form", "FC-3 手写数字识别"))
        self.pushButton.setText(_translate("Form", "运行指定功能"))
        self.pushButton2.setText(_translate("Form", "显示保存结果"))
        self.label_2.setText(_translate("Form", "运行结果"))

    def closeEvent(self, event):
        # check if subprocess exists
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.kill_process()

        event.accept()

    def run_selected_dataset(self):
        # 清空之前的画布
        self.figure.clear()
        self.current_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        # Determine which dataset is selected
        if self.radioButton.isChecked():
            self.executable = "../build/bin/lenet5-quan-run-mram" if self.chip == "MRAM" else "../build/bin/lenet5-quan-run-reram"  # Executable for Cifar-10
            self.exe_para=""
            self.app = "LeNet5"
            self.hmsize = 10
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_2.isChecked():
            self.executable = "../build/bin/fc3-quan-run-mram" if self.chip == "MRAM" else "../build/bin/fc3-quan-run-reram"  # Executable for MNIST
            self.exe_para="32 false"
            self.app = "FC3"
            self.hmsize = 10
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_3.isChecked():
            self.executable = "../build/bin/snn-quan-run-mram" if self.chip == "MRAM" else "../build/bin/snn-quan-run-reram"
            self.exe_para="8"
            self.app = "SNN"
            self.hmsize = 11
            self.run_executable(self.executable)
            self.timer.stop()  # 停止定时器
            self.timer_started = False
        elif self.radioButton_4.isChecked():
            self.subWindow = Draw(self.chip)  # 创建子界面实例
            self.subWindow.show()  # 显示子界面
        else:
            self.textBrowser.append("请先选择一个功能")
            return

    def run_executable(self, executable):
        # check if subprocess exists
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.kill_process()

        self.predictions = {}
        # 创建 QProcess
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        print(executable)
        #self.process.start("sudo", [executable])
        if self.app == "LeNet5":
            self.process.start("sudo", [executable])
        else:
            self.process.start("sudo", [executable, self.exe_para])
        self.process.finished.connect(self.on_finished)
        # if not self.timer_started:
        #     print("timer started")
        #     self.timer_started = True
        #     self.timer.start(1000)
        #     self.timer.timeout.connect(self.update_heatmap)

    def on_readyReadStandardOutput(self):
        if self.process == None:
            return
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
        use_saved_pre = False
        # 检查 predictions 是否为空
        if not self.predictions:
            if self.saved_predictions:
                use_saved_pre = True
            else:
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
            self.app = "LeNet5"
        elif self.radioButton_2.isChecked():
            dataset_name = "MNIST"
            self.app = "FC3"
        else:
            self.info_label.setText("错误：当前选项没有可显示图片！")

        # 如果序号合法，显示对应的图片和预测数据
        try:
            image_path = f"data/{dataset_name}/test_{image_index}.png"
        except:
            # self.info_label.setText("SNN has no images")
            pred = self.predictions if not use_saved_pre else self.saved_predictions
            keys = list(pred.keys())
            values = list(pred.values())
            try:
                print("key")
                print(keys[image_index])
            except:
                self.info_label.setText(f"not yet inferred")
                return
            match = re.search(r"(\d+)/(.*)\.txt", keys[image_index])
            print("matchgroups")
            print(match.groups())

            if match:
                id, name = match.groups()
                file_name = "DVSGesture_frames/"+str(id)+"/"+name+".npz"
                data = np.load(file_name)
                frames = data['frames']

                self.info_label.setText(f"{values[image_index]}")
                plt.figure(1)
                plt.clf()
                for i in range(16):
                    plt.imshow(frames[i][0]+frames[i][1], cmap="jet")
                    plt.grid(False)
                    plt.xticks([])
                    plt.yticks([])
                    plt.show()
                    plt.pause(0.1)

            return
        cifar10 = {
            0 : "airplane",
            1 : "automobile",
            2 : "bird",
            3 : "cat",
            4 : "deer",
            5 : "dog",
            6 : "frog",
            7 : "horse",
            8 : "ship",
            9 : "truck"
        }
        try:
            # 尝试加载图片
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                self.info_label.setText(f"错误：无法加载图片 test_{image_index}.png")
                return
            scaled_pixmap = pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
        except Exception as e:
            self.info_label.setText(f"错误：加载图片时出现问题 ({str(e)})")
            return
        # 显示对应的预测数据
        try:
            if(use_saved_pre):
                print("saved predictions")
                prediction_data = self.saved_predictions[f"test_{image_index}.txt"]
            else:
                print("predictions")
                prediction_data = self.predictions[f"test_{image_index}.txt"]
            print(self.app)
            if(self.app == "FC3"):
                self.info_label.setText(f"{prediction_data}")
            elif(self.app == "LeNet5"):
                print("lenet5")
                self.info_label.setText(f"'label': {prediction_data['label']}({cifar10[prediction_data['label']]}),\n'predicted': {prediction_data['predicted']}({cifar10[prediction_data['predicted']]})")
                # self.info_label.setText(f"'label': {cifar10[prediction_data['label']]},\n'predicted': {cifar10[prediction_data['predicted']]}")
        except:
            self.info_label.setText("Not yet inferred.")
            return
        
    def on_finished(self):
        save_file_path = f"{self.app}-{self.current_time}.txt"
        with open(save_file_path, "w", encoding="utf-8") as file:
            json.dump(self.predictions, file, ensure_ascii=False, indent=4)

    def show_saved_data(self):
        if self.radioButton.isChecked():
            self.hmsize = 10
            if self.parameter ==16 or self.parameter ==17:# MRAM saved data
                read_file_path = "LeNet5-2025-01-21-14:23:00.txt"
            else:
                read_file_path = ""
        elif self.radioButton_2.isChecked():
            self.hmsize = 10
            if self.parameter ==16 or self.parameter ==17:
                read_file_path = "FC3-2025-01-21-13:30:12.txt"
            else:
                read_file_path = ""
        elif self.radioButton_3.isChecked():
            self.hmsize = 11
            if self.parameter ==16 or self.parameter ==17:
                read_file_path = "SNN-2025-01-21-14:38:50.txt"
            else:
                read_file_path = ""
        
        # 从 txt 文件读取字典
        print(read_file_path)
        with open(read_file_path, "r", encoding="utf-8") as file:
            self.saved_predictions = json.load(file)
        # 初始化一个10x10的矩阵，表示10个类别的混淆矩阵
        confusion_matrix = np.zeros((self.hmsize, self.hmsize), dtype=int)
        # 遍历每一张图片的预测结果
        for image_name, data in self.saved_predictions.items():
            true_label = data["label"]
            predicted_label = data["predicted"]
            # 更新混淆矩阵的对应位置
            confusion_matrix[true_label][predicted_label] += 1
        # 绘制热力图
        self.draw_heatmap(confusion_matrix)
        sum = 0
        for i in range(self.hmsize):
            sum += confusion_matrix[i][i]
        sum = sum/len(self.saved_predictions)
        print(sum)
        self.textBrowser.append(f"Accuracy: {sum*100:.2f}%")

            
    
    def kill_process(self):
        if self.process:
            pid = self.process.processId()
            print(f"Now killing the subprocess {pid} of compiler window")
            if pid:
                os.system(f"sudo kill -9 {pid}")
            self.process = None