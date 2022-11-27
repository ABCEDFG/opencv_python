import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)

img_h, img_w, img_ch = img.shape

x = 100
y = 200
print(img_h, img_w, img_ch)

# 平移
m = np.float32([[1, 0, x], [0, 1, y]])
img2 = cv2.warpAffine(img, m, (img_w, img_h))  # 平移   

# 旋转
m2 = cv2.getRotationMatrix2D((img_w/2, img_h/2), 45, 0.6)
img3 = cv2.warpAffine(img, m2, (img_w, img_h))

# 复杂仿射
p1 = np.float32([[0, 0], [img_w - 1, 0], [0, img_h - 1]])
p2 = np.float32([[0, img_h * 0.33], [img_w * 0.85, img_h * 0.25], [img_w * 0.15, img_h * 0.7]])
m3 = cv2.getAffineTransform(p1, p2) 
img4 = cv2.warpAffine(img, m3, (img_w, img_h))

# 透视
p3 = np.float32([[0, 100], [100, img_w - 50], [img_h - 50, 100], [img_h - 50, img_w - 50]])
p4 = np.float32([[50, 50], [img_h - 50, 50], [50, img_w - 50], [img_h - 50, img_w - 50]])
m4 = cv2.getPerspectiveTransform(p3, p4)
img5 = cv2.warpPerspective(img, m4, (img_w, img_h))

# 重映射
img = cv2.imread("E:/000/01.jpg", 0)
mapx = np.ones(img.shape, np.float32) * 3 
mapy = np.ones(img.shape, np.float32) * 0 
img6 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR) 

# 复制
mapx = np.zeros(img.shape, np.float32)
mapy = np.zeros(img.shape, np.float32)
for i in range(img_h):
    for j in range(img_w):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
img7 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# （复制）并绕 x 轴翻转
for i in range(img_h):
    for j in range(img_w):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), img_h - 1 - i)
img8 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# （复制）并绕 y 轴翻转
for i in range(img_h):
    for j in range(img_w):
        mapx.itemset((i, j), img_w - 1 - j)
        mapy.itemset((i, j), i)
img9 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# （复制）并 x 轴、 y 轴互换
for i in range(img_h):
    for j in range(img_w):
        mapx.itemset((i, j), i)
        mapy.itemset((i, j), j)
img10 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# 图像缩放(缩小)
img = cv2.imread("E:/000/01.jpg", -1)
mapx = np.zeros([img_h, img_w], np.float32)
mapy = np.zeros([img_h, img_w], np.float32)
for i in range(img_h):
    for j in range(img_w):
        if 0.25 * img_h < i < 0.75 * img_h and 0.25 * img_w < j < 0.75 * img_w:
            mapx.itemset((i, j), 2 * (j - img_w * 0.25) + 0.5)
            mapy.itemset((i, j), 2 * (i - img_h * 0.25) + 0.5)
        else:
            mapx.itemset((i, j), 0)
            mapy.itemset((i, j), 0)
img11 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)


cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.imshow("img5", img5)
cv2.imshow("img6", img6)
cv2.imshow("img7", img7)
cv2.imshow("img8", img8)
cv2.imshow("img9", img9)
cv2.imshow("img10", img10)
cv2.imshow("img11", img11)

cv2.waitKey(0)
cv2.destoryAllWindows()




