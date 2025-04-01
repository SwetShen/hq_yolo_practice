# 灰度化，本质就是单通道的黑白图
#        可以在单通道中，尽可能地提取图像中的信息
import cv2
import numpy as np

image = cv2.imread("./imgs/colors.png")
h, w, _ = image.shape
# 将三通道的像素值缩小到0~1
blue_channel = image[:, :, 0] / 255
green_channel = image[:, :, 1] / 255
red_channel = image[:, :, 2] / 255

# 加权平均灰度化
tmp = (blue_channel * 0.6 + green_channel * 0.3 + red_channel * 0.1) * 255
tmp = tmp.astype(np.uint8)

cv2.imshow("src", image)  # 多通道 图像 是彩色图
cv2.imshow("tmp", tmp)  # 单通道 图像 是黑白图
cv2.waitKey(0)
