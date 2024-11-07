# 数据为心脏病数据，为求解1和-1两位分类问题，通过求解决策函数y = sign(（wx) + b)，判断另一个点的输入其结果的正负号；最后通过自检判断函数的优劣；
# 具体过程：

# 以下为简略matlab代码
# %从heart.txt中导入数据；

# %数据分别保存在向量yt和举证xt；

# %C为权衡系数；

# %n为训练点的个数，举证H对应于yi*yj*(xi*xj)；

# %限制条件：Aeq,beq为yi*ai=0，lb,ub为0<=a<=C；

# %求解w和b

# %显决决策函数y = sign(（wx) + b)；

 

# %检测决策函数的准确度；

# temp = 0;

# correct = 0;

# x = xt;

# for j = 1:n

#     for i = 1:n

#         temp = temp + yt(i)*a(i)*dot(xt(i,:),x(j,:));

#         %temp=（w x)；

#     end

#     y = sign(temp + b);

#     if y == yt(j)

#         %记录决策准确个数；

#         correct = correct + 1;

#     end

# end

# %决策准确度；

# correct = correct/n*100;

 

# %显决策准确度；

# disp('决策准确度 ');

# disp(correct)

# disp('%');

'''
具体的matlab实现代码
% 从 heart.txt 文件加载数据
data = load('heart.txt');
xt = data(:, 1:end-1);  % 特征数据
yt = data(:, end);      % 类别标签 (+1 或 -1)
% disp(unique(yt));  % 查看标签中的唯一值

% 创建支持向量机模型
svm = fitcecoc(xt, yt, 'Coding', 'onevsall');

% 使用训练好的模型进行预测
yt_pred = predict(svm, xt);

% 计算决策准确度
accuracy = sum(yt_pred == yt) / length(yt) * 100;

% 输出准确度
disp('决策准确度:');
disp(accuracy);
'''




# 以下为python实现代码
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 从 heart.txt 文件加载数据
data = np.loadtxt('heart.txt') # 从相对路径读取heart.txt文件
xt = data[:, :-1]  # 特征数据
yt = data[:, -1]   # 类别标签 (+1 或 -1)

# 创建支持向量机模型，C是正则化参数，可根据需要随时调整
svm = SVC(C=1, kernel='linear')

# 训练模型
svm.fit(xt, yt)

# 计算决策准确度
accuracy = accuracy_score(yt, svm.predict(xt)) * 100

# 输出准确度
print('决策准确度:')
print(f'{accuracy:.2f}%')



