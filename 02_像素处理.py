import cv2
import numpy as np

img = cv2.imread("E:/000/01.jpg", 1) # 读取图片

img[100 : 200, 150 : 200] = 0;  # 改变图片像素值

cv2.namedWindow("img") # 新建窗口命名为 img

cv2.imshow("img", img)  # 在 img 窗口显示 img 图片, 如未有名字可自动新建一次窗口命名


while 1:
    key = cv2.waitKey(0)  # 按键
    
    if key == 27:
        print("结束！")
        cv2.destroyWindow("img")  # 销毁指定窗口
        x = cv2.imwrite('E:/000/999.jpg', img)  # 保存图片
        if x == 1:
            print("图片保存成功！")

