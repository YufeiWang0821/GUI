import sys
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QImage, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsScene, QGraphicsView
from datetime import datetime
import torch
from torchvision import transforms
import subprocess
from PIL import Image
import re

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
            # painter.setPen(QPen(QColor(255,255,255,255), 25, Qt.SolidLine))
            painter.setPen(QPen(Qt.white, 25, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        pass

    def clear(self):
        self.image.fill(Qt.black)
        self.update()

    def process_and_save(self):
        # 保存QImage图像
        self.image.save("output_image.png")

        # 读取保存的PNG文件
        pil_image = Image.open("output_image.png").convert('L').resize((28,28))
        img_array = np.array(pil_image, dtype=np.float32)
        
        # process the image, resize and stuff
        img_array = (img_array*255.0)/img_array.max()
        img_array = img_array/255.0
        img_array = 2*img_array - 1
        img_tensor = torch.tensor(img_array)
        np.savetxt("image_matrix.txt", img_tensor.numpy(), fmt="%.4f", delimiter=" ")

        # quantitize the tensor for fc3
        scale_tensor = torch.tensor([0.0311])
        mnist_tensor = ((img_tensor / scale_tensor)).round().to(torch.int8)
        np.savetxt("output_matrix.txt", mnist_tensor.numpy(), fmt="%d", delimiter=" ")

        # try to convert mnist_tensor back to png
        tensor_normalized = (((mnist_tensor+32)/64)*255).clamp(0, 255)
        array_normalized = tensor_normalized.numpy().astype(np.int8)
        image_normalized = Image.fromarray(array_normalized, mode='L')
        image_normalized.save("output_image_28.png")


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
        self.current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.drawing_area.process_and_save()
        self.info_label.setText(f"图像已保存为图片并处理成矩阵 ({self.current_time})")

    def recognize(self):
        #调用程序进行识别
        # 调用可执行文件并获取输出
        exe_file = '../build/bin/fc3-quan-run'  # 替换为实际可执行文件路径
        try:
            result = subprocess.run(['sudo', exe_file, 'true'], capture_output=True, text=True, check=True)
            output = result.stdout  # 获取可执行文件的标准输出
            predicted_match = re.search(r'Predicted:\s(\d+)', output)
            predicted_match_value = predicted_match.group(1) if predicted_match else "unkown"
            self.output_label.setText(f"数字识别为：{predicted_match_value} ({self.current_time})")
        except subprocess.CalledProcessError as e:
            self.output_label.setText(f"执行错误：{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Draw()
    window.show()
    sys.exit(app.exec_())
