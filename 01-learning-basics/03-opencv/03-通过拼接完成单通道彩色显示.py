import cv2
import numpy as np

image = cv2.imread("./imgs/logo.jpg")
# 获取原图的高、宽、通道数量
h, w, c = image.shape
# 取出图像中的一个通道
blue_channel = image[:, :, 0]  # 是图像的第一通道
# 构建一个全黑的三通道图
# dtype=np.uint8 是指该矩阵的每一个元素必须满足（0~255）
tmp_image = np.zeros((h, w, c), dtype=np.uint8)
# 在黑图的对应通道插入原图的蓝色通道
tmp_image[:, :, 0] = blue_channel

# 展示每个通道
cv2.imshow("src", image)  # 多通道 图像 是彩色图
cv2.imshow("blue_channel", blue_channel)  # 单通道 图像 是黑白图
cv2.imshow("tmp", tmp_image)
cv2.waitKey(0)
