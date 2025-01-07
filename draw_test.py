import sys
import numpy as np
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QImage, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsScene, QGraphicsView
from datetime import datetime
import torch
from PIL import Image

class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("手写数字绘制")
        self.setFixedSize(300, 300)
        self.last_point = QPoint()
        self.image = QImage(self.size(), QImage.Format_RGB888)
        self.image.fill(Qt.white)  # 设置背景为白色

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        pass

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    # def save_image(self):
    #     pixmap = QPixmap(self.size())
    #     self.render(pixmap)
    #     pixmap.save("drawing.png", "PNG")  # 保存图像为PNG格式

    def process_and_save(self):
        self.image.save("output_image.png")

        # 将绘制区域缩放至28x28
        scaled_image = self.image.scaled(28, 28, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 将QImage转换为NumPy数组
        # 注意QImage.pixelFormat()为QImage.Format_RGB888
        scaled_image_array = np.array([
            scaled_image.pixel(x, y) & 0xFF for y in range(28) for x in range(28)
        ], dtype=np.uint8)  # 这里的y, x顺序确保读取时按正确方向存储数据

        # 将scaled_image_array转换为float32类型
        scaled_image_array = scaled_image_array.astype(np.float32)

        # 进行缩放处理（例如，除以某个值进行标准化）
        scaled_image_array = (scaled_image_array / 0.0311).round().astype(np.int8)

        # 重新整形为28x28的矩阵
        pixels = scaled_image_array.reshape(28, 28)

        # 保存矩阵到txt文件
        np.savetxt('output_matrix.txt', pixels, fmt='%d')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("手写数字识别")
        self.setGeometry(100, 100, 400, 400)

        # 初始化控件
        self.drawing_area = DrawingArea()
        self.confirm_button = QPushButton("确认")
        self.clear_button = QPushButton("清除")
        self.info_label = QLabel("请在框内绘制数字")

        self.confirm_button.clicked.connect(self.on_confirm)
        self.clear_button.clicked.connect(self.drawing_area.clear)

        layout = QVBoxLayout()
        layout.addWidget(self.drawing_area)
        layout.addWidget(self.info_label)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

    def on_confirm(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.drawing_area.process_and_save()
        self.info_label.setText(f"图像已保存为图片并处理成矩阵 ({current_time})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
