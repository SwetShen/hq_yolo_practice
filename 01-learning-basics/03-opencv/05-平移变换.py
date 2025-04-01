import cv2
import numpy as np

image = cv2.imread("./imgs/test.jpg")
h, w, c = image.shape

# 变换矩阵(平移矩阵)
M = np.float32([[1, 0, 20], [0, 1, 30]])

# 执行变换
# warpAffine(原图像内容，变换矩阵，输出图像大小)
result = cv2.warpAffine(image, M, dsize=(w, h))
cv2.imshow("result", result)
cv2.waitKey(0)
