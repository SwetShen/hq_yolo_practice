import numpy as np
import matplotlib.pyplot as plt

# 在区间中构建一个连续且均匀的点集
# linspace(起始点位置，终止点位置，创建的点的数量)
# np.pi 圆周率
x = np.linspace(0, np.pi, 20)  # 一维矩阵
# 构建x与y的映射关系
y = np.sin(x)
# 构建一个新的映射关系
y1 = x ** 2

plt.plot(x, y, label="sin function")  # 绘制图表1
plt.plot(x, y1, label="power function")  # 绘制图表2
plt.legend()  # 显示上述的label图示
plt.show()
