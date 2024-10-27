# -*- coding: utf-8 -*-
# @Time: 2024/10/27 19:15
# @Author: dayu

import random
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """从文件加载数据点"""
    groups = []
    with open(file_path, 'r') as f:
        for line in f:
            groups.append(np.array(line.split(), dtype=np.float64))
    return groups

def initialize_centroids(groups, k):
    """随机选择初始质心"""
    return random.sample(groups, k)

def assign_clusters(groups, mean_vectors):
    """将数据点分配到最近的质心"""
    clusters = [[] for _ in range(len(mean_vectors))]
    for melon in melons:
        distances = np.linalg.norm(melon - mean_vectors, axis=1)  # 计算距离
        closest_centroid = np.argmin(distances)  # 找到最近的质心
        clusters[closest_centroid].append(melon)
    return clusters

def update_centroids(clusters):
    """更新质心"""
    new_centroids = []
    for cluster in clusters:
        if len(cluster) > 0:
            new_centroids.append(np.mean(cluster, axis=0))  # 计算均值
        else:
            new_centroids.append(np.zeros_like(cluster[0]))  # 如果没有点，返回零向量
    return np.array(new_centroids)

def kmeans(groups, k, round_limit=20, threshold=1e-10):
    """K-means 聚类算法实现"""
    mean_vectors = initialize_centroids(melons, k)
    rnd = 0

    while True:
        rnd += 1
        clusters = assign_clusters(melons, mean_vectors)
        new_mean_vectors = update_centroids(clusters)

        # 检查收敛
        change = np.linalg.norm(mean_vectors - new_mean_vectors)
        if rnd > round_limit or change < threshold:
            break

        mean_vectors = new_mean_vectors

    return clusters, mean_vectors, rnd

def plot_clusters(clusters, mean_vectors):
    """可视化聚类结果"""
    colors = ['red', 'green', 'blue', 'yellow', 'black', 'purple', 'cyan']
    plt.figure(figsize=(8, 6))

    for i, cluster in enumerate(clusters):
        cluster_array = np.array(cluster)
        plt.scatter(cluster_array[:, 0], cluster_array[:, 1], color=colors[i % len(colors)], label=f'Cluster {i + 1}')

    # 绘制质心
    # plt.scatter(mean_vectors[:, 0], mean_vectors[:, 1], color='black', marker='X', s=200, label='Centroids')

    plt.title('K-means Clustering')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# 主程序
if __name__ == "__main__":
    k = int(input('请输入簇数：k = '))
    melons = load_data("test_Kmeans.txt")
    clusters, mean_vectors, iterations = kmeans(melons, k)
    print(f'算法在 {iterations} 次迭代后收敛.')
    plot_clusters(clusters, mean_vectors)
