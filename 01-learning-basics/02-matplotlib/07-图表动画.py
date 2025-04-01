import numpy as np
import matplotlib.pyplot as plt

# 设计一个水平移动的sin曲线
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

# 步骤1：获取绘制对象
line, = plt.plot(x, y, 'r-')

# 步骤2：设置动画的循环
for i in range(1000):
    # 步骤3：获取每一轮循环的变化结果
    y_new = np.sin(x + i * 0.05)
    # 步骤4：重新绘制表格
    line.set_data(x, y_new)
    # 步骤5: 设置延迟
    #      pause(需要暂停的秒值)
    plt.pause(0.5)
    # plt.show() 在动画中是不用设置，因此它可以通过pause自动显示
