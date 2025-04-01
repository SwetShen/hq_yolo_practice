"""
opencv 开启摄像头，获取图像信息
1、确保电脑可以打开摄像头（在设备中存在摄像头、能否打开它）
2、通过代码方式打开摄像头

"""
import cv2

# 获取默认的摄像头设备
cap = cv2.VideoCapture(0)

while True:
    # flag 是一个判断是否成功获取摄像头画面的值，True/False
    # frame 是从摄像头中获取的每一帧图像
    flag, frame = cap.read()
    if flag is False:
        print("摄像头获取图像出现问题")
        break
    cv2.imshow("capture", frame)
    # 当我们按下空格时，会退出摄像头
    # ord(" ") : 空格键编码
    if cv2.waitKey(2) == ord(" "):
        break
# 销毁所有的开启的窗口
cv2.destroyAllWindows()

