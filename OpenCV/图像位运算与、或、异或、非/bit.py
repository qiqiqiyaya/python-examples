import cv2
import numpy as np

# 创建一张图片，默认黑色
# img = np.zeros((200, 200), np.uint8)
# img = cv2.imread("./smallcat1.jpeg")
# 中填充白色,y,x轴
# img[20:120, 20:120] = 0
# 非 运算，取反
# new_Img = cv2.bitwise_not(img)
# cv2.imshow("img", img)
# cv2.imshow("new", new_Img)

# 与 运算，找出图像交叉点，图像的交集
# img1 = np.zeros((200, 200), np.uint8)
# img1[80:180, 80:180] = 255

# new_img = cv2.bitwise_and(img, img1)
# cv2.imshow("img1", img1)
# cv2.imshow("img", img)
# cv2.imshow("new_img", new_img)


# 或 运算，取并集，所有集合全放一起
# img = np.zeros((200, 200), np.uint8)
# img[20:120, 20:120] = 255
# img1 = np.zeros((200, 200), np.uint8)
# img1[80:180, 80:180] = 255

# new_img = cv2.bitwise_or(img, img1)
# cv2.imshow("img", img)
# cv2.imshow("img1", img1)
# cv2.imshow("new_img", new_img)

# 异或，有交集则取反，没有交集放一起
img = np.zeros((200, 200), np.uint8)
img[20:120, 20:120] = 255
img1 = np.zeros((200, 200), np.uint8)
img1[80:180, 80:180] = 255

new_img = cv2.bitwise_xor(img, img1)
cv2.imshow("img", img)
cv2.imshow("img1", img1)
cv2.imshow("new_img", new_img)


cv2.waitKey(0)
