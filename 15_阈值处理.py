import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)


# t: 返回的阈值
# r: 处理后的图像
t, r = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 二值化阈值        >阈值：255，<阈值：0
#t, r = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)   # 反二值化阈值  >阈值：0 ， <阈值：255
#t, r = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)   # 截断值化   大于127的设定为127
#t, r = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)   # 超阈值0处理
#t, r = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)   # 低阈值0

# 自动阈值处理貌似只能处理黑白照片
img = cv2.imread("E:/000/01.jpg", 0)
ath1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 3)   # 自适应阈值处理   领域所有像素点的权重是一致的
ath2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)   # 自适应阈值处理   权重与到中心点距离有关
t1, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   # otsu 处理

print("rst: ", t)
cv2.imshow("img", img)
cv2.imshow("rst", r)
cv2.imshow("ath1", ath1)
cv2.imshow("ath2", ath2)
cv2.imshow("otsu", otsu)

cv2.waitKey(0)
cv2.destoryAllWindows()




