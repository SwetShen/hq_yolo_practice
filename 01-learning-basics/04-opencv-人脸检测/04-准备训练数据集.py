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
    # 将图像对象进行复制
    frame_cp = frame.copy()
    detect_face(frame_cp)
    cv2.imshow("capture", frame_cp)
    num = cv2.waitKey(2)
    if num == ord(" "):
        break
    elif num == ord("s"):  # 按s拍摄照片
        # 保存图片到指定的区域
        cv2.imwrite("./data/shen.1.jpg", frame)
cv2.destroyAllWindows()
