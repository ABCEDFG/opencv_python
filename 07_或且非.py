import cv2
import numpy as np

'''
cv2.bitwise_and()  # 按位 与
cv2.bitwise_or()   # 按位 或
cv2.bitwise_xor()  # 按位 异或
cv2.bitwise_not()  # 按位 取反
'''

img1 = cv2.imread("E:/000/01.jpg", -1)  # 以彩色图像读取
# img2 = cv2.imread("E:/000/02.jpg", -1)  # 以彩色图像读取

img2 = np.zeros(img1.shape, dtype = np.uint8)  # 定义一个和 img1一样大的数组

img2[100 : 400, 200 : 400, 1] = 255
img2[100 : 500, 100 : 200, 2] = 255

# 逻辑操作（按位）
#img3 = cv2.bitwise_and(img1, img2)  # 按位 与
#img3 = cv2.bitwise_or(img1, img2)   # 按位 或
#img3 = cv2.bitwise_xor(img1, img2)  # 按位 异或
img3 = cv2.bitwise_not(img1)  # 按位 取反

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destoryAllWindows()
