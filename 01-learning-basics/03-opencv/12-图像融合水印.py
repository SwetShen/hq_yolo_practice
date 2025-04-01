import cv2

logo = cv2.imread("./imgs/print.png")
src = cv2.imread("./imgs/test.jpg")

# ------------ 循环方式下的添加水印 -------------
h, w, _ = logo.shape
for i in range(h):
    for j in range(w):
        # 取出一个像素下的三通道的值
        l_bgr = logo[i, j]
        s_bgr = src[i, j]
        # 将像素值最大的部分保留下来
        if l_bgr[0] > s_bgr[0]:
            src[i, j, 0] = l_bgr[0]
        if l_bgr[1] > s_bgr[1]:
            src[i, j, 1] = l_bgr[1]
        if l_bgr[2] > s_bgr[2]:
            src[i, j, 2] = l_bgr[2]

cv2.imshow("src", src)
cv2.waitKey(0)
