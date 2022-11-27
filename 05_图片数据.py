import numpy as np
import cv2

gray = cv2.imread("E:/000/01.jpg", 0)  # 以灰度图像读取
color = cv2.imread("E:/000/01.jpg", -1)  # 以彩色图像读取

# 灰度
print('图像 灰色 属性：')
print('gray.shape=', gray.shape)  # 行数 列数 通道数
print('gray.size=', gray.size)  # 图像像素点 * 通道数
print('gray.dtype=', gray.dtype)  # np.unit8
print()

# 彩色
print('图像 彩色 属性：')
print('color.shape=', color.shape)  # 行数 列数 通道数
print('color.size=', color.size)  # 图像像素点 * 通道数
print('color.dtype=', color.dtype)  # np.unit8

