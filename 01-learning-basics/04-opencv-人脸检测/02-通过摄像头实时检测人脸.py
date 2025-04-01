import cv2

classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")


def detect_face(image):
    # 检测出的人脸的坐标位置
    result = classifier.detectMultiScale(
        image=image,  # 检测的图片
        scaleFactor=1.01,  # 检测区域的最大倍率
        minNeighbors=5,  # 一次可以检测多少个人脸
        flags=0,
        minSize=[100, 100],  # 检测图像的最小尺寸
        maxSize=[200, 200]  # 检测图像的最大尺寸
    )
    # 检测照片中的所有人脸
    for person in result:
        x, y, w, h = person
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)


cap = cv2.VideoCapture(0)

while True:
    flag, frame = cap.read()
    if flag is False:
        print("摄像头获取图像出现问题")
        break
    detect_face(frame)
    cv2.imshow("capture", frame)
    if cv2.waitKey(2) == ord(" "):
        break
cv2.destroyAllWindows()
