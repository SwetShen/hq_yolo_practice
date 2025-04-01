import cv2
import numpy as np

image = cv2.imread("./imgs/test.jpg")
h, w, c = image.shape

# 设置图像翻转
# result = cv2.flip(image, 0)

# 使用代码方式实现翻转
# 水平翻转
# result = image[:, ::-1]
# 垂直翻转
result = image[::-1, :]

cv2.imshow("src", image)
cv2.imshow("result", result)
cv2.waitKey(0)
