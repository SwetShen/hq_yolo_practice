import numpy as np
import matplotlib.pyplot as plt

# ------------------ 散点图 -----------------------
x = np.linspace(0, 1, 20)
y = 3 * x + 2  # 直线公式
# 噪点率: 点的散乱程度，当值越大，散乱程度越高
noise = 0.2
# np.random.normal 按要求随机生成正态分布
y += np.random.normal(0, noise, y.shape)

plt.plot(x, y, 'ro')
plt.show()
