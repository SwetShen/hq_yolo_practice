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
line, = plt.plot(x, y_predict, 'b--')
# ------------------ 衡量预测线的方式 -----------------------
epochs = 10000  # w 的值变化一万次
for epoch in range(epochs):
    # 预测
    y_predict = w * x + b
    # 斜率
    slope_w = np.mean(2 * x * (y_predict - y))  # np.mean 平均值
    slope_b = np.mean(2 * (y_predict - y))  # np.mean 平均值
    # w,b变化 ==> w新 = w旧 - 斜率 * 小固定值 ==> 随机梯度下降法 ==> SGD算法
    w -= slope_w * 0.1
    b -= slope_b * 0.1
    # 更新图表直线
    line.set_data(x, y_predict)
    # 总距离的衡量
    distance = np.sum((y_predict - y) ** 2)
    print(f"{epoch + 1} / {epochs} -- distance :{distance}")
    # 时间延迟
    plt.pause(0.1)
