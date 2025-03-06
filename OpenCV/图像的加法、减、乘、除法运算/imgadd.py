import cv2
import numpy as np


dog = cv2.imread("./dog.jpeg")
# 图的加法运算就是矩阵的加法运算
# 因此，加法运算的 两图 必须相等

# 得到图片信息 宽、高、通道
# print(dog.shape)

# 得到另一张图
img = np.ones((1200, 1920, 3), np.uint8) * 50

# cv2.imshow("new", img)
# cv2.imshow("dog", dog)

# 加法
# result = cv2.add(dog, img)
# cv2.imshow("result", result)

# 减法
# result1 = cv2.subtract(result, img)
# result1 = cv2.subtract(dog, img)
# cv2.imshow("result1", result1)

# cv2.multiply 乘法，等于多次相加，加 -> 越亮
# cv2.divide 除法，等于多次相减，加 -> 越暗

cv2.waitKey(0)
