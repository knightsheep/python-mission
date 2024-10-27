import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

"""
未采用七段式进行绘制
"""

# 图片路径，采用相对路径
image_path = "background.jpg"
image = cv.imread(image_path)

# 设置字体与线性
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
line = cv.LINE_AA

# 调用putText函数进行绘制数字
cv.putText(image,'69',(500,2500),font,50,(255,255,255),50,line)

# 将图片的颜色空间从BGR转换为RGB
# OpenCV默认使用BGR颜色格式（蓝-绿-红），而matplotlib使用的是RGB格式（红-绿-蓝）
# 因此为了在matplotlib中正确显示颜色，需要进行颜色空间的转换
image_rgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)

# 显示图形
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

