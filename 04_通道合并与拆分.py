import numpy as np
import cv2

img = cv2.imread("E:/000/01.jpg")

''' 按通道拆分图片 '''
'''
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
'''
b, g, r = cv2.split(img)  # 两种方式是等价的
 

''' 通道合并 '''
bgr = cv2.merge([b, g, r])  # 通道合并 顺序 b g r
rgb = cv2.merge([r, g, b])


cv2.imshow("img", img)
cv2.imshow("bgr", bgr)
cv2.imshow("rgb", rgb)
'''
cv2.imshow("blue",a)
cv2.imshow("green",b)
cv2.imshow("red",c)
'''


cv2.waitKey()  # 按键
cv2.destroyAllWindows()   # 销毁指定窗口