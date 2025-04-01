import numpy as no
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 40)
# 激活函数  sigmoid函数
# y = 1 / (1 + np.exp(-x))
# 激活函数 tanh函数
y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

plt.plot(x, y, 'r-')
plt.show()
