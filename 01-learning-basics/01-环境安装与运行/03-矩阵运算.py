import numpy as np

# 定义两个矩阵
a = np.float16(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)
b = np.float16(
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
)
c = np.float16(
    [
        [1, 1, 1]
    ]
)
# 矩阵的加减 --> 对位运算
# print(a - b)
# print(a + b)
# 如果矩阵加减一个小矩阵（必须保证最后一个维度要相等） -> 广播机制
#  广播机制 可以作用在所有的运算中
# print(a.shape)
# print(c.shape)
# print(a - c)
# print(a + c)

# 乘除法 （默认对位运算活着广播机制）
print(a * b)
print(a * c)

# 线性代数的转置运算
# matmul 线性代数的运算法则：n x m . m x k == n x m . (k . m)^T
print(np.matmul(a, b))
print(np.matmul(a, c.T))
