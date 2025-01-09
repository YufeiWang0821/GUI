import sys
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QImage, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsScene, QGraphicsView
from datetime import datetime
import torch
import subprocess
from PIL import Image

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("手写数字绘制")
        self.setFixedSize(300, 300)
        self.last_point = QPoint()
        self.image = QImage(self.size(), QImage.Format_RGB888)
        self.image.fill(Qt.black)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.white, 5, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        pass

    def clear(self):
        self.image.fill(Qt.black)
        self.update()

    # def gamma_correction(image, gamma=1.2):
    #     lut = np.array([((i/225.0)** gamma)*255 for i in range(256)], dtype=np.unit8)
    #     return image.point(lut)

    # def process_and_save(self):
    #     self.image.save("output_image.png")
        

    #     # 将绘制区域缩放至28x28
    #     scaled_image = self.image.scaled(28, 28, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #     scaled_image = self.gamma_correction(scaled_image)
    #     scaled_image.save("scaled_image.png")
    #     # 将图像转换为灰度图像
    #     gray_image = scaled_image.convertToFormat(QImage.Format_Grayscale8)
    #     gray_image.save("gray_image.png")
    #     width = gray_image.width()
    #     height = gray_image.height()
        
    #     # 从QImage获取像素数据
    #     pixels = np.array([gray_image.pixel(x, y) & 0xFF for y in range(height) for x in range(width)])
    #     pixels = pixels.reshape((height, width))
        
    #     # 将像素值归一化到[-1, 1]范围，黑色是-1，白色是1
    #     pixels = (pixels / 127.5) - 1.0  # 将像素值从[0, 255]转换到[-1, 1]
        
    #     # 将数据保存为MNIST格式，可以使用torch保存为Tensor
    #     mnist_tensor = torch.tensor(pixels, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # 添加batch和channel维度
    #     print(mnist_tensor.shape)
    #     np.savetxt("image_matrix.txt", mnist_tensor.squeeze().numpy(), fmt="%.4f", delimiter=" ")
        
    
    def process_and_save(self):
        # 保存QImage图像
        self.image.save("output_image.png")
        # 读取保存的PNG文件，转换为PIL图像
        pil_image = Image.open("output_image.png")
        # 将图像缩放至28x28
        scaled_image = pil_image.resize((28, 28), Image.ANTIALIAS)
        # 转换为灰度图像
        gray_image = scaled_image.convert("L")
        # 转换为NumPy数组
        pixels = np.array(gray_image)
        # 将像素值归一化到[-1, 1]范围，黑色是-1，白色是1
        pixels = (pixels / 127.5) - 1.0  # 将像素值从[0, 255]转换到[-1, 1]
        # 将数据保存为MNIST格式，可以使用torch保存为Tensor
        mnist_tensor = torch.tensor(pixels, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # 添加batch和channel维度
        print(mnist_tensor.shape)
        # 保存数据到文本文件
        np.savetxt("image_matrix.txt", mnist_tensor.squeeze().numpy(), fmt="%.4f", delimiter=" ")

        mnist_tensor = (mnist_tensor / 0.0311).round().to(torch.int8)
        print(mnist_tensor.shape)
        np.savetxt("output_matrix.txt", mnist_tensor.squeeze().numpy(), fmt="%d", delimiter=" ")




class Draw(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("手写数字识别")
        self.setGeometry(1000, 1000, 500, 500)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)

        # 初始化控件
        self.drawing_area = DrawingArea()
        self.confirm_button = QPushButton("确认")
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet(
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
        self.recgonize_button = QPushButton("识别")
        self.recgonize_button.setFont(font)
        self.recgonize_button.setStyleSheet(
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
        self.clear_button = QPushButton("清除")
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet(
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
        self.info_label = QLabel("请在框内绘制数字")
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("color: #333333;")
        self.output_label = QLabel("数字识别为：")
        self.output_label.setFont(font)
        self.output_label.setStyleSheet("color: #333333;")

        self.confirm_button.clicked.connect(self.on_confirm)
        self.recgonize_button.clicked.connect(self.recognize)
        self.clear_button.clicked.connect(self.drawing_area.clear)

        layout = QVBoxLayout()
        layout.addWidget(self.drawing_area)
        layout.addWidget(self.info_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.recgonize_button)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

    def on_confirm(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.drawing_area.process_and_save()
        self.info_label.setText(f"图像已保存为图片并处理成矩阵 ({current_time})")

    def recognize(self):
        #调用程序进行识别
        # 调用可执行文件并获取输出
        exe_file = '../build/bin/fc3-quan-run'  # 替换为实际可执行文件路径
        try:
            result = subprocess.run(['sudo', exe_file, 'true'], capture_output=True, text=True, check=True)
            output = result.stdout  # 获取可执行文件的标准输出
            self.output_label.setText(f"数字识别为：{output[-1]}")
        except subprocess.CalledProcessError as e:
            self.output_label.setText(f"执行错误：{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Draw()
    window.show()
    sys.exit(app.exec_())
