import cv2
import matplotlib.pyplot as plt
import torch
from torch import nn
import numpy as np

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# 输入： 28 x 28 x 3 图片
image = cv2.imread("./data/numbers/0/0.png")  # opencv中加载的图片都是 BGR图
ax1.set_title(f"{image.shape}")
ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # plt中显示的图是RGB

# 设置一个卷积过程
layer = nn.Sequential(
    # (28 - 3 + 2 * 1) / 1 + 1 = 28
    nn.Conv2d(3, 6, 3, 1, 1),  # 卷积 （w,b）
    # (28 - 2) / 2 + 1  = 14
    nn.MaxPool2d(2, 2)  # 池化 (没有w，b)
)

# 输出： 14 x 14 x 6 图片
# 在放入image之前，image必须将自身的1、（28，28，3） => (1,3,28,28)  2、numpy -> torch.tensor
image = np.expand_dims(image, 0)  # （28，28，3） => (1,28,28,3)
image = torch.from_numpy(image)  # numpy -> torch.tensor
image = image.permute([0, 3, 1, 2])  # (1,28,28,3) => (1,3,28,28)

result = layer(image.float())  # result的大小(1,6,14,14)
ax2.set_title(f"{result.shape}")
ax2.imshow(result.squeeze()[0].detach().numpy())

plt.show()
