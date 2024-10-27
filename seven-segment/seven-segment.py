# -*- coding: utf-8 -*-
# @Time: 2024/10/9 00:54
# @Author: dayu
"""
采用七段式进行绘制数字
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 创建一个3000x4000像素的背景图像（白色背景）
image1 = np.ones((4000, 3000, 3), dtype=np.uint8) * 255  # 3000x4000 白色背景
image2 = cv.imread("background.jpg")

# 定义线段的宽度和颜色
segment_width = 50  # 线段的宽度，适合于高分辨率
color = (255, 255, 255)

# 七段数码管的段定义
# 每个段由两点确定，分别是 (x1, y1) 和 (x2, y2)，我们以相对坐标（居中）来计算

# 数字 6 的线段坐标 (相对于起始点)
six_segments = [
    ((0, 0), (220, segment_width)),  # 顶部横线
    ((0, 300), (200, 300 + segment_width)),  # 中间横线
    ((0, 600), (250, 600 + segment_width)),  # 底部横线
    ((0, 0), (segment_width, 300)),  # 左上竖线
    ((0, 300), (segment_width, 600)),  # 左下竖线
    ((200, 300), (200 + segment_width, 600))  # 右下竖线
]

# 数字 9 的线段坐标 (相对于起始点)
nine_segments = [
    ((300, 0), (500, segment_width)),  # 顶部横线
    ((300, 300), (500, 300 + segment_width)),  # 中间横线
    ((300, 600), (550, 600 + segment_width)),  # 底部横线
    ((300, 0), (300 + segment_width, 300)),  # 左上竖线
    ((500, 0), (500 + segment_width, 300)),  # 右上竖线
    ((500, 300), (500 + segment_width, 600))  # 右下竖线
]

# 计算居中的起始位置，假设七段式字符区域总大小是500x600（宽x高）
start_x = (3000 - 500) // 2  # 横向居中起始点
start_y = (4000 - 600) // 2  # 纵向居中起始点

# 绘制数字 6 的七段显示
for (start, end) in six_segments:
    x1, y1 = start
    x2, y2 = end
    # 在图像上绘制对应的矩形段，位置需要偏移到居中区域
    cv.rectangle(image2, (start_x + x1, start_y + y1), (start_x + x2, start_y + y2), color, -1)

# 绘制数字 9 的七段显示
for (start, end) in nine_segments:
    x1, y1 = start
    x2, y2 = end
    # 同样绘制对应的矩形段，位置偏移到居中区域
    cv.rectangle(image2, (start_x + x1, start_y + y1), (start_x + x2, start_y + y2), color, -1)

# 将图像从BGR转换为RGB，以便通过matplotlib显示
image_rgb = cv.cvtColor(image2, cv.COLOR_BGR2RGB)

# 使用matplotlib显示图片
plt.imshow(image_rgb)
plt.axis('off')  # 关闭坐标轴
plt.show()
