"""
数字识别网络设计过程：
1、加工数据集为可训练的数据集
2、设计模型
3、训练
4、预测
"""

# =========================加工数据集=========================
from torchvision.datasets import ImageFolder  # 1、直接加载图像数据集目录 2、根据目标自动划分分类
from torchvision import transforms  # 针对图像数据集进行一定程度加工
from torch.utils.data import DataLoader, Dataset  # 1、将数据集进行顺序打乱 2、将数据进行批次划分
from torch.utils.data import random_split  # 随机按比例划分数据集

transform = transforms.Compose([
    transforms.ToTensor()  # 将图像的数据集转化为 torch.tensor
])

dataset = ImageFolder("./data/numbers", transform=transform)
# 将数据集分割为训练集、验证集
train_dataset, valid_dataset = random_split(dataset, [0.8, 0.2])
train_loader = DataLoader(train_dataset, batch_size=1000, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=1000)

# =========================设计模型=========================
from torch import nn

# 输入图像大小（3 x 28 x 28）
model = nn.Sequential(
    nn.Conv2d(3, 16, 3, 1, 1),  # （16 x 28 x 28）
    nn.ReLU(),  # 激活函数
    nn.MaxPool2d(2, 2),  # （16 x 14 x 14）
    nn.Conv2d(16, 32, 3, 1, 1),  # （32 x 14 x 14）
    nn.ReLU(),  # 激活函数
    nn.MaxPool2d(2, 2),  # （32 x 7 x 7） # 最后一个卷积的图像大小（5，6，7，8）
    nn.Flatten(),  # 展平特征到（1568）
    nn.Linear(32 * 7 * 7, 1024),
    nn.ReLU(),  # 激活函数
    nn.Linear(1024, 10),  # 最终输出为分类的数量
    nn.LogSoftmax(dim=-1)  # softmax 激活函数
)

# =========================训练=========================
import torch

criterion = nn.CrossEntropyLoss()  # 交叉熵损失（softmax + 交叉熵）
# ----------------- 优化器 -----------------
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# ----------------- 开始训练 -----------------
epochs = 3000
for epoch in range(epochs):
    print(f"{epoch + 1} / {epochs}")
    model.train()  # 开启训练模式
    # 将图像数据集按照批次进行运算
    for batch, data in enumerate(train_loader):
        features, labels = data
        optimizer.zero_grad()  # 对所有的求导清零
        labels_predict = model(features.float())  # 用模型预测结果
        loss = criterion(labels_predict, labels.long())  # MSE均方差要求两个参数的矩阵大小一致
        loss.backward()  # 开启参数求导
        optimizer.step()  # 更新所有求导的w，b的值，进行下一轮训练

        if batch % 100 == 0:
            print(f"批次:{batch} -- 损失:{loss.item():.4f}")

    model.eval()  # 开启验证模式
    for batch, data in enumerate(valid_loader):
        features, labels = data
        labels_predict = model(features.float())  # 用模型预测结果
        labels_predict = torch.argmax(labels_predict, dim=-1)
        # 准确率计算
        accuracy = sum(labels_predict == labels) / len(labels)

        if batch % 10 == 0:
            print(f"批次:{batch} -- 准确率:{accuracy * 100:2f}%")
