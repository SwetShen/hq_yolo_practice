import cv2

classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./train/example.yaml")


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
        # 将上述的人脸信息放入recognizer中进行检索
        # 就会返回两个内容，一个id，一个是相似距离（距离越小越相似，越大就越不相似）
        gray_img = cv2.cvtColor(image[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
        result = recognizer.predict(gray_img)
        print(result)


# image = cv2.imread("./data/shen.1.jpg")
# detect_face(image) # shen.1.jpg"
# image = cv2.imread("./imgs/test2.jpg")
# detect_face(image) # shen.1.jpg"
