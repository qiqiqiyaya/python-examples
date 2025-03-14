import cv2


def callback(userdata):
    pass


cv2.namedWindow("color", cv2.WINDOW_NORMAL)
img = cv2.imread("E:\\R-C.jfif")

colorspaces = [
    cv2.COLOR_BGR2RGBA,
    cv2.COLOR_BGR2BGRA,
    cv2.COLOR_BGR2GRAY,
    cv2.COLOR_BGR2HSV,
    cv2.COLOR_BGR2YUV,
]

cv2.createTrackbar("curcolor", "color", 0, 4, callable)

while True:
    index = cv2.getTrackbarPos("curcolor", "color")

    # 颜色空间转换API
    cvt_img = cv2.cvtColor(img, colorspaces[index])

    cv2.imshow("color", cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
