import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)
img_r, img_c, img_g = img.shape  # 得到图片的行高

# 随机生成 高×行×通道 的三维数组  以做密钥
img_key = np.random.randint(0, 256, size =  [img_r, img_c, img_g], dtype = np.uint8)

img1 = cv2.bitwise_xor(img, img_key)
img2 = cv2.bitwise_xor(img1, img_key)

cv2.imshow("img", img)  # 显示原图
cv2.imshow("img_key", img_key)  # 显示密钥
cv2.imshow("img1", img1)  # 显示加密图片
cv2.imshow("img2", img2)  # 显示解密图片

cv2.waitKey(0)
cv2.destoryAllWindows()
