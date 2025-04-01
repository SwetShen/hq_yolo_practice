import cv2
import os
import numpy as np

classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")


def get_train_data(path="./data"):
    # 定义两个列表缓存id和image
    idx = []
    faces = []
    for filename in os.listdir(path):
        id = int(filename.split(".")[1])  # 取出名称中id的部分
        image = cv2.imread(os.path.join(path, filename))
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
        x, y, w, h = result[0]
        # 照片中的人脸区域
        face_img = image[y:y + h, x:x + w]
        # 灰度图转化(变成单通道的黑白图)
        gray_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        # 对id和face图像进行存储
        idx.append(id)
        faces.append(gray_img)
    return idx, faces


if __name__ == '__main__':
    # 获取id和face的数据
    idx, faces = get_train_data()
    idx = np.array(idx)
    # 此处需要安装辅助的库：pip install opencv-contrib-python
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 通过id和face对其进行训练
    recognizer.train(faces, idx)
    # 保存训练的数据集到train目录下
    recognizer.save("./train/example.yaml")
