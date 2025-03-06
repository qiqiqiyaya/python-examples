import cv2
import numpy as np

# 通过array定义矩阵
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])

# print(a)
# print(b)

# 定义ones矩阵
# d = np.ones((8, 8), np.uint8)
# print(d)

# 定义full矩阵
# e = np.full((8, 8), 10, np.uint8)
# print(e)

# 定义单位矩阵identity
# f = np.identity(8)
# print(f)

# g = np.eye(5, 7, k=1)
# print(g)

img = np.zeros((480, 640, 3), np.uint8)
# img = np.eye(480, 640, k=1)

# 从矩阵中读某个元素的值
# print(img[100, 100])

roi = img[100:400, 100:600]
roi[:] = [0, 0, 255]
roi[:, 10] = [0, 0, 0]
roi[10:200, 10:200] = [0, 255, 0]

cv2.imshow("img", roi)
key = cv2.waitKey(0)
if key & 0xFF == ord("q"):
    cv2.destroyAllWindows()
