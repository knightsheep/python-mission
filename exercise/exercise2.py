# Exercise2（25分）:
# 输入：平面上n个三角形的三个顶点坐标和m个任意点的坐标
# 输出：m个任意点中位于三角形内（包含恰好在边上）的个数
# Submit the python script or notebook to me as well as the outputs.
# 比如，右侧的平面内有2个三角形，其顶点坐标为已知，m个任意点的坐标也已知，问这m个点中有多少位于这2个三角形内，需明确位于每个三角形内的点的个数。


import numpy as np

# 计算三角形的面积
def triangle_area(p1, p2, p3):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)

# 判断点是否在三角形内（包含边上）
def is_point_in_triangle(pt, p1, p2, p3):
    # 三角形整体面积
    A = triangle_area(p1, p2, p3)

    # 三个小三角形的面积
    A1 = triangle_area(pt, p1, p2)
    A2 = triangle_area(pt, p2, p3)
    A3 = triangle_area(pt, p3, p1)

    # 判断面积之和是否相等（考虑浮点数误差）
    return np.isclose(A, A1 + A2 + A3)

# 主函数：统计每个三角形内的点数量
def count_points_in_triangles(triangles, points):
    # 初始化每个三角形的点计数
    counts = [0] * len(triangles)
    for pt in points:
        for i, (p1, p2, p3) in enumerate(triangles):
            if is_point_in_triangle(pt, p1, p2, p3):
                counts[i] += 1
    return counts

triangles = []
num_triangles = int(input("请输入三角形的数量: "))

for i in range(num_triangles):
    points = []
    for j in range(3):
        point = input(f"请输入三角形 {i + 1} 的第 {j + 1} 个顶点 (格式: x,y): ") #英文状态下输入逗号
        x, y = map(float, point.split(","))
        points.append((x, y))
    triangles.append(points)

# 输入测试点
test_points = []
num_test_points = int(input("请输入测试点的数量: "))

for i in range(num_test_points):
    point = input(f"请输入第 {i + 1} 个测试点 (格式: x,y): ") #英文状态下输入逗号
    x, y = map(float, point.split(","))
    test_points.append((x, y))

result = count_points_in_triangles(triangles, points)
print("每个三角形内的点数：", result)
