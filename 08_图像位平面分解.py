import cv2
import numpy as np

img1 = cv2.imread("E:/000/01.jpg", 0)
img1_r, img1_c = img1.shape  # 得到图片的行高

img2 = np.zeros((img1_r, img1_c, 8), dtype = np.uint8)  # 建立一个 img1_r * img1_c * 8 的三维列表

# 设置用于提取各个位平面的提取矩阵
for i in range(8):
    img2[:, :, i] =  2 ** i

img3 = np.zeros((img1_r, img1_c, 8), dtype = np.uint8)

# 实现了各个位平面的提取、阈值处理和显示
for i in range(8):
    img3[:, :, i] = cv2.bitwise_and(img1, img2[:, :, i])
    mask = img3[:, :, i] > 0
    img3[mask] = 255
    cv2.imshow(str(i), img3[:, :, i])

cv2.waitKey(0)
cv2.destoryAllWindows()
