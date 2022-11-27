import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)

img1 = cv2.blur(img, (3, 3))  # 均值滤波  均值范围：3 * 3
img2 = cv2.boxFilter(img, -1, (3, 3), normalize = 0)  # 方框滤波   直接使用领域像素值之和
img3 = cv2.GaussianBlur(img, (3, 3), 0, 0)   # 高斯滤波   权重会随着距离减小  0, 0  让函数自己去计算
img4 = cv2.medianBlur(img, 3)  # 中值滤波
img5 = cv2.bilateralFilter(img, 25, 100, 100)  # 双边滤波

k = np.ones((9, 9), np.float32) / 81
img6 = cv2.filter2D(img, -1, k)  # 2D 卷积  可自定


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.imshow("img5", img5)
cv2.imshow("img6", img6)


cv2.waitKey(0)
cv2.destoryAllWindows()




