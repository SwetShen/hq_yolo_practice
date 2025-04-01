# 轮廓检测如何进行

import cv2

image = cv2.imread("./imgs/colors.png")
# 红色单通道图像
red_channel = image[:, :, 2]
# 检测单通道图像轮廓工具
# findContours(单通道图，检测模式（外轮廓、内轮廓）,检测边缘的算法)
contours = cv2.findContours(red_channel, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓的方法
# drawContours(绘制的图像,轮廓参数，起始绘制位置，颜色，边框宽度)
# cv2.drawContours(image, contours[0], 0, color=(255, 255, 255), thickness=2)
# 设置标注框
result = cv2.boundingRect(contours[0][0])
# 获取左上角坐标和宽、高
x_min, y_min, h, w = result
# 绘制矩形框
# rectangle(绘制的图像，左上角坐标，右下角坐标，颜色，边框宽度)
cv2.rectangle(image, (x_min, y_min), (x_min + w, y_min + h), color=(255, 255, 255), thickness=2)
# 绘制文本
cv2.putText(image,"red",(x_min, y_min),1,1.5,color=(255, 255, 255), thickness=2)

# 展示每个通道
cv2.imshow("src", image)
cv2.imshow("red_channel", red_channel)
cv2.waitKey(0)
