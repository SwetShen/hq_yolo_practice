import cv2

image = cv2.imread("./imgs/logo.jpg")
# image的三个通道分别是蓝、绿、红
# print(image.shape) # 图像大小 (214, 198, 3)
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# 展示每个通道
cv2.imshow("src", image)  # 多通道 图像 是彩色图
cv2.imshow("blue_channel", blue_channel)  # 单通道 图像 是黑白图
cv2.imshow("green_channel", green_channel)  #
cv2.imshow("red_channel", red_channel)
cv2.waitKey(0)
