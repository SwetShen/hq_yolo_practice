import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 20)
y = np.sin(x)
y1 = np.sin(0.9 * x)
y2 = np.sin(0.8 * x)

# 线条的样式：
# - ：实线  -- ： 虚线  . : 点线
# 点的样式
# o : 实心圆点  ^ : 上三角形  v：下三角形
# 颜色
# r : 红色  g：绿色  b：蓝色

plt.plot(x, y, 'r-o', label="line01")
plt.plot(x, y1, '--^', label="line02")
plt.plot(x, y2, 'v', label="line03")
plt.legend()  # 显示上述的label图示
plt.show()
