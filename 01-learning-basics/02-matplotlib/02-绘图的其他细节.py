import matplotlib.pyplot as plt  # 绘图工具
import numpy as np  # 绘图的主要类型为numpy

# plt.rcParams['font.sans-serif'] 设置表格内容的编码模式
# 'SimHei' : 小黑字体 'Microsoft YaHei'
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'

x = np.arange(0, 10, 1)
y = [0.1, 0.5, 0.3, 0.7, 0.5, 0.8, 0.7, 0.9, 1.0, 1.2]
y = np.array(y)

# plt.title("table") 设置标题
plt.title("表格")
plt.xlabel("X轴")  # 设置x坐标轴的名称
plt.ylabel("Y轴")  # 设置y坐标轴的名称
plt.grid()  # 设置表格线
plt.plot(x, y)
plt.show()
