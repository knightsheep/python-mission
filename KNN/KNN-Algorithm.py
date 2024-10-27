# -*- coding: utf-8 -*-
# @Time: 2024/10/20 00:24
# @Author: dayu

import matplotlib.pyplot as plt
import numpy as np


def load_data(file_path):
    """从文本文件加载数据。"""
    return np.loadtxt(file_path)


def get_grouped_points(data, group_value):
    """返回属于特定列的点。"""
    return data[data[:, 2] == group_value]


def calculate_distances(test_point, data):
    """计算从测试点到所有数据点的平方距离。"""
    return np.sum((data[:, :2] - test_point) ** 2, axis=1)


def knn_classification(test_points, data, k):
    """使用KNN进行分类。"""
    results = np.zeros(test_points.shape[0])
    for idx, test_point in enumerate(test_points):
        distances = calculate_distances(test_point, data)
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = data[nearest_indices, 2]

        # Count the occurrences of each class
        type1 = np.sum(nearest_labels == 1)
        type2 = np.sum(nearest_labels == 2)

        results[idx] = 1 if type1 > type2 else 2
    return results


def plot_data(points, color, marker, label, size=1, alpha=0.8):
    """分类数据点的散点图。"""
    plt.scatter(points[:, 0], points[:, 1], color=color, marker=marker, s=size, alpha=alpha, label=label)


def main():
    data = load_data("trainData.txt")

    group1_points = get_grouped_points(data, 1)
    group2_points = get_grouped_points(data, 2)

    plt.scatter(group1_points[:, 0], group1_points[:, 1], color='r', label="Training group 1")
    plt.scatter(group2_points[:, 0], group2_points[:, 1], color='b', label="Training group 2")

    x_axis = np.linspace(-6, 6, 121)
    y_axis = np.linspace(-6, 6, 121)
    k = int(input('请问K等于几？'))

    result = np.zeros((121, 121))
    x1, y1, x2, y2 = [], [], [], []

    for j, y in enumerate(y_axis):
        for i, x in enumerate(x_axis):
            test_point = np.array([x, y])
            label = knn_classification(np.array([test_point]), data, k)[0]
            result[i, j] = label

            if label == 1:
                x1.append(x)
                y1.append(y)
            else:
                x2.append(x)
                y2.append(y)

    plot_data(np.column_stack((x1, y1)), 'r', '+', "Data in group 1")
    plot_data(np.column_stack((x2, y2)), 'b', '*', "Data in group 2")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


