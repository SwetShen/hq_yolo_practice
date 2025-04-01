import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 20)  # 一维矩阵
# 构建x与y的映射关系
y = np.sin(x)
# 构建一个新的映射关系
y1 = x ** 2

# 构建图表的设置对象
fig = plt.figure(figsize=(10, 4))  # figsize=(宽, 高)
# 构建图表1的绘制对象
# fig.add_subplot 创建一个图表绘制区域
# add_subplot(几行，几列，第几个)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y, label="sin function")  # 绘制图表1
ax1.set_title("sin function")  # 设置标题
ax1.set_xlabel("x axis")  # 设置x轴坐标
ax1.set_ylabel("y axis")  # 设置y轴坐标
plt.legend()  # 显示上述的label图示

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y1, label="power function")  # 绘制图表2
plt.legend()  # 显示上述的label图示

plt.show()
