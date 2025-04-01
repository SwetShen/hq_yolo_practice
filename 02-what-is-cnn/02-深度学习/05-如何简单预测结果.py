import torch
from torch import nn

# ========================加载模型结构=============================
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

# ===========================加载权重 ==========================
state_dict = torch.load("./save/best.pt")
model.load_state_dict(state_dict)  # 模型结构加入权重

# ========================加载数据=============================
import cv2
import numpy as np

image = cv2.imread("./data/test/7.png")  # numpy数据
image = np.expand_dims(image, 0)  # (1,28,28,3) numpy数据
image = torch.from_numpy(image).permute([0, 3, 1, 2])  # (1,3,28,28) torch数据

model.eval()  # 启动验证模式
result = model(image.float())  # 预测结果（此时结果为softmax值）
result = torch.argmax(result, dim=-1)  # 得到最终的预测的数字内容（此处因为下标与数字的值是一致的，因此不需要映射表）
print(result)
