import cv2

# opencv中操作的图像的数据类型是numpy

# imread 加载图像
image = cv2.imread("./imgs/test.jpg")
# image是numpy的数据类型
print(image.shape)  # (248, 258, 3) == (高度，宽度，通道数)
# 展示图像
cv2.imshow("image", image)
# waitKey(0) 无限等待（直到关闭窗口时，停止显示）
cv2.waitKey(0)
