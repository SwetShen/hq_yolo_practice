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

transform = transforms.Compose([
    transforms.ToTensor()  # 将图像的数据集转化为 torch.tensor
])

dataset = ImageFolder("./data/numbers", transform=transform)
dataloader = DataLoader(dataset, batch_size=1000, shuffle=True)

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
    # 将图像数据集按照批次进行运算
    for batch, data in enumerate(dataloader):
        features, labels = data
        optimizer.zero_grad()  # 对所有的求导清零
        labels_predict = model(features.float())  # 用模型预测结果
        loss = criterion(labels_predict, labels.long())  # MSE均方差要求两个参数的矩阵大小一致
        loss.backward()  # 开启参数求导
        optimizer.step()  # 更新所有求导的w，b的值，进行下一轮训练

        print(f"批次:{batch} -- 损失:{loss.item():.4f}")
