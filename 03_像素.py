import numpy as np
import cv2

''' 蓝色通道 '''
blue=np.zeros((300,300,3),dtype=np.uint8)
blue[:,:,0]=255
print("blue=\n",blue)
cv2.imshow("bluw",blue)

''' 绿色通道 '''
green=np.zeros((300,300,3),dtype=np.uint8)
green[:,:,1]=255
print("green=\n",green)
cv2.imshow("green",green)

''' 红色通道 '''
red=np.zeros((300,300,3),dtype=np.uint8)
red[:,:,2]=255
print("red=\n",red)
cv2.imshow("red",red)

''' 三色 '''
img=np.zeros((300,300,3),dtype=np.uint8)
img[:,0:100,0]=255
img[:,100:200,1]=255
img[:,200:300,2]=255
cv2.imshow("img",img)


''' 黑白 '''
img=np.random.randint(0,256,size=[300,300],dtype=np.uint8)   # 生成一个数组为 0～255 的 300×300 的二维列表
print(img.item(3,2))   # 读取 [3,2] 的像素值  该函数效率较高
cv2.imshow("demo",img)
img.itemset((3,2),255)   # 将 [3,2] 的像素值修改为 255  该函数效率较高
print(img.item(3,2))   # 读取 [3,2] 的像素值  该函数效率较高
#cv2.waitKey()   # 按键 用于暂停


''' 彩色 '''
img=np.random.randint(0,256,size=[300,300,3],dtype=np.uint8)
cv2.imshow("demo2",img)
#cv2.waitKey()
#cv2.destroyAllWindows()




cv2.waitKey()  # 按键
cv2.destroyAllWindows()   # 销毁指定窗口