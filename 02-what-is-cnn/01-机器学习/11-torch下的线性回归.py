import torch
import matplotlib.pyplot as plt
from torch import nn

# ------------------ 曲线图 -----------------------
x = torch.linspace(-3, 3, 40)
y = x ** 2

plt.plot(x.detach().numpy(), y.detach().numpy(), 'ro')
# ------------------ 重要：将数据调整为模型输入格式 -----------------------
# 官方的格式要求：(batch_size,input_features) => (数量, 输入特征大小)
x = x.reshape(40, 1)
y = y.reshape(40, 1)
# ------------------ 定义模型 -----------------------
# Sequential 组装模型层的工具
model = nn.Sequential(
    # 输入
    nn.Linear(1, 10),
    # 激活函数
    nn.Tanh(),
    # 输出
    nn.Linear(10, 1)
)
# ------------------ 定义损失函数 -----------------------
criterion = nn.MSELoss()  # 等效于均方差的距离衡量公式
# ------------------ 定义优化器 -----------------------
# model.parameters() 获取模型中的所有w,b (requires_grad=True)
# lr = learning rate 学习率 (之前的固定值)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
# ------------------ 开始训练 -----------------------
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()  # 对所有的求导清零
    y_predict = model(x)  # 用模型预测结果
    loss = criterion(y_predict, y)  # 衡量预测结果与真实结果的差距
    loss.backward()  # 开启参数求导
    optimizer.step()  # 更新所有求导的w，b的值，进行下一轮训练

    print(f"{epoch + 1} / {epochs} -- loss:{loss.item():.4f}")

# ------------------ 预测 -----------------------
model.eval()  # 开启模型的预测模式
y_predict = model(x)  # 预测结果
plt.plot(x.detach().numpy(), y_predict.detach().numpy(), 'b--')
plt.show()
