import cv2
import numpy as np


img = cv2.imread("E:/000/01.jpg", -1)

img1 = cv2.Canny(img, 128, 200)  # 边缘检测
img2 = cv2.Canny(img, 32, 200)

cv2.imshow("img", img)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)


cv2.waitKey(0)
cv2.destoryAllWindows()




