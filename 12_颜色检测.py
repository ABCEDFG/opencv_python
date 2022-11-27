import cv2
import numpy as np

lena = cv2.imread("E:/000/01.jpg", -1)
hsv = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV)

#==============蓝色值的范围======================
minBlue=np.array([110,50,50])
maxBlue=np.array([130,255,255])

mask=cv2.inRange(hsv,minBlue,maxBlue)   # 确定蓝色区域

blue=cv2.bitwise_and(lena,lena,mask=mask)
cv2.imshow("blue",blue)


#==============绿色值的范围======================
minGreen=np.array([50,50,50])
maxGreen=np.array([70,255,255])

mask=cv2.inRange(hsv,minGreen,maxGreen)   # 确定红色区域
#green=cv2.inRange(hsv,minGreen,manGreen)

green=cv2.bitwise_and(lena,lena,mask=mask)
cv2.imshow("green",green)


#==============绿色值的范围======================
minRed=np.array([0,50,50])
maxRed=np.array([30,255,255])

mask=cv2.inRange(hsv,minRed,maxRed)  # 确定绿色区域

red=cv2.bitwise_and(lena,lena,mask=mask)
cv2.imshow("red",red)

cv2.waitKey(0)
cv2.destoryAllWindows()
