import cv2
import numpy as np


img = cv2.imread("E:\\R-C.jfif")

# 包括3个信息，高度、长度、通道数
print(img.shape)

#
print(img.size)

# 图像中每个元素的位深
print(img.dtype)
