# 矩阵 --> 线性代数
import numpy as np

# a 是一个3x3的矩阵，a是一个一维为3，二维为3的矩阵
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a)
# shape 展示该矩阵的维度
print(a.shape)

# 构建矩阵
# random.rand 设定随机数矩阵（每个随机数在0~1之间）
b = np.random.rand(1, 3, 2, 2)  # 1 有多少个 3 通道  2 x 2 图像大小
# np.arange(起点位置, 终点位置, 步长)
c = np.arange(0, 10, 1)  # 一维矩阵
# np.reshape(定义维度参数) 更改矩阵维度
d = np.arange(1, 10, 1)
d = d.reshape(3, 3)  # 从1维到2维 称为升维操作
print(d)
# d = d.reshape(-1, ) # -1 任意长度（此处的意思是拉伸到一维）
d = d.reshape(9, )  # -1 任意长度（此处的意思是拉伸到一维）
print(d)             # 从2维到1维 称为降维操作
