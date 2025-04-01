"""
通过摄像头的方式，检测颜色区域
"""
import cv2


# 检测颜色的函数
def detect_color(image):
    # 颜色标准
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 只取出绿色的区域的黑白图
    mask = cv2.inRange(image_hsv, (100, 43, 46), (124, 255, 255))
    contours, h = cv2.findContours(mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    # 由于检测到的绿色有若干个，因此需要用循环方式遍历
    for contour in contours:
        if len(contour) >= 4:
            result = cv2.boundingRect(contour)
            x_min, y_min, w, h = result
            # 面积处理
            if h * w >= 1000:
                cv2.rectangle(image, (x_min, y_min), (x_min + w, y_min + h), color=(255, 255, 255), thickness=2)
                cv2.putText(image, "blue", (x_min, y_min), 1, 1.5, color=(255, 255, 255), thickness=2)


cap = cv2.VideoCapture(0)

while True:

    flag, frame = cap.read()
    if flag is False:
        print("摄像头获取图像出现问题")
        break
    # 执行颜色检测
    detect_color(frame)
    cv2.imshow("capture", frame)
    if cv2.waitKey(2) == ord(" "):
        break
cv2.destroyAllWindows()
