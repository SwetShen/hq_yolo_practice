"""
以下内容为设计思路
"""
# ==========================如何处理图像为输入特征==========================
import cv2
import numpy as np
import os

import torch
from torch import nn

images = []
labels = []
# 处理 0 的所有图片为一个矩阵
for filename in os.listdir("./data/numbers/0"):
    # 取出该图片的黑白单通道图
    image = cv2.imread(os.path.join("./data/numbers/0", filename), 0)
    image = image.reshape(1, 28 * 28)
    images.append(image)
    labels.append(0)

images = np.concatenate(images, axis=0)
images = torch.from_numpy(images)
labels = torch.tensor(labels, dtype=torch.long)
print(images.shape)
print(labels.shape)

# ==========================如何设计模型==========================
model = nn.Sequential(
    # 输入
    nn.Linear(28 * 28, 14 * 14),
    # 激活
    nn.Tanh(),
    # 中间层
    nn.Linear(14 * 14, 7 * 7),
    # 激活
    nn.Tanh(),
    # 输出
    nn.Linear(7 * 7, 2),
    nn.LogSoftmax(dim=-1)  # 激活函数，算每一种概率的占比
)
