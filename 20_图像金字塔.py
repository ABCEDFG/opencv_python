import cv2
import numpy as np


img = cv2.imread("E:/000/01.jpg", 0)


# 高斯金字塔
r1 = cv2.pyrDown(img)   # 向下采样   面积缩小 4 倍
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)

s1 = cv2.pyrUp(img)   # 向上采样   面积放大 4 倍
s2 = cv2.pyrUp(s1)
s3 = cv2.pyrUp(s2)

 
# 拉普拉斯金字塔
l1 = img - cv2.pyrUp(r1)
l2 = r1 - cv2.pyrUp(r2)
l3 = r2 - cv2.pyrUp(r3)


cv2.imshow("img", img)

cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.imshow("s1", s1)
cv2.imshow("s2", s2)
cv2.imshow("s3", s3)

cv2.imshow("l1", l1)
cv2.imshow("l2", l2)
cv2.imshow("l3", l3)


cv2.waitKey(0)
cv2.destoryAllWindows()




