import numpy as np
import cv2

img1 = cv2.imread("E:/000/01.jpg", -1)  # 以彩色图像读取
img2 = cv2.imread("E:/000/02.jpg", -1)  # 以彩色图像读取

# 读取图片的行数、列数、通道数（二值图像只读取行列数）
img1_shape = img1.shape
img2_shape = img2.shape

# 截取部分图像
img1 = img1[0 : 400, 0 : 400]
img2 = img2[0 : 400, 0 : 400]

img = cv2.addWeighted(img1, 0.7, img2, 0.5, 1)  # 权重相加 img1 和 img2 的横列数必须相同

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img", img)

cv2.waitKey()
cv2.destoryAllWindows()
