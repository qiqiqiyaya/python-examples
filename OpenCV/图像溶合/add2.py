import cv2
import numpy as np

# 宽高通道一样才能 溶合，即属性一样才能溶合
back = cv2.imread("./back.jpeg")
cat = cv2.imread("./smallcat1.jpeg")

# 参数 cat 图片，0.7 cat图片权重，back 图片，0.3 back图片权重，0 静态权重
result = cv2.addWeighted(cat, 0.7, back, 0.3, 0)

cv2.imshow("add2", result)
cv2.waitKey(0)
