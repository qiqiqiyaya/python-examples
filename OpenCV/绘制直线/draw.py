import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

cv2.line(img, (1, 20), (300, 400), (0, 0, 255), 5, 4)


# 画多边形
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255))
# 填充这个3角型多边形
cv2.fillPoly(img, [pts], (255, 255, 0))

# 绘制文本
cv2.putText(img, "Hello World!", (10, 400), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 0))

cv2.imshow("draw", img)
cv2.waitKey(0)
