# 输入：整数n，平面上的1个圆心坐标(x,y)和半径r
# 输出：n个圆上点的坐标，这n个点在圆上的位置要均匀隔开（结果输出为*.txt等文本格式和图）
# Submit the python script or notebook to me as well as the outputs.
# 比如，n=5，圆心坐标为(0,0)，半径为1，那么要求位于该圆上的5个点的坐标，这5个点
# 在圆上的位置均匀隔开。注意，这只是个举例，你的程序不能只针对这个例子，而是可以针对任意n和圆心、半径。

import numpy as np
import matplotlib.pyplot as plt

# 定义函数来生成均匀分布在圆上的点
def generate_circle_points(x, y, r, n):
    # 均匀分布的角度
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    points = [(x + r * np.cos(angle), y + r * np.sin(angle)) for angle in angles]
    return points

# 保存文件
def save_points_to_txt(points, filename):
    with open(filename, "w") as f:
        for point in points:
            f.write(f'{point[0]:.6f},{point[1]:.6f}\n')


# 保存图像
def plot_circle_points(x, y, r, points, filename):
    fig, ax = plt.subplots()
    circle = plt.Circle((x, y), r, color="r", fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal', 'box')

    # 绘制点并且设置为红色
    xs, ys = zip(*points)
    ax.plot(xs, ys, 'ro')

    # 设置图像范围
    ax.set_xlim(x - r - 1, x + r + 1)
    ax.set_ylim(x - r - 1, x + r + 1)

    plt.grid(True)
    plt.title(f'{n} Points on Circle with center ({x},{y} and radius {r})')
    plt.savefig(filename)
    plt.show()


# 输入参数
n = int(input("请输入点的个数n："))
x = float(input("请输入圆心x的坐标："))
y = float(input("请输入圆心y的坐标："))
r = float(input("请输入圆的半径r："))

# 生成圆上点的坐标
points = generate_circle_points(x, y, r, n)

# 保存坐标为txt
txt_filename = 'circle_points.txt'
save_points_to_txt(points, txt_filename)
print(f'坐标已经保存到{txt_filename}中')

# 绘制图像保存为图片
img_filename = 'circle_points.png'
plot_circle_points(x, y, r, points, img_filename)
print(f'图像已经保存到{img_filename}文件中')
