import cv2
import numpy as np

lena = cv2.imread("E:/000/01.jpg", -1)
hsv = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV)

#=============== 缩放 ======================================
img = cv2.resize(lena, None, fx = 2, fy = 2)
img2 = cv2.resize(lena, None, fx=0.5, fy=0.5)   # 长×0.5  宽×0.5

cv2.imshow("lena", lena)
cv2.imshow("img", img)
cv2.imshow("ims2", img2)

#=============== 翻转 =======================================
x = cv2.flip(lena, 0)   # 绕 x轴 翻转
y = cv2.flip(lena, 1)   # 绕 y轴 翻转
xy = cv2.flip(lena, -1) # 绕 x、y轴 翻转

cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("xy", xy)

cv2.waitKey(0)
cv2.destoryAllWindows()
