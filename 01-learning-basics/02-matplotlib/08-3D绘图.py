import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
# 设置一个3D图表
# add_subplot 设置3D显示参数 :projection='3d'
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, 1, 20)
y = np.linspace(0, 1, 20)
z = x * 0.5 + y * 1.2
# plot只有在绘制3D图时，才能设置三个位置参数，否则一般情况下不可以设置
ax.plot(x, y, z, 'ro-')

plt.show()

# 一维空间的问题，可以在二维空间中可视化
# 二维空间的问题，可以在三维空间中可视化
# ...
