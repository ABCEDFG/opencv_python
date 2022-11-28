import cv2
import numpy as np

img = cv2.imread('E:/000/01.jpg')

g = img.shape

h1 = int(g[0]*1.5)
w1 = int(g[1]*1.5)

dstImage = np.zeros((h1,w1,3),np.uint8)

for i in range(0,h1):
    for j in range(0,w1):
        iNew = int(i*g[0]*1.0/h1)
        jNew = int(j*g[1]*1.0/w1)
        dstImage[i,j] = img[iNew,jNew]

cv2.imshow("img",img)
cv2.imshow("date",dstImage)

cv2.waitKey(0)

cv2.destroyAllWindows()

