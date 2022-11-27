import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将 BGR 转化为 GRAY--8 位灰度图
bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # 将 GRAY 转化为 BGR
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将 BGR 转化为 RGB
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 将 BGR 转换为 BGRA
xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)  # 将 BGR 转换为 XYZ


b, g, r, a = cv2.split(bgra)
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

cv2.imshow("gray", gray)
cv2.imshow("bgra", bgra)
cv2.imshow("bgra0", bgra0)
cv2.imshow("img", img)
cv2.imshow("rgb", rgb)

cv2.waitKey(0)
cv2.destoryAllWindows()
