import cv2
import numpy as np

image = cv2.imread("./imgs/test.jpg")
h, w, c = image.shape
# 设置旋转的中心位置
center = (h // 2, w // 2)

# 变换矩阵
# getRotationMatrix2D(旋转中心点位置,旋转角度,缩放值)
M = cv2.getRotationMatrix2D(center, 15., 1.0)

result = cv2.warpAffine(image, M, dsize=(w + 40, h + 40))
cv2.imshow("result", result)
cv2.waitKey(0)

