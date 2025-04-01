"""
torch的安装
pip3 install torch torchvision torchaudio
"""
import torch

# -----------------通用的使用法则
# torch的使用方法 约等于 numpy的使用方法

# a = torch.tensor([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(a.shape)
# print(a.reshape(1, 6))
# print(a[:, :2])

# -----------------torch的自动求导
x = torch.tensor([1., 2., 3., 4.])
# 步骤1：在需要求导的变量位置，设置requires_grad=True
x.requires_grad = True
y = x ** 2

torch.sum(y).backward()  # # 步骤2：由结果开启求导(注意，y不可以是矩阵，只能是一个值)
# 步骤3：求导数
print(x.grad)
