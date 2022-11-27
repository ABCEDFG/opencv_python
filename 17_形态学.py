import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)

k = np.ones((5, 5), np.uint8)

# 核函数
k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字架
k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆

# 形态学运算

img1 = cv2.erode(img, k)  # 腐蚀
img2 = cv2.dilate(img1, k)  # 膨胀

# 下面的运算均为腐蚀和膨胀的结合                                                             
img3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)  # 开运算  先腐蚀载膨胀  除去外部毛刺 区域划分
img4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k, iterations = 3)   # 闭运算  先膨胀再腐蚀  除去内部小孔 区域连接
img5 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)   # 形态学梯度  膨胀-腐蚀
img6 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)     # 礼貌运算  原图片的外部毛刺
img7 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)   # 黑帽运算  原图片的内部小孔


cv2.imshow("img", img)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.imshow("img5", img5)
cv2.imshow("img6", img6)
cv2.imshow("img7", img7)


cv2.waitKey(0)
cv2.destoryAllWindows()




