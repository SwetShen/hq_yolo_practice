import matplotlib.pyplot as plt  # 绘图工具
import numpy as np  # 绘图的主要类型为numpy

# x 轴方向上的所有坐标
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = np.arange(0, 10, 1)  # 可以将上述的列表转化为numpy的数据格式
# y 轴方向上的所有坐标
y = [0.1, 0.5, 0.3, 0.7, 0.5, 0.8, 0.7, 0.9, 1.0, 1.2]
y = np.array(y)  # 将指定数据转化为numpy的数据格式

plt.plot(x, y)
plt.show()  # 图像展示
