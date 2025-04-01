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
# ------------------ 预测线 -----------------------
w = 0.1  # 预设的斜率
b = 0.1  # 预设的偏移
y_predict = w * x + b
plt.plot(x, y_predict, 'b--')
# ------------------ 衡量预测线的方式 -----------------------
distance = np.sum((y_predict - y) ** 2)
print(distance)
plt.show()
