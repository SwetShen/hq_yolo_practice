import torch
import matplotlib.pyplot as plt

# ------------------ 曲线图 -----------------------
x = torch.linspace(0, 3, 40)
y = x ** 2

plt.plot(x.detach().numpy(), y.detach().numpy(), 'ro')


# ------------------ 激活函数 -----------------------
def sigmoid(x):  # 0~1
    return 1 / (1 + torch.exp(-x))


def tanh(x):  # -1 ~ 1
    return (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))


# ------------------ 自定义的w和b -----------------------
w1 = torch.tensor(0.1, requires_grad=True)  # 预设的斜率
b1 = torch.tensor(0.1, requires_grad=True)  # 预设的偏移
w2 = torch.tensor(0.1, requires_grad=True)  # 对激活函数结果进行二次斜率映射调整
b2 = torch.tensor(0.1, requires_grad=True)  # 对激活函数结果进行二次偏移映射调整
# ------------------ 训练 -----------------------
epochs = 30000  # w 的值变化一万次
for epoch in range(epochs):
    # 预测
    y_predict = w2 * tanh(w1 * x + b1) + b2  # 加入激活函数
    # 总距离的衡量
    distance = torch.mean((y_predict - y) ** 2)
    # 启动求导
    distance.backward()
    # 自动求导
    with torch.no_grad():  # 保证以下的计算内容不会影响之后的导数求解
        w1 -= w1.grad * 0.1  # 斜率 * 小固定值 SGD算法
        b1 -= b1.grad * 0.1
        w2 -= w2.grad * 0.1
        b2 -= b2.grad * 0.1
        w1.grad.zero_()  # 方便下一次对斜率的求解
        b1.grad.zero_()  # 方便下一次对斜率的求解
        w2.grad.zero_()  # 方便下一次对斜率的求解
        b2.grad.zero_()  # 方便下一次对斜率的求解

    # print(f"{epoch + 1} / {epochs} -- distance :{distance.item()}")

# ------------------ 预测 -----------------------
y_predict = w2 * tanh(w1 * x + b1) + b2
plt.plot(x.detach().numpy(), y_predict.detach().numpy(), 'g--')
plt.show()
