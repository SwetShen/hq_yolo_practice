import cv2

image = cv2.imread("./imgs/test1.jpg")

# CascadeClassifier 级联分类器
classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")
# 检测出的人脸的坐标位置
result = classifier.detectMultiScale(
    image=image,  # 检测的图片
    scaleFactor=1.01,  # 检测区域的最大倍率
    minNeighbors=5,  # 一次可以检测多少个人脸
    flags=1,
    minSize=[50, 50],  # 检测图像的最小尺寸
    maxSize=[500, 500]  # 检测图像的最大尺寸
)

# 检测照片中的所有人脸
for person in result:
    x, y, w, h = person
    cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)
cv2.imshow("image",image)
cv2.waitKey(0)
