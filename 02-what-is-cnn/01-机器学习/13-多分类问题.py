import torch
import matplotlib.pyplot as plt
from torch import nn

# ----------------- 创建多个图表 -----------------
fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)


def draw_point(features, labels, ax):
    """
    绘制点到图表中
    :param features:
    :param labels:
    :param ax:
    :return:
    """
    for feature, label in zip(features, labels):
        x, y = feature
        if label == 0:
            ax.plot([x.item()], [y.item()], 'ro')
        elif label == 1:
            ax.plot([x.item()], [y.item()], 'bo')
        elif label == 2:
            ax.plot([x.item()], [y.item()], 'go')


# ----------------- 簇族点的定义 -----------------
# 离散度值
noise = 0.2
# A簇族 的label：0  B簇族 的label：1  C簇族 的label: 2
points_a_features = torch.normal(0.5, noise, (20, 2))  # 此处的(20, 2) 是指20个xy
points_a_labels = torch.zeros((points_a_features.shape[0], 1))  # 定了A簇族每个点分类信息
points_a = torch.cat([points_a_features, points_a_labels], dim=-1)
points_b_features = torch.normal(1.5, noise, (20, 2))
points_b_labels = torch.ones((points_b_features.shape[0], 1))  # 定了B簇族每个点分类信息
points_b = torch.cat([points_b_features, points_b_labels], dim=-1)
points_c_x = torch.normal(0.5, noise, (20, 1))
points_c_y = torch.normal(1.5, noise, (20, 1))
points_c_features = torch.cat([points_c_x, points_c_y], dim=-1)
points_c_labels = torch.ones((points_c_features.shape[0], 1)) * 2  # 定了C簇族每个点分类信息
points_c = torch.cat([points_c_features, points_c_labels], dim=-1)
# 将上述的两个簇的信息进行整合
points = torch.cat([points_a, points_b, points_c], dim=0)
# 将所有的点打乱顺序 torch.randperm 生成随机的下标
indices = torch.randperm(points.shape[0])
points = points[indices]  # 所有的点按照indices 的顺序打乱

# ----------------- 对数据进行特征与标签的分割 -----------------
features = points[:, :2]  # (40x2) 所有的坐标值作为输入特征（输入特征数量为2）
labels = points[:, 2]  # (40,) 每个点所对应的分类（0，1,2）
draw_point(features, labels, ax1)
# ----------------- 定义一个模型 -----------------
model = nn.Sequential(
    # 输入
    nn.Linear(2, 10),
    # 激活
    nn.Tanh(),
    # 输出
    nn.Linear(10, 3),
    nn.LogSoftmax(dim=-1)  # 激活函数，算每一种概率的占比
)
# ----------------- 损失函数 -----------------
criterion = nn.CrossEntropyLoss()  # 交叉熵损失（softmax + 交叉熵）
# ----------------- 优化器 -----------------
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# ----------------- 开始训练 -----------------
epochs = 3000
for epoch in range(epochs):
    optimizer.zero_grad()  # 对所有的求导清零
    labels_predict = model(features)  # 用模型预测结果
    loss = criterion(labels_predict, labels.long())  # MSE均方差要求两个参数的矩阵大小一致
    loss.backward()  # 开启参数求导
    optimizer.step()  # 更新所有求导的w，b的值，进行下一轮训练

    print(f"{epoch + 1} / {epochs} -- loss:{loss.item():.4f}")

# ------------------ 预测 -----------------------
model.eval()
x = torch.linspace(0, 2, 20)
y = torch.linspace(0, 2, 20)
x, y = torch.meshgrid([x, y], indexing='ij')
test_features = torch.cat([x.reshape(400, 1), y.reshape(400, 1)], dim=-1)
test_labels = model(test_features)  # 由于直接预测的结果是0~1之间的小数,因此需要将结果转化为0,1
# 取出对应的最大概率的下标
test_labels = torch.argmax(test_labels, dim=-1)
# 绘制预测的结果
draw_point(test_features, test_labels, ax2)
plt.show()
