import numpy as np
import cv2

image = cv2.imread("./imgs/test.jpg")
# image是一个numpy矩阵，因此我们可以通过切片方法对图像进行处理
cv2.imshow("crop", image[:100, :100, :])
# 保存图像 imwrite
cv2.imwrite("./imgs/crop.jpg", image[:100, :100, :])
cv2.waitKey(0)
