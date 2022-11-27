import cv2
import numpy as np


img = cv2.imread("E:/000/01.jpg", -1)

# 梯度 Sobel 算子
s1 = cv2.Sobel(img, cv2.CV_64F, 1, 0)  # x 方向梯度
s1 = cv2.convertScaleAbs(s1)  # 取绝对值

s2 = cv2.Sobel(img, cv2.CV_64F, 0, 1)  # y 方向梯度
s2 = cv2.convertScaleAbs(s2)  # 取绝对值

s3=cv2.Sobel(img, cv2.CV_64F, 1, 1)   # xy 方向梯度
s3=cv2.convertScaleAbs(s3)   # 取绝对值

sxy = cv2.addWeighted(s1, 1, s2, 1, 0)   # 两图片权重相加


# 梯度 Scharr 算子
w1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)   # x方向梯度
w1 = cv2.convertScaleAbs(w1)   # 取绝对值
     
w2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)   # y方向梯度
w2 = cv2.convertScaleAbs(w2)   # 取绝对值

xy1=cv2.addWeighted(w1, 0.5, w2, 0.5, 0)


# 梯度 Laplacian 算子
la = cv2.Laplacian(img, cv2.CV_64F)
la = cv2.convertScaleAbs(la)


cv2.imshow("img", img)

cv2.imshow("s1", s1)
cv2.imshow("s2", s2)
cv2.imshow("s3", s3)
cv2.imshow("sxy", sxy)

cv2.imshow("w1", w1);
cv2.imshow("w2", w2);
cv2.imshow("xy1", xy1);

cv2.imshow("la", la)


cv2.waitKey(0)
cv2.destoryAllWindows()




