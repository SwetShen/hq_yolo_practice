import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)  # 随机种子（使得后续的随机值生成按照固定的规则）
data = {'a': np.arange(50),  # 0~49的一维矩阵  # {}: 对象  理解方式 一个人名字、身高、地址....
        'c': np.random.randint(0, 50, 50),  # 50个0~49的随机整数（一维矩阵）
        'd': np.random.randn(50)}  # 50 个随机整数（一维矩阵）
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100  # np.abs 绝对值 确保'd'中的值全为正数

# fig ：图表的配置文件（图表的大小、图表的显示区域等等）
# ax：图表对象
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')  # 生成一个图表对象
# scatter 点区域的绘制方法
# 'a'和'b'的值设置点的坐标位置
# 'c' 控制颜色（值越大颜色越深）
# 'd' 控制点的范围（值越大范围越大）
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

plt.show()
