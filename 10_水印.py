import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", -1)
key = cv2.imread("E:/000/01.jpg", -1)
imgx = cv2.imread("E:/000/01.jpg", -1)

key_r, key_c, key_g = key.shape  # 得到图片的行高
imgx_r, imgx_c, imgx_g = imgx.shape

key[0 : imgx_r, 0 : imgx_c, 0 : imgx_g] = imgx[0 : imgx_r, 0 : imgx_c, 0 : imgx_g]

k = key[:, :] > 0
key[k] = 1

img_r, img_c, img_g = img.shape

t254 = np.ones((img_r, img_c, img_g), dtype = np.uint8) * 254

img_H7 = cv2.bitwise_and(img, t254)

e = cv2.bitwise_or(img_H7, key)

t1 = np.ones((img_r, img_c, img_g), dtype = np.uint8)

wm = cv2.bitwise_and(e, t1)

print(wm)
w = wm[:, :] > 0
wm[w] = 255

cv2.imshow("img", img)
cv2.imshow("key", key)
cv2.imshow("e", e)
cv2.imshow("wm", wm)

cv2.waitKey(0)
cv2.destoryAllWindows()
