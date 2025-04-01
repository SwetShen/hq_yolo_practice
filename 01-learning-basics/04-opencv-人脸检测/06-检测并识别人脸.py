import os
import cv2

classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./train/example.yaml")


# 获取一个id与名字的映射表
def idx2name():
    names = {}
    for filename in os.listdir("./data"):
        name = filename.split(".")[0]
        id = filename.split(".")[1]
        names[id] = name
    return names


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
        # 识别到的id
        id = result[0]
        # 相似度的距离
        distance = result[1]
        # 获取映射表
        name_dict = idx2name()
        # 判断是否是识别到的目标
        if distance <= 50:
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
            cv2.putText(image, name_dict[str(id)], (x, y), 1, 1, color=(0, 0, 255), thickness=2)
        else:
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 0, 0), thickness=2)
            cv2.putText(image, 'unknown', (x, y), 1, 1, color=(255, 0, 0), thickness=2)


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
